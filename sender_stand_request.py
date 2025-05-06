import configuration
import requests
import data 

#Создание заказа
def post_new_order():
    return requests.post(configuration.URL + configuration.CREATE_ORDERS,
                         json=data.zakaz)
     
                         
def get_order_by_track(track_number):
    return requests.get(
        configuration.URL + configuration.GET_ORDERS,
        params={"t": track_number}
    )

