# coding: utf8
import profile


def profile_test():
    total = 1
    for i in range(10):
        total *= (i+1)
        print total
    return total

if __name__ == "__main__":
    profile.run("profile_test()")
    # run第二个参数可以将分析结果写入到日志文件中
"""
性能分析结果
1
2
6
24
120
720
5040
40320
362880
3628800
         5 function calls in 0.007 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 :0(range)
        1    0.007    0.007    0.007    0.007 :0(setprofile)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.007    0.007 profile:0(profileTest())
        0    0.000             0.000          profile:0(profiler)
        1    0.000    0.000    0.000    0.000 test.py:4(profileTest)

:param ncalls:  表示函数的调用次数
:param tottime: 表示指定函数的总的运行时间,除掉函数中调用子函数的时间
:param percall: 第一个percall表示tottime/ncalls;
:param cumtime: 表示该函数及所有子函数的调用运行时间,即函数开始到函数返回的时间
:param percall: 第二个percall即函数平均运行一次的时间 cumtime/ncalls
:param filename:lineno: 每个函数调用的具体信息


Process finished with exit code 0
"""
