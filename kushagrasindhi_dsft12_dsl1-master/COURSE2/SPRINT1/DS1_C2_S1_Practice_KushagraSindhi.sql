create database techmac_db;
use techmac_db; -- T1

create table techhyve_employees (
	employee_id int,
	first_name varchar(15),
    last_name varchar(15),			-- T2
    gender char(6),
    age int);

create table techcloud_employees like techhyve_employees;  
create table techsoft_employees like techhyve_employees;		-- T2

alter table techhyve_employees add ProficiencyLevel int check(proficiencylevel > 0 AND proficiencylevel < 6); -- T3
alter table techcloud_employees add ProficiencyLevel int check(proficiencylevel > 0 AND proficiencylevel < 6);
alter table techsoft_employees add ProficiencyLevel int check(proficiencylevel > 0 AND proficiencylevel < 6);

alter table techhyve_employees add constraint t primary key(employee_id);	-- T4
alter table techcloud_employees add constraint t primary key(employee_id);
alter table techsoft_employees add constraint t primary key(employee_id);

alter table techhyve_employees modify ProficiencyLevel int check(proficiencylevel > 0 AND proficiencylevel < 6) default 1; -- added new column with default constraint
alter table techcloud_employees modify ProficiencyLevel int check(proficiencylevel > 0 AND proficiencylevel < 6) default 1;
alter table techsoft_employees modify ProficiencyLevel int check(proficiencylevel > 0 AND proficiencylevel < 6) default 1;

alter table techhyve_employees modify age int check(age>20 AND age<56); -- T4
alter table techcloud_employees modify age int check(age>20 AND age<56);
alter table techsoft_employees modify age int check(age>20 AND age<56);

insert into techhyve_employees values('TH0001',	'Eli',	'Evans',	'Male',	26,	1),
		('TH0002',	'Carlos',	'Simmons'	,	'Male'	,	32,	2),
		('TH0003',	'Kathie',	'Bryant'	,	'Female',	25,	1),			-- T5
		('TH0004',	'Joey'	,	'Hughes'	,	'Male'	,	41,	4),
		('TH0005',	'Alice'	,	'Matthews'	,	'Female',	52,	4);
insert into techcloud_employees values('TC0001',	'Teresa',	'Bryant',	'Female',	39,	2),
		('TC0002',	'Alexis',	'Patterson',	'Male',	48,	5),
		('TC0003',	'Rose',	'Bell',	'Female',	42,	3),
		('TC0004',	'Gemma',	'Watkins',	'Female',	44,	3),
		('TC0005',	'Kingston',	'Martinez',	'Male',	29,	2);
insert into techsoft_employees values('TS0001',	'Peter',	'Burtler',	'Male',	44,	4),
		('TS0002',	'Harold',	'Simmons',	'Male',	54,	4),
		('TS0003',	'Juliana',	'Sanders',	'Female',	36,	2),
		('TS0004',	'Paul',	'Ward',	'Male',	29,	2),
		('TS0005',	'Nicole',	'Bryant',	'Female',	30,	2);



create table techhyve_employees_bkp select * from techhyve_employees;		-- T6
create table techcloud_employees_bkp select * from techcloud_employees;
create table techsoft_employees_bkp select * from techsoft_employees;



delete from techhyve_employees where employee_id = "TH0003";
delete from techhyve_employees where employee_id = "TH0005";
delete from techsoft_employees where employee_id = "TH0001";	-- T7
delete from techsoft_employees where employee_id = "TH0004";


create table techhyvecloud_employees like techhyve_employees;
insert into techhyvecloud_employees select * from techhyve_employees;
insert into techhyvecloud_employees select * from techcloud_employees;		-- T8


truncate table techhyve_employees; -- T8
truncate table techcloud_employees;