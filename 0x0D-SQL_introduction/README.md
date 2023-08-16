# RELATIONAL DATABASE

## SQL (Structured Query Language)
This Directory contains the commands used for the `DDL`
(Data Definition Language) and `DML` (Data Manipulation Language)
in MYSQL Server


## Projects Folder
### [0-list_databases.sql](0-list_databases.sql) 
* > * list all databases of MYSQL server 

### [1-create_database_if_missing.sql](1-create_database_if_missing.sql)
* > * create a database if exists do nothing in MYSQL server

### [2-remove_database.sql](2-remove_database.sql)
* > * delete a database if exists do nothing in MYSQL server

### [3-list_tables.sql](3-list_tables.sql)
* > * list all tables of a database in MySQL server

### [4-first_table.sql](4-first_table.sql)
* > * create a table in the database of MYSQL server

### [5-full_table.sql](5-full_table.sql)
* > * display a full list of a table in MYSQL server

### [6-list_values.sql](6-list_values.sql)
* > * display all rows in a table in MYSQL server

### [7-insert_value.sql](7-insert_value.sql)
* > * insert a new row to a table in MYSQL server

[8-count_89.sql](8-count_89.sql)
* > * display the number of records with id=89

### [9-full_creation.sql](9-full_creation.sql)
* > * create a table in the database with multiple rows

### [10-top_score.sql](10-top_score.sql)
* > * list records in a table order by descending

### [11-best_score.sql](11-best_score.sql)
* > * list records with score >= 10

### [12-no_cheating.sql](12-no_cheating.sql)
* > * update records in a table

### [13-change_class.sql](13-change_class.sql)
* > * delete records from table where score was <= 10

### [14-average.sql](14-average.sql)
* > * average of the score

### [15-groups.sql](15-groups.sql)
* > * number of records with the same score and group it by score order by number descending

### [16-no_links.sql](16-no_link.sql)
* > * list score and name and only rows with name not null or empty

### [101-avg_temperature.sql](101-avg_temperatures.sql)
* > * get the average temp as avg_temp and group by city ordered by avg_temp in descending order
* Referenced table is [temperatures.sql in directory](temperatures.sql) 

### [102-top_city.sql](102-top_city.sql)
* > * display from July to August while displaying only the top 3 from there
* Referenced table is [temperatures.sql in directory](temperatures.sql)

### [103-max_state.sql](103-max_state.sql)
* > * get max value from a column
* Referenced table is [temperatures.sql in directory](temperatures.sql)

