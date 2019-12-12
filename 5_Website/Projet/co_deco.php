<?php

function connexion(){
  //paramètres de la base de données
   $hote  = "devisenfdhruche.mysql.db";   // adresse du serveur FTP
   $user  = "devisenfdhruche";  // ton login SQL
   $pwd   = "CNB1Ruche";  // ton password SQL

   $connect = "mysql:dbname=".$user.";host=".$hote;
   try{
      //connexion à la base de données
      $bdd = new PDO($connect, $user, $pwd);
    }catch (PDOException $e){
      echo "Connexion échouée : <font color=red><b>" . $e->getMessage()."</b></font> <br> \n";
    }
    return $bdd;
};

?>
