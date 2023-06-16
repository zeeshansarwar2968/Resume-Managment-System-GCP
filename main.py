import functions_framework
from google.api_core.client_options import ClientOptions
from google.cloud import documentai
from google.cloud import storage
import json

def process_document_sample(
    project_id: str,
    location: str,
    processor_id: str,
    processor_version_id: str,
    file_path: str,
    mime_type: str,
    field_mask: str,
) -> None:
    # You must set the api_endpoint if you use a location other than 'us'.
    opts = ClientOptions(api_endpoint=f"{location}-documentai.googleapis.com")

    client = documentai.DocumentProcessorServiceClient(client_options=opts)

    name = client.processor_version_path(project_id, location, processor_id, processor_version_id)

    # Read the file into memory
    with open(file_path, "rb") as image:
        image_content = image.read()

    # Load Binary Data into Document AI RawDocument Object
    raw_document = documentai.RawDocument(content=image_content, mime_type=mime_type)

    # Configure the process request
    request = documentai.ProcessRequest(
        name=name, raw_document=raw_document, field_mask=field_mask
    )

    result = client.process_document(request=request)
    document = result.document

    # Extract entities as key-value pairs (type and mentioned text)
    extracted_entities = {}
    for entity in document.entities:
        extracted_entities[entity.type_] = entity.mention_text

    return extracted_entities

def write_text_to_storage(text_data, destination_bucket_name, file_name):
    # Initialize the Cloud Storage client
    client = storage.Client()

    # Get the bucket
    bucket = client.get_bucket(destination_bucket_name)

    # Define the file path
    file_path = f"{file_name}.json"

    # Write the text data to the file
    blob = bucket.blob(file_path)
    blob.upload_from_string(json.dumps(text_data), content_type="application/json")


def temp_file_path(bucket_name, file_name):
    # Extract the file information from the Cloud Storage event

    # Initialize the Cloud Storage client
    storage_client = storage.Client()

    # Get the bucket
    bucket = storage_client.get_bucket(bucket_name)

    # Get the PDF file blob
    blob = bucket.blob(file_name)

    # Download the PDF file to a local temporary file
    temp_file_path = "/tmp/temp.pdf"  # Set your desired temporary file path
    blob.download_to_filename(temp_file_path)
    return temp_file_path


# Triggered by a change in a storage bucket
@functions_framework.cloud_event
def extract_resume(cloud_event):
    data = cloud_event.data
    
    bucket_name = data["bucket"]
    file_name = data["name"]

    project_id = 'document-al-extraction'
    location = 'us' 
    processor_id = '7fcafe1c6c5e6680'
    processor_version_id = 'b48cef46d3903822'
    mime_type = 'application/pdf' 
    field_mask = "text,entities,pages.pageNumber" 

    destination_bucket_name = "extracted_resumes"

    file_path = temp_file_path(bucket_name, file_name)

    file_content = process_document_sample(project_id, location, processor_id, processor_version_id, file_path, mime_type, field_mask)

    write_text_to_storage(file_content, destination_bucket_name, file_name)