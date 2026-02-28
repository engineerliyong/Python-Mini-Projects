import pandas as pd

def load_csv(file_path):
    #Load a CSV file into a pandas DataFrame.
    try:
        df = pd.read_csv(file_path)
        print(f" CSV file '{file_path}' loaded successfully.\n")
        return df
    except Exception as e:
        print(f" Error loading CSV file: {e}")
        return None


def show_basic_info(df):
    #Display basic information about the dataset.
    print(" BASIC DATASET INFORMATION")
    print("-" * 30)
    print(f"Number of rows: {df.shape[0]}")
    print(f"Number of columns: {df.shape[1]}\n")

    print(" Column Data Types")
    print(df.dtypes, "\n")

    print(" First 5 rows of the dataset")
    print(df.head(), "\n")


def clean_data(df):
    #Handle missing values in the dataset.
    print(" CLEANING DATA")
    print("-" * 30)

    print("Missing values before cleaning:")
    print(df.isnull().sum(), "\n")

    # Fill numeric columns with mean
    numeric_columns = df.select_dtypes(include="number")
    df[numeric_columns.columns] = numeric_columns.fillna(numeric_columns.mean())

    # Fill non-numeric columns with 'Unknown'
    categorical_columns = df.select_dtypes(exclude="number")
    df[categorical_columns.columns] = categorical_columns.fillna("Unknown")

    print("Missing values after cleaning:")
    print(df.isnull().sum(), "\n")

    return df


def analyze_data(df):
    #Perform basic statistical analysis.
    print("📈 DATA ANALYSIS")
    print("-" * 30)

    print("Statistical Summary:")
    print(df.describe(), "\n")

    # Example: analyze 'Score' column if it exists
    if "Score" in df.columns:
        print("Score Analysis:")
        print(f"Average Score: {df['Score'].mean():.2f}")
        print(f"Highest Score: {df['Score'].max()}")
        print(f"Lowest Score: {df['Score'].min()}")
    else:
        print("No 'Score' column found for detailed analysis.")


if __name__ == "__main__":
    file_path = "sample_data.csv"  

    data = load_csv(file_path)

    if data is not None:
        show_basic_info(data)
        data = clean_data(data)
        analyze_data(data)

    
