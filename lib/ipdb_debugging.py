#!/usr/bin/env python3

# import ipdb

# def plus_two(num):
#     num + 2
#     ipdb.set_trace()
#     return num
import ipdb

def plus_two(num):
    num += 2  # Add 2 to num and assign it back to num
 
    return num  # Return the updated value of num

result = plus_two(3)
print(result)
