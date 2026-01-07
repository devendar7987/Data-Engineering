# Loading single table  data  into a parent table and child tables

import pandas as pd
from sqlalchemy import create_engine

def extract(file_name):
    print(f"Extracting data from {file_name}")
    return pd.read_csv(file_name)

def transform(data_frame):
    print("Transforming data...")
    transformed_df = data_frame.drop_duplicates()
    transformed_df = transformed_df[transformed_df["salary"]>0]
    return transformed_df

def load(data_frame, table_name, engine):
    print(f"Loading data into {table_name} table...")
    data_frame.to_sql(table_name, engine, if_exists="replace", index=False)

# Extract data from the source file
extracted_data = extract("employee_raw.csv")
print("Extracted data from source file:")
print(extracted_data)

# Transform the extracted data
transformed_data = transform(extracted_data)
print("Transformed data")
print(transformed_data)

# Create the parent table (employees) from transformed data
parent_df = transformed_data[["emp_id", "emp_name", "dept"]]
print("Parent Table: Employees")
print(parent_df)

# Create child table: employee salary details
salary_df = transformed_data[["emp_id", "salary"]]
print("Child Table: Employee Salary")
print(salary_df)

# Create child table: employee project details
projects_df = transformed_data[["emp_id", "project", "project_hours"]]
print("Child Table: Employee Projects")
print(projects_df)

# Create child table: employee contact details
contact_df = transformed_data[["emp_id", "address", "phone"]]
print("Child Table: Employee Contact")
print(contact_df)

# Load the parent table and child tables into the database

username = "postgres"
password = "chintu7987" 
host = "localhost"
port = 5432
database_name = "Datacamp"

db_engine = create_engine(
    f"postgresql+psycopg2://{username}:{password}@{host}:{port}/{database_name}"
)

# Load data into the parent table (employees)
load(parent_df,"employees",db_engine)

# Load data into child tables
load(salary_df, "employee_salary", db_engine)
load(projects_df, "employee_projects", db_engine)
load(contact_df, "employee_contact", db_engine)

# Validate loaded data
employees_check = pd.read_sql("SELECT * FROM employees;", db_engine)
print("Validating employees table...")
print(employees_check)

salary_check = pd.read_sql("SELECT * FROM employee_salary;", db_engine)
print("Validating employee_salary table...")
print(salary_check)

projects_check = pd.read_sql("SELECT * FROM employee_projects", db_engine)
print("Validating employee_projects table...")
print(projects_check)

contact_check =  pd.read_sql("SELECT * FROM employee_contact", db_engine)
print("Validating employee_contact table...")
print(contact_check)