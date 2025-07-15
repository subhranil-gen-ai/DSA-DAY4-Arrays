def count_frequency(arr,target):
  count=0
  for i in range(len(arr)):
    if arr[i]==target:
      count += 1
  return count
arr=[2,4,4,1,1,3,9]
target=4
result=count_frequency(arr,target)
print("Frequency of target:",result)
