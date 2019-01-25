drop table if exists crime_result;

create table if not exists crime_data (
dr_number	int,
date_reported TIMESTAMP,
date_occurred TIMESTAMP,	
time_occurred int,	
area_id	int,
area_name string,
reporting_district int,	
crime_code int,	
crime_code_description	string,
mo_codes string,
victim_age int,
victim_sex string,
victim_descent string,	
premise_code int,
premise_description	string,
weapon_used_code int,	
weapon_description	string,
status_code string,
status_desc string,
crime_code1 int,
crime_code2 int,
crime_code3 int,
crime_code4 int,
address string,
cross_street string,
loc string
)
row format delimited
fields terminated by ',';

