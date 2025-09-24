SELECT * FROM artist;

SELECT first_name, last_name
FROM customer LIMIT 100;

SELECT * FROM album
WHERE artist_id = 1;

SELECT last_name, first_name
FROM employee
ORDER BY last_name ASC;

SELECT DISTINCT customer_id
FROM invoice
ORDER BY customer_id;

SELECT COUNT(*) AS total_artists
FROM artist;

SELECT country, COUNT(*) AS total_customers
FROM customer
GROUP BY country
ORDER BY total_customers DESC;