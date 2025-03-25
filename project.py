import os
import pymysql
from urllib.request import urlopen
import re
import requests



db_config = {
    'host': os.getenv('DB_HOST', 'localhost'),
    'user': os.getenv('DB_USER', 'root'),
    'password': os.getenv('DB_PASSWORD', ''),
    'database': os.getenv('DB_NAME', 'mydatabase')
}


def get_user_input():
        user_input = input('Enter your name: ').strip()

        return user_input


def send_email(to, subject, body):
    os.system(f'echo {body} | mail -s "{subject}" {to}')



def get_data():
    url = 'http://insecure-api.com/get-data'
    try:
        response = requests.get(url, timeout=15)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None
    
