import pandas as pd

def preprocess_data(df):
    # Example: Handle missing values
    df = df.dropna()
    
    # Example: Convert categorical variables into dummy/indicator variables
    df = pd.get_dummies(df)
    
    return df

if _name_ == "_main_":
    data = pd.read_csv("../data/full_filled_stroke_data.csv")
    clean_data = preprocess_data(data)
    clean_data.to_csv("../data/clean_stroke_data.csv", index=False)