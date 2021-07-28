
item = int(input("Please choose a number between 0 and 30: "))

def binary_search(sequence_a, low, high, item):

    if high >= low:

        mid = (high + low) // 2

        if sequence_a[mid] == item:
            return mid

        elif sequence_a[mid] > item:
            return binary_search(sequence_a, low, mid - 1, item)

        else:
            return binary_search(sequence_a, mid + 1, high, item)

    else:
        return -1

# Create an array to be tested

def sequence_a(q1, q2):
  
    if (q1 == q2):
        return q1
  
    else:
  
        # Create empty list
        sequence_a = []
  
        while(q1 < q2+2 ):
              
            sequence_a.append(q1)
            q1 += 2
        return sequence_a
      
q1, q2 = 0, 30
# print(sequence_a(q1, q2))

sequence_a = sequence_a(q1, q2)
# item = 15

# Function call
result = binary_search(sequence_a, 0, len(sequence_a)-1, item)

if result != -1:
    print("Element is present at index item", str(result))
else:
    print("Element is not present in the array")

