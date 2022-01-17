/*
A local bakery creates unique cake sets. Each cake set contains three different cakes.

Write a query to sort the cakes by calorie count and select the first 3 cakes from the list to offer the customer.
Try to combine ORDER BY and LIMIT keywords.
*/
SELECT name,calories  from cakes
ORDER by calories asc
limit 3
