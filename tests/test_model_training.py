import pandas as pd
from sklearn.model_selection import train_test_split
from src.model_training import train_model

def test_train_model():
    # Sample data
    sample_data = {
        'feature1': [1, 2, 3, 4],
        'feature2': [10, 20, 30, 40],
        'target_column': [0, 1, 0, 1]
    }
    df = pd.DataFrame(sample_data)
    
    X = df.drop('target_column', axis=1)
    y = df['target_column']
    
    # Train test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    
    # Train model
    model = train_model(X_train, y_train)
    
    # Check if model is trained
    assert model is not None

if _name_ == "_main_":
    test_train_model()