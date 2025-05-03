from my_module import find_index
import os
friends = 'Ram,Naresh,Manish,Suresh,Kajal,Akshita'.split(',')

result_search = find_index(friends,'ram   ')
print(f"Ram is found at {result_search} index position.")
print(os.getcwd())