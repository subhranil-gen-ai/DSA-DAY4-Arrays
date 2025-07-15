def first_occurrence(arr,target):
  low=0
  high=len(arr)-1
  result=-1
  while low<=high:
    mid=(low+high)//2
    if arr[mid]==target:
      result=mid
      high=mid-1 #checking left
    elif target>arr[mid]:
      low=mid+1
    else:
      high=mid-1
  return result    
def last_occurrence(arr,target):
  low=0
  high=len(arr)-1
  result=-1
  while low<=high:
    mid=(low+high)//2
    if arr[mid]==target:
      result=mid
      low=mid+1 #checking right
    elif target>arr[mid]:
      low=mid+1
    else:
      high=mid-1
  return result   
def find_first_last(arr,target):
  first=first_occurrence(arr,target)
  last=last_occurrence(arr,target)
  return first,last
arr=[2,4,4,4,8,10]
target=4
f,l=find_first_last(arr,target)
print(f"first occurrence: {f} , last occurrence: {l}") 
