# Resume-Managment-System-GCP
Implementation of Resume Management System using Google Document AI
In today's fast-paced business environment, organizations often encounter a considerable influx of resumes when seeking to fill job vacancies. The human resources department, responsible for reviewing and assessing applicant qualifications, faces the daunting challenge of efficiently processing a large number of resumes. The current approach of manually reviewing and extracting relevant information from these documents proves to be time-consuming and error prone. As a result, there is a critical need for a solution that can automate the extraction of data from resumes, enabling faster and more accurate analysis of applicant information. 

## extract_resume_cloud_function_1
* The Cloud Function is designed to be triggered by changes in a Cloud Storage bucket. This event-based architecture ensures that the function is automatically executed whenever a new file is added to the specified bucket.

* The function utilizes the Google Cloud Document AI service to process the added file. It extracts relevant information from the resume using machine learning and natural language processing techniques. This enables faster and more accurate analysis of applicant information, saving time and reducing manual effort.

* The extracted data is then saved to another Cloud Storage bucket. This ensures that the processed output is stored securely and can be accessed or further processed as needed. Storing the results in a separate bucket also allows for easy integration with other applications or services that require access to the processed data.

* The function uses the google-cloud-storage and google-cloud-documentai libraries to interact with Cloud Storage and Document AI services respectively. These libraries provide convenient and efficient ways to read input files from Cloud Storage, process them using Document AI, and write the output back to Cloud Storage.

* These are the libraries used in this function

```
google-api-core
```
```
google-cloud-storage
```
```
google-cloud-bigquery
```
## load_to_bigquery_cloud_function_2

* Once the data is extracted from the file, the function stores it in BigQuery, a fully managed data warehouse provided by Google Cloud. BigQuery is highly scalable and allows for efficient storage and querying of large datasets.


* These are the libraries used in this function
```
google-cloud-storage
```
```
google-cloud-bigquery
```
