# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

###Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>>  Lists are a list of values. Each one of them is numbered starting from zero - the first one is numbered 0, the second 1, etc. You can remove values from the list, and add new values to the end. Tuples are like lists, but you can't change their values. They're not mutable. Again, each value is numbered starting from zero. Tuples can work as keys in dictionaries becuase of their immutability. 
    

---

###Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>> There are a few differences between sets and lists. For example, sets can not contain duplicates while lists can. Sets are also unordered. In addition, a hash lookup is used to find an element in a set. Likewise sets can only contain hashable items. In practical applications, lists are very nice to sort and have order while sets are nice to use when you don't want duplicates and don't care about order.

---

###Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> Lambda expressions allow us to create "anonymous" functions. This basically means we can quickly make ad-hoc functions without needing to properly define a function using def. Function objects returned by running lambda expressions work exactly the same as those created and assigned by defs.

An example of using lambda in the 'key' argument to 'sorted' is below.
Let's say we have a collection that contains the different animals in the zoo and the number of each animal.
```python
zoo = [('monkey',5), ('donkey',2), ('elephant',10), ('lion',1), ('tiger',4)]
```

We can use the lambda expression to sort the collection by the amount of animals in each species.
```python
sorted(zoo, key = lambda k: k[1])
```

---

###Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> List comprehensions allow us to build out lists using a different notation. We can think of it as essentially a one line for loop built inside of brackets.

An example of a list comprehension is below.

```python
lst = [x**2 for x in range(0,11)]
```

This is the same as writing:
```python
lst = []
for number in range(0,11):
    lst.append(number**2)
```

map() is a function that takes in two arguments: a function and a sequence iterable. Using map is commonly used with lambda expressions since the entire purpose of map() is to save effort on having to create manual for loops. Below is an example.
```python
lst = range(0,11)
map(lambda x: x**2, lst)
```
The function filter(function, list) offers a convenient way to filter out all the elements of an iterable, for which the function returns True. The function filter(function(),l) needs a function as its first argument. The function needs to return a Boolean value (either True or False). This function will be applied to every element of the iterable. Only if the function returns True will the element of the iterable be included in the result. An example is below.

```python
##First we will create a function
def odd_check(num):
    if num%2!=0:
        return True
```

Now we will filter a list of numbers.
```python
lst = range(20)
filter(odd_check,lst)
```
The lambda expression is also commonly used with filter. We will reproduce the same result as above by using the lambda expression.
```python
filter(lambda x: x%2!=0,lst)
```

---

###Complete the following problems by editing the files below:

###Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> 937 days

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> 513 days

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE  (answer will be in number of days)

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

###Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

###Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

###Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)





