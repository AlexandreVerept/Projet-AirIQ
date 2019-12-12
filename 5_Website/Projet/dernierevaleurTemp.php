<?php

try{

  // Connexion à la base de données
  $bdd = connexion();

    // Permet de définir quelle ruche prendre
    if(isset($_GET["ruche"])){
    $ruche = $_GET["ruche"];
    $ruche = ($ruche <= 2)? ($ruche <= 0)? 1 : $ruche : 1;
  }else {
    $ruche = 1;
  }

  // Récupération des données de la Ruche souhaitée dans la base de données
  $sql_query="SELECT TempInt, TempExt, TempBord, time  FROM `RecuperationDonnees` WHERE NumRuche=".$ruche;    // Requête
	$result_query = $bdd->query($sql_query);    // Exécution de la requête

  // On affiche les données recueillies dans une phrases sur la page
  while($row = $result_query->fetch()){
    $v1 = $row['TempBord'];
    $v2 = $row['TempInt'];
    $v5 = $row['TempExt'];
    $v7 = $row['time'];
  }
  echo '<p>A '.date("H", strtotime($v7)).'h'.date("i", strtotime($v7)).', la température extérieure était de '.$v5.'°C, la température au centre de la ruche était de '.$v2.'°C, et la température au bord de la ruche était de '.$v1.'°C.</p>';
}


catch (PDOException $e){
  echo "Connexion échouée : <font color=red><b>" . $e->getMessage()."</b></font> <br> \n";
}

?>
