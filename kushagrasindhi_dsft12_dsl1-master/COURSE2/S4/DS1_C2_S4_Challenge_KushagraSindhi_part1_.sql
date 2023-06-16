-- task 1.1
select name from country where code in ("usa", "gbr", "are");

-- task 1.2
select avg(population) as 'World_Average' from (select continent, sum(population) population from country group by continent) AveragePop;

-- task 1.3
select name, continent from country where code in (select countrycode from countrylanguage where language = "french" and continent = "europe");

-- task 1.4
select name, population, continent from country task8country1 where population >= all (select population from country task8country2 where task8country1.continent = task8country2.continent);