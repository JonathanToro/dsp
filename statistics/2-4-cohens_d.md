[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)
```
import nsfg
import thinkstats2
import math

preg = nsfg.ReadFemPreg()
live = preg[preg.outcome == 1]
firsts = live[live.birthord == 1]
others = live[live.birthord != 1]

def CohenEffectSize(group1, group2):
  diff = group1.mean() - group2.mean()
  var1 = group1.var()
  var2 = group2.var()
  n1, n2 = len(group1), len(group2)
  
  pooled_var = (n1*var1+n2*var2)/(n1+n2)
  d = diff/math.sqrt(pooled_var)
  return d
  
CohenEffectSize(firsts.totalwgt_lb, others.totalwgt_lb)   #we would get -.08967
CohenEffectSize(firsts.prglngth,others.prglngth) #we would get .02887

firsts.totalwgt_lb.mean()   #we would get 7.2010
others.totalwgt_lb.mean()   #we would get 7.3258
```
I calculated the mean weight of the firsts group and others group and found out that the firsts group on average weigh less than the others group by .1248 lb. However, after calculated the Cohen's d statistic of this variable I would get -.08967 pooled standard deviations. This results seems insignificant. Therefore, we cannot conclude that the firsts group do actually weigh less than the others group. Comparing this result with the pregnancy length variable it seems that the difference in weight is more significant than the difference in pregnancy length. However, both of these differences are insignificant. 
