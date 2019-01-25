set hive.cli.print.header=true;

SELECT 
a.area_name AS AREA_NAME,
a.crime_code_description AS CRIME_CODE_DESCRIPTION,
MAX(a.crime_count) as NUMBER_OF_CRIMES
FROM (
SELECT 
area_name,
crime_code_description,
COUNT(crime_code_description) as crime_count
FROM
crime_data GROUP BY
area_name,crime_code_description)a
GROUP BY a.area_name,a.crime_code_description;
