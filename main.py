# Write a Python Program to perform linear search by using functions
def search(lst,n):
  count=0
  for i in lst:
    if(n==i):
      return print("found at ",i)
      count=1
  if(count==0):
    return print("Not found")
lst=[11,55,9,2,4,56,86,2]
num=int(input())
search(lst,num)