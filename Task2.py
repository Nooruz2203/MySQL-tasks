
mysql> USE home_task;
Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A

Database changed
mysql> SELECT first_name "First Name", last_name "Last Name" FROM employees;
+------------+------------+
| First Name | Last Name  |
+------------+------------+
| Steven     | King       |
| Neena      | Kochhar    |
| Lex        | DeHaan     |
| Alexander  | Hunold     |
| Bruce      | Ernst      |
| David      | Austin     |
| Valli      | Pataballa  |
| Diana      | Lorentz    |
| Nancy      | Greenberg  |
| Daniel     | Faviet     |
| John       | Chen       |
| Ismael     | Sciarra    |
| JoseManuel | Urman      |
| Luis       | Popp       |
| Alexander  | Khoo       |
| Shelli     | Baida      |
| Sigal      | Tobias     |
| Guy        | Himuro     |
| Karen      | Colmenares |
+------------+------------+
19 rows in set (0.00 sec)

mysql> SELECT DISTINCT department_id FROM employees;
+---------------+
| department_id |
+---------------+
|            90 |
|            60 |
|           100 |
|            30 |
+---------------+
4 rows in set (0.00 sec)

mysql> SELECT * FROM employees ORDER BY first_name DESC;
+-------------+------------+------------+----------+--------------+------------+------------+--------+---------------+------------+---------------+
| employee_id | first_name | last_name  | email    | phone_number | hire_date  | job_id     | salary | comission_pct | manager_id | department_id |
+-------------+------------+------------+----------+--------------+------------+------------+--------+---------------+------------+---------------+
|         106 | Valli      | Pataballa  | VPATABAL | 590.423.4560 | 1987-06-23 | IT_PROG    |   4800 |             0 |        103 |            60 |
|         100 | Steven     | King       | SKING    | 515.123.4567 | 1987-06-17 | AD_PRES    |  24000 |             0 |          0 |            90 |
|         117 | Sigal      | Tobias     | STOBIAS  | 515.127.4564 | 1987-07-04 | PU_CLERK   |   2800 |             0 |        114 |            30 |
|         116 | Shelli     | Baida      | SBAIDA   | 515.127.4563 | 1987-07-03 | PU_CLERK   |   2900 |             0 |        114 |            30 |
|         101 | Neena      | Kochhar    | NKOCHHAR | 515.123.4568 | 1987-06-18 | AD_VP      |  17000 |             0 |        100 |            90 |
|         108 | Nancy      | Greenberg  | NGREENBE | 515.124.4569 | 1987-06-25 | FI_MGR     |  12000 |             0 |        101 |           100 |
|         113 | Luis       | Popp       | LPOPP    | 515.124.4567 | 1987-06-30 | FI_ACCOUNT |   6900 |             0 |        108 |           100 |
|         102 | Lex        | DeHaan     | LDEHAAN  | 515.123.4569 | 1987-06-19 | AD_VP      |  17000 |             0 |        100 |            90 |
|         119 | Karen      | Colmenares | KCOLMENA | 515.127.4566 | 1987-07-06 | PU_CLERK   |   2500 |             0 |        114 |            30 |
|         112 | JoseManuel | Urman      | JMURMAN  | 515.124.4469 | 1987-06-29 | FI_ACCOUNT |   7800 |             0 |        108 |           100 |
|         110 | John       | Chen       | JCHEN    | 515.124.4269 | 1987-06-27 | FI_ACCOUNT |   8200 |             0 |        108 |           100 |
|         111 | Ismael     | Sciarra    | ISCIARRA | 515.124.4369 | 1987-06-28 | FI_ACCOUNT |   7700 |             0 |        108 |           100 |
|         118 | Guy        | Himuro     | GHIMURO  | 515.127.4565 | 1987-07-05 | PU_CLERK   |   2600 |             0 |        114 |            30 |
|         107 | Diana      | Lorentz    | DLORENTZ | 590.423.5567 | 1987-06-24 | IT_PROG    |   4200 |             0 |        103 |            60 |
|         105 | David      | Austin     | DAUSTIN  | 590.423.4569 | 1987-06-22 | IT_PROG    |   4800 |             0 |        103 |            60 |
|         109 | Daniel     | Faviet     | DFAVIET  | 515.124.4169 | 1987-06-26 | FI_ACCOUNT |   9000 |             0 |        108 |           100 |
|         104 | Bruce      | Ernst      | BERNST   | 590.423.4568 | 1987-06-21 | IT_PROG    |   6000 |             0 |        103 |            60 |
|         115 | Alexander  | Khoo       | AKHOO    | 515.127.4562 | 1987-07-02 | PU_CLERK   |   3100 |             0 |        114 |            30 |
|         103 | Alexander  | Hunold     | AHUNOLD  | 590.423.4567 | 1987-06-20 | IT_PROG    |   9000 |             0 |        102 |            60 |
+-------------+------------+------------+----------+--------------+------------+------------+--------+---------------+------------+---------------+
19 rows in set (0.00 sec)

