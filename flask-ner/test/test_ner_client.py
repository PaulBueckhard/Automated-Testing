import unittest
from ner_client import NamedEntityClient
from test_doubles import NerModelTestDouble

class TestNerClient(unittest.TestCase):

    # { ents: [{...}],
    #   html: "<span>..."}
    
    def test_get_ents_returns_dictionary_given_empty_string(self):
        model = NerModelTestDouble("eng")
        model.returns_doc_ents([])
        ner = NamedEntityClient(model)
        ents = ner.get_ents("")
        self.assertIsInstance(ents, dict)
    
    def test_get_ents_returns_dictionary_given_nonempty_string(self):
        model = NerModelTestDouble("eng")
        ner = NamedEntityClient(model)
        ents = ner.get_ents("Berlin is the capital of Germany")
        self.assertIsInstance(ents, dict)