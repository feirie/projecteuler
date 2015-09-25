__author__ = 'feirie'
from functools import reduce
import operator

sumOfMultiples=lambda total:reduce(operator.add,filter(lambda x : x % 3==0 or x % 5==0,range(1,total)))
print(sumOfMultiples(1000))