

# Homework Assignment

## Installation Instructions

* Refer to the [installation guide](Installation.md) to install the necessary files.

## Instructions

* 1a. Display the first and last names of all actors from the table `actor`.

###  SELECT first_name, last_name FROM sakila.actor;

* 1b. Display the first and last name of each actor in a single column in upper case letters. Name the column `Actor Name`.
###SELECT UPPER(CONCAT(first_name, ' ', last_name)) AS 'ACTOR NAME' FROM actor;
* 2a. You need to find the ID number, first name, and last name of an actor, of whom you know only the first name, "Joe." What is one query would you use to obtain this information?
###SELECT actor_id, first_name, last_name from actor where first_name = 'JOE';
* 2b. Find all actors whose last name contain the letters `GEN`:
### SELECT * FROM actor WHERE last_name LIKE '%GEN%';
* 2c. Find all actors whose last names contain the letters `LI`. This time, order the rows by last name and first name, in that order:
select * from actor
where last_name like '%LI%' Order BY last_name, first_name

* 2d. Using `IN`, display the `country_id` and `country` columns of the following countries: Afghanistan, Bangladesh, and China:
SELECT country_id, country
from country
where country in ('Afghanistan', 'Bangladesh', 'China');

* 3a. Add a `middle_name` column to the table `actor`. Position it between `first_name` and `last_name`. Hint: you will need to specify the data type.

* 3b. You realize that some of these actors have tremendously long last names. Change the data type of the `middle_name` column to `blobs`.

* 3c. Now delete the `middle_name` column.

* 4a. List the last names of actors, as well as how many actors have that last name.

* 4b. List last names of actors and the number of actors who have that last name, but only for names that are shared by at least two actors

* 4c. Oh, no! The actor `HARPO WILLIAMS` was accidentally entered in the `actor` table as `GROUCHO WILLIAMS`, the name of Harpo's second cousin's husband's yoga teacher. Write a query to fix the record.

* 4d. Perhaps we were too hasty in changing `GROUCHO` to `HARPO`. It turns out that `GROUCHO` was the correct name after all! In a single query, if the first name of the actor is currently `HARPO`, change it to `GROUCHO`. Otherwise, change the first name to `MUCHO GROUCHO`, as that is exactly what the actor will be with the grievous error. BE CAREFUL NOT TO CHANGE THE FIRST NAME OF EVERY ACTOR TO `MUCHO GROUCHO`, HOWEVER! (Hint: update the record using a unique identifier.)

* 5a. You cannot locate the schema of the `address` table. Which query would you use to re-create it?

  * Hint: <https://dev.mysql.com/doc/refman/5.7/en/show-create-table.html>

* 6a. Use `JOIN` to display the first and last names, as well as the address, of each staff member. Use the tables `staff` and `address`:

* 6b. Use `JOIN` to display the total amount rung up by each staff member in August of 2005. Use tables `staff` and `payment`.

* 6c. List each film and the number of actors who are listed for that film. Use tables `film_actor` and `film`. Use inner join.

* 6d. How many copies of the film `Hunchback Impossible` exist in the inventory system?

* 6e. Using the tables `payment` and `customer` and the `JOIN` command, list the total paid by each customer. List the customers alphabetically by last name:

  ```
  	![Total amount paid](Images/total_payment.png)
  ```

* 7a. The music of Queen and Kris Kristofferson have seen an unlikely resurgence. As an unintended consequence, films starting with the letters `K` and `Q` have also soared in popularity. Use subqueries to display the titles of movies starting with the letters `K` and `Q` whose language is English.

* 7b. Use subqueries to display all actors who appear in the film `Alone Trip`.

* 7c. You want to run an email marketing campaign in Canada, for which you will need the names and email addresses of all Canadian customers. Use joins to retrieve this information.

* 7d. Sales have been lagging among young families, and you wish to target all family movies for a promotion. Identify all movies categorized as family films.

* 7e. Display the most frequently rented movies in descending order.

* 7f. Write a query to display how much business, in dollars, each store brought in.

