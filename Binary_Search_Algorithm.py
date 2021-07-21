
# iterative implementation of binary search in Python

def sequence_a(r1, r2):
  
    # Testing if range r1 and r2 
    # are equal
    if (r1 == r2):
        return r1
  
    else:
  
        # Create empty list
        a_list = []
  
        # loop to append successors to 
        # list until r2 is reached.
        while(r1 < r2+2 ):
              
            a_list.append(r1)
            r1 += 2
        return a_list
      

def binary_search(sequence, item):
    begin_index = 0
    end_index = len(sequence_a) - 1

    while begin_index < end_index:
        midpoint = begin_index + (end_index - begin_index) // 2
        midpoint_value = sequence_a[midpoint]
        if midpoint_value == item:
            return midpoint

        elif item < midpoint_value:
            end_index = midpoint - 1

        else:
            begin_index = midpoint + 1

    return None

# sequence_a = [2,4,6,8,10,12,14]
# item_a = 12

# Driver Code
r1, r2 = 0, 14
print(sequence_a(r1, r2))
item_a = 12

# print(binary_search(sequence_a, item_a))









""" Binary Search Algorithm 
----------------------------------------
"""
# iterative implementation of binary search in Python

# def sequence_a(r1, r2):
  
#     # Testing if range r1 and r2 
#     # are equal
#     if (r1 == r2):
#         return r1
  
#     else:
  
#         # Create empty list
#         a_list = []
  
#         # loop to append successors to 
#         # list until r2 is reached.
#         while(r1 < r2+2 ):
              
#             a_list.append(r1)
#             r1 += 2
#         return a_list
      
# # Driver Code
# r1, r2 = 0, 10
# print(sequence_a(r1, r2))

# item = int(input("Please enter a number between 0 and 10: "))


# def binary_search(a_list, item):
#     """Performs iterative binary search to find the position of an integer in a given, sorted, list.
#     a_list -- sorted list of integers
#     item -- integer you are searching for the position of
#     """
#     first = 0
#     last = len(a_list) - 1
#     while first <= last:
#         i = (first + last) / 2
#         if a_list[i] == item:
#             return ' found at position '.format(item=item, i=i)
#         elif a_list[i] > item:
#             last = i - 1
#         elif a_list[i] < item:
#             first = i + 1
#         else:
#             return ' not found in the list'.format(item=item)

# recursive implementation of binary search in Python
# def binary_search_recursive(a_list, item):
#     """Performs recursive binary search of an integer in a given, sorted, list.
#     a_list -- sorted list of integers
#     item -- integer you are searching for the position of
#     """
#     first = 0
#     last = len(a_list) - 1
#     if len(a_list) == 0:
#         return ' was not found in the list'.format(item=item)
#     else:
#         i = (first + last) // 2
#         if item == a_list[i]:
#             return ' found'.format(item=item)
#         else:
#             if a_list[i] < item:
#                 return binary_search_recursive(a_list[i+1:], item)
#             else:
#                 return binary_search_recursive(a_list[:i], item)