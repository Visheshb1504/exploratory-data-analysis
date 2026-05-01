import pandas as pd

def load_data():
    df = pd.read_csv('data/netflix_data.csv')
    return df

def basic_info(df):
    print("First 5 rows:")
    print(df.head(), "\n")

    print("Data Info:")
    df.info()
    print()

    print("Summary Statistics:")
    print(df.describe(), "\n")

def genre_analysis(df):
    print("Genre Distribution:")
    genre_counts = df['Genre'].value_counts()
    print(genre_counts, "\n")

def type_analysis(df):
    print("Content Type Distribution:")
    type_counts = df['Type'].value_counts()
    print(type_counts, "\n")

def year_analysis(df):
    print("Release Year Trend:")
    year_counts = df['Release_Year'].value_counts().sort_index()
    print(year_counts.tail(), "\n")

def country_analysis(df):
    print("Top Countries:")
    country_counts = df['Country'].value_counts()
    print(country_counts.head(), "\n")

def main():
    df = load_data()

    basic_info(df)
    genre_analysis(df)
    type_analysis(df)
    year_analysis(df)
    country_analysis(df)

if __name__ == "__main__":
    main()
