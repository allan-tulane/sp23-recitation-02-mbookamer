# CMPS 2200  Recitation 02

**Name (Team Member 1):** Mackenzie Bookamer

**ANSWERS ARE IN THIS TEXT FILE**


In this recitation, we will investigate recurrences. 
To complete this recitation, follow the instructions in this document. Some of your answers will go in this file, and others will require you to edit `main.py`.


## Setup
- Make sure you have a Github account.
- Login to Github.
- Login to repl.it, using "sign in with github"
- Click on the assignment link sent through canvas and accept the assignment.
- Click on your personal github repository for the assignment.
- Click on the "Work in Repl.it" button. This will launch an instance of `repl.it` initialized with the code from your repository.
- You'll work with a partner to complete this recitation. To do so, we'll break you into Zoom rooms. You will be able to code together in the same `repl.it` instance. You can choose whose repl.it instance you will share. This person will click the "Share" button in their repl.it instance and email the lab partner.

## Running and testing your code
- In the command-line window, run `./ipy` to launch an interactive IPython shell. This is an interactive shell to help run and debug your code. Any code you change in `main.py` will be reflected from this shell. So, you can modify a function in `main.py`, then test it here.
  + If it seems things don't refresh, try running `from main import *`
- You can exit the IPython prompt by either typing `exit` or pressing `ctrl-d`
- To run tests, from the command-line shell, you can run
  + `pytest main.py` will run all tests
  + `pytest main.py::test_one` will just run `test_one`
  + We recommend running one test at a time as you are debugging.

## Turning in your work

- Once complete, click on the "Version Control" icon in the left pane on repl.it.
- Enter a commit message in the "what did you change?" text box
- Click "commit and push." This will push your code to your github repository.
- Although you are working as a team, please have each team member submit the same code to their repository. One person can copy the code to their repl.it and submit it from there.

## Recurrences

In class, we've started looking at recurrences and how to we can establish asymptotic bounds on their values as a function of $n$. In this lab, we'll write some code to generate recursion trees (via a recursive function) for certain kinds of recurrences. By summing up nodes in the recurrence tree (that represent contributions to the recurrence) we can compare their total cost against the corresponding asymptotic bounds. We'll focus on  recurrences of the form:

$$ W(n) = aW(n/b) + f(n) $$

where $W(1) = 1$.

- [x ] 1. (2 point) In `main.py`, you have stub code which includes a function `simple_work_calc`. Implement this function to return the value of $W(n)$ for arbitrary values of $a$ and $b$ with $f(n)=n$.

- [ x] 2. (2 point) Test that your function is correct by calling from the command-line `pytest main.py::test_simple_work` by completing the test cases and adding 3 additional ones.

- [ x] 3. (2 point) Now implement `work_calc`, which generalizes the above so that we can now input $a$, $b$ and a *function* $f(n)$ as arguments. Test this code by completing the test cases in `test_work` and adding 3 more cases.

- [FIX ] 4. (2 point) Now, derive the asymptotic behavior of $W(n)$ using $f(n) = 1$, $f(n) = \log n$ and $f(n) = n$. Then, generate actual values for $W(n)$ for your code and confirm that the trends match your derivations.

-When f(n) = 1, we see that the function is leaf dominated, with the total work at the last level being $2^i$. We know our last level is when i = $\log_2 n$, and when we compute this value, we get n, meaning that O(n) is correct.

-When f(n) = $\log n$, the function is root dominated because the work done at each level decreases, so we only care about the work done at the root, which is $\log n$, so O($\log n$) is correct. 

-When f(n) = n, we see that the function is balanced, with the work on the first level being the same as the work done on the last level, which is equal to n. Thus, our total work is given by multiplying our tree depth by the work done at every level, yielding O(n * $\log_2 n$).

Fixed a, b =2. 

table for $w_1$ = f(n) =1, $w_2$ = f(n) = n: 
|     n |   W_1 |    W_2 |
|-------|-------|--------|
|    10 |    15 |     36 |
|    20 |    31 |     92 |
|    50 |    63 |    276 |
|   100 |   127 |    652 |
|  1000 |  1023 |   9120 |
|  5000 |  8191 |  61728 |
| 10000 | 16383 | 133456 |

