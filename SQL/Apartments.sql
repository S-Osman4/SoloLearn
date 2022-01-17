/*
Apartments
You want to rent an apartment and have the following table named Apartments
Write a query to output the apartments whose prices are greater than the average and are also not rented, sorted by the 'Price' column.
Recall the AVG keyword.
*/
SELECT id, city, address, price, status FROM Apartments 
WHERE price > ( SELECT AVG(price)FROM Apartments)
ORDER BY price;
