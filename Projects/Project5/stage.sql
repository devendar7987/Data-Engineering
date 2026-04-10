-- Create Storage Integration

CREATE OR REPLACE STORAGE INTEGRATION s3_int
TYPE = EXTERNAL_STAGE
STORAGE_PROVIDER = S3
ENABLED = TRUE
STORAGE_AWS_ROLE_ARN = 'arn:aws:iam::306158388879:role/snowflake-role'
STORAGE_ALLOWED_LOCATIONS = ('s3://devendar-full-load-project/');


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

-- Customers Stage
CREATE OR REPLACE STAGE customers_stage
URL = 's3://devendar-full-load-project/customers/'
STORAGE_INTEGRATION = s3_int
FILE_FORMAT = (
    TYPE = CSV
    SKIP_HEADER = 1
);


-- Orders Stage
CREATE OR REPLACE STAGE orders_stage
URL = 's3://devendar-full-load-project/orders/'
STORAGE_INTEGRATION = s3_int
FILE_FORMAT = (
    TYPE = CSV
    SKIP_HEADER = 1
);


-- Payments Stage
CREATE OR REPLACE STAGE payments_stage
URL = 's3://devendar-full-load-project/payments/'
STORAGE_INTEGRATION = s3_int
FILE_FORMAT = (
    TYPE = CSV
    SKIP_HEADER = 1
);