mysql> SELECT employee_id, first_name, last_name, salary FROM employees ORDER BY salary;
+-------------+------------+------------+--------+
| employee_id | first_name | last_name  | salary |
+-------------+------------+------------+--------+
|         119 | Karen      | Colmenares |   2500 |
|         118 | Guy        | Himuro     |   2600 |
|         117 | Sigal      | Tobias     |   2800 |
|         116 | Shelli     | Baida      |   2900 |
|         115 | Alexander  | Khoo       |   3100 |
|         107 | Diana      | Lorentz    |   4200 |
|         105 | David      | Austin     |   4800 |
|         106 | Valli      | Pataballa  |   4800 |
|         104 | Bruce      | Ernst      |   6000 |
|         113 | Luis       | Popp       |   6900 |
|         111 | Ismael     | Sciarra    |   7700 |
|         112 | JoseManuel | Urman      |   7800 |
|         110 | John       | Chen       |   8200 |
|         109 | Daniel     | Faviet     |   9000 |
|         103 | Alexander  | Hunold     |   9000 |
|         108 | Nancy      | Greenberg  |  12000 |
|         102 | Lex        | DeHaan     |  17000 |
|         101 | Neena      | Kochhar    |  17000 |
|         100 | Steven     | King       |  24000 |
+-------------+------------+------------+--------+
19 rows in set (0.00 sec)

mysql> SELECT COUNT(*) FROM employees;
+----------+
| COUNT(*) |
+----------+
|       19 |
+----------+
1 row in set (0.00 sec)

mysql> SELECT  first_name, last_name, salary FROM employees WHERE salary NOT BETWEEN 10000 AND 15000;
+------------+------------+--------+
| first_name | last_name  | salary |
+------------+------------+--------+
| Steven     | King       |  24000 |
| Neena      | Kochhar    |  17000 |
| Lex        | DeHaan     |  17000 |
| Alexander  | Hunold     |   9000 |
| Bruce      | Ernst      |   6000 |
| David      | Austin     |   4800 |
| Valli      | Pataballa  |   4800 |
| Diana      | Lorentz    |   4200 |
| Daniel     | Faviet     |   9000 |
| John       | Chen       |   8200 |
| Ismael     | Sciarra    |   7700 |
| JoseManuel | Urman      |   7800 |
| Luis       | Popp       |   6900 |
| Alexander  | Khoo       |   3100 |
| Shelli     | Baida      |   2900 |
| Sigal      | Tobias     |   2800 |
| Guy        | Himuro     |   2600 |
| Karen      | Colmenares |   2500 |
+------------+------------+--------+
18 rows in set (0.00 sec)

mysql> SELECT  first_name, last_name, department_id FROM employees WHERE department_id IN (30,100) ORDER BY department_id ASC;
+------------+------------+---------------+
| first_name | last_name  | department_id |
+------------+------------+---------------+
| Alexander  | Khoo       |            30 |
| Shelli     | Baida      |            30 |
| Sigal      | Tobias     |            30 |
| Guy        | Himuro     |            30 |
| Karen      | Colmenares |            30 |
| Nancy      | Greenberg  |           100 |
| Daniel     | Faviet     |           100 |
| John       | Chen       |           100 |
| Ismael     | Sciarra    |           100 |
| JoseManuel | Urman      |           100 |
| Luis       | Popp       |           100 |
+------------+------------+---------------+
11 rows in set (0.00 sec)

