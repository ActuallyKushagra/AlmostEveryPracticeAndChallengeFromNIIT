create database stylexcarz_db;				-- t1
use stylexcarz_db;

create table salespersons(
	salespersonid int primary key,
    salesperson_name varchar(20) not null,
    salesperson_city varchar(15) not null,   -- t2
    commission_rate int);
    
create table customers(
	customerid int primary key,
    c_firstname varchar(10) not null,	-- t2
    c_lastname varchar(10) not null,
    c_city varchar(15) not null,
    c_rating int not null);
    
create table orders(
	orderid int primary key,
    amount int not null,
    orderdate date not null,		-- t2
    salespersonid int, 
    customerid int, 
    foreign key(salespersonid) references salespersons(salespersonid),
    foreign key(customerid) references customers(customerid));

insert into salespersons values 
	(1001,	'William',	'London',	12),
	(1002,	'Liam',	'San Jose',	13),
	(1003,	'Axelrod',	'New York',	10),
	(1004,	'James',	'London',	11),		-- t3
	(1005,	'Fran',	'London',	26),
	(1007,	'Oliver',	'Barcelona',	15),
	(1008,	'John',	'London',	0),  -- 3
	(1009,	'Charles',	'Florida',	0);
    
insert into customers values
	(2001,	'Hoffman',	'Anny',	'London',	100),
	(2002,	'Giovanni',	'Jenny',	'Rome',	200),
	(2003,	'Liu',	'Williams','San Jose',	100),		-- t3
	(2004,	'Grass',	'Harry',	'Berlin',	300),
	(2005,	'Clemens',	'John',	'London',	200),
	(2006,	'Cisneros',	'Fanny',	'San Jose',	200),
	(2007,	'Pereira',	'Jonathan',	'Rome',	300);
set sql_mode = "";
insert into orders values
	(3001,	123,	'2021-02-01',	1009,	2007),
	(3002,	100,	'2021-07-30​',	1001,	2007),
	(3003,	187,	'2021-10-02​',	1001,	2001),
	(3005,	201,	'2021-10-09​',	1003,	2003),
	(3007,	167,	'2021-04-02​',	1004,	2002),
	(3008,	189,	'2021-03-06​',	1002,	2002),		-- t3
	(3009,	145,	'2021-10-10​',	1009,	2005),
	(3010,	200,	'2021-02-23​',	1007,	2007),
	(3011,	100,	'2021-09-18​',	1001,	2004);


update salespersons set commission_rate = 15   -- t4
where commission_rate between 0 and 13;
set sql_safe_updates = 0;

create table orders_bkp select * from orders;  -- t5

create table orders_placed_history select * from orders;
delete from orders
where orderid = 3005 or orderid = 3008;		-- t6
delete from orders_placed_history
where orderid = 3005 or orderid = 3008;


update customers set c_rating = c_rating + 50
where customerid = 2007 or customerid = 2002;		-- t7


select * from customers;
--  drop table salespersons, customers, orders;
-- drop database stylexcarz_db;