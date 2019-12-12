<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title>test</title>
    <!-- Styles -->
    <style>
    #chartdiv {
      width: 100%;
      height: 500px;
    }
    </style>

    <!-- Resources -->
    <script src="https://www.amcharts.com/lib/4/core.js"></script>
    <script src="https://www.amcharts.com/lib/4/charts.js"></script>
    <script src="https://www.amcharts.com/lib/4/themes/animated.js"></script>
  </head>
<body>

<div id="chartdiv"></div>

<script type="text/javascript">

/* Chart code */

// Themes begin
am4core.useTheme(am4themes_animated);
// Themes end


// Create chart
let chart = am4core.create("chartdiv", am4charts.XYChart);
chart.paddingRight = 20;

chart.data = generateChartData();

// Créer des axes aux graphiques
let dateAxis = chart.xAxes.push(new am4charts.DateAxis());
dateAxis.baseInterval = {
  "timeUnit": "minute",
  "count": 1
};

// Changer le format de la date : Année/Mois/Jour/Heure/Minute/Seconde
chart.dateFormatter.inputDateFormat = "yyyy-MM-dd HH:mm:ss";
dateAxis.tooltipDateFormat = "yyyy-MM-dd HH:mm:ss";

// Valeur de l'axe des ordonnées
let valueAxis = chart.yAxes.push(new am4charts.ValueAxis());
valueAxis.tooltip.disabled = true;
valueAxis.title.text = "Températures (en °C)";

//Créer différentes courbes avec la fonction "series"
let series = chart.series.push(new am4charts.LineSeries());
series.dataFields.dateX = "time";
series.dataFields.valueY = "TempBord";
series.tooltipText = "Température au bord de la ruche: [bold]{valueY}[/]";
series.fillOpacity = 0.3;

let series2 = chart.series.push(new am4charts.LineSeries());
series2.dataFields.dateX = "time";
series2.dataFields.valueY = "TempInt";
series2.tooltipText = "Température au centre de la ruche : [bold]{valueY}[/]";
series2.fillOpacity = 0.3;

let series3 = chart.series.push(new am4charts.LineSeries());
series3.dataFields.dateX = "time";
series3.dataFields.valueY = "TempExt";
series3.tooltipText = "Température à l'extérieur de la ruche : [bold]{valueY}[/]";
series3.fillOpacity = 0.3;

chart.cursor = new am4charts.XYCursor();
chart.cursor.lineY.opacity = 0;
chart.scrollbarX = new am4charts.XYChartScrollbar();
chart.scrollbarX.series.push(series);


chart.events.on("datavalidated", function () {
    dateAxis.zoom({start:0.8, end:1});
});


function generateChartData() {
    let chartData = [];

<?php
  // Connexion à la base de données
  $bdd = connexion();
  try
    {
      // Permet de définir quelle ruche prendre
    if(isset($_GET["ruche"])){
      $ruche = $_GET["ruche"];
      $ruche = ($ruche <= 2)? ($ruche <= 0)? 1 : $ruche : 1;
    }else {
      $ruche = 1;
    }
    // Récupération des données de la Ruche souhaitée dans la base de données
    $sql_query="SELECT TempInt, TempExt, TempBord, time  FROM `RecuperationDonnees` WHERE NumRuche=".$ruche;    //Requête
  $result_query = $bdd->query($sql_query);       // Exécution de la requête

  // On affiche les données pour vérification
  while($row = $result_query->fetch()){
   $v1 = $row['TempBord'];
   $v2 = $row['TempInt'];
   $v7 = $row['time'];
   $v5 = $row['TempExt'];

   echo "chartData.push({
    time : \"$v7\",
    TempInt : \"$v2\",
    TempExt : \"$v5\",
    TempBord : \"$v1\" });";
  }

    }catch (PDOException $e){
    echo "Connexion échouée : <font color=red><b>" . $e->getMessage()."</b></font> <br> \n";
    }
?>

console.log(chartData);
return chartData;
}

</script>
</body>
</html>