mysql> SELECT  first_name, last_name, hire_date FROM employees WHERE YEAR(hire_date) LIKE '1987%';
+------------+------------+------------+
| first_name | last_name  | hire_date  |
+------------+------------+------------+
| Steven     | King       | 1987-06-17 |
| Neena      | Kochhar    | 1987-06-18 |
| Lex        | DeHaan     | 1987-06-19 |
| Alexander  | Hunold     | 1987-06-20 |
| Bruce      | Ernst      | 1987-06-21 |
| David      | Austin     | 1987-06-22 |
| Valli      | Pataballa  | 1987-06-23 |
| Diana      | Lorentz    | 1987-06-24 |
| Nancy      | Greenberg  | 1987-06-25 |
| Daniel     | Faviet     | 1987-06-26 |
| John       | Chen       | 1987-06-27 |
| Ismael     | Sciarra    | 1987-06-28 |
| JoseManuel | Urman      | 1987-06-29 |
| Luis       | Popp       | 1987-06-30 |
| Alexander  | Khoo       | 1987-07-02 |
| Shelli     | Baida      | 1987-07-03 |
| Sigal      | Tobias     | 1987-07-04 |
| Guy        | Himuro     | 1987-07-05 |
| Karen      | Colmenares | 1987-07-06 |
+------------+------------+------------+
19 rows in set (0.00 sec)

mysql> SELECT last_name, job_id,salary FROM employees WHERE job_id IN ('IT_PROG', 'SH_CLERK') AND salary NOT IN (4500,10000,15000);
+-----------+---------+--------+
| last_name | job_id  | salary |
+-----------+---------+--------+
| Hunold    | IT_PROG |   9000 |
| Ernst     | IT_PROG |   6000 |
| Austin    | IT_PROG |   4800 |
| Pataballa | IT_PROG |   4800 |
| Lorentz   | IT_PROG |   4200 |
+-----------+---------+--------+
5 rows in set (0.00 sec)

mysql> SELECT * FROM employees WHERE last_name IN ('BLAKE', 'SCOTT','KING','FORD');
+-------------+------------+-----------+-------+--------------+------------+---------+--------+---------------+------------+---------------+
| employee_id | first_name | last_name | email | phone_number | hire_date  | job_id  | salary | comission_pct | manager_id | department_id |
+-------------+------------+-----------+-------+--------------+------------+---------+--------+---------------+------------+---------------+
|         100 | Steven     | King      | SKING | 515.123.4567 | 1987-06-17 | AD_PRES |  24000 |             0 |          0 |            90 |
+-------------+------------+-----------+-------+--------------+------------+---------+--------+---------------+------------+---------------+
1 row in set (0.01 sec)

mysql> SELECT SUM (salary) FROM employees;
ERROR 1630 (42000): FUNCTION home_task.SUM does not exist. Check the 'Function Name Parsing and Resolution' section in the Reference Manual
mysql> SELECT SUM(salary) FROM employees;
+-------------+
| SUM(salary) |
+-------------+
|      152300 |
+-------------+
1 row in set (0.00 sec)

mysql> SELECT MIN(salary) FROM employees;
+-------------+
| MIN(salary) |
+-------------+
|        2500 |
+-------------+
1 row in set (0.00 sec)

mysql> SELECT AVG(salary), COUNT(*) FROM employees WHERE department_id=90;
+-------------+----------+
| AVG(salary) | COUNT(*) |
+-------------+----------+
|  19333.3333 |        3 |
+-------------+----------+
1 row in set (0.00 sec)

mysql> SELECT job_id, COUNT(*) FROM employees GROUP BY job_id;
+------------+----------+
| job_id     | COUNT(*) |
+------------+----------+
| AD_PRES    |        1 |
| AD_VP      |        2 |
| FI_ACCOUNT |        5 |
| FI_MGR     |        1 |
| IT_PROG    |        5 |
| PU_CLERK   |        5 |
+------------+----------+
6 rows in set (0.00 sec)    
mysql> SELECT job_id, AVG(salary) FROM employees WHERE job_id <> 'IT_PROG' GROUP BY job_id;
+------------+-------------+
| job_id     | AVG(salary) |
+------------+-------------+
| AD_PRES    |  24000.0000 |
| AD_VP      |  17000.0000 |
| FI_ACCOUNT |   7920.0000 |
| FI_MGR     |  12000.0000 |
| PU_CLERK   |   2780.0000 |
+------------+-------------+
5 rows in set (0.00 sec)

