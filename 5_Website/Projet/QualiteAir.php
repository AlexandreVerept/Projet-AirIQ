<?php
// Appel de la page permettant la connexion à la base de données
require_once('co_deco.php');
// Appel de la page header
require_once('includes/header.php'); ?>

<h1>Prédiction</h1>
<?php
// Appel de la page dernière valeur
require_once('dernierevaleurPrediction.php');

// Appel du graphique
require_once('Graph/graphPrediction.php');

// Appel de la page footer
require_once('includes/footer.php'); ?>
