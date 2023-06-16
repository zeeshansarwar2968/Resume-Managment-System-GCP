import os
import functions_framework
from google.cloud import bigquery
from google.cloud import storage
import json

# Triggered by a change in a storage bucket
@functions_framework.cloud_event
def insrt_to_big_query_table(cloud_event):
    data = cloud_event.data
    """Triggered by a change to a Cloud Storage bucket.
    Args:
         event (dict): Event payload.
         context (google.cloud.functions.Context): Metadata for the event.
    """
    # Retrieve the file details from the Cloud Storage event
    bucket_name = data['bucket']
    file_name = data['name']
    
    # Set up BigQuery client
    bq_client = bigquery.Client()
    
    # Set up Cloud Storage client
    storage_client = storage.Client()
    
    # Get the file from Cloud Storage
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(file_name)
    
    # Download the file content as a string
    file_content = blob.download_as_text()
    
    # Parse the file content as JSON
    data = json.loads(file_content)
    
    # Define the BigQuery table and dataset details
    dataset_id = 'Resume_Dataset'
    table_id = 'extracted_resumes'
    
    # Construct the BigQuery table reference
    table_ref = bq_client.dataset(dataset_id).table(table_id)
    
    # Create a BigQuery row to insert
    columns = ['candidate_name', 'candidate_mob_no', 'candidate_email', 'candidate_address', 'summary', 'skills', 
           'current_company', 'current_designation', 'current_work_experience', 'start_year_of_current_company', 
           'previous_designation_1', 'previous_company_name_1', 'start_year_of_company_1', 'end_year_of_company_1', 
           'experience_history_1', 'previous_designation_2', 'previous_company_name_2', 'start_year_of_company_2', 
           'end_year_of_company_2', 'experience_history_2', 'previous_designation_3', 'previous_company_name_3', 
           'start_year_of_company_3', 'end_year_of_company_3', 'experience_history_3', 'education_institute_1', 
           'degree_from_institute_1', 'start_year_of_education_1', 'education_institute_2', 'degree_from_institute_2',
           'certifications', 'achievements']


    row_to_insert = {}

    for c in columns:
        if c not in list(data.keys()):
            row_to_insert[c] = "null"
        else:
            row_to_insert[c] = data[c]
    
    # Insert the row into BigQuery table
    errors = bq_client.insert_rows_json(table_ref, [row_to_insert])
    
    if errors:
        print(f"Encountered errors while inserting row: {errors}")
    else:
        print("Row inserted successfully!")
