'''
1. LinkedList Twin Sum Leetcode#≈≈.Maximum Twin Sum of a Linked List

'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        def getMid(head):
            p1 = head
            p2 = head
            while p2.next and p2.next.next:
                p1 = p1.next
                p2 = p2.next.next
            return p1
        mid = getMid(head)
        secondHalfHead = mid.next
        mid.next = None
        firstHalf = head

        def reverseLinkedList(prev, head):
            cur = head
            while cur:
                tmp = cur.next
                cur.next = prev
                prev = cur
                cur = tmp
            return prev # not return cur.next cuz cur is none
        reversedSecondHalf = reverseLinkedList(None, secondHalfHead)
        maxTwinSum = 0
        p1 = firstHalf
        p2 = reversedSecondHalf
        while p1 and p2:
            maxTwinSum = max(maxTwinSum, p1.val+p2.val)
            p1 = p1.next
            p2 = p2.next
        return maxTwinSum



'''
2. Find Minimum Days to Deliver Parcels

Amazon Delivery Centers dispatch parcels every day. There are n delivery centers, each having parcels(i) parcels to be delivered. 
On each day, an equal number of parcels are to be dispatched from each delivery center that has at least one parcel remaining.
Find the minimum number of days needed to deliver all the parcels.
Example - [4,2,3,3,3] -> it would take 3 days
2 shipments from each warehouse on 1st day => [2,0,1,1,1]
1 shipment from each warehouse on 2nd day => [1,0,0,0,0]
1 shipment from the 1st warehouse on 3rd day

# 2357 https://leetcode.com/problems/make-array-zero-by-subtracting-equal-amounts/description/
'''

class Solution:
    def getMinDay(self, parcels):
        parcelsSet = set()
        for parcel in parcels:
            if parcel != 0:
                parcelsSet.add(parcel)
        return len(parcelsSet)


'''
3. Pile Leecode#2355
Amazon Fresh is a new grocery store designed from the ground up to offer a seamless grocery shopping experience to consumers. 
As part of a stock clearance exercise at the store, given many piles of fresh products, follow the rules given below to stack the products in an orderly manner.
• There are a total of n piles of products.
• The number of products in each pile is represented by the array numProducts.
• Select any subarray from the array numProducts and pick up products from that subarray 
  such that the number of products you pick from the ith pile is strictly less than the number of products you pick from the i+1th pile for all indices i of the subarray.

Find the maximum number of products that can be picked.

Example:
The numbers of products in each pile are
numProducts = [7, 4, 5, 2, 6, 5].

These are some ways strictly increasing subarrays can be chosen (1-based index):
• Choose subarray from indices (1, 3) and pick products [3, 4, 5] respectively from each index, 
  which is 12 products. Note that we are forced to pick only 3 products from index 1 
  as the maximum number of products we can pick from index 2 is 4 and we need to make sure it is greater than the number of products picked from index 1.
• Choose subarray from indices (3, 6) and pick products [1, 2, 4, 5] respectively from each Index, 
  which is 12 products. Similar to the above case, we are forced to pick only 1 product from index 3 as the number of products at index 4 Is only 2.
• Choose subarray from indices (3, 5) and pick products [1, 2, 6] respectively from each Index, which is 9 products.
• Choose subarray from indices (1, 1) and pick all the 7 products.
'''

class Solution:
    def maximumBooks(self, books: List[int]) -> int:
        n = len(books)

        # Helper function to calculate the sum of books in a given range [l, r]
        def calculateSum(l, r):
            cnt = min(books[r], r - l + 1)
            return (2 * books[r] - (cnt - 1)) * cnt // 2

        stack = []
        dp = [0] * n

        for i in range(n):
            # While we cannot push i, we pop from the stack
            while stack and books[stack[-1]] - stack[-1] >= books[i] - i:
                stack.pop()

            # Compute dp[i]
            if not stack:
                dp[i] = calculateSum(0, i)
            else:
                j = stack[-1]
                dp[i] = dp[j] + calculateSum(j + 1, i)

            # Push the current index onto the stack
            stack.append(i)

        # Return the maximum element in the dp array
        return max(dp)




'''
4. Max deviation among all substrings leetcode#2272
Amazon is developing a string processing library for some of its NLP-related use cases.
You are tasked with developing a service that takes in a string consisting of lower case English letters and returns an integer.
More formally, given a string, the frequency deviation of a substring as the difference between the maximum and the minimum frequencies of the characters in the substring. 
A substring of string is formed by any contiguous segment of the string. For times is 'a' with 1 occurrence. The frequency deviation of the entire string is 4 - 1 = 3.

