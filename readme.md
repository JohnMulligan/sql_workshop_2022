# INTRO. MYSQL WORKSHOP 2022

We're going to be using a large public dataset to familiarize ourselves with MySQL Workbench. This repository is mostly a supplement to our discussion.

For the workshop, you'll want to:

	* download the Desktop client: https://www.mysql.com/products/workbench/
	* If you are remote, install the Rice VPN client to connect to the example db
	
What follows lays out how I built the database we're going to use. We'll visit this repository at the end of the lesson to show you how to go further with it if you're interested.

We are interested in how they make this interesting web interface: https://arcweb.hcad.org/parcel-viewer-v2.0/

## first, some resources

* Dataset 
	* HCAD IMPORT INSTRUCTIONS: https://hcad.org/assets/uploads/pdf/Import_Instructions.pdf
	* CODEBOOK for importation: https://hcad.org/assets/uploads/pdf/pdataCodebook.pdf
	* DOWNLOADABLE DATASESTS: https://hcad.org/pdata/pdata-property-downloads.html
* In this repository
	* MySQL server setup recipe (it's dated but for transparency this is how I built this one)
	* a translation of some tables from the HCAD codebook pdf into a tab-separated file
	* a python script for generating the appropriate CREATE TABLE statements

## set up the server mysql server (Ubuntu 22.06)

first, install mysql server

	sudo apt install mysql-server
	
then, make the service available over the network

the IP address for today's workshop, behind the firewall, is 10.134.196.54, so we use that

we open, using vim, the file at ```/etc/mysql/mysql.conf.d/mysqld.cnf``` and add the following lines

	bind-address=10.134.196.54
	port=3306

we then save our changes to the file and exit the text editor

now restart mysql with ```systemctl restart mysql-server```

## create a guest account

I created the following account for you all to log in today

	CREATE USER 'guest' IDENTIFIED BY 'justvisiting';
	GRANT all ON *.* TO 'guest';

You'll want to be a bit more secure than that!

## create & use database commands

then create the database that we'll be using

	create database HCAD_2022;
	use HCAD_2022;

then create the tables that we'll be importing our data into -- these are available in the file [create_table.sql](create_table.sql) and are based on my reading of the HCAD documentation of their files.

these were generated by our python script, using our tab-separated transcription of the HCAD codebook

we're only using a selection of the tables in the 2022 zip files:

* https://download.hcad.org/data/CAMA/2022/Real_acct_owner.zip
* https://download.hcad.org/data/CAMA/2022/Real_building_land.zip

# import our data into the created tables

https://dev.mysql.com/doc/refman/5.7/en/mysqlimport.html

The below commands are for the tables created above, only, for the purposes of showing you the import patterns.

Note: we're skipping an important flag in the below example, and in the data we're looking at in the server today. Specifically, we are not skipping the header row. I kept it in there as a basic validation for myself that my columns were lined up right. But we would want to use the --ignore-lines flag in mysqlimport in a more automated pipeline.

	sudo mysqlimport --local --lines-terminated-by="\n" --fields-terminated-by="\t" HCAD_2022 building_other.txt
	sudo mysqlimport --local --lines-terminated-by="\n" --fields-terminated-by="\t" HCAD_2022 building_res.txt
	sudo mysqlimport --local --lines-terminated-by="\n" --fields-terminated-by="\t" HCAD_2022 land.txt
	sudo mysqlimport --local --lines-terminated-by="\n" --fields-terminated-by="\t" HCAD_2022 real_neighborhood_code.txt
	sudo mysqlimport --local --lines-terminated-by="\n" --fields-terminated-by="\t" HCAD_2022 real_acct.txt
	sudo mysqlimport --local --lines-terminated-by="\n" --fields-terminated-by="\t" HCAD_2022 permits.txt
	sudo mysqlimport --local --lines-terminated-by="\n" --fields-terminated-by="\t" HCAD_2022 parcel_tieback.txt
	sudo mysqlimport --local --lines-terminated-by="\n" --fields-terminated-by="\t" HCAD_2022 owners.txt
	sudo mysqlimport --local --lines-terminated-by="\n" --fields-terminated-by="\t" HCAD_2022 deeds.txt
