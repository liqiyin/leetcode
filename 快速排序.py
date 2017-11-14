# coding:utf-8
def solution(low, high, array):
    if low >= high:
        return
    i = low
    j = high
    cur = array[i]
    while i < j:
        while i < j and array[j] > cur:
            j = j - 1
        array[i] = array[j]

        while i < j and array[i] <= cur:
            i = i + 1
        array[j] = array[i]

    array[i] = cur

    solution(low, i - 1, array)
    solution(i + 1, high, array)


array = [5, 47, 4, 17, 89, 9]
solution(0, len(array) - 1, array)
print array
