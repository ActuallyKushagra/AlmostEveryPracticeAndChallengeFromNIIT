-- task 1
-- select employee_id, first_name, last_name, department_name from employees join departments on departments.department_id = employees.employee_id;
select employee_id, first_name, last_name, (select department_name from departments d where e.department_id = d.department_id) as 'departmentName' from employees e order by departmentName;

-- task 2
select concat(first_name, ' ', last_name) as "Name" from employees where salary > (select avg(salary) from employees);

-- task 3
select concat(first_name, ' ', last_name) as "Name", salary from employees where salary < (select avg(salary) from employees) and department_id = (select department_id from departments where department_name = "sales");

-- task 4
select concat(first_name, ' ', last_name) as "Name", salary from employees where salary > (select avg(salary) from employees) and job_id = "IT_prog" order by salary desc;

-- task 5
select concat(first_name, ' ', last_name) as "Name" from employees where salary = (select min(salary) from employees);

-- task 6
select E1.first_name, E1.last_name from employees E1 where salary > (select sum(salary)*0.6 from employees E2 where E1.department_id =  E2.department_id);

-- task 7
select first_name, last_name from employees where manager_id in (select employee_id from employees where department_id in (select department_id from departments where location_id in (select location_id from locations where country_id = 'UK')));

-- task 8
select salary, first_name, last_name from employees where salary > (select avg(salary) from employees) limit 5 into outfile 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/filename.csv' fields terminated by ',';