Given a string, s, representing the input string, find the maximum possible frequency deviation of any substring of the string.
Note: A substring of a string is formed by any contiguous segment of the string.
''' 


class Solution:
    def largestVariance(self, s: str) -> int:
        pos = defaultdict(list)
        for i, ch in enumerate(s):
            pos[ch].append(i)

        ans = 0
        for c0, pos0 in pos.items():
            for c1, pos1 in pos.items():
                if c0 != c1:
                    i = j = 0
                    f, g = 0, float("-inf")
                    while i < len(pos0) or j < len(pos1):
                        if j == len(pos1) or (i < len(pos0) and pos0[i] < pos1[j]):
                            f, g = max(f, 0) + 1, g + 1
                            i += 1
                        else:
                            f, g = max(f, 0) - 1, max(f, g, 0) - 1
                            j += 1
                        ans = max(ans, g)
        
        return ans





'''
5. Minimum Swaps To Make A Binary String Palindrome leetcode#2193
Given a binary string, write an algorithm to calculate minimum number of swaps required to make it a palindrome 
eg 11101 requires on swap between 3rd and 4th to make it 11011
'''

class Solution:
    def minMovesToMakePalindrome(self, s: str) -> int:
        @cache
        def dfs(s: str) -> int:
            n = len(s)
            if n <= 1:
                return 0
            for i in range(n - 1):
                if s[i] == s[-1]:
                    return i + dfs(s[:i] + s[i + 1 : -1])
            for i in range(n - 1, 0, -1):
                if s[i] == s[0]:
                    return n - 1 - i + dfs(s[1:i] + s[i + 1 :])
            return -1

        return dfs(s)

    
'''
6. 连续下降的评分 Leetcode#713类似
Amazon Shopping recently launched a new item whose daily customer ratings for n days is represented by the array ratings.
They monitor these ratings to identify products that are not performing well. 
Find the number of groups that can be formed consisting of 1 or more consecutive days 
such that the rating continuously decreases over the days.

The rating is consecutively decreasing if it has the form: r, r - 1, r - 2... and so on, where r is the rating on the first day of the group being considered. 
Two groups are considered different if they contain the ratings of different consecutive days.
Example
ratings = [4, 3, 5, 4, 3]
There are 9 periods in which the rating consecutively decreases.
'''


class Solution:
    def ContinuouslyDecreases(self, ratings):
        n = len(ratings)
        dp = [1]*n
        for i in range(1, n):
            if ratings[i-1]-ratings[i]==1:
                dp[i] = dp[i-1]+1
        return sum(dp)

solution = Solution()
ratings = [4, 3, 5, 4, 3]
res = solution.ContinuouslyDecreases(ratings)
print(res)     


'''
7. Shipment Imbalance no more than k segment Leetcode 2104
Amazon warehouse has a group of n items of various weights lined up in a row. 
A segment of contiguously placed items can be shipped together 
if and only if the difference between the weights of the heaviest and lightest item differs by at most k to avoid load imbalance.

Given the weights of the n items and an integer k, find the number of segments of items that can be shipped together.
Note: A segment (l, r) is a subarray starting at index /and ending at index where Is r.

Example
k=3
weights = [1, 3, 6]
Weight difference between max and min for each (l, r) index pair are:
• (0, 0) > max(weights[0]) - min(weights[O)) = max(1)- min(1) = 1-1=0
• (0, 1) > max(1, 3)- min(1, 3) = 3 - 1 = 2
• (0, 2) -> max(1, 3, 6) - min(1, 3, 6) - 6 - 1 = 5, difference > K
• (1, 1) as max(3) - min(3) = 3-3 = 0
• (1, 2) as max(3, 6) - min(3, 6) = 6 - 3 = 3
• (2, 2) as max(6) - min(6) = 6-6 = 0
5 of the 6 possible segments have a difference less than or equal to 3. Return 5.

'''
class Solution:
    def NumberofSegments(self, weights, k):
        left = 0 
        curMin = float('inf')
        curMax = float('-inf')
        res = 0 
        for right in range(len(weights)):
            curMin = min(curMin, weights[right])
            curMax = max(curMax, weights[right])
            while curMax - curMin > k:
                curMin = min(weights[left+1: right+1])
                curMax = max(weights[left+1: right+1])
                left+=1
            res += right-left+1
        return res
    
solution = Solution()
print(solution.NumberofSegments([1, 3, 6], 3))     



'''
8. sum of Subarray Ranges Leetcode#2104原题
'''

class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        n, answer = len(nums), 0 
        stack = []
        
        # Find the sum of all the minimum.
        for right in range(n + 1):
            while stack and (right == n or nums[stack[-1]] >= nums[right]):
                mid = stack.pop()
                left = -1 if not stack else stack[-1]
                answer -= nums[mid] * (mid - left) * (right - mid)
            stack.append(right)

        # Find the sum of all the maximum.
        stack.clear()
        for right in range(n + 1):
            while stack and (right == n or nums[stack[-1]] <= nums[right]):
                mid = stack.pop()
                left = -1 if not stack else stack[-1]
                answer += nums[mid] * (mid - left) * (right - mid)
            stack.append(right)
        
        return answer




'''
9. Maximum Quality of the Channel -- maximize the median sum

