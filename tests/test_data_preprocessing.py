import pandas as pd
from src.data_preprocessing import preprocess_data

def test_preprocess_data():
    # Load sample data
    sample_data = {
        'age': [45, None, 67],
        'bmi': [22.3, 25.6, None],
        'smoking_status': ['never', 'formerly', 'currently']
    }
    df = pd.DataFrame(sample_data)
    
    # Preprocess data
    processed_data = preprocess_data(df)
    
    # Check if missing values are handled
    assert processed_data.isnull().sum().sum() == 0

if __name__ == "__main__":
    test_preprocess_data()
