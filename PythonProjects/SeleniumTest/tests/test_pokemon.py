import requests
import pytest

URL = 'https://api.pokemonbattle.me:9104'
HEADER = {'Content-Type': 'application/json'}
def test_get_trainers():

    """
    Status code is 200
    """
    response = requests.get(url=f'{URL}/pokemons', params={'level':1}, headers=HEADER)
    assert response.status_code == 200, 'Unexpected status code'



URL = 'https://api.pokemonbattle.me:9104'
HEADER = {'Content-Type': 'application/json'}
def test_get_trainers_by_id():

    """
    test get trainers by id
    """
    response = requests.get(url=f'{URL}/trainers', params={'trainer_id':3516}, headers=HEADER)
    assert response.json()['trainer_name'] == 'Лев', ''
    


