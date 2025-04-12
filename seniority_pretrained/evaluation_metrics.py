from sklearn.metrics import f1_score, classification_report

def evaluate_predictions(y_true, y_pred):
    return {
        "f1_weighted": f1_score(y_true, y_pred, average='weighted'),
        "classification_report": classification_report(y_true, y_pred)
    }
