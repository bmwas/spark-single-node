# -*- coding: utf-8 -*-
"""
A very short function to demonstrate how to use apache spark with python (pyspark)
@author: Benson Mwangi  2017
NB: This code assumes spark is properly installed and executed in a standalone node or cluster.
"""
# import pyspark ( sparkcontext and sparkconf)
#Note:- Sparkcontext represents a connection to a spark cluster & also used to create a RDD
#Note:- SparkConf Configuration for a Spark application. Used to set various Spark parameters 
from pyspark import SparkContext, SparkConf
 
data = [1,2,3,444,3,44,5,6,7,333,7,8,99999,0,0,2,1,0.0,2,1,99,0]


#We have to import python packages and wrapp them in a function
def compute_sqrt(x):
    import numpy as np
    sdr=np.sqrt(x)
    return sdr

##spark configurations
conf = SparkConf().setAppName('testapp')
sc = SparkContext(conf=conf)
#declare a rdd
rdd = sc.parallelize(data)
#Execute the function usng pyspark
newrdd=rdd.map(lambda x: compute_sqrt(x))
#Collect results.
print newrdd.collect()