use sakila;

-- task 1 - list of actors and last update timestamp
select actor_id, concat(first_name, ' ', last_name), last_update from actor;

-- task 2.1 + 2.2 actors with same names
select concat(first_name, ' ',last_name) as 'full_name' from actor group by full_name having count(full_name) > 1;

-- task 2.3 actors with unique names
select concat(first_name, ' ', last_name) as fullname from actor group by fullname having count(*) = 1;


-- task 3.1 names not repeated
select concat(first_name, ' ', last_name) as fullname from actor group by fullname having count(*) = 1; 

-- task 3.2  names repeated
select concat(first_name, ' ', last_name) as fullname, count(*) as repeatedcount from actor group by fullname having count(*) > 1;

-- task 4 film category according to actors preference
select category.name as genre, concat(first_name, ' ', last_name) as actorname from category join film_category using(category_id) join film_actor using (film_id) join actor using(actor_id) where name = "action" or name = "romanace" or name = "horror" or name = "mystery";		

-- task 5.1 film per category
select count(film_id) as film_count, name as category_name from film join film_category using(film_id) join category using(category_id) group by category_name;

-- task 5.2  movies with nc-17 ratings
select title, description, name as category_name, rating from film join film_category using(film_id) join category using(category_id) where rating = 'NC-17' group by category_name;

-- task 5.3 movies with pg-13 ratings
select title, description, name as category_name, rating from film join film_category using(film_id) join category using(category_id) where rating = 'PG-13' group by category_name;

-- task 6.1  replacement greater than 9 (no data)
select title, replacement_cost from film where replacement_cost <= 9;

-- task 6.2 replacement cost betweem 15 and 20
select title, replacement_cost from film where replacement_cost between 15 and 20;

-- task 6.3 movies with highest replacement but lowest rental
select title, max(replacement_cost), min(rental_rate) from film order by replacement_cost desc;

-- task 7  number of actors in each film
select title, count(actor_id) from film join film_actor on film.film_id = film_actor.film_id group by title;

-- task 8 movies starting from k and q
select title from film  where title like 'q%' or title like 'k%';

-- task 9 actors in agent truman film
select actor_id, concat(first_name,' ',last_name) as 'full_name' from actor where actor_id in (select actor_id from film_actor  where film_id = (select film_id from film where title = 'agent truman'));

-- task 10 movies with family as category
select film_id, title from film where film_id in (select film_id from film_category where category_id = (select category_id from category where name = 'family'));

-- task 11 frequently rented movies
select title, count(rental_id) as borrowed_count from film left join inventory on film.film_id = inventory.film_id left join rental on rental.inventory_id = inventory.inventory_id group by title order by borrowed_count desc;

-- task 12 movies with difference in avg replacement and avg rental rate greater than 15
select (select (select name from category where category.category_id = film_category.category_id) from film_category where film_category.film_id = film.film_id) as genre, avg(replacement_cost), avg(rental_rate), avg(replacement_cost) - avg(rental_rate) as cost_difference from film group by genre having avg(replacement_cost) - avg(rental_rate) > 15;

-- task 13 number of films per category 60 - 70 range
select (select (select name from category where category.category_id = film_category.category_id) from film_category where film_category.film_id = film.film_id) as genre , count(film_id) as movie_count from film group by genre having movie_count between 60 and 70;