table for $w_1$ = f(n) = n, $w_2$= f(n) = $\log n$:
|     n |    W_1 |       W_2 |
|-------|--------|-----------|
|    10 |     36 |    19.966 |
|    20 |     92 |    44.253 |
|    50 |    276 |   107.311 |
|   100 |    652 |   221.265 |
|  1000 |   9120 |  1896.421 |
|  5000 |  61728 | 12497.283 |
| 10000 | 133456 | 25007.854 |

**TODO: your answer goes here**

- [ ] 5. (4 points) Now that you have a nice way to empirically generate valuess of $W(n)$, we can look at the relationship between $a$, $b$, and $f(n)$. Suppose that $f(n) = n^c$. What is the asypmptotic behavior of $W(n)$ if $c < \log_b a$? What about $c > \log_b a$? And if they are equal? Modify `compare_work` to compare empirical values for different work functions (at several different values of $n$) to justify your answer. 

I plugged in values of a=4, b=2 to use for my values to compute the exponents. In order to get the exponent value, for $c < \log_b a$, I put $c = \log_b a -1$ as the exponent. For $c > \log_b a$, I put $c = \log_b a +1$ as the exponent. For the equality, I simply put $c = \log_b a$ as the exponent. My results are below. 

table for $w_1$ = $c = \log_b a -1$, $w_2$= $c = \log_b a +1$:
|     n |           W_1 |               W_2 |
|-------|---------------|-------------------|
|    10 |       126.000 |          1692.000 |
|    20 |       524.000 |         14768.000 |
|    50 |      2518.000 |        236908.000 |
|   100 |     10172.000 |       1947632.000 |
|  1000 |    697496.000 |    1987993280.000 |
|  5000 |  34237688.000 |  249711292352.000 |
| 10000 | 136960752.000 | 1998845169408.000 |

table for $w_1$ = $c = \log_b a -1$, $w_2$= $c = \log_b$: 

|     n |           W_1 |            W_2 |
|-------|---------------|----------------|
|    10 |       126.000 |        328.000 |
|    20 |       524.000 |       1712.000 |
|    50 |      2518.000 |      12936.000 |
|   100 |     10172.000 |      61744.000 |
|  1000 |    697496.000 |    8544512.000 |
|  5000 |  34237688.000 |  294904064.000 |
| 10000 | 136960752.000 | 1279616256.000 |



**TODO: your answer goes here**

- [ x] 6. (3 points) $W(n)$ is meant to represent the running time of some recursive algorithm. Suppose we always had $a$ processors available to us and we wanted to compute the span of the same algorithm. Implement the function `span_calc` to compute the empirical span, where the work of the algorithm is given by $W(n)$. Implement `test_compare_span` to create a new comparison function for comparing span functions. Derive the asymptotic expressions for the span of the recurrences you used in problem 4 above. Confirm that everything matches up as it should. 

-When f(n) = 1, we see that the span is balanced, so we just multiply our total cost at each node by the number of levels, yielding O($\log n$). 

-When f(n) = $\log n$, the function is leaf dominated because the work done at each level increases, so we only care about the work done at the last level, which is $\log n$ * $\log n$, so O($\log^2 n$) is correct. 

-When f(n) = n, we see that the function is root dominated because the work done at each level decreases, so we only care about the work done at the root, which is $\log n$, so O(n) is correct. 


table for $s_1$ = f(n) = n, $s_2$= f(n) = $\log n$:
|     n |    S_1 |       S_2 |
|-------|--------|-----------|
|    10 |     36 |    19.966 |
|    20 |     92 |    44.253 |
|    50 |    276 |   107.311 |
|   100 |    652 |   221.265 |
|  1000 |   9120 |  1896.421 |
|  5000 |  61728 | 12497.283 |
| 10000 | 133456 | 25007.854 |

table for $s_1$ = f(n) =1, $s_2$ = f(n) = n:
|     n |   S_1 |    S_2 |
|-------|-------|--------|
|    10 |    15 |     36 |
|    20 |    31 |     92 |
|    50 |    63 |    276 |
|   100 |   127 |    652 |
|  1000 |  1023 |   9120 |
|  5000 |  8191 |  61728 |
| 10000 | 16383 | 133456 |


**TODO: your answer goes here**
