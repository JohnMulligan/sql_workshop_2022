1. In MySQL Workbench:
	1. select: https://dev.mysql.com/doc/refman/8.0/en/selecting-all.html
	1. limit: https://dev.mysql.com/doc/refman/8.0/en/limit-optimization.html
	1. order by: https://dev.mysql.com/doc/refman/8.0/en/order-by-optimization.html
	1. then look at the dataset:
		1. downloads https://hcad.org/pdata/pdata-property-downloads.html
		1. gui import instructions: https://hcad.org/assets/uploads/pdf/Import_Instructions.pdf
		1. documentation: https://hcad.org/assets/uploads/pdf/pdataCodebook.pdf
	1. filter: https://dev.mysql.com/doc/refman/8.0/en/where-optimization.html
		1. gte, lte, eq
		1. iexact str matches
	1. delete: https://dev.mysql.com/doc/refman/8.0/en/delete.html
	1. update: https://dev.mysql.com/doc/refman/8.0/en/update.html
	1. insert (optional): https://dev.mysql.com/doc/refman/8.0/en/insert.html
	1. join statements: https://dev.mysql.com/doc/refman/8.0/en/join.html
		1. and aliases
	1. heavier stuff
		1. alter table: https://dev.mysql.com/doc/refman/8.0/en/alter-table.html
		1. select into: https://dev.mysql.com/doc/refman/8.0/en/select-into.html
1. CLI examples, looking at this repo as a guide:
	1. create database
	1. create table
	1. mysqlimport
	1. drop table
	1. alter table (loop back to the above workbench section)