mysql> SELECT location_id, street_address, city, state_province, country_name FROM locations NATURAL JOIN countries;
+-------------+---------------------------+---------------------+-----------------+--------------------------+
| location_id | street_address            | city                | state_province  | country_name             |
+-------------+---------------------------+---------------------+-----------------+--------------------------+
|        1000 | 1297 Via Cola di Rie      | Roma                |                 | Italy                    |
|        1100 | 93091 Calle della Testa   | Venice              |                 | Italy                    |
|        1400 | 2014 Jabberwocky Rd       | Southlake           | Texas           | United States of America |
|        1500 | 2011 Interiors Blvd       | South San Francisco | California      | United States of America |
|        1600 | 2007 Zagora St            | South Brunswick     | New Jersey      | United States of America |
|        1700 | 2004 Charade Rd           | Seattle             | Washington      | United States of America |
|        1800 | 147 Spadina Ave           | Toronto             | Ontario         | Canada                   |
|        1900 | 6092 Boxwood St           | Whitehorse          | Yukon           | Canada                   |
|        2000 | 40-5-12 Laogianggen       | Beijing             |                 | China                    |
|        2100 | 1298 Vileparle (E)        | Bombay              | Maharashtra     | India                    |
|        2200 | 12-98 Victoria Street     | Sydney              | New South Wales | Australia                |
|        2300 | 198 Clementi North        | Singapore           |                 | Singapore                |
|        2400 | 8204 Arthur St            | London              |                 | United Kingdom           |
|        2500 | "Magdalen Centre          | OX9 9ZB             | Oxford          | United Kingdom           |
|        2600 | 9702 Chester Road         | Stretford           | Manchester      | United Kingdom           |
|        2700 | Schwanthalerstr. 7031     | Munich              | Bavaria         | Germany                  |
|        2800 | Rua Frei Caneca 1360      | Sao Paulo           | Sao Paulo       | Brazil                   |
|        2900 | 20 Rue des Corps-Saints   | Geneva              | Geneve          | Switzerland              |
|        3000 | Murtenstrasse 921         | Bern                | BE              | Switzerland              |
|        3100 | Pieter Breughelstraat 837 | Utrecht             | Utrecht         | Netherlands              |
+-------------+---------------------------+---------------------+-----------------+--------------------------+
20 rows in set (0.01 sec)
mysql> SELECT  first_name, last_name, department_id, department_name FROM employees JOIN departments USING (department_id);
+------------+------------+---------------+-----------------+
| first_name | last_name  | department_id | department_name |
+------------+------------+---------------+-----------------+
| Steven     | King       |            90 | Executive       |
| Neena      | Kochhar    |            90 | Executive       |
| Lex        | DeHaan     |            90 | Executive       |
| Alexander  | Hunold     |            60 | IT              |
| Bruce      | Ernst      |            60 | IT              |
| David      | Austin     |            60 | IT              |
| Valli      | Pataballa  |            60 | IT              |
| Diana      | Lorentz    |            60 | IT              |
| Nancy      | Greenberg  |           100 | Finance         |
| Daniel     | Faviet     |           100 | Finance         |
| John       | Chen       |           100 | Finance         |
| Ismael     | Sciarra    |           100 | Finance         |
| JoseManuel | Urman      |           100 | Finance         |
| Luis       | Popp       |           100 | Finance         |
| Alexander  | Khoo       |            30 | Purchasing      |
| Shelli     | Baida      |            30 | Purchasing      |
| Sigal      | Tobias     |            30 | Purchasing      |
| Guy        | Himuro     |            30 | Purchasing      |
| Karen      | Colmenares |            30 | Purchasing      |
+------------+------------+---------------+-----------------+
19 rows in set (0.00 sec)
mysql> SELECT employee_id, job_title, end_date-start_date Days FROM job_history NATURAL JOIN jobs WHERE department_id=90;
+-------------+--------------------------+-------+
| employee_id | job_title                | Days  |
+-------------+--------------------------+-------+
|         200 | Administration Assistant | 59700 |
|         200 | Public Accountant        | 40530 |
+-------------+--------------------------+-------+
2 rows in set (0.00 sec)

mysql> SELECT d.department_name, e.first_name, l.city FROM departments d JOIN employees e ON (d.manager_id=e.employee_id) JOIN locations l USING (location_id);
+-----------------+------------+-----------+
| department_name | first_name | city      |
+-----------------+------------+-----------+
| IT              | Alexander  | Southlake |
| Executive       | Steven     | Seattle   |
| Finance         | Nancy      | Seattle   |
+-----------------+------------+-----------+
3 rows in set (0.00 sec)
mysql> SELECT  first_name, last_name, hire_date, salary, (DATEDIFF(now(), hire_date))/365 Experience FROM departments d JOIN employees e ON (d.manager_id=e.employee_id)  WHERE (DATEDIFF(now(), hire_date))/365>15;
+------------+-----------+------------+--------+------------+
| first_name | last_name | hire_date  | salary | Experience |
+------------+-----------+------------+--------+------------+
| Alexander  | Hunold    | 1987-06-20 |   9000 |    32.9534 |
| Steven     | King      | 1987-06-17 |  24000 |    32.9616 |
| Nancy      | Greenberg | 1987-06-25 |  12000 |    32.9397 |
+------------+-----------+------------+--------+------------+
3 rows in set (0.00 sec)

