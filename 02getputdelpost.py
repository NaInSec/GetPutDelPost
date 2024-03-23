# Script Get,Put,Del,Post - Code By Sachi Henakyy.

import os
import requests
import json
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup

def create_folder(folder_name):
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

def save_to_json(data, file_path):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

def save_to_xml(data, file_path):
    root = ET.Element('root')
    xml_data = ET.SubElement(root, 'data')
    for key, value in data.items():
        sub_element = ET.SubElement(xml_data, key)
        sub_element.text = str(value)
    tree = ET.ElementTree(root)
    tree.write(file_path)

def save_to_txt(data, file_path):
    with open(file_path, 'w') as file:
        file.write(data)

def save_to_html(data, file_path):
    soup = BeautifulSoup(data, 'html.parser')
    with open(file_path, 'w') as file:
        file.write(soup.prettify())

def get_request(url, folder_path):
    response = requests.get(url)
    try:
        json_data = response.json()
        save_to_json(json_data, os.path.join(folder_path, 'get_response.json'))
    except ValueError:
        try:
            xml_root = ET.fromstring(response.text)
            xml_dict = xml_to_dict(xml_root)
            save_to_xml(xml_dict, os.path.join(folder_path, 'get_response.xml'))
        except ET.ParseError:
            save_to_txt(response.text, os.path.join(folder_path, 'get_response.txt'))
        else:
            save_to_html(response.text, os.path.join(folder_path, 'get_response.html'))

def post_request(url, data, folder_path):
    response = requests.post(url, json=data)
    try:
        json_data = response.json()
        save_to_json(json_data, os.path.join(folder_path, 'post_response.json'))
    except ValueError:
        try:
            xml_root = ET.fromstring(response.text)
            xml_dict = xml_to_dict(xml_root)
            save_to_xml(xml_dict, os.path.join(folder_path, 'post_response.xml'))
        except ET.ParseError:
            save_to_txt(response.text, os.path.join(folder_path, 'post_response.txt'))
        else:
            save_to_html(response.text, os.path.join(folder_path, 'post_response.html'))

def put_request(url, data, folder_path):
    response = requests.put(url, json=data)
    try:
        json_data = response.json()
        save_to_json(json_data, os.path.join(folder_path, 'put_response.json'))
    except ValueError:
        try:
            xml_root = ET.fromstring(response.text)
            xml_dict = xml_to_dict(xml_root)
            save_to_xml(xml_dict, os.path.join(folder_path, 'put_response.xml'))
        except ET.ParseError:
            save_to_txt(response.text, os.path.join(folder_path, 'put_response.txt'))
        else:
            save_to_html(response.text, os.path.join(folder_path, 'put_response.html'))

def delete_request(url, folder_path):
    response = requests.delete(url)
    save_to_json({'status_code': response.status_code}, os.path.join(folder_path, 'delete_response.json'))

def xml_to_dict(xml_root):
    xml_dict = {}
    for child in xml_root:
        xml_dict[child.tag] = child.text
    return xml_dict

url = input("Masukkan URL: ")
folder_name = input("Masukkan nama Folder Output: ")

create_folder(folder_name)
data = {'key': 'value'}
get_request(url, folder_name)
post_request(url, data, folder_name)
put_request(url, data, folder_name)
delete_request(url, folder_name)
