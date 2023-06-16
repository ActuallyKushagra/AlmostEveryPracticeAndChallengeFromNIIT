-- task 1
select count(employees.employee_id) as "employees", locations.city from employees join departments on employees.department_id = departments.department_id join locations on departments.location_id = locations.location_id group by locations.city order by count(employee_id) desc;

-- task 2
select first_name, last_name, country_name, department_name, salary, locations.city from employees join departments on employees.department_id = departments.department_id join locations on departments.location_id = locations.location_id join countries on countries.country_id = locations.country_id group by locations.city order by count(employee_id) desc limit 5;

-- task 3
select count(employees.employee_id) as "employees", locations.city from employees join departments on employees.department_id = departments.department_id join locations on departments.location_id = locations.location_id group by locations.city order by count(employee_id) desc limit 5;

-- task 4
select * from employees join departments on employees.department_id = departments.department_id where (year(curdate()) - year(hire_date)) >= 10;

-- task 5
select manager_id from employees join job_history on job_history.employee_id = employees.employee_id where (year(curdate()) - year(hire_date)) >= 10 group by manager_id;

-- task 6
select country_name from employees join departments on employees.department_id = departments.department_id join locations on departments.location_id = locations.location_id join countries on locations.country_id = countries.country_id where (year(curdate()) - year(employees.hire_date)) group by country_name order by count(employees.employee_id) desc limit 3;

