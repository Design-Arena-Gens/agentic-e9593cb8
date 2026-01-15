from pathlib import Path
import pandas as pd


def main() -> None:
    data = [
        {"Make": "Ford", "Model": "Mustang", "Year": 2024, "Type": "Coupe", "MSRP": 31520},
        {"Make": "Chevrolet", "Model": "Corvette", "Year": 2024, "Type": "Sports", "MSRP": 68730},
        {"Make": "Tesla", "Model": "Model 3", "Year": 2024, "Type": "Sedan", "MSRP": 38990},
        {"Make": "Dodge", "Model": "Charger", "Year": 2023, "Type": "Sedan", "MSRP": 32230},
        {"Make": "Jeep", "Model": "Wrangler", "Year": 2024, "Type": "SUV", "MSRP": 31295},
    ]

    df = pd.DataFrame(data)
    output_path = Path("usa_cars.xlsx")
    df.to_excel(output_path, index=False, engine="openpyxl")

    print("Generated Excel file:", output_path.resolve())
    print()
    print("Data preview:")
    print(df.to_string(index=False))


if __name__ == "__main__":
    main()
