<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
	<meta http-equiv="refresh" content="300">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title></title>
    <meta name="description" content="<?php print $description;?>" />
		<link href="https://fonts.googleapis.com/css?family=Open+Sans" rel="stylesheet">
		<link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.5.0/css/all.css" integrity="sha384-B4dIYHKNBt8Bc12p+WXckhzcICo0wtJAoU8YZTY5qE0Id1GSseTk6S+L3BlXeVIU" crossorigin="anonymous">
		<link rel="stylesheet" href="style.css" media="all">
  </head>
  <body>
  <header>
    <table id="tableMenu">
    	<tr>
    		<td>
    				<img src="img/titre.png" alt="titre" id='titre'/>
    		</td>
    		<td>
    				<a href="index.php" style="float:right;" >
    				<img src="img/logo.png" alt="abeille" title="Retour à la page d'accueil" id='abeille'></a>
    		</td>
    	</tr>
    </table>
    <nav class="menu">
      <ul id="menu-deroulant">
      <li><a href="index.php">Accueil</a></li>
    	<li><a href=''>Ruche 1</a>
    		<ul>
    			<li><a href='TempRuche.php?ruche=1'>Température</a></li>
    			<li><a href='HygroRuche.php?ruche=1'>Hygrométrie</a></li>
    			<li><a href='PoidsRuche.php?ruche=1'>Poids</a></li>
    		</ul>
    	</li>
        <li><a href=''>Ruche 2</a>
    		<ul>
          <li><a href='TempRuche.php?ruche=2'>Température</a></li>
    			<li><a href='HygroRuche.php?ruche=2'>Hygrométrie</a></li>
    			<li><a href='PoidsRuche.php?ruche=2'>Poids</a></li>
    		</ul>
    	</li>
      <li><a href=''>Tensions</a>
      <ul>
        <li><a href='PanneauS.php'>Panneau solaire</a></li>
        <li><a href='Batterie.php'>Batterie</a></li>
      </ul>
      </li>
      <li><a href=''>Qualité de l'air</a>
      <ul>
        <li><a href='QualiteAir.php'>Prédiction</a></li>
      </ul>
      </li>
    </ul>
    </nav>
  </header>
  </body>

</html>
