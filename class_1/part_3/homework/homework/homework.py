def fancy_divide(list_of_numbers, index):
   denom = list_of_numbers[index]
   return [simple_divide(item, denom) for item in list_of_numbers]

"""
Your task is to change the definition of simple_divide so that the call does not raise an exception. 
When dividing by 0, fancy_divide should return a list with all 0 elements. 
Any other error cases should still raise exceptions. You should only handle the ZeroDivisionError.
"""

def simple_divide(item, denom):
   try:
       result = item/denom
   except ZeroDivisionError:
       return 0
   else:
       return result

print(fancy_divide([0, 2, 4], 0))
