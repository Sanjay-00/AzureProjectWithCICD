import os

folders = [
    "assets/adf_pipeline_screenshots",
    "assets/databricks_dlt_screenshots",
    "source_data",
    "notebooks/silver",
    "notebooks/gold",
    "pipelines",
    "devops"
]

# Create folders
for folder in folders:
    os.makedirs(folder, exist_ok=True)


print("📁 Project structure with source files folder created successfully!")
