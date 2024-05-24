# https://docs.google.com/document/d/1IkWbZqmFMmoCz6JJAkidRZ_JHz3e9AAa/edit

'''
Given an array of integers (unsorted) and a value n indicating number of channels. 
You have to send all these numbers through n channels (At least one number should go through each channel)
get the maxian median of each channel 

ex: 
Input:
nums = [1 2 3 2 1 5], n = 3
Send 1 2 3 using channel 1, 2 using channel 2, 1 5 using channel 3.
Calculate median of each channel :
channel 1 , median of (1 2 3) is 2
channel 2, median of (2) is 2
channel 3, median of (1 5) is 3
sum = 7


1 2 3 2 1 5 , n=3
Send 1 2 2 1 using channel 1, 3 using channel 2, 5 using channel 3.
Calculate median of each channel :
channel 1 , median of (1 2 2 1) is 1.5
channel 2, median of (3) is 3
channel 3, median of (5) is 5
sum = 9.5
'''








        
        
'''
Given a password string, calculate its strength, 
where strength is equals to the sum of count of distinct characters in all the substrings of that string.
Example: "aba" -> answer is 9

https://leetcode.com/problems/count-unique-characters-of-all-substrings-of-a-given-string/description/

'''
class Solution



'''
AWS has several data centers which have multiple processors that perform computations.
In one such data center, these processors are placed in a sequence with their IDs denoted by 1, 2, ...., n. 
Each Processor consumes a certain amount of power to boot up, denoted by booting Power[i]
After booting, a processor uses processing Power[i] to run the processes.
For maximum utilization, the data center wishes to group these processors into clusters. 
Clusters can only be formed of processors located adjacent to each other. 
For example, processors 2, 3, 4, 5 can form a cluster, but 1, 3, 4 can not.
The net power consumption of a clus‍‌‌‍‍‌‌‌‌‍‌‍‍‌‍‌‍‍‌‌ter of K processors (i, j+1, ...., j+k-1) is defined as : max booting Power[i], booting Power[i+1], ...., booting power[i+k-1]
return the max cluster per net power consumption.
'''




 

'''
LinkedList 头尾sum

'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        if not head:
            return 
        pairSum = [head.val]
        p1 = head
        p2 = head
        while p2.next and p2.next.next:
            p1 = p1.next
            pairSum.append(p1.val)
            p2 = p2.next.next
        # now the p1 is the mid        
        cnt = 1 
        length = len(pairSum)
        while p1:
            pairSum[length-cnt] += p1.val
            p1 = p1.next
            cnt+=1
        return max(pairSum)



