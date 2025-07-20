def find_floor_ceil(arr,x):
  left=0
  right=len(arr)-1
  floor=None
  ceil=None
  for i in range(len(arr)):
    mid=(left+right)//2
    if arr[mid]==x:
      return x,x
    elif arr[mid]<x:
      floor=arr[mid]
      left=mid+1
    else:
      ceil=arr[mid]
      right=mid-1
  return floor,ceil
arr=[6,8,9,10,12]
x=7
print(find_floor_ceil(arr,x))
