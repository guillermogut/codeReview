class Solution:





    
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        #test cases
        #[1,2] target = 3
        #[1,-2] target = -1
        #[1,3,2] target = 5
        #[0,1,4,8] target = 8
        
        
        #basic idea:
        #since there is no guarantee that the array is sorted, we check all the indeces.
        #at first glance we can compare each number to the rest of the array to see if they equal the target.
        #this is no problem since there is exactly one solution.
        #this would require a double loop so it would be O(n^2) time complexity.
        
        
        #for a better solution:
        #everytime we check a number, we know the difference between the current integer and the target.
        #this means we could possibly search a data structure to see if we encountered a number equal to
        #the difference of the current integer and target already.
        #we stop searching when we found a pair of numbers that equal the target or when we checked the entire array with no match.
        #checking the input array is O(n) and for every integer we check, say a dictionary, which would be O(1) on average 
        #but can possibly take O(n) worst case so it is between O(n) and O(n^2) ( O(nlogn) ?)
        #O(n) space complexity
        
        
        #brute force
        
        
        
#             for i in range(len(nums)):
                
#                 for j in range(len(nums)):
                    
#                     #dont check the same index against itself
#                     if i == j:
#                         continue
#                     else:
                        
#                         #check if integers equal the target
#                         if nums[i] + nums[j] ==target:
#                             return i,j
                        
                        
        # faster solution
        
            checkedInts = {}
            
            
            for i in range(len(nums)):
                
                
                if target- nums[i]  in checkedInts:
                    
                    return i,checkedInts[target- nums[i]]
                    
                if nums[i] not in checkedInts:
                    checkedInts[nums[i]] = i       
        