#importation du module mysql.connector pour connecter python 

import mysql.connector

#definition la fonction get_connection() 
#modifier ces informations de connexion en fonction des vôtres

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="MYSQLNEWDEV@882004",
        database="gestion_stock",
        charset="utf8mb4",
        collation="utf8mb4_unicode_ci"
    )
