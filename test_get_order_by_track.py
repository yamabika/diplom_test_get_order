# Столбов Николай, 7-я когорта — Финальный проект. Инженер по тестированию плюс

import requests
import pytest

URL_SERVICE = "https://df50e91a-1dcf-453f-9865-0053d91253c1.serverhub.praktikum-services.ru"
CREATE_ORDER = "/api/v1/orders/"
GET_ORDER = "/api/v1/orders/track/"

# Открытие фикстуры
# Шаг 1: Выполнить запрос на создание заказа
@pytest.fixture
def created_order():
    order_data = {
        "firstName": "Антон",
        "lastName": "Убдурахмангаджи",
        "address": "Центральный проезд Хорошёвского Серебряного Бора 2",
        "metroStation": 204,
        "phone": "+34916123451",
        "rentTime": 5,
        "deliveryDate": "2023-08-17",
        "comment": "Привет, Абдурахмангаджи!"
    }
    response = requests.post(URL_SERVICE + CREATE_ORDER, json=order_data)
    assert response.status_code == 201

    # Шаг 2: Сохранить номер трека заказа
    track_number = response.json()["track"]
    # Закрытие фикстуры
    yield track_number

    # Начало теста
def test_get_order_by_track(created_order):
    # Шаг 3: Выполнить запрос на получение заказа по треку
    response = requests.get(URL_SERVICE + GET_ORDER, params={"t": created_order})
    # Шаг 4: Проверить, что код ответа равен 200
    assert response.status_code == 200