mysql> SELECT date (((PERIOD_ADD(EXTRACT(YEAR_MONTH FROM CURDATE()),-3)*100)+1));
+--------------------------------------------------------------------+
| date (((PERIOD_ADD(EXTRACT(YEAR_MONTH FROM CURDATE()),-3)*100)+1)) |
+--------------------------------------------------------------------+
| 2020-02-01                                                         |
+--------------------------------------------------------------------+
1 row in set (0.00 sec)
mysql> SELECT STR_TO_DATE(CONCAT(12,31, EXTRACT(YEAR FROM CURDATE())),'%m%d%Y');
+-------------------------------------------------------------------+
| STR_TO_DATE(CONCAT(12,31, EXTRACT(YEAR FROM CURDATE())),'%m%d%Y') |
+-------------------------------------------------------------------+
| 2020-12-31                                                        |
+-------------------------------------------------------------------+
1 row in set (0.37 sec)

mysql> SELECT DATE_FORMAT(CURDATE(),'%M %e, %Y') AS 'Current_date';
+--------------+
| Current_date |
+--------------+
| May 25, 2020 |
+--------------+
1 row in set (0.00 sec)

mysql> SELECT first_name, last_name FROM employees WHERE MONTH(hire_date)=6;
+------------+-----------+
| first_name | last_name |
+------------+-----------+
| Steven     | King      |
| Neena      | Kochhar   |
| Lex        | DeHaan    |
| Alexander  | Hunold    |
| Bruce      | Ernst     |
| David      | Austin    |
| Valli      | Pataballa |
| Diana      | Lorentz   |
| Nancy      | Greenberg |
| Daniel     | Faviet    |
| John       | Chen      |
| Ismael     | Sciarra   |
| JoseManuel | Urman     |
| Luis       | Popp      |
+------------+-----------+
14 rows in set (0.34 sec)

mysql> SELECT first_name,SYSDATE(), hire_date,DATEDIFF(SYSDATE(), hire_date)/365 FROM employees;
+------------+---------------------+------------+------------------------------------+
| first_name | SYSDATE()           | hire_date  | DATEDIFF(SYSDATE(), hire_date)/365 |
+------------+---------------------+------------+------------------------------------+
| Steven     | 2020-05-25 16:53:53 | 1987-06-17 |                            32.9616 |
| Neena      | 2020-05-25 16:53:53 | 1987-06-18 |                            32.9589 |
| Lex        | 2020-05-25 16:53:53 | 1987-06-19 |                            32.9562 |
| Alexander  | 2020-05-25 16:53:53 | 1987-06-20 |                            32.9534 |
| Bruce      | 2020-05-25 16:53:53 | 1987-06-21 |                            32.9507 |
| David      | 2020-05-25 16:53:53 | 1987-06-22 |                            32.9479 |
| Valli      | 2020-05-25 16:53:53 | 1987-06-23 |                            32.9452 |
| Diana      | 2020-05-25 16:53:53 | 1987-06-24 |                            32.9425 |
| Nancy      | 2020-05-25 16:53:53 | 1987-06-25 |                            32.9397 |
| Daniel     | 2020-05-25 16:53:53 | 1987-06-26 |                            32.9370 |
| John       | 2020-05-25 16:53:53 | 1987-06-27 |                            32.9342 |
| Ismael     | 2020-05-25 16:53:53 | 1987-06-28 |                            32.9315 |
| JoseManuel | 2020-05-25 16:53:53 | 1987-06-29 |                            32.9288 |
| Luis       | 2020-05-25 16:53:53 | 1987-06-30 |                            32.9260 |
| Alexander  | 2020-05-25 16:53:53 | 1987-07-02 |                            32.9205 |
| Shelli     | 2020-05-25 16:53:53 | 1987-07-03 |                            32.9178 |
| Sigal      | 2020-05-25 16:53:53 | 1987-07-04 |                            32.9151 |
| Guy        | 2020-05-25 16:53:53 | 1987-07-05 |                            32.9123 |
| Karen      | 2020-05-25 16:53:53 | 1987-07-06 |                            32.9096 |
+------------+---------------------+------------+------------------------------------+
19 rows in set (0.00 sec)
