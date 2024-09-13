# MySQL Connector plugin testausta - connect to db ihmiset

import mysql.connector

yhteys = mysql.connector.connect(
  host='127.0.0.1',
  port= 3306,
  database='ihmiset',
  user='tontsah',
  password='tontsah1234',
  autocommit=True
)
