import pandas as pd
from sqlalchemy import create_engine, Table, MetaData, Column, Integer, String


class Extractor:
    def __init__(self, extract_type="csv"):
        self.extract_type = extract_type.lower()
        self.extracted_data = pd.DataFrame()

    def extract(self, connection_string, query=None):
        if self.extract_type == "csv":
            self.extract_from_csv(connection_string)
        if self.extract_type == "sqlite":
            self.extract_from_database(connection_string, query)
        return self.extracted_data

    def extract_from_csv(self, file_path: str):
        """
        Extract data from a CSV file using pandas.

        :param file_path: str, the path to the CSV file.
        :return: pandas.DataFrame containing the data from the CSV file.
        """
        try:
            # Read data from CSV
            data = pd.read_csv(file_path)
            print("Data extracted from CSV successfully!")
            self.extracted_data = data
            return data
        except Exception as e:
            print(f"An error occurred while reading the CSV file: {e}")
            return pd.DataFrame()

    def extract_from_database(self, connection_string: str, query: str):
        """
        Extract data from a SQL database using pandas.

        :param connection_string: str, the database connection string.
        :param query: str, the SQL query to execute for data extraction.
        :return: pandas.DataFrame containing the data retrieved from the database.
        """
        try:
            # Create a database engine
            engine = create_engine(connection_string)
            # Connect to the database and execute the query
            with engine.connect() as connection:
                data = pd.read_sql(query, connection)
            print("Data extracted from database successfully!")
            self.extracted_data = data
            return data
        except Exception as e:
            print(f"An error occurred while extracting data from the database: {e}")
            return pd.DataFrame()


# Example usage
if __name__ == "__main__":
    # Extracting from a CSV file
    extractor = Extractor("CSV")
    extracted_csv_data = extractor.extract(
        r"C:\Users\Sam\code\etl_application\etl_application\data\iris.csv"
    )
    print(extracted_csv_data.head())  # Display the first few rows of the DataFrame

    # Prepping database for extraction
    #########
    db_connection_string = (
        r"sqlite:///C:\Users\Sam\code\etl_application\etl_application\data\sqlite.db"
    )
    engine = create_engine(db_connection_string)

    metadata = MetaData()
    employees = Table(
        "employees",
        metadata,
        Column("id", Integer, primary_key=True),
        Column("name", String),
        Column("age", Integer),
        Column("department", String),
    )
    metadata.drop_all(engine)
    metadata.create_all(engine)

    with engine.connect() as con:
        # Begin a transaction
        trans = con.begin()
        try:
            con.execute(
                employees.insert(),
                [
                    {"name": "Sam Sheen", "age": 30, "department": "Data Engineering"},
                    {
                        "name": "Tom Sheen",
                        "age": 25,
                        "department": "Software Engineering",
                    },
                ],
            )
            # Commit the transaction
            trans.commit()
        except:
            # Rollback the transaction in case of error
            trans.rollback()
            raise
    ######

    # Extracting from a Database
    extractor = Extractor("sqlite")
    sql_query = "SELECT * FROM employees"
    extracted_sqlite_data = extractor.extract(db_connection_string, sql_query)
    print(extracted_sqlite_data.head())
