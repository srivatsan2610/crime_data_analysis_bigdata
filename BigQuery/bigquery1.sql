/*Top 5 number of crimes occured in each type from 2010-present*/
SELECT 
crime_code_description,COUNT(*) AS crime_count
FROM [bigquery1021022.crime_data] 
GROUP BY 
crime_code_description 
ORDER BY 
crime_count DESC
LIMIT
5;