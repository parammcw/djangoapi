import requests
import json

URL="http://localhost:8000/studentapi/"

def get_data(id=None):
    data={}
    if id is not None:
        data={'id':id}

    json_data=json.dumps(data)
    r=requests.get(url=URL, data=json_data)
    data=r.json()
    print(data)

# get_data()
# get_data(2)

def post_data():
    data={
        'name': 'Dileep',
        'roll': 103,
        'city': 'Gudgaon'
    }
    json_data=json.dumps(data)
    r=requests.post(url=URL, data=json_data)
    data=r.json()
    print(data)

# post_data()

def update_data():
    data={
        'id': 5,
        'name': 'Rohit',
        'city': 'Noida'
    }
    json_data=json.dumps(data)
    r=requests.put(url=URL, data=json_data)
    data=r.json()
    print(data)

# update_data()


def delete_data():
    data={'id': 5}
    json_data=json.dumps(data)
    r=requests.delete(url=URL, data=json_data)
    data=r.json()
    print(data)

delete_data()