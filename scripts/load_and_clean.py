import pandas as pd

def load_data(path):
    return pd.read_csv(path)

def clean_data(df):
    df.columns = df.columns.str.lower().str.replace(' ', '_')
    df = df.dropna()
    return df

def main():
    raw_path = 'data/raw/meal_data.csv'
    clean_path = 'data/cleaned/meal_data_cleaned.csv'

    df = load_data(raw_path)
    df = clean_data(df)
    df.to_csv(clean_path, index=False)

if __name__ == '__main__':
    main()
