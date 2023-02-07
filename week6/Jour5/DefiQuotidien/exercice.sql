import psycopg2
import requests
from random import randint
HOSTNAME = 'localhost'
USERNAME = 'postgres'
PASSWORD = '   '
DATABASE = 'postgres'

def api_pays():
    # request =requests.get('https://restcountries.com/v3.1/region/africa')
    request =requests.get('https://restcountries.com/v2/all')
    request=request.json()
    return request

data=api_pays()

# print(data[0]['name'])
# print(data[0]['flag'])
# print(data[0]['subregion'])
# print(data[0]['population'])

connection=psycopg2.connect(host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE)
cursor=connection.cursor()
for i in range (10):
    country=data[randint(1,200)]
    query=f"INSERT INTO pays(names,flag,subregion,population)VALUES ('{country['name']}','{country['flag']}','{country['subregion']}',{country['population']})"
    cursor.execute(query)
connection.commit()
connection.close()