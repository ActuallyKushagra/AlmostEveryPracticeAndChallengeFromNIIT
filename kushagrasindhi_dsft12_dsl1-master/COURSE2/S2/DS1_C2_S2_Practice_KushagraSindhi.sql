create database s2practice;
use s2practice;

-- task 1
select * from salespersons where salesperson_city = "london";

-- task 2
select * from salespersons where commission_rate = 0;

-- task 3
select * from salespersons order by commission_rate desc limit 3;

-- task 4
select avg(commission_rate) from salespersons;
select * from salespersons where commission_rate < (select avg(commission_rate) from salespersons);		-- task 4 alt method 1
select * from salespersons where commission_rate < 10.8750;		-- task 4 alt method 2

-- task 5
select avg(commission_rate) from salespersons;
select * from salespersons where commission_rate < (select avg(commission_rate) from salespersons) and salesperson_city = "london"; -- task 5 alt method 1
select * from salespersons where commission_rate < 10.8750 and salesperson_city = "london"; -- t5 alt method 2

-- task 6
select * from salespersons where salesperson_city = "florida" and salesperson_city = "barcelona" and salesperson_city = "san jose";

-- task 7
select min(c_rating) from customers;
select * from customers where c_rating = 100; 		-- task 7 alt method 1
select * from customers where c_rating <= (select min(c_rating) from customers);		-- task 7 alt method 2

-- task 8
select max(c_rating) from customers;
select * from customers where c_rating = 300;		 -- task 8 alt method 1
select * from customers where c_rating >= (select max(c_rating) from customers);		-- task 8 alt method 2

-- task 9
select max(c_rating) from customers;
select c_city from customers where c_rating = 300;
select c_city from customers where c_rating >= (select max(c_rating) from customers);

-- task 10
select * from customers order by c_rating desc;

-- task 11
select concat(c_firstname, ' ', c_lastname) as "Name" from customers where c_firstname like 'J_n%';
-- select c_firstname from customers where c_firstname like 'j_n%';

-- task 12
select avg(amount) as "average amount", max(amount) as "maximum amount" from orders;

-- task 13
select count(*) from orders;

-- task 14
select month(orderdate), sum(amount), avg(amount)  from orders group by month(orderdate);