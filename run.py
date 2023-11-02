#! /usr/bin/env python3
import os
import requests
BASEPATH = '/data/feedback/' # varible with path
folder = os.listdir(BASEPATH)
list = []
for file in folder:
   with open(BASEPATH + file, 'r') as f:
       list.append({"title":f.readline().rstrip("\n"), # простой способ чтения данных из файлов с отзывами
           "name":f.readline().rstrip("\n"),
           "date":f.readline().rstrip("\n"),
           "feedback":f.read().rstrip("\n")})
for item in list:
   resp = requests.post('http://[corp-web-external-IP]/feedback/', json=item) #отправляет данные на сервер по одной записи за раз
   if resp.status_code != 201:
       raise Exception('POST error status={}'.format(resp.status_code))
   print('Created feedback ID: {}'.format(resp.json()["id"]))