import pandas as pd
import logging
from pydantic import BaseModel


class DataFrameValidator:
    @staticmethod
    def compare(df: pd.DataFrame, model: BaseModel) -> bool:
        logging.basicConfig(level=logging.INFO)

        # Get the DataFrame columns and their types
        df_columns = df.columns
        df_types = df.dtypes

        # Get the Pydantic model fields and their types
        model_fields = model.__annotations__

        # Check if the DataFrame columns match the model fields
        if set(df_columns) != set(model_fields.keys()):
            logging.error("Column names do not match.")
            return False

        # Check if the data types match
        for field_name, field_type in model_fields.items():
            # Map Pydantic types to Pandas types
            if field_type == str:
                expected_type = "object"  # Pandas uses 'object' for string types
            elif field_type == float:
                expected_type = "float64"
            elif field_type == int:
                expected_type = "int64"
            elif field_type == bool:
                expected_type = "bool"
            else:
                expected_type = None  # Handle other types as needed

            # Check if the DataFrame column type matches the expected type
            if expected_type and df_types[field_name] != expected_type:
                logging.error(
                    f"Type mismatch for column '{field_name}': expected {expected_type}, got {df_types[field_name]}"
                )
                return False

        logging.info("Schema and data types match.")
        return True
