README - PHASE4 - II
Srivatsan Ananthakrishnan(1021022)

PART 3:
SPARK (pyspark)

1.	Where to downoad the dataset?
https://catalog.data.gov/dataset/crime-data-from-2010-to-present

All the available formats for present in the above link. Preferred (.csv)

2.ZIP contains:

It contains a separate folder for "Spark"

- spark_1.py
- spark_5.py

- sample_dataset.csv

3.	Put the dataset into hdfs "Crime_Data_from_2010_to_Present.csv"
	The dataset can be downloaded from the above link or from the google drive link:
	
	https://drive.google.com/open?id=11fQ2iQopovjY3yYHOaP8oU1uQhMGt2db
	
4.	To run Spark ./pyspark Job:

First check for pyspark in your terminal by entering 
[training@localhost phase4] pyspark

Place spark_1.py , spark_5.py and the dataset in the same folder (say /phase4 directory in my case).
Then use the below script to run.

[training@localhost phase4] spark-submit spark_1.py
[training@localhost phase4] spark-submit spark_5.py


4.	The output file will be displayed in the terminal in a table format( since I used SqlContext to show as my result).

-------------------------------------------------------------------------------------------------------------------

PART 4:
BigQuery:

1.	The script for thge BigQuery is present in the ZIP folder.

It contains a separate folder for "BigQuery"

- bigquery1.sql
- bigquery2.sql
- bigquery3.sql
- bigquery4.sql

The results for the above query is downloaded in .csv and kept in the same folder.

- results-bigquery1.csv
- results-bigquery2.csv
- results-bigquery3.csv
- results-bigquery4.csv

2. BigQuery is performed in GCP.

a.	To load the dataset to BigQuery:

First create a BigQuery project in GCP.

Select the Google Drive Link option for loading the table and select automatic schema.
Link:

https://drive.google.com/open?id=11fQ2iQopovjY3yYHOaP8oU1uQhMGt2db


b.	Once table structure is created and the values are populated , in the query editor pane we can start entering the sql queries as per the problem statements

- Copy the contents from the bigquery1.sql , bigquery2.sql, bigquery3.sql.
- On running the query, you can see the results in the below results pane in the table format.

1) Problem statement 1: 
	Top 5 number of crimes occured in each type from 2010-present. (bigquery1.sql)
	Result (results-bigquery1.csv)
2) Problem statement 2: 
	Top 10 type of crimes happenned to womens in the year 2017. (bigquery2.sql)
	Result (results-bigquery2.csv)
3) Problem statement 3: 
	Analysis of number of crimes occurred in a particular area in the years 2017 and 2018. (bigquery3.sql)
	Result (results-bigquery3.csv)
4) Problem statement 4: 
	Number of crimes that has involved theft of $950.01 and over every year. (bigquery4.sql)
	Result (results-bigquery4.csv)

Note: Video for the demo and presentation for Mapreduce,Spark,Hive and BigQuery will be explained in Phase 5.

