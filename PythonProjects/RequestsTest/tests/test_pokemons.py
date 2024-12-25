import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '8f895f1e2bd16919617034cc761a79bb'
HEADER = {'trainer_token' : '8f895f1e2bd16919617034cc761a79bb'}
TRAINER_ID = '12682'

def test_status_code ():
    response = requests.get(url=f'{URL}/pokemons', params = {'trainer_id':TRAINER_ID})
    assert response.status_code == 200

def test_part_of_respones():
 response_get = requests.get(url=f'{URL}/pokemons', params={'trainer_id':TRAINER_ID})
 assert response_get.json() ['name']=='первый'