from datetime import date
def str_to_date(a):
    y, m, d = str(a).split('-')
    return date(int(y), int(m), int(d))

import string
import secrets

def generate_order_book():
    alphabet = string.digits
    order = ''.join(secrets.choice(alphabet) for i in range(8))
    return order

def message(order,from_date,to_date,num):
    mes = f'Здравствуйте вы успешно бронировали номер - {num} в нашем отеле с {from_date} до {to_date} ' \
          f' ваш код для выполнение операций {order}'
    return mes