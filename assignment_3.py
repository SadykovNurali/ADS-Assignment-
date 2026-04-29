def twoSum(nums, target):
    hashmap = {}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in hashmap:
            return [hashmap[diff], i]
        hashmap[num] = i

    def firstUniqChar(s):
        count = {}

        for ch in s:
            count[ch] = count.get(ch, 0) + 1

        for i, ch in enumerate(s):
            if count[ch] == 1:
                return i

        return -1


def isIsomorphic(s, t):
    mapping = {}

    for i in range(len(s)):
        if s[i] in mapping:
            if mapping[s[i]] != t[i]:
                return False
        else:
            if t[i] in mapping.values():
                return False
            mapping[s[i]] = t[i]

    return True


def isHappy(n):
    seen = set()

    while n != 1 and n not in seen:
        seen.add(n)
        n = sum(int(d)**2 for d in str(n))

    return n == 1

# RUN
print(isHappy(19))  # True

def maxDepth(root):
    if not root:
        return 0
    return 1 + max(maxDepth(root.left), maxDepth(root.right))

def isSymmetric(root):
    def check(l, r):
        if not l and not r:
            return True
        if not l or not r:
            return False
        return l.val == r.val and check(l.left, r.right) and check(l.right, r.left)

    return check(root, root)




def longestConsecutive(root):
    def dfs(node, parent_val, length):
        if not node:
            return length

        if node.val == parent_val + 1:
            length += 1
        else:
            length = 1

        return max(length,
                   dfs(node.left, node.val, length),
                   dfs(node.right, node.val, length))

    if not root:
        return 0

    return dfs(root, root.val - 1, 0)

def sortColors(nums):
    low, mid, high = 0, 0, len(nums) - 1

    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1

def quickSort(arr, l, r):
    if l < r:
        p = partition(arr, l, r)
        quickSort(arr, l, p-1)
        quickSort(arr, p+1, r)

def partition(arr, l, r):
    pivot = arr[r]
    i = l

    for j in range(l, r):
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1

    arr[i], arr[r] = arr[r], arr[i]
    return i

# RUN
arr = [5,3,8,4,2]
quickSort(arr, 0, len(arr)-1)
print(arr)


def mergeSort(nums):
    if len(nums) > 1:
        mid = len(nums) // 2
        left = nums[:mid]
        right = nums[mid:]

        mergeSort(left)
        mergeSort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                nums[k] = left[i]
                i += 1
            else:
                nums[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            nums[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            nums[k] = right[j]
            j += 1
            k += 1

def heapify(nums, n, i):
    largest = i
    left = 2*i + 1
    right = 2*i + 2

    if left < n and nums[left] > nums[largest]:
        largest = left

    if right < n and nums[right] > nums[largest]:
        largest = right

    if largest != i:
        nums[i], nums[largest] = nums[largest], nums[i]
        heapify(nums, n, largest)

def heapSort(nums):
    n = len(nums)

    for i in range(n//2 - 1, -1, -1):
        heapify(nums, n, i)

    for i in range(n-1, 0, -1):
        nums[i], nums[0] = nums[0], nums[i]
        heapify(nums, i, 0)
