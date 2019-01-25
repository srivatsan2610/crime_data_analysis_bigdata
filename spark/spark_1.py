
#import SQLContext and row
from pyspark import SparkContext
from pyspark.sql import SQLContext,Row

sc = SparkContext() 
sqlContext=SQLContext(sc)

#load the data set and split the records
 
lines =sc.textFile("sample_dataset.csv")

parts = lines.map(lambda l: l.split(","))
 
# construct the Rows by by passing a list of key/value pairs as kwargs

Crimes = parts.map(lambda p:Row(DR_number =p[0],date_reported=p[1],date_occured=p[2],time_occured=p[3],area_id=p[4],area_name=p[5],reporting_district=p[6],crime_code =p[7],crime_code_desc=p[8],mo_codes= p[9],victim_age=p[10],victim_sex=p[11],victim_desc=p[12],premise_code=p[13],premise_desc=p[14],weapon_used_code=p[15],weapon_desc=p[16],status_code=p[17],status_desc=p[18],crime_code_1=p[19],crime_code_2=p[20],crime_code_3=p[21],crime_code_4=p[22],address = p[23],cross_street= p[24],location = p[25]))
 
 
# Create the DataFrame and register it has Table
 
schema1=sqlContext.createDataFrame(Crimes)
 
schema1.registerTempTable("Crimes")
 
#run the query for getting the required result
 
result=sqlContext.sql("SELECT crime_code_desc,COUNT(*) AS crime_count FROM Crimes GROUP BY crime_code_desc ORDER BY crime_count DESC")
 
result.show()