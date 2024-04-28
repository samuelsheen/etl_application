import pandas as pd
import pytest
from etl_application.transform import DataTransformer


class TestDataTransformer:
    @pytest.fixture(scope="class")
    def data(self):
        """Sample data used for testing."""
        data = {
            "Name": ["Alice", "Bob", None],
            "Age": [25, 30, 28],
            "Salary": [50000, None, 42000],
        }
        return pd.DataFrame(data)

    @pytest.fixture(scope="class")
    def transformer(self, data):
        """DataTransformer instance with sample data."""
        return DataTransformer(data)

    def test_normalise_column_names(self, transformer):
        """Test that column names are normalized correctly."""
        transformer.normalise_column_names()
        expected_columns = ["name", "age", "salary"]
        assert transformer.df.columns.tolist() == expected_columns

    def test_fill_missing_values(self, transformer):
        """Test filling missing values."""
        transformer.fill_missing_values("name", "Unknown")
        transformer.fill_missing_values("salary", 0)
        assert transformer.df["name"].isnull().sum() == 0
        assert transformer.df["salary"].isnull().sum() == 0

    def test_convert_data_types(self, transformer):
        """Test converting data types of columns."""
        transformer.convert_data_types("salary", "float")
        assert transformer.df["salary"].dtype == float

    def test_create_new_column(self, transformer):
        """Test creating a new column based on existing ones."""
        transformer.create_new_column("age_in_days", "age * 365")
        assert "age_in_days" in transformer.df.columns
        assert transformer.df.at[0, "age_in_days"] == 25 * 365

    def test_drop_columns(self, transformer):
        """Test dropping specified columns."""
        transformer.drop_columns(["age"])
        assert "age" not in transformer.df.columns

    def test_get_transformed_data(self, transformer):
        """Test getting the transformed DataFrame."""
        transformed_df = transformer.get_transformed_data()
        assert isinstance(transformed_df, pd.DataFrame)
