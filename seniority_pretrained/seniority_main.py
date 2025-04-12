import pandas as pd
from html_extractor import extract_text_from_html
from entity_extractor import SeniorityExtractor
from text_normalizer import normalize_text
from evaluation_metrics import evaluate_predictions

def main():
    df = pd.read_csv('../data/seniority_labelled_development_set.csv')

    df['clean_text'] = df['job_ad_details'].apply(extract_text_from_html)
    df['normalized_text'] = df['clean_text'].apply(normalize_text)

    extractor = SeniorityExtractor()
    extractor.set_labels(df['y_true'].unique().tolist())

    df['predicted_seniority'] = df['normalized_text'].apply(extractor.extract_seniority)

    results = evaluate_predictions(df['y_true'], df['predicted_seniority'])
    print(f"F1 Score: {results['f1_weighted']}")
    print(f"Classification Report:\n{results['classification_report']}")

if __name__ == "__main__":
    main()
