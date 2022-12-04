from flask_ner.ner_client import NamedEntityClient

class NerModelTestDouble(NamedEntityClient):

    def __init__(self, model):
        self.model = model

    def get_ents(self, sentence):
        doc = self.model(sentence)
        entities = [{ 'ent': ent.text, 'label': self.map_label(ent.label_) } for ent in doc.ents]
        return { 'ents': entities, 'html': "" }

    def returns_doc_ents(self, ents):
        self.ents = ents 

    def __call__(self, sent):
        return DocTestDouble(sent, self.ents)

class DocTestDouble:
    def __init__(self, sent, ents): 
        self.ents = [SpanTestDouble(ent['text'], ent['label_']) for ent in ents]

class SpanTestDouble:
    def __init__(self, text, label):
        self.text = text
        self.label_ = label