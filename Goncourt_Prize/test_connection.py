
from daos.dao import Dao, get_connection

try:
	conn = get_connection()
	with conn.cursor() as cursor:
		cursor.execute("SELECT VERSION();")
		version = cursor.fetchone()
		print("Connexion OK. Version MySQL :", version)
except Exception as e:
	print("ERREUR de connexion :", e)