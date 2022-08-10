--prints the Numbers of the second_table.
SELECT `score` COUNT (*) AS `number`
FROM `second_table`
GROUP BY `Score`
ORDER BY `number` DESC;
