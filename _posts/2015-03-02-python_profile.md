---
layout: post
title: Python性能相关的Tips
---


### List的append和insert操作    
   python的List不是一个单向列表或者一个双向列表,而是一个Array,存储在连续的内存块中.
   因此python中使用append和insert进行列表操作的效率不同,append的时间复杂度是O(1),
   而insert的时间复杂度是O(len(list)),也就是O(n).
   *code example:*
    
    
    # coding: utf8
    import time
    
    num = 5**10
    
    
    def test_append():
        x1 = time.time()
        list1 = list()
        for x in xrange(num):
            list1.append(x)
            
        list1.reverse()
        print "append cost time is %s " % (time.time() - x1)
        
        
    def test_insert():
        x2 = time.time()
        list2 = list()
        for x in xrange(num):
            list2.insert(0, x)
        print "insert cost time is %s " % (time.time() - x2)
        
    test_append()
    test_insert()
    
    
### Floating point computation is by nature inexact 

    >>> sum(0.1 for i in xrange(10)) == 1.0  # False
