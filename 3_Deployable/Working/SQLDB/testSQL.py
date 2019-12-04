import pymysql

#http://phpmyadmin.cluster026.hosting.ovh.net/

cnx=pymysql.connect(host="phpmyadmin.cluster026.hosting.ovh.net",
                  user="devisenfdhruche",
                  passwd="CNB1Ruche",
                  db="devisenfdhruche.mysql.db")
print("lol")
cnx.close()