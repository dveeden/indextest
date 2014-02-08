#!/usr/bin/python3
import pprint
import inspect
import json
import mysql.connector

class IndexTester:
    def query(self, query, debug=False):
        test = IndexTest(query, self.dbparams, debug)
        return test

    def runall(self):
        testcount = 0
        resultpass = 0
        resultfail = 0

        members = inspect.getmembers(self, predicate=inspect.ismethod)
        for membername, method in members:
            if membername.startswith('test_'):
                testcount += 1
                result = method()
                if result is True:
                    resultpass += 1
                elif result is False:
                    resultfail += 1
        print('Tested {} queries, Pass: {}, Fail: {}'.format(
               testcount, resultpass, resultfail))

class IndexTest:
    def __init__(self, query, dbparams, debug):
        self.con = mysql.connector.connect(**dbparams)
        self.query = query
        self.debug = debug
        self.result = None
    
    def _runquery(self):
        cur = self.con.cursor()
        res = cur.execute("EXPLAIN FORMAT=JSON " + self.query)
        mresult = cur.fetchall()
        self.result = json.loads(mresult[0][0])
        if self.debug:
            pprint.pprint(self.result)

    def testEqual(self, field, value):
        if not self.result:
            self._runquery()
        
        res = self.result
        for k in field.split('.'):
            res = res.get(k)
        qval = res

        qres = qval == value
        print('Query: {query}\n'
              'Test: {field} == {value}\n'
              'Result: {value} == {qval}: {result}\n'.format(
               query=self.query, field=field, value=value, qval=qval, result=qres))
        return qres
