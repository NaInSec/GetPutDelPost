# Script Get,Put,Del,Post - Code By Sachi Henakyy.

import requests
import json
import xml.etree.ElementTree as ET

def get_request(url):
    response = requests.get(url)
    try:
        return response.json()
    except ValueError:
        try:
            xml_root = ET.fromstring(response.text)
            xml_dict = xml_to_dict(xml_root)
            return xml_dict
        except ET.ParseError:
            return response.text

def put_request(url, data):
    response = requests.put(url, json=data)
    try:
        return response.json()
    except ValueError:
        try:
            xml_root = ET.fromstring(response.text)
            xml_dict = xml_to_dict(xml_root)
            return xml_dict
        except ET.ParseError:
            return response.text

def delete_request(url):
    response = requests.delete(url)
    return {'status_code': response.status_code}

def post_request(url, data):
    response = requests.post(url, json=data)
    try:
        return response.json()
    except ValueError:
        try:
            xml_root = ET.fromstring(response.text)
            xml_dict = xml_to_dict(xml_root)
            return xml_dict
        except ET.ParseError:
            return response.text

def xml_to_dict(xml_root):
    xml_dict = {}
    for child in xml_root:
        xml_dict[child.tag] = child.text
    return xml_dict

url = input("Masukkan URL: ")

get_data = get_request(url)
if isinstance(get_data, dict):
    with open('get_response.json', 'w') as file:
        json.dump(get_data, file, indent=4)
else:
    with open('get_response.txt', 'w') as file:
        file.write(get_data)

put_data = {'key': 'value'}
put_data_response = put_request(url, put_data)
if isinstance(put_data_response, dict):
    with open('put_response.json', 'w') as file:
        json.dump(put_data_response, file, indent=4)
else:
    with open('put_response.txt', 'w') as file:
        file.write(put_data_response)

delete_response = delete_request(url)
with open('delete_response.json', 'w') as file:
    json.dump(delete_response, file, indent=4)

post_data = {'key': 'value'}
post_data_response = post_request(url, post_data)
if isinstance(post_data_response, dict):
    with open('post_response.json', 'w') as file:
        json.dump(post_data_response, file, indent=4)
else:
    with open('post_response.txt', 'w') as file:
        file.write(post_data_response)
