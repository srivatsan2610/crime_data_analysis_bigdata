README - PHASE4 
Srivatsan Ananthakrishnan(1021022)

PART 1:
MapReduce (Python)

1.	Where to downoad the dataset?
https://catalog.data.gov/dataset/crime-data-from-2010-to-present

All the available formats for present in the above link. Preferred (.csv)

2.	For running in Python - streaming jar for running python mapreduce jobs has to be downloaded.
You can find the same in the .zip file

ZIP contains:

mapper1.py
reduce1.py
hadoop-streaming.jar

crime_result.hql
hquery.hql
README.txt
sample_dataset.csv


3.	To run MapReduce Python Job:

Place mapper1.py , reducer1.py , hadoop-streamimg.jar, and the dataset in the same folder (say /phase5 directory in my case).
Then use the below script to run.

[training@localhost phase5] hadoop jar hadoop-streamimg.jar -input Crime_Data_from_2010_to_Present.csv -output actual_result3 -file mapper1.py -file reducer1.py -mapper mapper1.py -reducer reducer1

4.	The output file will be stored in actual_result3

[training@localhost phase5] hadoop fs -ls actual_result3/

5.	To view the output: (in my example)
[training@localhost phase5] hadoop fs -cat actual_result3/part-00000/

The above file contains the output which is the solution to the below problem:
Number of female those who were 'Asians' who were the victims of various crimes in each area from the year 2010 to present in LA city.

PART 2:
HiveQL

1.	The script for thge hiveQL is present in the ZIP folder.

a.	To load the dataset to Hive:

crime_result.hql

b.	Once table structure is created, query to load the dataset values into the table is ,

load data local inpath 'Crime_Data_from_2010_to_Present.csv' into table crime_data;

2.	Query for solving another problem for my dataset is in the below script.

hquery.hql

to run the below script in hive, 

[training@localhost phase5] hive -f hquery.hql

3.	This query will display the number of crimes in each and every category
	type of the corresponding areas.
	

Note: Still working on various problem solutions and video with presented will be submitted along with spark and Big query



