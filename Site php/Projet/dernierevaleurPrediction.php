<?php

try{

  // Connexion à la base de données
  $bdd = connexion();

  // Récupération des données souhaitées dans la base de données
  $sql_query="SELECT prediction,time  From airiq WHERE time = (select MAX(time) from airiq)";    //Requête
	$result_query = $bdd->query($sql_query);    // Exécution de la requête

  // On affiche les données recueillies dans une phrases sur la page
  //echo "<p>".$result_query->fetch()."</p>";
  while($row = $result_query->fetch()){
    $v1 = $row['prediction'];
    $v2 = $row['time'];
  }
  echo '<p>A '.date("H", strtotime($v2)).'h'.date("i", strtotime($v2)).', la prédiction de qualité de l\'air pour demain est '.$v1.'</p>';
}


catch (PDOException $e){
  echo "Connexion échouée : <font color=red><b>" . $e->getMessage()."</b></font> <br> \n";
}

?>
