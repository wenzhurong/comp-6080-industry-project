import spacy

class SeniorityExtractor:
    def __init__(self, nlp_model='en_core_web_sm'):
        self.nlp = spacy.load(nlp_model)
        self.unique_labels = None  # 通过set_labels方法设置

    def set_labels(self, labels):
        self.unique_labels = labels

    def extract_seniority(self, text):
        doc = self.nlp(text)
        lemmas = [token.lemma_ for token in doc]

        for label in self.unique_labels:
            if all(kw in lemmas for kw in label.lower().split()):
                return label
        return "intermediate"
