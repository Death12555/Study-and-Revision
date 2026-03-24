class Merge_Sort:
    def merge(self, arr, low, mid, high):
        temp_arr = []
        left = low
        right= mid +1
        while left<=mid and right<=high:
            if arr[left]<=arr[right]:
                temp_arr.append(arr[left])
                left+=1
            else:
                temp_arr.append(arr[right])
                right+=1

        while left<=mid:
            temp_arr.append(arr[left])
            left+=1
        
        while right<=high:
            temp_arr.append(arr[right])
            right+=1
        
        for i in range(len(temp_arr)):
            arr[low+i] = temp_arr[i]
    
    def mergesort(self, arr, low, high):
        if low>=high:
            return
        
        mid = (low + high) // 2
        self.mergesort(arr, low, mid)
        self.mergesort(arr, mid+1, high)
        self.merge(arr, low, mid, high)


if __name__=='__main__':
    arr= [9, 4, 7, 6, 3, 1, 5]
    print("Before sorting array: ", *arr)
    print()
    ans= Merge_Sort()
    ans.mergesort(arr, 0, len(arr)-1)
    print("After sorting array: ", *arr)
