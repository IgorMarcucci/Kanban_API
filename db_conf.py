import os
import psycopg2

#  todo: implement .env credentials
conn = psycopg2.connect(
    host="localhost",
    database="Database",
    user=os.environ['DB_USERNAME'],
    password=os.environ['DB_PASSWORD'])