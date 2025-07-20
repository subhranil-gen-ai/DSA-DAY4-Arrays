def rotated_sorted_binary(arr,target):
  left=0
  right=len(arr)-1
  for i in range(len(arr)):
    mid=(left+right)//2
    if arr[mid]==target:
      return mid
    elif arr[left]<=arr[mid]:
      if arr[left]<=target<arr[mid]:
        right=mid-1
      else:
        left=mid+1
    else:
      if arr[mid]<=target<arr[right]:
        left=mid+1
      else:
        right=mid-1
arr=[4,5,6,7,0,1,2]
target=4
print(rotated_sorted_binary(arr,target))
