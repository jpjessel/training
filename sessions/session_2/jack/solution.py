from config import SchemaAndColumns
from processing import *

config_content = {
    "source_file": "session_2_source.csv",
    "target_file": "session_2_target.csv",
    "england": {
        "DATE": {
            "data_type": "date",
            "source_column": "Date"
        },
        "REGION_CODE": {
            "data_type": "string",
            "source_column": "Area Code"
        },
        "REGION_NAME": {
            "data_type": "string",
            "source_column": "Area Name"
        },
        "SEX": {
            "data_type": "string",
            "source_column": "Sex"
        },
        "COVERAGE_PERCENT": {
            "data_type": "float",
            "source_column": "Value"
        }
    },
    "imd": {
        "DATE": {
            "data_type": "date",
            "source_column": "Date"
        },
        "REGION_CODE": {
            "data_type": "string",
            "source_column": "Area Code"
        },
        "REGION_NAME": {
            "data_type": "string",
            "source_column": "Area Name"
        },
        "SEX": {
            "data_type": "string",
            "source_column": "Sex"
        },
        "IMD_DECILE": {
            "data_type": "integer",
            "source_column": "Category"
        },
        "COVERAGE_PERCENT": {
            "data_type": "float",
            "source_column": "Value"
        }
    }
}

config_file = SchemaAndColumns(config_content)

england_pipeline = bowel_cancer_england(config_file, "england")
print(england_pipeline)
imd_pipeline = bowel_cancer_imd(config_file, "imd")
print(imd_pipeline)