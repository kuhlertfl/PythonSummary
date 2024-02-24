import numpy as np 

test = np.random.binomial(n=1000 , p=0.5 , size = 500)
print(test)
#gives back 500 conducted experiments like a coin toss with the probability of 0.5 for success and 0.5 of failure with 1000 tosses in each experiment --> list of 500 numbers with the number of success like [500 , 499 , 506 ...]
