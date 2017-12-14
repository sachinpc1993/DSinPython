'''We use python timeit module which help
Python developers to make cross-platform timing measurements by running functions in a consistent environment and
using timing mechanisms that are as similar as possible
across operating systems.
'''
import timeit

def test1():
    l = []
    for i in range(1000):
        l = l + [i]

def test2():
    l = []
    for i in range(1000):
        l.append(i)

def test3():
    l = [i for i in range(1000)]

def test4():
    l = list(range(1000))

t1 = timeit.Timer("test1()", "from __main__ import test1")
print("concat ",t1.timeit(number=1000), "milliseconds")
t2 = timeit.Timer("test2()", "from __main__ import test2")
print("append ",t2.timeit(number=1000), "milliseconds")
t3 = timeit.Timer("test3()", "from __main__ import test3")
print("comprehension ",t3.timeit(number=1000), "milliseconds")
t4 = timeit.Timer("test4()", "from __main__ import test4")
print("list range ",t4.timeit(number=1000), "milliseconds")


#Popping from end
def test5():
    x.pop()

#Popping from index
def test6():
    x.pop(8)

#Popping from beginning
def test7():
    x.pop(0)

t5 = timeit.Timer("test5()","from __main__ import test5")
t6 = timeit.Timer("test6()","from __main__ import test6")
t7 = timeit.Timer("test7()","from __main__ import test7")

#print "    PopBeg, PopEnd, PopInd"
print "---------------------------------------------------------------------------------------------"
print "     " + "i" + "        " + "PopBeg" + "            " + "PopEnd" + "             " + "PopInd"
print "---------------------------------------------------------------------------------------------"
for i in range(1000000,100000001,1000000):
    x = list(range(i))
    pt = t5.timeit(number=1000)
    x = list(range(i))
    pz = t7.timeit(number=1000)
    x = list(range(i))
    pi = t6.timeit(number=1000)

    print str(i) + "   " + str(pz) + "   " + str(pt) + "   " + str(pi)
    #print("%d, %15.5f, %15.5f, %15.5f" %(i,pz,pt,pi))
