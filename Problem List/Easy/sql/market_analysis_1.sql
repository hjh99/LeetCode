-- +----------------+---------+
-- | Column Name    | Type    |
-- +----------------+---------+
-- | user_id        | int     |
-- | join_date      | date    |
-- | favorite_brand | varchar |
-- +----------------+---------+
-- user_id is the primary key (column with unique values) of this table.
-- This table has the info of the users of an online shopping website where users can sell and buy items.
 

-- Table: Orders

-- +---------------+---------+
-- | Column Name   | Type    |
-- +---------------+---------+
-- | order_id      | int     |
-- | order_date    | date    |
-- | item_id       | int     |
-- | buyer_id      | int     |
-- | seller_id     | int     |
-- +---------------+---------+
-- order_id is the primary key (column with unique values) of this table.
-- item_id is a foreign key (reference column) to the Items table.
-- buyer_id and seller_id are foreign keys to the Users table.
 

-- Table: Items

-- +---------------+---------+
-- | Column Name   | Type    |
-- +---------------+---------+
-- | item_id       | int     |
-- | item_brand    | varchar |
-- +---------------+---------+
-- item_id is the primary key (column with unique values) of this table.
 

-- Write a solution to find for each user, the join date and the number of orders they made as a buyer in 2019.

-- Return the result table in any order.

-- The result format is in the following example.

 

-- Example 1:

-- Input: 
-- Users table:
-- +---------+------------+----------------+
-- | user_id | join_date  | favorite_brand |
-- +---------+------------+----------------+
-- | 1       | 2018-01-01 | Lenovo         |
-- | 2       | 2018-02-09 | Samsung        |
-- | 3       | 2018-01-19 | LG             |
-- | 4       | 2018-05-21 | HP             |
-- +---------+------------+----------------+
-- Orders table:
-- +----------+------------+---------+----------+-----------+
-- | order_id | order_date | item_id | buyer_id | seller_id |
-- +----------+------------+---------+----------+-----------+
-- | 1        | 2019-08-01 | 4       | 1        | 2         |
-- | 2        | 2018-08-02 | 2       | 1        | 3         |
-- | 3        | 2019-08-03 | 3       | 2        | 3         |
-- | 4        | 2018-08-04 | 1       | 4        | 2         |
-- | 5        | 2018-08-04 | 1       | 3        | 4         |
-- | 6        | 2019-08-05 | 2       | 2        | 4         |
-- +----------+------------+---------+----------+-----------+
-- Items table:
-- +---------+------------+
-- | item_id | item_brand |
-- +---------+------------+
-- | 1       | Samsung    |
-- | 2       | Lenovo     |
-- | 3       | LG         |
-- | 4       | HP         |
-- +---------+------------+
-- Output: 
-- +-----------+------------+----------------+
-- | buyer_id  | join_date  | orders_in_2019 |
-- +-----------+------------+----------------+
-- | 1         | 2018-01-01 | 1              |
-- | 2         | 2018-02-09 | 2              |
-- | 3         | 2018-01-19 | 0              |
-- | 4         | 2018-05-21 | 0              |
-- +-----------+------------+---------------

# Write your MySQL query statement below
select u.user_id as buyer_id, u.join_date, count(o.order_id) as orders_in_2019 from Users u
left join Orders o on u.user_id = o.buyer_id and o.order_date between '2019-01-01' and '2019-12-31'
group by u.user_id, u.join_date;

-- Why this works:
-- LEFT JOIN: This ensures every user from the Users table stays in the final list, even if they have no matching orders.
-- The AND in the Join: By putting the date filter inside the ON clause (instead of a WHERE or HAVING clause), we tell SQL: "Match these users with orders if the order happened in 2019; otherwise, just put a NULL there."

-- -- COUNT(o.order_id): Since COUNT ignores NULL values, the users who had no orders in 2019 will correctly show a count of 0.
-- In SQL, the GROUP BY clause determines the unique "buckets" for your results.

-- Grouping by o.buyer_id: Creates a bucket for User 1, User 2, and one giant bucket for NULL (Users 3 and 4 combined).

-- Grouping by u.user_id: Creates a bucket for User 1, User 2, User 3, and User 4.