* 7g. Write a query to display for each store its store ID, city, and country.

* 7h. List the top five genres in gross revenue in descending order. (**Hint**: you may need to use the following tables: category, film_category, inventory, payment, and rental.)

* 8a. In your new role as an executive, you would like to have an easy way of viewing the Top five genres by gross revenue. Use the solution from the problem above to create a view. If you haven't solved 7h, you can substitute another query to create a view.

* 8b. How would you display the view that you created in 8a?

* 8c. You find that you no longer need the view `top_five_genres`. Write a query to delete it.

## Appendix: List of Tables in the Sakila DB

* A schema is also available as `sakila_schema.svg`. Open it with a browser to view.

```sql
	'actor'
	'actor_info'
	'address'
	'category'
	'city'
	'country'
	'customer'
	'customer_list'
	'film'
	'film_actor'
	'film_category'
	'film_list'
	'film_text'
	'inventory'
	'language'
	'nicer_but_slower_film_list'
	'payment'
	'rental'
	'sales_by_film_category'
	'sales_by_store'
	'staff'
	'staff_list'
	'store'
```

## Uploading Homework

* To submit this homework using BootCampSpot:

  * Create a GitHub repository.
  * Upload your .sql file with the completed queries.
  * Submit a link to your GitHub repo through BootCampSpot.



  USE sakila;

# 1a. Display the first and last names of all actors from the table `actor`.
SELECT first_name, last_name FROM sakila.actor;

# 1b. Display the first and last name of each actor in a single column in upper case letters. Name the column `Actor Name`.
SELECT UPPER(CONCAT(first_name, ' ', last_name)) AS 'ACTOR NAME' 
FROM actor;

#* 2a. You need to find the ID number, first name, and last name of an actor, of whom you know only the first name, "Joe." What is one query would you use to obtain this information?
SELECT actor_id, first_name, last_name
FROM actor
WHERE first_name = 'JOE';

#* 2b. Find all actors whose last name contain the letters `GEN`:
SELECT * FROM actor
WHERE last_name LIKE '%GEN%';

#* 2c. Find all actors whose last names contain the letters `LI`. This time, order the rows by last name and first name, in that order:
SELECT actor_id, last_name, first_name
FROM actor
WHERE last_name LIKE '%LI%' ORDER BY last_name, first_name;

#* 2d. Using `IN`, display the `country_id` and `country` columns of the following countries: Afghanistan, Bangladesh, and China:
SELECT country_id, country
FROM country
WHERE country IN ('Afghanistan', 'Bangladesh', 'China');

#* 3a. Add a `middle_name` column to the table `actor`. Position it between `first_name` and `last_name`. Hint: you will need to specify the data type.
ALTER TABLE actor
ADD COLUMN middle_name VARCHAR(15) DEFAULT NULL after first_name;

SELECT*FROM actor;

#* 3b. You realize that some of these actors have tremendously long last names. Change the data type of the `middle_name` column to `blobs`.
ALTER TABLE actor 
MODIFY COLUMN middle_name BLOB; 

#* 3c. Now delete the `middle_name` column.
ALTER TABLE actor
DROP COLUMN middle_name;

#* 4a. List the last names of actors, as well as how many actors have that last name.
SELECT DISTINCT last_name, COUNT(last_name) AS 'count'
FROM actor
GROUP BY last_name;

#* 4b. List last names of actors and the number of actors who have that last name, but only for names that are shared by at least two actors
SELECT DISTINCT last_name, COUNT(last_name) AS 'count'
FROM actor
GROUP BY last_name HAVING COUNT >=2;

#* 4c. Oh, no! The actor `HARPO WILLIAMS` was accidentally entered in the `actor` table as `GROUCHO WILLIAMS`, the name of Harpo's second cousin's husband's yoga teacher. Write a query to fix the record.
UPDATE actor
SET first_name = 'HARPO'
WHERE first_name = 'GROUCHO' AND last_name = 'WILLIAMS';

