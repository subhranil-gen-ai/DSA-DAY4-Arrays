def binary_search(arr,target):
  low=0
  high=len(arr)-1
  while low <= high:
    mid=(low+high)//2
    if arr[mid]==target:
      return mid
    elif target > arr[mid]:
      low=mid+1
    else:
      high=mid-1
  return -1
arr=[1,2,3,4,5]
target=1
result=binary_search(arr,target)
print("Element found at index :"if result!=-1 else "Element not found",result)
