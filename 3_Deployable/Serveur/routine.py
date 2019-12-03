import schedule
import time
import os


# Fonction call_script appelle le fichier python que l'on veut reveiller
def call_script():
	# A inserer le fichier .py que l'on veut reveiller chaque jour, le fichier doit etre dans le meme dossier que celui que l'on veut reveiller, ici test sur testRoutine.py
	os.system('python testRoutine.py args')


# Appelle la fonction call script qui va appeler le script python tous les jours à 10h
schedule.every().day.at('10:00').do(call_script)

# Boucle infinie afin de pouvoir appeler la fonction au moment predefini 
while True:
	schedule.run_pending()
	time.sleep(1)

