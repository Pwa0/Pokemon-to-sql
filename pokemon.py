import requests
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="Test",
  password="Test",
  database="pokemon"
)

mycursor = mydb.cursor()
mycursor.execute("DROP TABLE IF EXISTS pokemon;")
mycursor.execute("CREATE TABLE pokemon (naam varchar(255), id int not null AUTO_INCREMENT, height int, weight int, PRIMARY KEY (id));")

for x in range(1, 151):
   
    r = requests.get(f"https://pokeapi.co/api/v2/pokemon/{x}")
    r.raise_for_status()
    jsonResponse = r.json()
    sql = "INSERT INTO pokemon (naam, id, height, weight) VALUES (%s, %s, %s, %s)"
    val = jsonResponse["forms"][0]["name"], jsonResponse["id"], jsonResponse["height"], jsonResponse["weight"]
    mycursor.execute(sql, val)
    mydb.commit()
    


