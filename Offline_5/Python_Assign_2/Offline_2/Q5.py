#=========================Q5==================================
def merge(arr1,arr2):
   i=0
   j=0
   arr=[]
   while(i<len(arr1) and j<len(arr2)):
      if(arr1[i]<arr2[j]):
         arr.append(arr1[i])
         i+=1
      else:
         arr.append(arr2[j])
         j+=1
   while(i<len(arr1)):
      arr.append(arr1[i])
      i+=1
   while(j<len(arr2)):
      arr.append(arr2[j])
      j+=1
   return arr

def merge_sort(array):
   if(len(array)==1):
      return array
   mid=(len(array))//2
   arr1=merge_sort(array[:mid])
   arr2=merge_sort(array[mid:])
   return merge(arr1,arr2)

n = int(input("Enter the Array size:"))
i=0
array=[]
while i<n:
  val=int(input("Enter the Value:"))
  array.insert(i,val)
  i=i+1
print(merge_sort(array))
 



