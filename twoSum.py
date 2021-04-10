# Problem:
# Given an array of integers and target integer, return the indexes of two array elements that sum to the target, or None if doesn't exist

# brute_force
# Check all pairs of elements to see if they match the target.
# O(n^2) time complexity

def brute_force(nums: [int], target: int) -> [int]:
    for i in range(len(nums)):
        for j in range(len(nums)):
            #dont check the same index against itself
            if i == j:
                continue
            else:
                #check if integers equal the target
                if nums[i] + nums[j] == target:
                    return [i,j]
    return None

# Faster solution:
# everytime we check a number, we know the difference between the current integer and the target.
# this means we could possibly search a data structure to see if we encountered a number equal to
# the difference of the current integer and target already.
# we stop searching when we found a pair of numbers that equal the target or when we checked the entire array with no match.
# checking the input array is O(n) and for every integer we check, say a dictionary, which would be O(1) on average 
# Expected runtime is O(n), with worst case O(n^2), with O(n) additional space

def fast_map(nums: [int], target: int) -> [int]:
    value_to_index = {}
        
    for i in range(len(nums)):
        diff = target - nums[i]
        if diff in value_to_index:
            return [value_to_index[diff], i]
        value_to_index[nums[i]] = i
    return None

def main():
    for solution in [brute_force, fast_map]:
        print('testing ', solution)
        assert solution([1,2], 3) == [0,1]
        assert solution([1,-2], -1) == [0,1]
        assert solution([1,3,2], 5) == [1,2]
        assert solution([0,1,4,8], 8) == [0,3]
        assert solution([0,1,4,8], 10) == None
    print('all tests pass')

if __name__ == "__main__":
    main()

