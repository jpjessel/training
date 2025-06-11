from typing import Dict
from datetime import datetime

class SchemaAndColumns:

    def __init__(
            self, 
            config: Dict[str, Dict]
        ):
        self.config = config
        self.data_type_map = {
            "date": "datetime64[ns]",
            "float": "float64",
            "str": "string",
            "string": "string",
            "int": "int64",
            "integer": "int64"
        }
        self.source_file = config["source_file"]
        self.target_file = config["target_file"]

    def create_schema(self, filter: str):
        filter = filter.lower()
        columns_names = {}
        for key, value in self.config[filter].items():
            columns_names[key] = self.data_type_map.get(value["data_type"])

        return columns_names

    def create_column_map(self, filter: str):
        filter = filter.lower()
        columns_names = {}
        for key, value in self.config[filter].items():
            columns_names[value["source_column"]] = key

        return columns_names