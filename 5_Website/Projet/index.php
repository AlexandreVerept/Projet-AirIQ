<!DOCTYPE html>
<html lang="fr" dir="ltr">
	<head>
		<meta charset="utf-8">
		
		<title>Page d'accueil</title>
	</head>

<?php
// Appel de la page header
require_once('includes/header.php'); ?>

	<h1>Présentation</h1>
<table>
	<tr>
		<td id='presentation_texte'>
			<p class='text'>Alors que les abeilles sont déclarées espèce en voie d’extinction depuis près de trois ans, l’apiculture est un véritable enjeu pour leur préservation. C’est pourquoi des écoles comme l’<a href="https://www.isen-lille.fr" target="_blank" id='isen'>ISEN</a> ou l'<a href="https://www.isa-lille.fr" target="_blank" id='isen'>ISA</a> ont décidé d’installer des ruches sur leurs toîts. Afin d’avoir un suivi plus précis et à distance de ces ruches, des capteurs de température et d’humidité ont été installés. Les données récupérées par ces capteurs sont traitées dans les onglets correspondants.</p>
		</td>
		<td>
			<img src="img/presentation.jpg" alt="presentation" id='presentation'/>
		</td>
	</tr>
</table>

<?php 
// Appel de la page footer
require_once('includes/footer.php'); ?>
