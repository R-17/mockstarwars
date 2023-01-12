import json
from app import app


def test_say_hello_route_return_say_property():
    response = app.test_client().get('/character/1/movies')
    data = json.loads(response.data.decode('utf-8'))

    assert data['movies'] == [{"title": "A New Hope"}, {"title": "The Empire Strikes Back"}, {"title": "Return of the Jedi"}, {"title": "Revenge of the Sith"}, {"title": "The Force Awakens"} ]
    assert response.status_code == 200
