"""
pokemons tests api
"""
#создание покемона
import requests
import pytest
URL = 'https://api.pokemonbattle.me:9104'
HEADER = {'Content-Type': 'application/json'}
HEADER = {'trainer_token': 'c48f5a0318461595d4ae125278759d03'}
body = {
    "name": "Лаврик",
    "photo": "https://dolnikov.ru/pokemons/albums/001.png"
 }

response =requests.post(url=f'{URL}/pokemons', json=body, headers=HEADER)
print(f'Статус код: {response.status_code}. Сообщение: {response.text}')



#Обновление информации о покемоне
import requests
URL = 'https://api.pokemonbattle.me:9104'
HEADER = {'Content-Type': 'application/json'}
HEADER = {'trainer_token': 'c48f5a0318461595d4ae125278759d03'}
body = {
    "pokemon_id": "28273",
    "name": "Чемпион",
    "photo": "https://dolnikov.ru/pokemons/albums/008.png"
}

response =requests.put(url=f'{URL}/pokemons', json=body, headers=HEADER)
print(f'Статус код: {response.status_code}. Сообщение: {response.text}')




#Поймать в покебол
import requests
import pytest
URL = 'https://api.pokemonbattle.me:9104'
HEADER = {'Content-Type': 'application/json'}
HEADER = {'trainer_token': 'c48f5a0318461595d4ae125278759d03'}
body = {
    "pokemon_id": "28273"
}

response =requests.post(url=f'{URL}/trainers/add_pokeball', json=body, headers=HEADER)
print(f'Статус код: {response.status_code}. Сообщение: {response.text}')
