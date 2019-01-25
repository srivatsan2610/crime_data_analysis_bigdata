/*Analysis of number of crimes occurred in a particular area in the years 2017 and 2018*/
SELECT 
YEAR(date_reported) AS YEARS,
area_name,
MAX(COUNT(crime_code)) AS crime_count
FROM [bigquery1021022.crime_data] 
GROUP BY 
area_name,YEARS
HAVING
YEARS > 2016 and YEARS <= 2018
ORDER BY 
area_name DESC;