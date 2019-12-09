This section is in French as this is the instructions to setup the real time application on the school's server.

# Instructions d'installation sur le serveur ISEN

- Copier tout le contenu du dossier "4_Production" et le mettre dans le repertoire de votre choix.
- Créer la table "airiq" dans la la base de données SQL (vous pouvez pour cela utiliser le fichier "createAirIQ.sql" dans le dossier SQL).
- Installer un environnement python 3.7 avec les librairies indiquées dans "librairies.txt".
- Dans "db_informations.json", remplacez les informations par défaut par le login de la base de donnée devisenfdhruche:
  - {"host": nom_de_l'hôte, "user": utilisateur, "passwd": mot_de_passe, "db": nom_de_base_de_donnees}
- Lancer le script "routineProjetAirIQ.py", qui est une routine et appellera les scripts nécessaires régulièrement.
  - PS: si vous voulez changer l'intervalle de temps de la routine, il faut modifier le script (vers la fin):
    - Pour toutes les x minutes: schedule.every(x).minutes.do(call_script)
    - Pour toutes les x heures: schedule.every(x).hours.do(call_script)
    - Pour toutes les jours à une heure précise: schedule.every().day.at('xx:xx').do(call_script)
- Si tout c'est bien déroulé, vous pouvez supprimer le dossier "installation" si vous le désirez.