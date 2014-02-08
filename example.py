#!/usr/bin/python3
import indextest


class tester(indextest.IndexTester):
    def __init__(self):
        dbparams = { 'user': 'msandbox',
                     'password': 'msandbox',
                     'host': 'localhost',
                     'port': '5615',
                     'database': 'imdb'}
        self.dbparams = dbparams

    def test_query1(self):
        q1 = self.query("SELECT * FROM movies WHERE rank>9.8")
        return q1.testEqual('query_block.table.access_type', 'range')

    def test_query2(self):
        q2 = self.query("SELECT * FROM actors WHERE first_name='Tom'")
        return q2.testEqual('query_block.table.access_type', 'range')

    def test_query3(self):
        q3 = self.query("SELECT * FROM actors WHERE first_name='%Tom'")
        return q3.testEqual('query_block.table.key', 'idx_first_name')

run = tester()
run.runall()
