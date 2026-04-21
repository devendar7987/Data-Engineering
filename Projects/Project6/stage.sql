-- Create Storage Integration

CREATE OR REPLACE STORAGE INTEGRATION s3_int
TYPE = EXTERNAL_STAGE
STORAGE_PROVIDER = S3
ENABLED = TRUE
STORAGE_AWS_ROLE_ARN = 'arn:aws:iam::306158388879:role/ecommerce-data-pipeline-role'
STORAGE_ALLOWED_LOCATIONS = ('s3://ecommerce-data-pipeline-devendar');


/* 
DESC INTEGRATION s3_int; is used to get storage integration details.
From the output, we take:
1) STORAGE_AWS_IAM_USER_ARN
2) STORAGE_AWS_EXTERNAL_ID

These values are updated in the AWS IAM Role Trust Policy
to allow Snowflake to securely access the S3 bucket.
*/

DESC INTEGRATION s3_int;

-- Create External Stages

-- ORDERS_DETAILED Stage
CREATE OR REPLACE STAGE ORDERS_DETAILED_STAGE
URL = 's3://ecommerce-data-pipeline-devendar/processed/orders_detailed/'
STORAGE_INTEGRATION = s3_int
FILE_FORMAT = (
    TYPE = CSV
    SKIP_HEADER = 1
);


-- CUSTOMER_SUMMARY Stage
CREATE OR REPLACE STAGE CUSTOMER_SUMMARY_STAGE
URL = 's3://ecommerce-data-pipeline-devendar/processed/customer_summary/'
STORAGE_INTEGRATION = s3_int
FILE_FORMAT = (
    TYPE = CSV
    SKIP_HEADER = 1
);

