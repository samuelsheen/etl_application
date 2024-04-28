import pandas as pd
from sqlalchemy.engine import Engine
from unittest.mock import patch, MagicMock


from etl_application.extract import Extractor


expected_data = pd.DataFrame(
    columns=["sepal_length", "sepal_width", "petal_length", "petal_width", "species"],
    data=[
        [5.1, 3.5, 1.4, 0.2, "setosa"],
        [4.9, 3.0, 1.4, 0.2, "setosa"],
        [4.7, 3.2, 1.3, 0.2, "setosa"],
        [4.6, 3.1, 1.5, 0.2, "setosa"],
        [5.0, 3.6, 1.4, 0.2, "setosa"],
        [5.4, 3.9, 1.7, 0.4, "setosa"],
        [4.6, 3.4, 1.4, 0.3, "setosa"],
        [5.0, 3.4, 1.5, 0.2, "setosa"],
        [4.4, 2.9, 1.4, 0.2, "setosa"],
        [4.9, 3.1, 1.5, 0.1, "setosa"],
        [5.4, 3.7, 1.5, 0.2, "setosa"],
        [4.8, 3.4, 1.6, 0.2, "setosa"],
        [4.8, 3.0, 1.4, 0.1, "setosa"],
        [4.3, 3.0, 1.1, 0.1, "setosa"],
        [5.8, 4.0, 1.2, 0.2, "setosa"],
        [5.7, 4.4, 1.5, 0.4, "setosa"],
        [5.4, 3.9, 1.3, 0.4, "setosa"],
        [5.1, 3.5, 1.4, 0.3, "setosa"],
        [5.7, 3.8, 1.7, 0.3, "setosa"],
        [5.1, 3.8, 1.5, 0.3, "setosa"],
        [5.4, 3.4, 1.7, 0.2, "setosa"],
        [5.1, 3.7, 1.5, 0.4, "setosa"],
        [4.6, 3.6, 1.0, 0.2, "setosa"],
        [5.1, 3.3, 1.7, 0.5, "setosa"],
        [4.8, 3.4, 1.9, 0.2, "setosa"],
        [5.0, 3.0, 1.6, 0.2, "setosa"],
        [5.0, 3.4, 1.6, 0.4, "setosa"],
        [5.2, 3.5, 1.5, 0.2, "setosa"],
        [5.2, 3.4, 1.4, 0.2, "setosa"],
        [4.7, 3.2, 1.6, 0.2, "setosa"],
        [4.8, 3.1, 1.6, 0.2, "setosa"],
        [5.4, 3.4, 1.5, 0.4, "setosa"],
        [5.2, 4.1, 1.5, 0.1, "setosa"],
        [5.5, 4.2, 1.4, 0.2, "setosa"],
        [4.9, 3.1, 1.5, 0.1, "setosa"],
        [5.0, 3.2, 1.2, 0.2, "setosa"],
        [5.5, 3.5, 1.3, 0.2, "setosa"],
        [4.9, 3.1, 1.5, 0.1, "setosa"],
        [4.4, 3.0, 1.3, 0.2, "setosa"],
        [5.1, 3.4, 1.5, 0.2, "setosa"],
        [5.0, 3.5, 1.3, 0.3, "setosa"],
        [4.5, 2.3, 1.3, 0.3, "setosa"],
        [4.4, 3.2, 1.3, 0.2, "setosa"],
        [5.0, 3.5, 1.6, 0.6, "setosa"],
        [5.1, 3.8, 1.9, 0.4, "setosa"],
        [4.8, 3.0, 1.4, 0.3, "setosa"],
        [5.1, 3.8, 1.6, 0.2, "setosa"],
        [4.6, 3.2, 1.4, 0.2, "setosa"],
        [5.3, 3.7, 1.5, 0.2, "setosa"],
        [5.0, 3.3, 1.4, 0.2, "setosa"],
        [7.0, 3.2, 4.7, 1.4, "versicolor"],
        [6.4, 3.2, 4.5, 1.5, "versicolor"],
        [6.9, 3.1, 4.9, 1.5, "versicolor"],
        [5.5, 2.3, 4.0, 1.3, "versicolor"],
        [6.5, 2.8, 4.6, 1.5, "versicolor"],
        [5.7, 2.8, 4.5, 1.3, "versicolor"],
        [6.3, 3.3, 4.7, 1.6, "versicolor"],
        [4.9, 2.4, 3.3, 1.0, "versicolor"],
        [6.6, 2.9, 4.6, 1.3, "versicolor"],
        [5.2, 2.7, 3.9, 1.4, "versicolor"],
        [5.0, 2.0, 3.5, 1.0, "versicolor"],
        [5.9, 3.0, 4.2, 1.5, "versicolor"],
        [6.0, 2.2, 4.0, 1.0, "versicolor"],
        [6.1, 2.9, 4.7, 1.4, "versicolor"],
        [5.6, 2.9, 3.6, 1.3, "versicolor"],
        [6.7, 3.1, 4.4, 1.4, "versicolor"],
        [5.6, 3.0, 4.5, 1.5, "versicolor"],
        [5.8, 2.7, 4.1, 1.0, "versicolor"],
        [6.2, 2.2, 4.5, 1.5, "versicolor"],
        [5.6, 2.5, 3.9, 1.1, "versicolor"],
        [5.9, 3.2, 4.8, 1.8, "versicolor"],
        [6.1, 2.8, 4.0, 1.3, "versicolor"],
        [6.3, 2.5, 4.9, 1.5, "versicolor"],
        [6.1, 2.8, 4.7, 1.2, "versicolor"],
        [6.4, 2.9, 4.3, 1.3, "versicolor"],
        [6.6, 3.0, 4.4, 1.4, "versicolor"],
        [6.8, 2.8, 4.8, 1.4, "versicolor"],
        [6.7, 3.0, 5.0, 1.7, "versicolor"],
        [6.0, 2.9, 4.5, 1.5, "versicolor"],
        [5.7, 2.6, 3.5, 1.0, "versicolor"],
        [5.5, 2.4, 3.8, 1.1, "versicolor"],
        [5.5, 2.4, 3.7, 1.0, "versicolor"],
        [5.8, 2.7, 3.9, 1.2, "versicolor"],
        [6.0, 2.7, 5.1, 1.6, "versicolor"],
        [5.4, 3.0, 4.5, 1.5, "versicolor"],
        [6.0, 3.4, 4.5, 1.6, "versicolor"],
        [6.7, 3.1, 4.7, 1.5, "versicolor"],
        [6.3, 2.3, 4.4, 1.3, "versicolor"],
        [5.6, 3.0, 4.1, 1.3, "versicolor"],
        [5.5, 2.5, 4.0, 1.3, "versicolor"],
        [5.5, 2.6, 4.4, 1.2, "versicolor"],
        [6.1, 3.0, 4.6, 1.4, "versicolor"],
        [5.8, 2.6, 4.0, 1.2, "versicolor"],
        [5.0, 2.3, 3.3, 1.0, "versicolor"],
        [5.6, 2.7, 4.2, 1.3, "versicolor"],
        [5.7, 3.0, 4.2, 1.2, "versicolor"],
        [5.7, 2.9, 4.2, 1.3, "versicolor"],
        [6.2, 2.9, 4.3, 1.3, "versicolor"],
        [5.1, 2.5, 3.0, 1.1, "versicolor"],
        [5.7, 2.8, 4.1, 1.3, "versicolor"],
        [6.3, 3.3, 6.0, 2.5, "virginica"],
        [5.8, 2.7, 5.1, 1.9, "virginica"],
        [7.1, 3.0, 5.9, 2.1, "virginica"],
        [6.3, 2.9, 5.6, 1.8, "virginica"],
        [6.5, 3.0, 5.8, 2.2, "virginica"],
        [7.6, 3.0, 6.6, 2.1, "virginica"],
        [4.9, 2.5, 4.5, 1.7, "virginica"],
        [7.3, 2.9, 6.3, 1.8, "virginica"],
        [6.7, 2.5, 5.8, 1.8, "virginica"],
        [7.2, 3.6, 6.1, 2.5, "virginica"],
        [6.5, 3.2, 5.1, 2.0, "virginica"],
        [6.4, 2.7, 5.3, 1.9, "virginica"],
        [6.8, 3.0, 5.5, 2.1, "virginica"],
        [5.7, 2.5, 5.0, 2.0, "virginica"],
        [5.8, 2.8, 5.1, 2.4, "virginica"],
        [6.4, 3.2, 5.3, 2.3, "virginica"],
        [6.5, 3.0, 5.5, 1.8, "virginica"],
        [7.7, 3.8, 6.7, 2.2, "virginica"],
        [7.7, 2.6, 6.9, 2.3, "virginica"],
        [6.0, 2.2, 5.0, 1.5, "virginica"],
        [6.9, 3.2, 5.7, 2.3, "virginica"],
        [5.6, 2.8, 4.9, 2.0, "virginica"],
        [7.7, 2.8, 6.7, 2.0, "virginica"],
        [6.3, 2.7, 4.9, 1.8, "virginica"],
        [6.7, 3.3, 5.7, 2.1, "virginica"],
        [7.2, 3.2, 6.0, 1.8, "virginica"],
        [6.2, 2.8, 4.8, 1.8, "virginica"],
        [6.1, 3.0, 4.9, 1.8, "virginica"],
        [6.4, 2.8, 5.6, 2.1, "virginica"],
        [7.2, 3.0, 5.8, 1.6, "virginica"],
        [7.4, 2.8, 6.1, 1.9, "virginica"],
        [7.9, 3.8, 6.4, 2.0, "virginica"],
        [6.4, 2.8, 5.6, 2.2, "virginica"],
        [6.3, 2.8, 5.1, 1.5, "virginica"],
        [6.1, 2.6, 5.6, 1.4, "virginica"],
        [7.7, 3.0, 6.1, 2.3, "virginica"],
        [6.3, 3.4, 5.6, 2.4, "virginica"],
        [6.4, 3.1, 5.5, 1.8, "virginica"],
        [6.0, 3.0, 4.8, 1.8, "virginica"],
        [6.9, 3.1, 5.4, 2.1, "virginica"],
        [6.7, 3.1, 5.6, 2.4, "virginica"],
        [6.9, 3.1, 5.1, 2.3, "virginica"],
        [5.8, 2.7, 5.1, 1.9, "virginica"],
        [6.8, 3.2, 5.9, 2.3, "virginica"],
        [6.7, 3.3, 5.7, 2.5, "virginica"],
        [6.7, 3.0, 5.2, 2.3, "virginica"],
        [6.3, 2.5, 5.0, 1.9, "virginica"],
        [6.5, 3.0, 5.2, 2.0, "virginica"],
        [6.2, 3.4, 5.4, 2.3, "virginica"],
        [5.9, 3.0, 5.1, 1.8, "virginica"],
    ],
)


