# TASK1
def print_1_to_n(n):
    if n == 0:
        return
    print_1_to_n(n - 1)
    print(n, end=" ")

# TASK2
def print_n_to_1(n):
        if n == 0:
            return
        print(n, end=" ")
        print_n_to_1(n - 1)
# TASK3

def sum_n(n):
    if n == 0:
        return 0
    return n + sum_n(n - 1)
# TASK4

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)
# TASK5

def power(a, b):
    if b == 0:
        return 1
    return a * power(a, b - 1)

# TASK6

def sum_digits(n):
    if n == 0:
        return 0
    return n % 10 + sum_digits(n // 10)
# TASK7

def count_digits(n):
    if n == 0:
        return 0
    return 1 + count_digits(n // 10)
# TASK8

def reverse_number(n, rev=0):
    if n == 0:
        return rev
    return reverse_number(n // 10, rev * 10 + n % 10)
# TASK9

def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)
# TASK10


def is_palindrome(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])
# TASK11

def sum_array(arr, n):
    if n == 0:
        return 0
    return arr[n - 1] + sum_array(arr, n - 1)
# TASK12

def max_array(arr, n):
    if n == 1:
        return arr[0]
    return max(arr[n - 1], max_array(arr, n - 1))
# TASK13

def count_occurrences(arr, n, target):
    if n == 0:
        return 0
    count = 1 if arr[n - 1] == target else 0
    return count + count_occurrences(arr, n - 1, target)
# TASK14

def linear_search(arr, n, target):
    if n == 0:
        return False
    if arr[n - 1] == target:
        return True
    return linear_search(arr, n - 1, target)

# TASK15

def is_sorted(arr, n):
    if n == 1:
        return True
    if arr[n - 1] < arr[n - 2]:
        return False
    return is_sorted(arr, n - 1)

# TASK16





print("Task 1:")
print_1_to_n(5)
print("\n")

print("Task 2:")
print_n_to_1(5)
print("\n")

print("Task 3:")
print(sum_n(5))

print("\nTask 4:")
print(factorial(5))

print("\nTask 5:")
print(power(2, 4))

print("\nTask 6:")
print(sum_digits(572))

print("\nTask 7:")
print(count_digits(5729))

print("\nTask 8:")
print(reverse_number(1234))

print("\nTask 9:")
print(fibonacci(6))

print("\nTask 10:")
print("Palindrome" if is_palindrome("level") else "Not palindrome")

print("\nTask 11:")
arr1 = [3, 5, 2, 7]
print(sum_array(arr1, len(arr1)))

print("\nTask 12:")
arr2 = [4, 9, 1, 7, 3]
print(max_array(arr2, len(arr2)))

print("\nTask 13:")
arr3 = [1, 2, 3, 2, 2, 5]
print(count_occurrences(arr3, len(arr3), 2))

print("\nTask 14:")
arr4 = [4, 7, 1, 9, 3]
print("Found" if linear_search(arr4, len(arr4), 9) else "Not Found")

print("\nTask 15:")
arr5 = [1, 2, 4, 7, 9]
print("Sorted" if is_sorted(arr5, len(arr5)) else "Not sorted")






