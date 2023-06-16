use sakila;

-- task 2.1
select film_id, count(inventory_id) from inventory where film_id in (select film_id from film where title = "brotherhood blanket" or title = "soup wisdom") group by film_id;

-- task 2.2
select (select (select name from category where category.category_id = film_category.category_id) from film_category where inventory.film_id = film_category.film_id) as genre, count(inventory_id) from inventory group by genre;

-- task 2.3
select concat(first_name, ' ', last_name) as "Name", (select sum((select replacement_cost from film where film.film_id = film_actor.film_id)) from film_actor where actor.actor_id = film_actor.actor_id group by actor_id) as replacement_cost from actor order by replacement_cost desc limit 3;

-- task 2.4
select (select (select name from category where category.category_id = film_category.category_id) from film_category where inventory.film_id = film_category.film_id) as genre, count(inventory_id) * sum((select replacement_cost from film where film.film_id = inventory.film_id)) as total_sales from inventory group by genre;

-- task 2.5
select * from (select category.name, (select sum(amount) as totalsales from payment where rental_id in (select rental_id from rental where inventory_id in (select inventory_id from inventory where film_id in (select film_id from film_category where category.category_id = film_category.category_id)))) "totalsales" from category order by totalsales desc limit 10) a into outfile  'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/filename2.csv' fields terminated by ',' lines terminated by '\n';