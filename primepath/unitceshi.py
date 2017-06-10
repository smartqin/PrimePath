# -*- coding: utf-8 -*-
import codecs as cs
import filecmp
import graph1
import unittest, time
from HTMLTestRunner import HTMLTestRunner
import sys 

class myTest(unittest.TestCase):

    def setUp(self):
        print "Prime path test start."

    def test_path(self):
        for ii in range(16):
            name= 'case'+'%d'%ii+'.txt'
            graph=graph1.readGraph(name)
            #print graph
            graph1.get_prime(graph,ii)
            ans='answer'+'%d'%ii+'.txt'
            name2=r'hshanswer/'+ans
            comp=filecmp.cmp(ans,name2)
            #print "case"+str(i)+":",ans
            self.assertEqual(comp,True)


    def tearDown(self):
        print "Prime path test end."


if __name__ == "__main__":
    #unittest.main()
    
    testunit = unittest.TestSuite()
    testunit.addTest(myTest('test_path'))
    now = time.strftime("%Y-%m-%d %H-%M-%S")
    filename = './report' + now + '-result.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(stream=fp,                 
                        title='primepath test report',       
                        description='status：')    
    runner.run(testunit)    
    fp.close()
