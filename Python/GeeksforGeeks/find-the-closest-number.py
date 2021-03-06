"""
Problem Link: https://practice.geeksforgeeks.org/problems/find-the-closest-number/0

Given an array of sorted integers. The task is to find the closest value to the given number in array. 
Array may contain duplicate values.
Note: If the difference is same for two values print the value which is greater than the given number.

Input:
The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. 
Each test case consists of two lines. First line of each test case contains two integers N & K and 
the second line contains N space separated array elements.

Output:
For each test case, print the closest number in new line.

Constraints:
1<=T<=100
1<=N<=105
1<=K<=105
1<=A[i]<=105

Example:
Input:
2
4 4
1 3 6 7
7 4
1 2 3 5 6 8 9

Output:
3
5
"""
def binarySearch(arr, target):
    l = len(arr) - 1
    start,end = 1,l-1 
    while start <= end:
        mid = (start+end)//2
        if arr[mid] == target: 
            return arr[mid] 
        elif arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return arr[end] if target - nums[end] < nums[end+1] - target else arr[end+1]
    
for _ in range(int(input())):
    n,k = map(int,input().split())
    nums = list(map(int,input().split()))
    print(binarySearch(nums, k))
