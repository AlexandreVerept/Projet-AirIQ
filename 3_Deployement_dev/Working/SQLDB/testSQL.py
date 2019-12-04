import pymysql.cursors
import pandas as pd

#http://phpmyadmin.cluster026.hosting.ovh.net/
#phpmyadmin.cluster026.hosting.ovh.net:3306

connection=pymysql.connect(host="localhost",
                           user="root",
                           passwd="Gousse212",
                           db="devisenfdhruche",
                           cursorclass=pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursor:
        # Read a single record
        sql = "SELECT * FROM `RecuperationDonnees`;"
        cursor.execute(sql)
        result = cursor.fetchall()
finally:
    connection.close()
    
df = pd.DataFrame(result)
print(df)