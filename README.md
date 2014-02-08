Index Tester
============

This requires MySQL 5.6.5 to use FORMAT=JSON for EXPLAIN. 

Example run:

	$ ./example.py 
	Query: SELECT * FROM movies WHERE rank>9.8
	Test: query_block.table.access_type == range
	Result: range == range: True
	
	Query: SELECT * FROM actors WHERE first_name='Tom'
	Test: query_block.table.access_type == range
	Result: range == ref: False
	
	Query: SELECT * FROM actors WHERE first_name='%Tom'
	Test: query_block.table.key == idx_first_name
	Result: idx_first_name == idx_first_name: True
	
	Tested 3 queries, Pass: 2, Fail: 1
