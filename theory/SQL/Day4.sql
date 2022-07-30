-- Q1
Write an SQL query to report the IDs of all the employees with missing information. The information of an employee is missing if:
The employee's name is missing, or
The employee's salary is missing.
Return the result table ordered by employee_id in ascending order.

Input: 
Employees table:
+-------------+----------+
| employee_id | name     |
+-------------+----------+
| 2           | Crew     |
| 4           | Haven    |
| 5           | Kristian |
+-------------+----------+
Salaries table:
+-------------+--------+
| employee_id | salary |
+-------------+--------+
| 5           | 76071  |
| 1           | 22517  |
| 4           | 63539  |
+-------------+--------+
Output: 
+-------------+
| employee_id |
+-------------+
| 1           |
| 2           |
+-------------+
Explanation: 
Employees 1, 2, 4, and 5 are working at this company.
The name of employee 1 is missing.
The salary of employee 2 is missing.

-- Code
SELECT Employees.employee_id AS "employee_id" FROM Employees
LEFT JOIN Salaries
ON Employees.employee_id = Salaries.employee_id 
WHERE Salaries.salary IS NULL
UNION
SELECT Salaries.employee_id AS "employee_id"  FROM Salaries
LEFT JOIN Employees
ON Employees.employee_id = Salaries.employee_id 
WHERE Employees.name IS NULL
ORDER BY employee_id
-- ---------------------------------------------------------------------------------------------------------------------------------------
-- ---------------------------------------------------------------------------------------------------------------------------------------
-- ---------------------------------------------------------------------------------------------------------------------------------------
-- Q2
Write an SQL query to rearrange the Products table so that each row has (product_id, store, price). If a product is not available in a store, do not include a row with that product_id and store combination in the result table.
Return the result table in any order.

Input: 
Products table:
+------------+--------+--------+--------+
| product_id | store1 | store2 | store3 |
+------------+--------+--------+--------+
| 0          | 95     | 100    | 105    |
| 1          | 70     | null   | 80     |
+------------+--------+--------+--------+
Output: 
+------------+--------+-------+
| product_id | store  | price |
+------------+--------+-------+
| 0          | store1 | 95    |
| 0          | store2 | 100   |
| 0          | store3 | 105   |
| 1          | store1 | 70    |
| 1          | store3 | 80    |
+------------+--------+-------+
Explanation: 
Product 0 is available in all three stores with prices 95, 100, and 105 respectively.
Product 1 is available in store1 with price 70 and store3 with price 80. The product is not available in store2

SELECT product_id, "store1" AS "store", store1 AS price
FROM Products
WHERE store1 IS NOT NULL
UNION
SELECT product_id, "store2" AS "store", store2 AS price
FROM Products
WHERE store2 IS NOT NULL
UNION
SELECT product_id, "store3" AS "store", store3 AS price
FROM Products
WHERE store3 IS NOT NULL


-- ---------------------------------------------------------------------------------------------------------------------------------------
-- ---------------------------------------------------------------------------------------------------------------------------------------
-- ---------------------------------------------------------------------------------------------------------------------------------------
-- Q3
Each node in the tree can be one of three types:

"Leaf": if the node is a leaf node.
"Root": if the node is the root of the tree.
"Inner": If the node is neither a leaf node nor a root node.

Input: 
Tree table:
+----+------+
| id | p_id |
+----+------+
| 1  | null |
| 2  | 1    |
| 3  | 1    |
| 4  | 2    |
| 5  | 2    |
+----+------+
Output: 
+----+-------+
| id | type  |
+----+-------+
| 1  | Root  |
| 2  | Inner |
| 3  | Leaf  |
| 4  | Leaf  |
| 5  | Leaf  |
+----+-------+
Explanation: 
Node 1 is the root node because its parent node is null and it has child nodes 2 and 3.
Node 2 is an inner node because it has parent node 1 and child node 4 and 5.
Nodes 3, 4, and 5 are leaf nodes because they have parent nodes and they do not have child nodes.



SELECT id , "Root" AS "type" FROM Tree
WHERE p_id IS NULL
UNION
SELECT DISTINCT T1.id,"Inner" AS "type" 
FROM Tree AS T1
LEFT JOIN Tree AS T2
ON T1.id = T2.p_id
WHERE T2.p_id IS NOT NULL
AND T1.p_id IS NOT NULL
UNION
SELECT T1.id,"Leaf" AS "type"
FROM Tree AS T1
LEFT JOIN Tree AS T2
ON T1.id = T2.p_id
WHERE T2.p_id IS NULL
AND T1.p_id IS NOT NULL
ORDER BY id




-- ANOTHER CODE
SELECT DISTINCT T1.id,(CASE
             WHEN T1.p_id IS NULL THEN "Root"
             WHEN T1.p_id IS NOT NULL AND T2.p_id IS NOT NULL THEN "Inner"
             WHEN T1.p_id IS NOT NULL AND T2.p_id IS NULL THEN "Leaf"
             END
             ) AS "type"
FROM Tree AS T1
LEFT JOIN Tree AS T2
ON T1.id = T2.p_id
ORDER BY id

-- ---------------------------------------------------------------------------------------------------------------------------------------
-- ---------------------------------------------------------------------------------------------------------------------------------------
-- ---------------------------------------------------------------------------------------------------------------------------------------]
-- Q4
Write an SQL query to report the second highest salary from the Employee table. If there is no second highest salary, the query should report null.
Input: 
Employee table:
+----+--------+
| id | salary |
+----+--------+
| 1  | 100    |
| 2  | 200    |
| 3  | 300    |
+----+--------+
Output: 
+---------------------+
| SecondHighestSalary |
+---------------------+
| 200                 |
+---------------------+
Example 2:

Input: 
Employee table:
+----+--------+
| id | salary |
+----+--------+
| 1  | 100    |
+----+--------+
Output: 
+---------------------+
| SecondHighestSalary |
+---------------------+
| null                |
+---------------------+


SELECT MAX(salary) AS SecondHighestSalary 
FROM Employee
WHERE salary < (SELECT max(Salary) FROM Employee)