#* 4d. Perhaps we were too hasty in changing `GROUCHO` to `HARPO`. It turns out that `GROUCHO` was the correct name after all! In a single query, if the first name of the actor is currently `HARPO`, change it to `GROUCHO`. Otherwise, change the first name to `MUCHO GROUCHO`, as that is exactly what the actor will be with the grievous error. BE CAREFUL NOT TO CHANGE THE FIRST NAME OF EVERY ACTOR TO `MUCHO GROUCHO`, HOWEVER! (Hint: update the record using a unique identifier.)


UPDATE actor
SET first_name=CASE
	WHEN first_name = 'HARPO' THEN 'GROUCHO'
	ELSE 'MUCHO GROUCHO'
END
WHERE Actor_id = 172;

#* 5a. You cannot locate the schema of the `address` table. Which query would you use to re-create it?
CREATE TABLE IF NOT EXISTS `address` (
  `address_id` smallint(5) unsigned NOT NULL AUTO_INCREMENT,
  `address` varchar(50) NOT NULL,
  `address2` varchar(50) DEFAULT NULL,
  `district` varchar(20) NOT NULL,
  `city_id` smallint(5) unsigned NOT NULL,
  `postal_code` varchar(10) DEFAULT NULL,
  `phone` varchar(20) NOT NULL,
  `location` geometry NOT NULL,
  `last_update` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`address_id`),
  KEY `idx_fk_city_id` (`city_id`),
  SPATIAL KEY `idx_location` (`location`),
  CONSTRAINT `fk_address_city` FOREIGN KEY (`city_id`) REFERENCES `city` (`city_id`) ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=606 DEFAULT CHARSET=utf8;


#* 6a. Use `JOIN` to display the first and last names, as well as the address, of each staff member. Use the tables `staff` and `address`:
SELECT first_name, last_name, address
FROM staff
INNER JOIN address
ON staff.address_id = address.address_id;


#* 6b. Use `JOIN` to display the total amount rung up by each staff member in August of 2005. Use tables `staff` and `payment`.
SELECT first_name, last_name, SUM(amount) AS 'total_rung_up'
FROM staff
INNER JOIN payment
ON staff.staff_id = payment.staff_id
GROUP BY payment.staff_id
ORDER BY last_name ASC;




#* 6c. List each film and the number of actors who are listed for that film. Use tables `film_actor` and `film`. Use inner join.
SELECT title, COUNT(actor_id) AS 'number_of_actors'
FROM film
INNER JOIN film_actor
ON film.film_id = film_actor.film_id
GROUP BY title;

#* 6d. How many copies of the film `Hunchback Impossible` exist in the inventory system?

SELECT title, COUNT(inventory_id) AS 'total_copies'
FROM film
INNER JOIN inventory
ON film.film_id = inventory.film_id
WHERE title = 'Hunchback Impossible';


#* 6e. Using the tables `payment` and `customer` and the `JOIN` command, list the total paid by each customer. List the customers alphabetically by last name:
#![Total amount paid](Images/total_payment.png)

SELECT last_name, first_name, SUM(amount) AS 'total_paid'
FROM payment
INNER JOIN customer
ON payment.customer_id = customer.customer_id
GROUP BY payment.customer_id
ORDER BY last_name ASC;


#* 7a. The music of Queen and Kris Kristofferson have seen an unlikely resurgence. As an unintended consequence, films starting with the letters `K` and `Q` have also soared in popularity. Use subqueries to display the titles of movies starting with the letters `K` and `Q` whose language is English.

SELECT title 
FROM film
WHERE language_id in
	(SELECT language_id 
	FROM language
	WHERE name = "English" ) AND (title LIKE "K%") OR (title LIKE "Q%");

#* 7b. Use subqueries to display all actors who appear in the film `Alone Trip`.

SELECT actor_id, first_name, last_name
FROM actor
WHERE actor_id in
	(SELECT actor_id FROM film_actor
	WHERE film_id in 
		(SELECT film_id FROM film
		WHERE title = "Alone Trip"));

