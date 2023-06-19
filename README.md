# Resume-Managment-System-GCP
Implementation of Resume Management System using Google Document AI In today's fast-paced business environment, organizations often encounter a considerable influx of resumes when seeking to fill job vacancies. The human resources department, responsible for reviewing and assessing applicant qualifications, faces the daunting challenge of efficiently processing a large number of resumes. The current approach of manually reviewing and extracting relevant information from these documents proves to be time-consuming and error prone. As a result, there is a critical need for a solution that can automate the extraction of data from resumes, enabling faster and more accurate analysis of applicant information.

* The Cloud Function is designed to be triggered by changes in a Cloud Storage bucket, specifically when a new file is added. This event-based architecture ensures that the function is automatically executed whenever a new file is uploaded to the specified bucket.

* The function uses the Google Cloud Document AI service to process the added file and extract relevant information. This leverages machine learning and natural language processing techniques to analyze the contents of the file and extract structured data from it.

* Once the data is extracted from the file, the function stores it in BigQuery, a fully managed data warehouse provided by Google Cloud. BigQuery is highly scalable and allows for efficient storage and querying of large datasets.

* These commands used in this code
`google-cloud-storage` 
`google-cloud-bigquery libraries`
