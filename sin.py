import math
import numpy as np
import mysql.connector

inputValues = np.arange(0, 6*math.pi, 6*math.pi/999)
outputValues = []

mydb = mysql.connector.connect(
  host="172.17.0.5",
  user="root",
  password="admin",
  database="sinDB"
)

for value in inputValues:
    mycursor = mydb.cursor()
    outputValues.append(math.sin(value))
    sql = "INSERT INTO sinData (input, output) VALUES (%lf, %lf)"
    val = (value, math.sin(value))
    mycursor.execute(sql, val)
    mydb.commit()