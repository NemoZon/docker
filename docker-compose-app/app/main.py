# Приложение выводит список баз данных из mongodb
from pymongo import MongoClient # Этот модуль не скачен на моем компьютере, но модуль будет установлен на образ
from pprint import pprint

MONGO_URL = "mongodb://mongo:27017" # Адрес другого сервиса с использование его имени указаного в composer и стандартным портом для базы данных
client = MongoClient(MONGO_URL)
db = client.admin
dbs_list = db.command("listDatabases")
pprint(dbs_list)

print("Exit")