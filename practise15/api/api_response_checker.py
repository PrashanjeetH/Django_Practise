from django.dispatch import receiver
import requests
import json

URL = "http://127.0.0.1:8000/api/student_info/"


def check_student_list(id = None):
    data = {}
    if id is not None:
        data = {'id':id}
    json_data = json.dumps(data)
    response = requests.get(url=URL, data=json_data)
    return response


def create_student():
    data = {
        # 'name' : '',
        'roll_no': '122',
        'city': 'Mumbai',
    }
    json_data = json.dumps(data)
    response = requests.post(url=URL, data=json_data)
    return response

def update_student_data():
    data = {
        'id': 2,
        'name' : 'nameChange',
        'roll_no': '212',
        'city': 'CityChange',
    }
    json_data = json.dumps(data)
    response = requests.put(url=URL, data=json_data)
    return response

def delete_student():
    data = {'id': 3}
    json_data = json.dumps(data)
    response = requests.patch(url=URL, data=json_data)
    return response

if  __name__ == '__main__':

    # response = check_student_list(1)
    response = create_student()
    # response = update_student_data()
    # response = delete_student()
    received_data = response.json()
    print(received_data)