def find_duplicates(array):
     
  seen = set()
  duplicates = []
  for element in array:
    if element in seen:
      duplicates.append(element)
    else:
      seen.add(element)

  return duplicates


if __name__ == "__main__":
  array = [4, 3, 2, 7, 8, 2, 3, 1]
  duplicates = find_duplicates(array)
  print(duplicates)
