""" day 82, 1, 31th May
Design a class to find the kth largest element in a stream. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Your KthLargest class will have a constructor which accepts an integer k and an integer array nums, which contains initial elements from the stream. For each call to the method KthLargest.add, return the element representing the kth largest element in the stream.

Example:
    int k = 3;
    int[] arr = [4,5,8,2];
    KthLargest kthLargest = new KthLargest(3, arr);
    kthLargest.add(3);   // returns 4
    kthLargest.add(5);   // returns 5
    kthLargest.add(10);  // returns 5
    kthLargest.add(9);   // returns 8
    kthLargest.add(4);   // returns 8

Note:
    You may assume that nums' length ≥ k-1 and k ≥ 1.
"""
from heapq import nlargest

class KthLargest:
    # 88 ms, faster than 35.46%.
    def __init__(self, k: int, nums: List[int]):
        self.klq = heapq.nlargest(k, nums)
        self.k = k
        if len(nums) < k:
            self.klq.append(float('-inf'))

    def add(self, val: int) -> int:
        if val > self.klq[-1]:
            sp, ep = 0, self.k - 1
            while sp < ep:
                mp = (sp + ep) // 2
                if self.klq[mp] > val:
                    sp = mp + 1
                elif self.klq[mp] < val:
                    ep = mp
                else:
                    sp = mp
                    break
            self.klq.insert(sp, val)
            self.klq.pop()
        return self.klq[-1]


    # 72 ms, best solution from submissions (56 ms)
    def __init__(self, k: int, nums: List[int]):
        self.res = []
        self.k = k
        for i in nums:
            if len(self.res) < k:
                heapq.heappush(self.res,i)  # ***
            else:
                heapq.heappushpop(self.res,i)
    def add(self, val: int) -> int:
        if len(self.res) < self.k:
            heapq.heappush(self.res,val)
        else:
            heapq.heappushpop(self.res,val)
        return self.res[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)