# Test class for the Extractor
class TestExtractor:
    def test_extract_from_csv_success(self, capsys):
        # Setup
        path = r"C:\Users\Sam\code\etl_application\etl_application\data\iris.csv"

        # Instantiate and invoke the extractor
        extractor = Extractor("csv")
        result = extractor.extract(path)

        # Assertions
        assert result.notnull
        captured = capsys.readouterr().out
        assert "Data extracted from CSV successfully!" in captured  # checks stdout
        pd.testing.assert_frame_equal(result, expected_data)
        assert (
            "An error occurred while reading the CSV file: File not found"
            not in captured
        )

    def test_extract_from_csv_failure(self, capsys):
        # Setup
        test_path = "nonexistent/path.csv"

        # Instantiate and invoke the extractor
        extractor = Extractor("csv")
        result = extractor.extract(test_path)

        # Assertions
        assert result.empty
        assert (
            "An error occurred while reading the CSV file: [Errno 2] No such file or directory: 'nonexistent/path.csv'\n"
            in capsys.readouterr().out
        )

    def test_extract_from_database_success(self, mocker, capsys):
        # Setup
        test_query = "SELECT * FROM employees"
        test_connection_string = "sqlite:///:memory:"
        mock_data = pd.DataFrame(
            {
                "id": [1, 2],
                "name": ["Sam Sheen", "Tom Sheen"],
                "age": [30, 25],
                "department": ["Data Engineering", "Software Engineering"],
            }
        )

        # Mock sqlalchemy create_engine and pandas read_sql
        mock_engine = mocker.patch("sqlalchemy.create_engine", autospec=True)
        mock_connection = (
            mock_engine.return_value.connect.return_value.__enter__.return_value
        )
        mocker.patch("pandas.read_sql", return_value=mock_data)

        # Instantiate and invoke the extractor
        extractor = Extractor("sqlite")
        result = extractor.extract(test_connection_string, test_query)

        # Assertions
        pd.testing.assert_frame_equal(result, mock_data)
        assert "Data extracted from database successfully!" in capsys.readouterr().out

    def test_extract_from_database_failure(self, capsys):
        # Setup
        test_query = "SELECT * FROM employees"
        test_connection_string = "sqlite:///:memory:"

        extractor = Extractor("sqlite")
        result = extractor.extract(test_connection_string, test_query)

        # Assertions
        assert result.empty
        captured = capsys.readouterr().out
        assert "Data extracted from database successfully!" not in captured
        assert (
            "An error occurred while extracting data from the database: (sqlite3.OperationalError) no such table: employees"
            in captured
        )
