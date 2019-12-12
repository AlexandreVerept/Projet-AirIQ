<?php
// Appel de la page permettant la connexion à la base de données
require_once('co_deco.php');
// Appel de la page header
require_once('includes/header.php'); ?>

<h1>Tension du panneau solaire</h1>
<?php
// Appel de la page dernière valeur
require_once('dernierevaleurPanneauS.php');
// Appel du graphique
require_once('GraphTensions/graphPanneauS.php');
// Appel de la page footer
require_once('includes/footer.php'); ?>
