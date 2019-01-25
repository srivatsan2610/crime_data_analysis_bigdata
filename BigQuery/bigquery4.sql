/* Number of crimes that has involved theft of $950.01 and over every year */
SELECT
YEAR(date_reported) as YEARS,
  COUNT(*) AS Number_of_Thefts
FROM
  [bigquery1021022.crime_data] 
WHERE
  LOWER(crime_code_description) LIKE '%theft-grand%'
  GROUP BY YEARS
  ORDER BY YEARS DESC;