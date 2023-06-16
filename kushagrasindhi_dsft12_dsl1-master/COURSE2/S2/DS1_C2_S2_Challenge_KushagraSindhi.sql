-- task 1
select count(employee_id) from employees;

-- task 2 (doubt - null value in department_id, how to print department name)
-- select count(employee_id), count(department_name) group by department_id;
select department_id, count(employee_id) from employees group by department_id;

-- task 3
select first_name, salary from employees where salary > 6000;

-- task 4
select count(employee_id) from employees where salary > 20000;

-- task 5
select * from employees where commission_pct is not null;		-- alt 1
select * from employees where commission_pct > 0;		-- alt 2

-- task 6
select concat(first_name, ' ', last_name) as "fullname" from employees where commission_pct is null;

-- task 7
select employee_id as "Employee ID", concat(first_name, ' ', last_name) as "Employee Full Name", email as "Email ID", phone_number as "Contact Number"
from employees 
where commission_pct is not null;

-- task 8
-- select sum(salary), department_id, (select department_name from departments) from employees group by department_id;
 select max(salary), department_id from employees group by department_id limit 3;
 
 -- task 9
 select * from employees where job_id like '%clerk';
 
 -- task 10
 select count(employee_id), avg(salary) from employees where job_id like '%clerk%';
 
 -- task 11
 select department_id, count(employee_id) from employees  where salary between 7000 and 10000 group by department_id;