#* 7c. You want to run an email marketing campaign in Canada, for which you will need the names and email addresses of all Canadian customers. Use joins to retrieve this information.

SELECT country, first_name, last_name, email
FROM country
LEFT JOIN customer
ON country.country_id = customer.customer_id
WHERE country = 'Canada';


#* 7d. Sales have been lagging among young families, and you wish to target all family movies for a promotion. Identify all movies categorized as family films.

SELECT category, title
FROM film_list
WHERE category = 'Family';


#* 7e. Display the most frequently rented movies in descending order.

SELECT inventory.film_id, film_text.title, COUNT(rental.inventory_id) as 'rental_count'
FROM inventory 
INNER JOIN rental
ON inventory.inventory_id = rental.inventory_id
INNER JOIN film_text 
ON inventory.film_id = film_text.film_id
GROUP BY rental.inventory_id
ORDER BY COUNT(rental.inventory_id) DESC;


#* 7f. Write a query to display how much business, in dollars, each store brought in.

SELECT store.store_id, SUM(amount) as 'total_sales'
FROM store
INNER JOIN staff
ON store.store_id = staff.store_id
INNER JOIN payment p 
ON p.staff_id = staff.staff_id
GROUP BY store.store_id
ORDER BY SUM(amount);

#* 7g. Write a query to display for each store its store ID, city, and country.

SELECT store.store_id, city, country
FROM store
INNER JOIN customer
ON store.store_id = customer.store_id
INNER JOIN staff
ON store.store_id = staff.store_id
INNER JOIN address
ON customer.address_id = address.address_id
INNER JOIN city
ON address.city_id = city.city_id
INNER JOIN country
ON city.country_id = country.country_id;


#* 7h. List the top five genres in gross revenue in descending order. (**Hint**: you may need to use the following tables: category, film_category, inventory, payment, and rental.)
SELECT category.name AS 'genre', SUM(payment.amount) AS 'gross_revenue'
FROM category
INNER JOIN film_category
ON category.category_id = film_category.category_id
INNER JOIN inventory
ON inventory.film_id = film_category.film_id
INNER JOIN rental
ON rental.inventory_id = inventory.inventory_id
INNER JOIN payment
ON rental.rental_id = payment.rental_id
GROUP BY category.name ORDER BY gross_revenue DESC LIMIT 5;

#* 8a. In your new role as an executive, you would like to have an easy way of viewing the Top five genres by gross revenue. Use the solution from the problem above to create a view. If you haven't solved 7h, you can substitute another query to create a view.

CREATE VIEW top_five_genres AS
SELECT category.name AS 'genre', SUM(payment.amount) AS 'gross_revenue'
FROM category 
INNER JOIN film_category
ON category.category_id = film_category.category_id
INNER JOIN inventory 
ON inventory.film_id = film_category.film_id
INNER JOIN rental
ON rental.inventory_id = inventory.inventory_id
INNER JOIN payment
ON  rental.rental_id = payment.rental_id
GROUP BY category.name ORDER BY gross_revenue DESC  LIMIT 5;


#* 8b. How would you display the view that you created in 8a?

SELECT * FROM top_five_genres;

#* 8c. You find that you no longer need the view `top_five_genres`. Write a query to delete it.

DROP VIEW top_five_genres;


## Appendix: List of Tables in the Sakila DB

#* A schema is also available as `sakila_schema.svg`. Open it with a browser to view.

```sql
	'actor'
	'actor_info'
	'address'
	'category'
	'city'
	'country'
	'customer'
	'customer_list'
	'film'
	'film_actor'
	'film_category'
	'film_list'
	'film_text'
	'inventory'
	'language'
	'nicer_but_slower_film_list'
	'payment'
	'rental'
	'sales_by_film_category'
	'sales_by_store'
	'staff'
	'staff_list'
	'store'
```

## Uploading Homework

* To submit this homework using BootCampSpot:

  * Create a GitHub repository.
  * Upload your .sql file with the completed queries.
  * Submit a link to your GitHub repo through BootCampSpot.



)





