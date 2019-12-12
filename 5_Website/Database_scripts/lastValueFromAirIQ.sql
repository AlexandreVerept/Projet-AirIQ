use devisenfdhruche;

SELECT *
From airiq WHERE time = (select MAX(time) from airiq)