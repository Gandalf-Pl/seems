---
layout: post
title: PostgreSQL Window Function
---

- PostgreSQL Window Function
 A window function performs a calculation across a set of table rows that are somehow
 related to the current row. This is comparable to the type of calculation that can
 be done with an aggregate function. But unlike regular aggregate functions
 examples:  
 SELECT depname, empno, salary, rank() OVER (PARTITION BY depname ORDER BY salary DESC) FROM empslary;  
 这个sql语句的功能是将empslary表按照depname进行分类,同时在每个分类里面按照salary进行排序
 如果OVER函数中没有使用PARTITION BY,则表示整个查询结果集是同一个Window.
 **Window function are permitted only in the SELECT list and the ORDER BY clause of the query. they
 are forbidden elsewhere, such as in GROUP BY, HAVING, AND WHERE clause **
 
 window functions execute after regular aggregate functions. this means it is valid to include an 