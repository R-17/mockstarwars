from unittest import TestCase
from unittest.mock import patch
import requests 
from services.star_wars_movies_service import *


class MockResponse:
    def __init__(self, json_data):
        self.json_data = json_data

    def json(self):
        return self.json_data


class TestMock(TestCase):

    def test_get_star_war_movies_names_return_expected(self):

        expected_names = ['A New Hope', 'The Empire Strikes Back',
                          'Return of the Jedi', 'Revenge of the Sith', 'The Force Awakens']

        responses = {
            'https://swapi.py4e.com/api/people/1': {
                'films': [
                    'https://swapi.py4e.com/api/films/1/',
                    'https://swapi.py4e.com/api/films/2/',
                    'https://swapi.py4e.com/api/films/3/',
                    'https://swapi.py4e.com/api/films/6/',
                    'https://swapi.py4e.com/api/films/7/',
                ]
            },
            'https://swapi.py4e.com/api/films/1/': {'title': 'A New Hope'},
            'https://swapi.py4e.com/api/films/2/': {'title': 'The Empire Strikes Back'},
            'https://swapi.py4e.com/api/films/3/': {'title': 'Return of the Jedi'},
            'https://swapi.py4e.com/api/films/6/': {'title': 'Revenge of the Sith'},
            'https://swapi.py4e.com/api/films/7/': {'title': 'The Force Awakens'},
        }


        with patch.object(requests, 'get', side_effect=lambda url: MockResponse(responses[url])):
            result = get_star_war_movies_names('1')

        assert result == expected_names