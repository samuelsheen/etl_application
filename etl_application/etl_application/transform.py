import pandas as pd

class DataTransformer:
    def __init__(self, data_frame: pd.DataFrame):
        self.df = data_frame

    def normalise_column_names(self):
        """Normalise all column names to lower case and replace spaces with underscores."""
        self.df.columns = [col.lower().replace(' ', '_') for col in self.df.columns]
    
    def fill_missing_values(self, column_name, fill_value):
        """Fill missing values in a specified column using a provided fill value."""
        if column_name in self.df.columns:
            self.df[column_name] = self.df[column_name].fillna(fill_value)
        else:
            raise ValueError(f"Column {column_name} not found in DataFrame")

    def convert_data_types(self, column_name, new_type):
        """Convert the data type of a specified column."""
        if column_name in self.df.columns:
            self.df[column_name] = self.df[column_name].astype(new_type)
        else:
            raise ValueError(f"Column {column_name} not found in DataFrame")

    def create_new_column(self, new_column_name, formula):
        """Create a new column based on a formula applied to existing columns."""
        self.df[new_column_name] = self.df.eval(formula)

    def drop_columns(self, columns_to_drop):
        """Drop specified columns from the DataFrame."""
        self.df = self.df.drop(columns=columns_to_drop)

    def get_transformed_data(self):
        """Return the transformed DataFrame."""
        return self.df

# Example usage
if __name__ == "__main__":
    # Create sample data
    data = {'Name': ['Alice', 'Bob', None], 'Age': [25, 30, 28], 'Salary': [50000, None, 42000]}
    df = pd.DataFrame(data)

    # Initialize the transformer
    transformer = DataTransformer(df)

    # Apply transformations
    transformer.normalise_column_names()
    transformer.fill_missing_values('name', 'Unknown')
    transformer.fill_missing_values('salary', 0)
    transformer.create_new_column('age_in_days', 'age * 365')
    transformer.drop_columns(['age'])
   
    # Get the transformed data
    transformed_df = transformer.get_transformed_data()
    print(transformed_df)

