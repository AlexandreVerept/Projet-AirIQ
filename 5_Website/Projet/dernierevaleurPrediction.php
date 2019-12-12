<?php

try{

  // Connexion à la base de données
  $bdd = connexion();

  // Récupération des données souhaitées dans la base de données
  $sql_query="SELECT prediction, time  From airiq WHERE time = (select MAX(time) from airiq)";    //Requête
	$result_query = $bdd->query($sql_query);    // Exécution de la requête


  $sql_query2="SELECT time, valeur  From iq_mel  WHERE time = (select MAX(time)from iq_mel)";    //Requête
  $result_query2 = $bdd->query($sql_query2); 


  // On affiche les données recueillies dans une phrases sur la page
  //echo "<p>".$result_query->fetch()."</p>";
  while($row = $result_query->fetch()){
    $v1 = $row['prediction'];
    $v2 = $row['time'];
    
  }


  while($row = $result_query2->fetch()){
    $v3 = $row['valeur'];
    $v4 = $row['time'];
  }


  echo '<p> À '.date("H", strtotime($v2)).'h'.date("i", strtotime($v2)).', la prédiction de qualité de l\'air pour demain est de '.round($v1,1).'.</p>';

  echo '<p> Pour aujourd\'hui, la prédiction de qualité de l\'air de la MEL est de '.$v3.'.</p>';
}


catch (PDOException $e){
  echo "Connexion échouée : <font color=red><b>" . $e->getMessage()."</b></font> <br> \n";
}

?>