Amazon's AWS provides fast and efficient server solutions. The developers want to stress-test the quality of the servers' channels. 
They must ensure the following:
• Each of the packets must be sent via a single channel.
• Each of the channels must transfer at least one packet.
The quality of the transfer for a channel is defined by the median of the sizes of all the data packets sent through that channel.
Note: The median of an array is the middle element if the array is sorted in non-decreasing order. 
      If the number of elements in the array is even, the median is the average of the two middle elements.

Find the maximum possible sum of the qualities of all channels. 
If the answer is a floating-point value, round it to the next higher integer.

'''
# class Solution:
#     def MaximumQuality(self, packets, channels)

        

'''
10. vegetarian restaurants 
Given an array representing the locations of N vegetarian restaurants in the city, 
implement an algorithm to find the nearest X vegetarian restaurants to the customer's location.

The input to the function/method consists of two arguments: 
- alLocations a list af elements where each element corgists of a pair of integers representing the x and y coordinates of the vegetarian restaurant in the city;
- numRestaurants, an integer represerting the number of nearby vegetarian restaurants that would be returned to the customer 00.

Output
Return a lit of clements where each clement of the list represents the x and y integer coordinates of the nearest recommended vegetarian restaurant relative to customers location. 
It there is one tie, use the location with the closest X coordinate. 
if no location is possible, return a list with an erripty - location - not just an empty list.

