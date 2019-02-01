1. loaddb.py ==> This script loads csv file(sample record is available in contacts.csv) into postgres database which is on same machine.

2. logstash-postgres.conf ==> This is the logstash postgres configuration file which will connect to postgresql database, load all data into elasticsearch with the refernce of statement.
Like "statement => "SELECT * from contacts" " Loads all records available in contacts table into elasticsearch.

3. Make changes at required plances ==>
	a. elastic user/password
	b. jdbc user/password 
        c. elastic host ip/port


