/*Top 10 type of crimes happenned to womens in the year 2017*/
SELECT 
crime_code_description,COUNT(*) AS crime_count_2017
FROM [bigquery1021022.crime_data] 
WHERE
Victim_Sex='F'
AND YEAR(date_reported) = 2017
GROUP BY 
crime_code_description 
ORDER BY 
crime_count_2017 DESC
LIMIT
10;
