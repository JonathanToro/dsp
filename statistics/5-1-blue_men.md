[Think Stats Chapter 5 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2006.html#toc50) (blue men)

>> We have to determine what percent of the US male population is in the range of 5'10" and 6'1" in height.

```
import thinkstats2
import thinkplot
import scipy.stats

mu = 178
sigma = 7.7
dist = scipy.stats.norm(loc=mu, scale = sigma)
inch = 2.54
low = inch*70
high = inch*73
dist.cdf(high) - dist.cdf(low)    #the result is around 34%
```
