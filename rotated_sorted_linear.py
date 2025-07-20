def rotated_sorted_linear(arr,target):
  for i in range(len(arr)):
    if arr[i]==target:
      return i
  return 0
arr=[4,5,6,7,0,1,2]
target=0
print(rotated_sorted_linear(arr,target))
