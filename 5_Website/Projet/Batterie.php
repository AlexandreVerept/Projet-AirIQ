<?php
// Appel de la page permettant la connexion à la base de données
require_once('co_deco.php');
// Appel de la page header
require_once('includes/header.php'); ?>

<h1>Tension de la batterie</h1>
<?php
// Appel de la page dernière valeur
require_once('dernierevaleurBatterie.php');
// Appel du graphique
require_once('GraphTensions/graphBatterie.php');
// Appel de la page footer
require_once('includes/footer.php'); ?>
