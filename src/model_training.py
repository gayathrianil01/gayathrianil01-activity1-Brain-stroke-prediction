import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

def train_model(X_train, y_train):
    model = RandomForestClassifier()
    model.fit(X_train, y_train)
    return model

if __name__ == "__main__":
    data = pd.read_csv("../data/clean_stroke_data.csv")
    X = data.drop('target_column', axis=1)
    y = data['target_column']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    model = train_model(X_train, y_train)
    # Save model (optional)
