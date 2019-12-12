SELECT time,TempExt,HygroExt
FROM RecuperationDonnees
WHERE time > DATE_SUB(NOW(), INTERVAL 24 HOUR)
  AND time <= NOW()