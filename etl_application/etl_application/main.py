from extract import Extractor
from transform import DataTransformer
import pandas as pd


def main():

    ### Extract data
    extractor = Extractor("csv")
    extracted_csv_data = extractor.extract(
        r"C:\Users\Sam\code\etl_application\etl_application\data\iris.csv"
    )
    print("Extracted Data...")
    print(extracted_csv_data.head())

    ### Transform Data
    transformer = DataTransformer(extracted_csv_data)
    transformer.convert_data_types("species", "category")

    mean_sepal_length = extracted_csv_data["sepal_length"].mean()
    mean_sepal_width = extracted_csv_data["sepal_width"].mean()
    mean_petal_length = extracted_csv_data["petal_length"].mean()
    mean_petal_width = extracted_csv_data["petal_width"].mean()

    transformer.create_new_column(
        "Sepal length diff_from Mean", f"sepal_length - {mean_sepal_length}"
    )
    transformer.create_new_column(
        "SEPAL WIDTH DIFF FROM MEAN", f"sepal_width - {mean_sepal_width}"
    )
    transformer.create_new_column(
        "petal_length_diff_from_mean", f"petal_length - {mean_petal_length}"
    )
    transformer.create_new_column(
        "petal_width_diff_from_mean", f"petal_width - {mean_petal_width}"
    )

    transformer.normalise_column_names()

    print("Transformed Data...")
    print(transformer.get_transformed_data())


if __name__ == "__main__":
    main()
