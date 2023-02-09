"""
CMPS 2200  Recitation 2
"""

### the only imports needed are here
#import tabulate for grading github purposes 
import time
import math
###

#I coded this out in VS code and only put the final steps here for simplicity and clarity

def simple_work_calc(n, a, b):
	"""Compute the value of the recurrence $W(n) = aW(n/b) + n

	Params:
	n......input integer
	a......branching factor of recursion tree
	b......input split factor

	Returns: the value of W(n).
	"""
	# TODO
	if n <= 1:
		return 1 #base case
	else:
		return a*simple_work_calc(n/b, a, b) + n #recursive step 
	pass

def test_simple_work():
	""" done. """
	assert work_calc(10, 2, 2) == 56 #TODO
	assert work_calc(20, 3, 2) == 506.75 #TODO
	assert work_calc(30, 4, 2) == 1954 #TODO
	assert work_calc(16, 2, 3) == 80
	assert work_calc(20, 4, 2) == 1644
	assert work_calc(10, 2, 5) == 18
	
#pytest main.py::test_simple_work

def work_calc(n, a, b, f):
	"""Compute the value of the recurrence $W(n) = aW(n/b) + f(n)

	Params:
	n......input integer
	a......branching factor of recursion tree
	b......input split factor
	f......a function that takes an integer and returns 
           the work done at each node 

	Returns: the value of W(n).
	"""
	# TODO
	if n <= 1:
		return 1 #base case
	else: 
		return a*work_calc(n//b, a, b, f) + f(n) #recursive step that only works with integer values as opposed to simple_work
	pass

def span_calc(n, a, b, f):
	"""Compute the span associated with the recurrence $W(n) = aW(n/b) + f(n)

	Params:
	n......input integer
	a......branching factor of recursion tree
	b......input split factor
	f......a function that takes an integer and returns 
           the work done at each node 

	Returns: the value of W(n).
	"""
	# TODO
	if n<= 1:
		return 1 #base case
	else:
		return a*work_calc(n//b, a, b, f) + f(n) 
	pass

def test_work():
	""" done. """
	assert work_calc(10, 2, 2,lambda n: 1) == 15 #TODO
	assert work_calc(20, 1, 2, lambda n: n*n) == 530 #TODO
	assert work_calc(30, 3, 2, lambda n: n) == 300 #TODO
	assert work_calc(16, 1, 2,lambda n: n) == 31
	assert work_calc(8, 1, 2,lambda n: 1) == 4
	assert work_calc(24, 3, 2,lambda n: n*n) == 1656

def compare_work(work_fn1, work_fn2, sizes=[10, 20, 50, 100, 1000, 5000, 10000]):
	"""
	Compare the values of different recurrences for 
	given input sizes.

	Returns:
	A list of tuples of the form
	(n, work_fn1(n), work_fn2(n), ...)
	
	"""
	result_w = []
	for n in sizes:
		# compute W(n) using current a, b, f
		result_w.append((
			n,
			work_fn1(n),
			work_fn2(n)
			))
	return result_w



def print_result_work(result_w):
	""" done """
	print(tabulate.tabulate(result_w,
							headers=['n', 'W_1', 'W_2'],
							floatfmt=".3f",
							tablefmt="github"))

def test_compare_work():
	# curry work_calc to create multiple work
	# functions taht can be passed to compare_work
    
	# create work_fn1
	# create work_fn2

    def work_fn1(n):
        return work_calc(n, 2, 2, lambda n: n)
    
    def work_fn2(n):
        return work_calc(n, 2, 2,lambda n: math.log(n, 2))

    res = compare_work(work_fn1, work_fn2)
    print_result_work(res)

#test_compare_work()

def print_result_span(result_s):
	""" done """
	print(tabulate.tabulate(result_s,
							headers=['n', 'S_1', 'S_2'],
							floatfmt=".3f",
							tablefmt="github"))

def compare_span(span_fn1, span_fn2, sizes=[10, 20, 50, 100, 1000, 5000, 10000]):
	"""
	Compare the values of different recurrences for 
	given input sizes.

	Returns:
	A list of tuples of the form
	(n, span_fn1(n), span_fn2(n), ...)
	
	"""
	result_s = []
	for n in sizes:
		# compute W(n) using current a, b, f
		result_s.append((
			n,
			span_fn1(n),
			span_fn2(n)
			))
	return result_s

def test_compare_span():
	# curry span_calc to create multiple span
	# functions taht can be passed to compare_span
    
	# create span_fn1
	# create span_fn2

    def span_fn1(n):
        return span_calc(n, 2, 2, lambda n: 1)
    
    def span_fn2(n):
        return span_calc(n, 2, 2,lambda n: n)

    res = compare_span(span_fn1, span_fn2)
    print_result_span(res)

#test_compare_span()
