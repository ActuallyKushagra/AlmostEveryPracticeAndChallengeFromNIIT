use s3hr;
-- task 1
select concat(first_name, ' ', last_name) as "Fullname", employee_id from employees inner join departments on employees.department_id = departments.department_id where department_name = "IT";

-- task 2
select first_name, employees.job_id, min_salary, max_salary from employees left join jobs on employees.job_id = jobs.job_id;

-- task 3
select count(employees.employee_id) as "employees", locations.city from employees join departments on employees.department_id = departments.department_id join locations on departments.location_id = locations.location_id group by locations.city order by count(employee_id) desc;

-- task 4
select employees.employee_id, concat(first_name, ' ', last_name) from employees join job_history on employees.employee_id = job_history.employee_id where end_date = '1999-12-31';

-- task 5
select employees.employee_id, first_name as "name", department_name, (year(curdate()) - year(hire_date)) as "experience" from employees join departments on employees.department_id = departments.department_id where (year(curdate()) - year (hire_date)) >= 25;

