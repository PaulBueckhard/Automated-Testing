import unittest
import json
from flask import request

from flask_ner.app import app

class TestApi(unittest.TestCase):

    def test_ner_enpoint_given_json_body_with_empty_entities_returns_success(self):
        with app.test_client() as client:
            response = client.post("/ner", json={"sentence": ""})
            assert response._status_code == 200

    def test_ner_enpoint_given_empty_json_body_returns_error(self):
        with app.test_client() as client:
            response = client.post("/ner", json={})
            assert response._status_code == 500

    def test_ner_endpoint_given_json_body_returns_success(self):
        with app.test_client() as client:
            response = client.post("/ner", json={"sentence": "Steve Malkmus is in the band pavement."})
            assert response._status_code == 200

    def test_ner_endpoint_given_json_body_with_person_returns_entity_result(self):
        with app.test_client() as client:
            response = client.post("/ner", json={"sentence": "Kamala Harris"})
            data = json.loads(response.get_data())
            print(data)
            assert data["entities"][0]["ent"] == "Kamala Harris"
            assert data["entities"][0]["label"] == "Person"

    def test_ner_endpoint_given_json_body_with_group_returns_entity_result(self):
        with app.test_client() as client:
            response = client.post("/ner", json={"sentence": "British"})
            data = json.loads(response.get_data())
            print(data)
            assert data["entities"][0]["ent"] == "British"
            assert data["entities"][0]["label"] == "Group"

    def test_ner_endpoint_given_json_body_with_location_returns_entity_result(self):
        with app.test_client() as client:
            response = client.post("/ner", json={"sentence": "Italy"})
            data = json.loads(response.get_data())
            print(data)
            assert data["entities"][0]["ent"] == "Italy"
            assert data["entities"][0]["label"] == "Location"

    def test_ner_endpoint_given_json_body_with_person_returns_entity_result(self):
        with app.test_client() as client:
            response = client.post("/ner", json={"sentence": "Spanish"})
            data = json.loads(response.get_data())
            print(data)
            assert data["entities"][0]["ent"] == "Spanish"
            assert data["entities"][0]["label"] == "Language"