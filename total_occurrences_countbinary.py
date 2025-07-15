def first_occurrence(arr,target):
  low=0
  high=len(arr)-1
  result=-1
  while low <= high:
    mid=(low+high)//2
    if arr[mid]==target:
      result=mid
      high=mid-1
    elif target>arr[mid]:
      low=mid+1
    else:
      high=mid-1
  return result
def last_occurrence(arr,target):
  low=0
  high=len(arr)-1
  result=-1
  while low <= high:
    mid=(low+high)//2
    if arr[mid]==target:
      result=mid
      low=mid+1
    elif target>arr[mid]:
      low=mid+1
    else:
      high=mid-1
  return result
def total_occurrences(arr,target):
  first=first_occurrence(arr,target)
  last=last_occurrence(arr,target)
  if first==-1:
    return 0
  return last-first+1
arr=[2,4,4,4,8,10]
target=4
result=total_occurrences(arr,target)
print("Total occurrences:",result)

