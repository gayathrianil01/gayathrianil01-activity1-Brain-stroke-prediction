from sklearn.metrics import accuracy_score, confusion_matrix

def evaluate_model(model, X_test, y_test):
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    conf_matrix = confusion_matrix(y_test, y_pred)
    return accuracy, conf_matrix

# Usage in the main block
if _name_ == "_main_":
    accuracy, conf_matrix = evaluate_model(model, X_test, y_test)
    print(f"Model Accuracy: {accuracy}")
    print(f"Confusion Matrix: \n{conf_matrix}")