def find_subsets(nums):
    result = [[]]

    for n in nums:
        new_additions = []

        for current_subset in result:
            new_additions.append(current_subset + [n])
        
        result.extend(new_additions)

    return result

def find_subsets_with_duplicates(nums):
    nums.sort()

    result = [[]]
    last_added_size = 0

    for i in range(len(nums)):
        start_index = 0

        if i>0 and nums[i]==nums[i-1]:
            start_index = len(result)-last_added_size

        current_size = len(result)
        new_additions = []

        for j in range(start_index, current_size):
            new_additions.append(result[j]+[nums[i]])

        last_added_size = len(new_additions)
        result.extend(new_additions)

    return result

def find_subsets_recursive(nums):
    result = []

    def backtrack(index, current_subset):
        if index==len(nums):
            result.append(list(current_subset))
            return
        
        current_subset.append(nums[index])
        backtrack(index+1, current_subset)

        current_subset.pop()
        backtrack(index+1, current_subset)

    backtrack(0, [])
    return result

def find_subsets_with_dup_recursive(nums):
    nums.sort()
    result = []

    def backtrack(start_index, current_subset):
        result.append(list(current_subset))

        for i in range(start_index, len(nums)):
            if i>start_index and nums[i]==nums[i-1]:
                continue

            current_subset.append(nums[i])
            backtrack(i+1, current_subset)
            current_subset.pop()

    backtrack(0, [])
    return result


if __name__=='__main__':
    my_list = [1, 2, 3]
    print(find_subsets(my_list))
    print(find_subsets_with_duplicates([1, 2, 2]))
    print(find_subsets_recursive([1, 2])[::-1])
    print(find_subsets_with_dup_recursive([1, 2, 2]))