Note 
The customer begins at the location [0, 0J.
The distance from the customer's current location to a recommended vegetarian restaurant location (x, y) is the square rogé of x^2 + y^2.
If there are ties then return any of the locations as long as you satisfy returning exactly X nearby vegetarian restaurants.
The returned output can be in any order.

Example
Input:
allocations = [[1, 2], [3, 4], [1, -1]]
numRestaurants = 2

Output:
[1, -1], [1, 2]

Explanation:
The distance of the customer's-current location from location [1, 2] isauare root(S） = 2.236
The distance of the customer's current location from location [3, 4] is square root(25) = 5
The distarice of the customer's current location from location [1, -1] is square root(2) = 1.414
The required number of vegetarian restaurants is 2, hence output is [1, -1) and [1, 2]
'''
import heapq
class solution:
    def NearestRestaurants(self, allocations, numRestaurants):
        # get the top K small restaurant
        maxHeap = []
        for x, y in allocations:
            distance = x**2 + y**2 
            heapq.heappush(maxHeap, (-distance, x, y))
            while len(maxHeap) > numRestaurants:
                heapq.heappop(maxHeap)
        res = []
        while maxHeap:
            distance, x, y = heapq.heappop(maxHeap)
            res.append([x, y])
        return res

     
test = solution()
print(test.NearestRestaurants([[1,2], [3, 4], [1, -1]], 2))



'''
11. Optimal Utilization
Given 2 lists a and b. Each element is a pair of integers where the first integer represents the unique id and the second integer represents a value. 
find an element from a and an element form b such that the sum of their values is less or equal to target and as close to target as possible. 
Return a list of ids of selected elements. If no pair is possible, return an empty list.

Input:
a = [[1, 2], [2, 4], [3, 6]]
b = [[1, 2]]
target = 7

Output: [[2, 1]]

Explanation:
There are only three combinations [1, 1], [2, 1], and [3, 1], which have a total sum of 4, 6 and 8, respectively.
Since 6 is the largest sum that does not exceed 7, [2, 1] is the optimal pair.

Input:
a = [[1, 3], [2, 5], [3, 7], [4, 10]]
b = [[1, 2], [2, 3], [3, 4], [4, 5]]
target = 10

Output: [[2, 4], [3, 2]]

Explanation:
There are two pairs possible. Element with id = 2 from the list `a` has a value 5, and element with id = 4 from the list `b` also has a value 5.
Combined, they add up to 10. Similarily, element with id = 3 from `a` has a value 7, and element with id = 2 from `b` has a value 3.
These also add up to 10. Therefore, the optimal pairs are [2, 4] and [3, 2].


'''

class Solution:
    def optimal_utilization(self, a, b, target):
        #  # Binary search to find a value that is close or equal to the target
        def findElement(nums, target):
            left = 0 
            right = len(nums)-1
            while left<right:
                mid = left+(right-left)//2
                if nums[mid][1]>=target:
                    right = mid
                else:
                    left = mid+1
            return [left, nums[left][1]]

        a.sort(key = lambda x:x[1])
        b.sort(key = lambda x:x[1])
        res = 0 
        minDiff = float('inf')

        for i in range(len(a)):
            curValA = a[i][1]
            targetB = target - curValA
            indexB, curValB = findElement(b, targetB)
            curDiff = target - (curValA+curValB)
            if curDiff >= 0 and curDiff < minDiff:
                res = [[a[i][0], b[indexB][0]]]
                minDiff = curDiff
            elif curDiff >= 0 and curDiff == minDiff:
                res.append([a[i][0], b[indexB][0]])
        return res

Solution = Solution()
a = [[1, 2], [2, 4], [3, 6]]
b = [[1, 2]]
target = 7
print(Solution.optimal_utilization(a, b, target))


'''
12. Merge Package Shipping - Merge package shipping group acording to weight

To increase efficiency, the Amazon shipping team will group packages being shipped according to weight. 
They will merge a lighter package with a heavier package, which eliminates the need for separate shipments.
More formally, consider n packages, where packageWeights[i] represents the weight of the ith package. 
You can combine the i th and i+1 th package if packageWeights[i] < packageWeights[i+1] then discard the ith package. 
After this operation, the number of packages reduced by 1 and the weight of the (i+1)th package Increases by packageWeights[i]. 
You can merge the packages any number of times.

Find the maximum possible weight of a package that can be achieved after any sequence of merge-operations.

For example, packages are described as package weights
- [2, 9, 10, 3, 7]
The optimal order of operations is, using 1-based Indendng:
• Combine the packages at index 2 and index 3, the new array of package weights becomes [2, 19, 3, 71.
• Combine the packages at index 1 and index 2, the new array of package weights becomes (21, 3, 7).
• Combine the paclages at Index 2 and index 3, the neve artay of pachage wargts becomes [21. 10]
We can not combine the package anymore. The weight of the heaviest package achievable after merging is 21.

'''
# Started from the back and popped off numbers combining them with a stack O(n)
class solution:
    def getHeaviestPackage(self, packageWeights):
        n = len(packageWeights)
        stack = []
        for i in range(n-1, -1, -1):
            if not stack:
                stack.append(packageWeights[i])
            else:
                if packageWeights[i]<stack[-1]:
                    val = stack.pop()
                    stack.append(val+packageWeights[i])
                else:
                    stack.append(packageWeights[i])
        return max(stack)

test = solution()
print(test.getHeaviestPackage([2, 9, 10, 3, 7]))



'''
13. power subarray

given an array A. For all subarrays of you have to find sum of sum(A[l:r])min(A[l:r]) for every subarray
power = [2,3,2,1]
power[0,0] = min([2]) * sum([2]) = 4
power[0, 1] = min([2,3]) * sum([2, 3]) = 10
power[0, 2] = min([2,3,2]) * sum([2,3,2]) = 14
...
total will be 69

# https://leetcode.com/playground/m9BXwSBc
解法 1：TC O(n):  2个单调stack找min，然后用prefix sum of prefix sum算sum(subarrayPower)。建议提前练习一下。画个图就很明确了。
解法 2: link
https://leetcode.com/discuss/interview-question/1736639/solution-to-amazon-oa-2022-problem-sum-of-scores-of-subarray/1255065
https://leetcode.com/discuss/interview-question/1706805/Amazon-OA-Question-Is-there-an-O(n)

'''
def optimalScoresOfSubArrays(arr):
    prefixSums = []
    positionElementProdSums = []
    positionElementProdSumsReverse = []
    runningSum = 0
    posElementProdSum = 0
    n = len(arr)
    for i in range(n):
        runningSum += arr[i]
        posElementProdSum += (i+1) * arr[i]
        prefixSums.append(runningSum)
        positionElementProdSums.append(posElementProdSum)
    posElementProdSum = 0
    for i in range(n-1,-1,-1):
        posElementProdSum += (n-i) * arr[i]
        positionElementProdSumsReverse.append(posElementProdSum)
        
    sum = lambda sums, l, r: sums[r] - (sums[l-1] if l-1>=0 else 0) if l <= r else 0
    totalScore = 0
    stack = []
    for i in range(n):
        while stack and arr[stack[-1][0]] > arr[i]:
            minElementIndex, leftIndex = stack.pop()
            rightIndex = i
            rightCount = rightIndex - minElementIndex
            leftCount = minElementIndex - leftIndex
            minElement = arr[minElementIndex]
            shiftedPosEleProdSum = sum(positionElementProdSums, leftIndex + 1, minElementIndex) - sum(prefixSums, leftIndex  + 1, minElementIndex) * (leftIndex  + 1)
            currRangeScore = rightCount * minElement * shiftedPosEleProdSum
            totalScore += currRangeScore
            shiftedPosEleProdSum = sum(positionElementProdSumsReverse, n-rightIndex, n-minElementIndex-2) - sum(prefixSums, minElementIndex+1, rightIndex-1)*(n-rightIndex)
            currRangeScore = leftCount * minElement * shiftedPosEleProdSum
            totalScore += currRangeScore
        if not stack: stack.append((i, -1))
        else: stack.append((i, stack[-1][0]))
    while stack:
        minElementIndex, leftIndex = stack.pop()
        rightIndex = n
        rightCount = rightIndex - minElementIndex
        leftCount = minElementIndex - leftIndex
        minElement = arr[minElementIndex]
        shiftedPosEleProdSum = sum(positionElementProdSums, leftIndex + 1, minElementIndex) - sum(prefixSums, leftIndex  + 1, minElementIndex) * (leftIndex  + 1)
        currRangeScore = rightCount * minElement * shiftedPosEleProdSum
        totalScore += currRangeScore
        shiftedPosEleProdSum = sum(positionElementProdSumsReverse, n-rightIndex, n-minElementIndex-2) - sum(prefixSums, minElementIndex+1, rightIndex-1)*(n-rightIndex)
        currRangeScore = leftCount * minElement * shiftedPosEleProdSum
        totalScore += currRangeScore
    return totalScore
        


'''
14. Max Length of Valid Server Cluster

Give you a list servers. Their processing power is given as a array of integer, and boot power as a array of integer.
Write a function to return the max length of sub array which's power consumption is less than or equal to max power limit.

'''


'''
15. max subarray length with product
'''

'''
16. 
'''



'''
17a. Password strength determination

Given a password determine the strength of the password 
calculating strength based on number of unique characters in the substring and adding all 
e.g. if password= "good" . Then iterate over and find the distinct values:-
g = 1,
o = 1,
o = 1,
d = 1,
go = 2,
oo = 1,
od = 2,
goo = 2,
ood = 2,
good = 3
and at the end add all, Expected output = 16.
'''

class Solution:
    def getPasswordStrength(self, s: str) -> int:
        index = collections.defaultdict(list)
        for i, c in enumerate(s):
            index[c].append(i)

        res = 0
        for arr in index.values():
            arr = [-1] + arr + [len(s)]
            for i in range(1, len(arr) - 1):
                res += (arr[i] - arr[i - 1]) * (arr[i + 1] - arr[i])
        return res


'''
17.b Find the password strength2.
For each substring of the password which contains at least one vowel and one consonant, its strength goes up by 1.
vowels={'a', 'e', 'i', 'o', 'u'}, (Only lower alphabet letters)
https://www.1point3acres.com/bbs/thread-799111-1-1.html
'''





'''
21.  No two adjacent are same type leetcode #2222

Select 3 pages in ascending such that no two adjacent are same type
A binary string that represents pages of a book (0011010). 1 represents a bookmarked page and 0 represents non-bookmarked flag.
find the number of ways to select 3 characters, 
such that they are in ascending order (index wise) and no two adjacent selected characters are same.
Example: s = "01001"
these are ways:
(010 ) -> 010,
(01 0 ) -> 010 ,
( 10 1) -> 101,
( 1 01) -> 101

here space means, we omitting a character from the original string (01001).

answer: 4
'''
class Solution:
    def numberOfWays(self, s: str) -> int:
        n = len(s)     
        n0 = s.count('0')
        n1 = n-n0

        cnt0 = 0 
        cnt1 = 0
        res = 0
        for i, char in enumerate(s):
            if char == '0':
                cnt0+=1
                res += cnt1*(n1-cnt1) 
            else:
                cnt1+=1
                res+= cnt0*(n0-cnt0)
        return res




'''
25. Min changes to make non decreasing array similiar leetcode 2289

Given an array, find the minimum number of steps to make the array non decreasing. 
In one step any element of the array can be changed to any other number

Ex: 1 2 9 5 3 6
Ans: 2
Exp: Changing 9 to 2 and 3 to 5 will result in a non decreasing sequence: 1 2 2 5 5 6
Ex: 5 4 3 2
Ans: 3
'''
class Solution:
    def min_steps_to_make_non_decreasing(self, nums: List[int]) -> int:
        count = 0
        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                if i == 1 or nums[i-2] <= nums[i]:
                    nums[i-1] = nums[i]
                else:
                    nums[i] = nums[i-1]
                count += 1
        return count

test = Solution()
print(test.min_steps_to_make_non_decreasing([1, 2, 9, 5, 6]))







'''
16. valid Discount coupons

An empty string is valid
You can add same character to a valid string X, and create another valid string yXy
You can concatenate two valid strings X and Y, so XY will also be valid.
Ex: vv, xbbx, bbccdd are all valid.
'''

def isvalid(s ) :  
    stack = [] 
    for c in s : 

        if stack and stack[-1] != c : 
            stack.append(c) 

        else : 
            if not stack : stack.append(c)  
            else :  stack.pop() 
    return  len(stack) ==0 
            
# coupons = ['abba', 'abca','daabbd', 'abc','bbb']
# for x in coupons :
#     print(isvalid(x))







'''
18. student rank
'''




'''
19. decode string 
Input is an encoded string and a rowNumber, and your purpose is designing a method to decode it
decode stringhttps://leetcode.com/playground/AVks54Mp
https://leetcode.com/discuss/interview-question/1317796/amazon-oa-2021-hackerrank
https://leetcode.com/playground/8JPzuvm5
'''


'''
20. coin change 2

'''



'''
21. flip 01s/coin
'''









'''
22. Maximum Number of Engineering Teams

 You are given 3 inputs

int: teamSize:: representing the number of engineers to complete a team, otherwise the team does not count towards total

1 <= teamSize <= 10^4 unsure about constraint
int: maxDiff:: representing the maximum allowed gap in skill between the least skilled engineer on a team and the most skilled on the team

1 <= maxDiff <= 100 unsure about constraint
array[int]: skill:: representing the pool of engineers to build teams from, skill[i] being the skill level an engineer i

1 <= pool of enginers <= 10^4 unsure about constraint
1 <= skill[i] <= 100 unsure about constraint

what is the maximum number of teams that can be constructed from the pool of engineers, respecting the maxDiff rule for each team?
Example1:
input: teamSize: 1, maxDiff: 1, skill: [34, 5, 72, 48, 15, 2]
output: 6 ---> (resulting teams [[2], [5], [15], [34], [48], [72]])

Example2:
input: teamSize: 3, maxDiff: 20, skill: [34, 5, 72, 48, 15, 2]
output: 1 ---> (resulting teams [[2, 5, 15]])

Example3:
input: teamSize: 3, maxDiff: 30, skill: [34, 5, 72, 48, 15, 2]
output: 2 ---> (resulting teams [[2, 5, 15], [34, 48, 72]])

Example4:
input: teamSize: 3, maxDiff: 5, skill: [34, 5, 72, 48, 15, 2]
output: 0 ---> (resulting teams [])

Example5:
input: teamSize: 3, maxDiff: 25, skill: [1, 7, 18, 32, 65, 72, 90, 98, 100, 113, 146]
output: 3 ---> (resulting teams [[7, 18, 32], [65, 72, 90], [98, 100, 113]])

https://leetcode.com/discuss/interview-question/1688196
https://leetcode.com/problems/maximum-performance-of-a-team/description/

'''

class Solution:
    def getMaxNumber(self, teamSize:int, maxDiff:int, skills:list):
        if teamSize > len(skills):
            return 0 
        if teamSize == 1:
            return len(skills)
        skills.sort() # O(nlogn)
        p1 = 0 
        totalTeam = 0
        for p2 in range(len(skills)):
            if p2-p1+1 == teamSize:
                if skills[p2]-skills[p1] <= maxDiff:
                    totalTeam += 1
                    p1 = p2+1
                else:
                    p1+=1
            elif p2-p1+1 > teamSize:
                p1+=1
        return totalTeam
    
teamSize = 3
maxDiff = 5
skills = [34, 5, 72, 48, 15, 2]
Solution = Solution()
res = Solution.getMaxNumber(teamSize, maxDiff, skills)
print(res)


'''
23. 10year anniversary discount
https://leetcode.com/discuss/interview-question/1759477/amazon-new-grad-oa-2022-find-lowest-price

An Amazon seller is celebrating ten years in business! They are having a sale to honor their privileged members, those who have purchased from them in the past five years. 
These members receive the best discounts indicated by any discount tags attached to the product. 
Determine the minimum cost to purchase all products listed. 
As each potential price is calculated, round it to the nearest integer before adding it to the total. 
Return the cost to purchase all items as an integer.
There are three types of discount tags:
Type O: discounted price, the item is sold for a given price.
Type 1: percentage discount, the customer is given a fixed percentage discount from the retail price.
Type 2: fixed discount, the customer is given a fixed amount off from the retail price.

Example
products = [['10', 'd0', 'd1'], ['15', 'EMPTY', 'EMPTYI', ['20', 'd1','EMPTY']]
discounts = [['dO','1', '27'], ['d1' '2', '5']]

If a privileged member buys product 1 listed at a price of 10 with two discounts available:
-> Under discount do of type 1, the discounted price is 10 - 10 * 0.27 = 7.30, round to 7.
-> Under discount d1 of type 2, the discounted price is 10 - 5 = 5.
-> The price to purchase the product 1 is the lowest of the two, or 5 in this case
The second product is priced at 15 because there are no discounts available
The third product is priced at 20. Using discount tag d1 of type 2, the discounted price is 20 - 5 = 15

The total price to purchase the three items is 5 + 15 + 15 = 35.

Notes: Not all items will have the maximum number of tags. 
Empty tags may just not exist in input, or they may be filled with the string EMPTY. 
These are equivalent as demonstrated in the example above.
'''

class solution:
    def minCostToPurchase(self, products, discounts):
        def getDiscountPrice(price, discountType, discountValue):
            if discountType == 'dO':
                return int(discountValue)
            if discountType == 'd1':
                return int(price) * (1 - int(discountValue))
            if discountType == 'd2':
                return int(price) - int(discountValue)
            else:
                return int(price)
    

        n = len(products)
        totalCost = 0 
        for i in range(n):
            curProduct = products[i]
            price =  curProduct[0]
            minCost = price
            for discountType in curProduct[1:]:
                if discountType!='EMPTY':
                    for x, y, z in discounts:
                        if discountType == x:
                            newPrice = getDiscountPrice(price, discountType, z)
                            minCost = min(minCost, newPrice)
            totalCost += minCost
        return totalCost
        
products = [['10', 'd0', 'd1'], ['15', 'EMPTY', 'EMPTY'], ['20', 'd1','EMPTY']]
discounts = [['dO','1', '27'], ['d1' '2', '5']]
test = solution()
res = test.minCostToPurchase(products, discounts)
print(res)






'''
24. secret array 
https://leetcode.com/discuss/interview-question/1354480/amazon-oa

You have a secret array. You also have two integers upperbound and lowerbound. 
Now you need to return how many arrays exist within the upperbound and lowerbound that analogy to your secret array.
Two arrays are analogy if their difference between consecutive numbers are the same.
For example, array [1, 0, 3, 0] and array [2, 1, 4, 1] are analogy. Because the difference are the same [-1, 3, -3].

Inputs:
Arr = [1, 0, 3, 0], upperbound = 4, lowerbound = 0
Output:
1

Inputs:
Arr = [1, 1, 3, 2], upperbound = 5, lowerbound = 1
Output:
2
Explanation:
[2, 2, 4, 3], [3, 3, 5, 4]
'''

class solution:
    def countAnalogousArrays(secret_array, upperbound, lowerbound):
        def is_analogous(arr):
            for i in range(1, len(arr)):
                diff = [arr[i] - arr[i-1] for i in range(1, len(arr))]
            return all(d == diff[0] for d in diff)
        cnt = 0 
        for num in range(lowerbound, upperbound + 1 - len(secret_array)):
            if is_analogous([num + i for i in secret_array]):
                count += 1
        return count


'''
25. Number of Swaps to Sort / 315 Count of Smaller Numbers After Self
'''








'''
26. Music pair Leetcode # 1010
'''
class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        cnt = [0] * 60
        for t in time:
            cnt[t % 60] += 1
        res = 0
        for i in range(1, 30):
            res += cnt[i] * cnt[60 - i]
        res += cnt[0] * (cnt[0] - 1) // 2 + cnt[30] * (cnt[30] - 1) // 2
        return res

'''
27. Given list of processes where each value representing memory consuption by the process 
We need to delete m number of processes from the list in contiguous manner 
return minimum amount of main memory used by all the proccesses running after deleting contiguous segment of processes.

Example - processes = (10,4,8,13,20), m = 2;
output = 22 [removing 13 and 20 as its consuming large memory]
'''


class Solution:
    def minMemory(self, processes, m) -> int:
        left = 0 
        minSum = float('inf')
        curSum = sum(processes)
        for right in range(len(processes)):
            curSum-=processes[right]
            if right-left+1>m:
                curSum+=processes[left]
                left+=1
            minSum = min(minSum, curSum)
        return minSum
                
test = Solution()
res = test.minMemory([10,4,8], 2)
print(res)               



            
# test = Solution()
# a = [[1, 3], [2, 5], [3, 7], [4, 10]]
# b = [[1, 2], [2, 3], [3, 4], [4, 5]]
# target = 10
# res = test.getPairs(a, b, target)
# print(res)             
                

'''
29. 
Leetcode 2262
https://leetcode.com/problems/total-appeal-of-a-string/discuss/1996390/JavaC%2B%2BPython-Easy-and-Concise-with-Explanation

'''
            


'''
30. Min Shipping cost
Amazon ships millions of packages regularly. There are a number of parcels that need to be shipped.
Compute the minimum possible sum of transportation costs incurred in the shipment of additional parcels in the following scenario.
* A fully loaded truck carries k parcels.
* It is most efficient for the truck to be fully loaded.
+ There are a number of parcels already on the truck as listed in parcels
+ There are parcels with a unique id that ranges from 1 through infinity.
* The parcel id is also the cost to ship that parcel.
Given the parcel IDs which are already added in the shipment, find the minimum possible cost of shipping the items added to complete the load.

Example
parcel = [2, 5, 6, 10, 11] k = 9
After reviewing the current manifest, the remaining parcels to choose from are [1, 4, 5, 7, 8, 9, 12, 13...]. 
There are 5 parcels already on the truck, and it can carry k= 9 parcels when fully lauded,
Cheose 4 more packages to include: [1, 4, 5, 7]. Their shipping cost is 1 + 4 +3 + 7 = 17, which is minimal. Return 17.


getMinimumCost in the aditor below.
'''
class solution:
    def getMinimumCost(self, parcel):



'''
31. Pascal Triangle encryption

In order to ensure maximum security, the developers at Amazon employ multiple encryption methods to keep User data protected,
In one method, numbers are encrypted using a scheme called 'Pascal Triangle.
When an array of digits is fed to this systen, it sums the adjacent digits. 
It then takes the rightmost digit (least significant digit) of each addition for the next step. 
Thus, the number of digits in each step is reduced by 1. This procedure is repeated until there are only 2 digits left and this sequence of 2 digits forms the encrypted number.
Given the initial sequence of the digits of numbers, find the encrypted number.
You should report a string of digits representing the encrypted number.
'''



'''
32. getMingroup 
https://leetcode.com/discuss/interview-question/1774945/Amazon-or-OA1-New-Grad-2022-or-Minimum-Number-of-Groups

'''



'''
33. Reorder Data in Log Files telecommunications，junction box

'''




'''
34. Rainfall next n days

Given an array of predicted rainfall for next n days, where index i presents a day and day[i] represents the amount of rainfall on that day
return a list of ideal days such that -
day[i-k] >= day[i-k+1] >= ... day[i-1] >= day[i] <= day[i+1] ... <= day[i+k-1] <= day[i+k],
'''

'''
35. Demolition of Robot
https://leetcode.com/discuss/interview-question/1257344/amazon-oa-demolition-of-robot
'''



'''
36. Router

Takes in three lists and finds if all buildings are served -
A building is considered served when the number of routers supporting the building is equal to or greater than the head count of the building
- 'buildingCount' is a head count per building (each value represents a building) 
- 'routerLocation' is the building number where a router is located (buildings numbered ascending from 1)
- 'routerRange' is connected by index to routerLocation and represents the range of the router (location + & - range ---- inclusive)

Return the number of served buildings

A building is considered as served if the number of routers serving that building is greater than or equal to head count of that building.

Test case:
buildingCount: [2, 3, 3, 1, 5, 6] 表示0号楼有2位住户，1号楼有3位住户，2号楼有3位住户
routerLocation: [2, 4, 1] 表示0号router安装在2号楼，1号router安装在4号楼
routerRange: [2, 4, 3] 表示0号router能覆盖距离是2, 1号router覆盖范围是4

Number of routrers serving each building would be [2, 2, 3, 3, 3, 1] 
so buildings at indices. 0, 2 and 3 would be considered as served and hence the answer would be 3 (number of served buildings).
'''












'''
29. Given list of movies, and a variable k representing maximum allowed difference, we need to group the movies into groups. No groups can have movies which has difference amongst them greater than m. We need to return minimum number of groups which follows the condition.

Example - movies = [1,5,4,6,8,9,2], k=3;
output = 3 [groups-(1,2,4),(5,6,8),(9)]

I solved both the problems and passed all the test cases in both the code, but I got mail saying we cannot consider you for the next round without providing reason.

Can anyone tell me why this could have happened?
Where I gone wrong and how I can overcome this?
Am I the only one or someone out there also faced this situation?
Also I want to know when I can apply again for Amazon?

'''
















'''
Maximum Subarray Length 
Find a subarray of maximum length such that product of all the elements in the subarray is 1.
Example: [1, -1, -1, 1, 1, -1] - Output (Max length): 5
'''







import heapq
class solution:
    def reduceGifts(prices, k, threshold):
        n = len(prices)
        if n < k:
            return 0
        
        to_remove = set()
        
        def check_and_mark(prices, k, threshold, to_remove):
            for i in range(len(prices) - k + 1):
                window_sum = sum(prices[i:i + k])
                if window_sum > threshold:
                    max_in_window = max(prices[i:i + k])
                    for j in range(i, i + k):
                        if prices[j] == max_in_window and j not in to_remove:
                            to_remove.add(j)
                            break
            return len(to_remove)
        while True:
            prev_count = len(to_remove)
            new_count = check_and_mark(prices, k, threshold, to_remove)
            if new_count == prev_count:
                break
        return len(to_remove)
# reduceGifts = solution.reduceGifts
# prices = [3, 2, 1, 4, 6, 5]
# k = 3
# threshold = 14
# print(reduceGifts(prices, k, threshold)) 