def linear_search(arr,target):
  for i in range(len(arr)):
    if arr[i]==target:
      return i
  return -1
arr=[6,7,2,4,9]
target=7
result=linear_search(arr,target)
print("Element found at index: "if result != -1 else "Element not found",result)
