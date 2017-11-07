def solution(arr):
    for j in range(1, len(arr)):
        i = j
        temp = arr[j]
        while i > 0 and arr[i - 1] < temp:
            arr[i] = arr[i - 1]
            i = i - 1
        arr[i] = temp
    return arr
print solution([9,3,10,11])

