from unicodedata import name
import requests
import json
import random
URL = "http://127.0.0.1:8000/class_based_api/student_info/"

names = ['Harry Luna','Brent Roberts','Gordon Waters','Marion Phelps','Mason Curtis','Derek Ballard','Glenn Phelps','Brandon Gross','Irene Gross','Melvin Munoz','Jerome Barber','Julian Clark','Gordon Jordan','Vernon Hicks','Rebecca Griffith',]
countries = ['Cuba','Nepal','Tristan da Cunha','Peru','Liechtenstein','South Africa','Timor-Leste','Uruguay','Tristan da Cunha','Bahamas','Nepal','Tristan da Cunha','Zimbabwe','Ireland','Micronesia','French Southern Territories','French Southern Territories','St. Vincent & Grenadines','Mongolia',]


def check_student_list(id = None):
    data = {}
    if id is not None:
        data = {'id':id}
    json_data = json.dumps(data)
    headers = {'content-Type': 'application/json'}
    response = requests.get(url=URL, data=json_data, headers=headers)
    return response


def create_student():
    data = {
        'name' : random.choice(names),
        'roll_no': random.randint(100, 999),
        'city': random.choice(countries),
    }
    print(f"Data created: {data}")
    headers = {'content-Type': 'application/json'}
    json_data = json.dumps(data)
    response = requests.post(url=URL, data=json_data, headers=headers)
    return response

def update_student_data():
    data = {
        'id' : '2',
        'name' : random.choice(names),
        'roll_no': random.randint(100, 999),
        'city': random.choice(countries),
    }
    headers = {'content-Type': 'application/json'}
    json_data = json.dumps(data)
    response = requests.put(url=URL, data=json_data, headers=headers)
    return response

def delete_student():
    data = {'id': 3}
    headers = {'content-Type': 'application/json'}
    json_data = json.dumps(data)
    response = requests.patch(url=URL, data=json_data, headers=headers)
    return response

if  __name__ == '__main__':

    response = check_student_list()
    # response = create_student()
    # response = update_student_data()
    # response = delete_student()
    received_data = response.json()
    print(received_data)