def majority_element(array):
 
  n = len(array)
  majority_count = 0
  majority_element = None

  for element in array:
    if majority_count == 0:
      majority_element = element
      majority_count = 1
    elif element == majority_element:
      majority_count += 1
    else:
      majority_count -= 1

  if majority_count > n // 2:
    return majority_element
  else:
    return -1

arr = [2, 4, 5, 5, 5, 5, 5]
print(majority_element(arr))