class Quick_Sort:
    def merge(self, arr, low, high):
        pivot= arr[low]
        i= low+1
        j= high
        while i<j:
            
            while arr[i]<=pivot and i<=high-1:
                i+= 1
            
            while arr[j]>pivot and j>=low+1:
                j-= 1
            
            if i<j:
                arr[i], arr[j]= arr[j], arr[i]
            
            else: break
        
        arr[low], arr[j]= arr[j], arr[low]
        return j
    
    def quicksort(self, arr, low, high):
        if low<high:
            partition_index= self.merge(arr, low, high)
            self.quicksort(arr, low, partition_index-1)
            self.quicksort(arr, partition_index+1, high)


if __name__=='__main__':
    arr= [4,1,7,9,3]
    ans= Quick_Sort()
    ans.quicksort(arr, 0, len(arr)-1)
    print(*arr)
