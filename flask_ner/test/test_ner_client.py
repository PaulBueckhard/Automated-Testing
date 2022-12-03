import unittest

from flask_ner.test.test_doubles import NerModelTestDouble

class TestNerClient(unittest.TestCase):

    # { ents: [{...}],
    #   html: "<span>..."}
    
    def test_get_ents_returns_dictionary_given_empty_string(self):
        model = NerModelTestDouble("eng")
        model.returns_doc_ents([])
        ner = NerModelTestDouble(model)
        ents = ner.get_ents("")
        self.assertIsInstance(ents, dict)
    
    def test_get_ents_returns_dictionary_given_nonempty_string(self):
        model = NerModelTestDouble("eng")
        model.returns_doc_ents([])
        ner = NerModelTestDouble(model)
        ents = ner.get_ents("Berlin is the capital of Germany")
        self.assertIsInstance(ents, dict)

    def test_get_ents_given_spacy_person_is_returned(self):
        model = NerModelTestDouble("eng")
        doc_ents = [{"text": "Nikola Tesla", "label_": "PERSON"}]
        model.returns_doc_ents(doc_ents)
        ner = NerModelTestDouble(model)
        result = ner.get_ents("...")
        expected_result = { "ents": [{"ent": "Nikola Tesla", "label": "Person"}], "html": "" }
        self.assertListEqual(result["ents"], expected_result["ents"])

    def test_get_ents_given_spacy_norp_is_returned(self):
        model = NerModelTestDouble("eng")
        doc_ents = [{"text": "German", "label_": "NORP"}]
        model.returns_doc_ents(doc_ents)
        ner = NerModelTestDouble(model)
        result = ner.get_ents("...")
        expected_result = { "ents": [{"ent": "German", "label": "Group"}], "html": "" }
        self.assertListEqual(result["ents"], expected_result["ents"])

    def test_get_ents_given_spacy_loc_is_returned(self):
        model = NerModelTestDouble("eng")
        doc_ents = [{"text": "the ocean", "label_": "LOC"}]
        model.returns_doc_ents(doc_ents)
        ner = NerModelTestDouble(model)
        result = ner.get_ents("...")
        expected_result = { "ents": [{"ent": "the ocean", "label": "Location"}], "html": "" }
        self.assertListEqual(result["ents"], expected_result["ents"])

    def test_get_ents_given_spacy_language_is_returned(self):
        model = NerModelTestDouble("eng")
        doc_ents = [{"text": "sign language", "label_": "LANGUAGE"}]
        model.returns_doc_ents(doc_ents)
        ner = NerModelTestDouble(model)
        result = ner.get_ents("...")
        expected_result = { "ents": [{"ent": "sign language", "label": "Language"}], "html": "" }
        self.assertListEqual(result["ents"], expected_result["ents"])

    def test_get_ents_given_spacy_gpe_is_returned(self):
        model = NerModelTestDouble("eng")
        doc_ents = [{"text": "Australia", "label_": "GPE"}]
        model.returns_doc_ents(doc_ents)
        ner = NerModelTestDouble(model)
        result = ner.get_ents("...")
        expected_result = { "ents": [{"ent": "Australia", "label": "Location"}], "html": "" }
        self.assertListEqual(result["ents"], expected_result["ents"])

    def test_get_ents_given_multiple_ents(self):
        model = NerModelTestDouble("eng")
        doc_ents = [{"text": "Nikola Tesla", "label_": "PERSON"}, {"text": "Serbia", "label_": "LOC"}]
        model.returns_doc_ents(doc_ents)
        ner = NerModelTestDouble(model)
        result = ner.get_ents("...")
        expected_result = { "ents": 
                [{"ent": "Nikola Tesla", "label": "Person"},
                 {"ent": "Serbia",       "label": "Location"}], "html": "" }
        self.assertListEqual(result["ents"], expected_result["ents"])