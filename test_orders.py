# Илья Семенихин, 29-я когорта — Финальный проект. Инженер по тестированию плюс
import sender_stand_request

def test_create_and_get_order_by_track():
    # Создаём заказ
    response = sender_stand_request.post_new_order()
    assert response.status_code == 201, "Ожидал 201 при создании заказа"
    
    track = response.json().get("track")
    assert track is not None, "track отсутствует в ответе"

    # Получаем заказ по треку
    response_get = sender_stand_request.get_order_by_track(track)
    assert response_get.status_code == 200, "Ожидал 200 при получении заказа по треку"

def test1_get_order_without_track():
    response = sender_stand_request.get_order_by_track("")
    assert response.status_code == 400, "Ожидал 400 при пустом параметре трека"


def test2_get_order_invalid_track():
    response = sender_stand_request.get_order_by_track(99999999)
    assert response.status_code == 404, "Ожидал 404 при несуществующем треке"