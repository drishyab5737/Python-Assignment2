def binarysearch(arr, start,end ,key):
    if end>=start:
        mid=start + (end-start)//2
        if(arr[mid]==key):
            return mid
        elif(arr[mid]>key):
            return binarysearch(arr,start,mid-1,key)
        else:
            return binarysearch(arr,mid+1,end,key)
    else:
        return -1
arr=sorted(['d','r','i','s','h','y','a'])
key='d'
result=binarysearch(arr,0,len(arr)-1, key)
if result!=-1:
    print("Element is at " +str(result) )
else:
    print("Element not found")