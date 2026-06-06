q = [1,3,5]
w = [2,4,6,8]
def sort_arr(arr1,arr2):
    new_arr = []
    while len(new_arr) != (len(arr1) + len(arr2)):#len(arr1) != 0 and len(arr2) != 0
        if arr1[0] <= arr2[0]:
            new_arr.append(arr1.pop(0))
        else:
            new_arr.append(arr2.pop(0))
        if len():
            new_arr.extend(arr2)
        elif len(arr2) == 0:
            new_arr.extend(arr1)
    return new_arr
print(sort_arr(w,q))







q = [1,3,5]
w = [2,4,6,8]
def sort_arr(arr1,arr2):
    new_arr = []
    while len(arr1) != 0 and len(arr2) != 0:
        if arr1[0] <= arr2[0]:
            new_arr.append(arr1[0])
            del arr1[0]
        else:
            new_arr.append(arr2[0])
            del arr2[0]
        if len(arr1) == 0:
            new_arr.extend(arr2)
        elif len(arr2) == 0:
            new_arr.extend(arr1)
    return new_arr
print(sort_arr(w,q))







for i in range(0,min([len(q),len(w)])-1):
    value_int = q[i]
    if q[i] <= w[i]:
        arr.append(q.pop(i))
    else:
        arr.append(w.pop(i))


if len(q) == 0:
    arr.extend(w)
elif len(w) == 0:
    arr.extend(q)
print(arr)


Левосторонний бинарный поиск
arr = [1,2,3,3,6,6,6,6,6,8]
target = 6
def search(arr,target):
    left, right = 0,len(arr)-1
    while left < right:
        mid = (left+right)//2
        if arr[mid] >= target:
            right = mid
        else:
            left = mid+1 #Если цель больше мида, то самое первое нужное число точно правее
    return left
print(search(arr,target))

arr = [1,2,3,4,4,4,5,5,5,5,6,6,6,7,7,8]
x = 6
def search(arr):
    l,r = 0, len(arr)-1
    while l < r:
        mid = (l+r)//2
        if arr[mid]

Правосторонний бинарный поиск
arr = [1,2,3,3,6,6,6,6,6,8]
target = 6
def search(arr,target):
    left, right = 0,len(arr)-1
    while left < right:
        mid = (left+right+1)//2 # Округление вверх (+1), т.к LEFT = mid. Если LEFT = mid + 1, то округление вниз
        if arr[mid] <= target:
            left = mid
        else:
            right = mid-1
            #Если цель больше мида, то самое первое нужное число точно правее
    return left
print(search(arr,target))


УДАЛЕНИЕ ДУБЛИКАТОВ С ПОМОЩЬЮ TWO POINTS
sort_arr = [1,1,2,2,2,3,3,3,3,4,5,5]
def del_bub(arr):
    writer = 0
    for reader in range(1,len(arr)):
        if arr[reader] != arr[reader-1]:
            writer += 1
            arr[writer] = arr[reader]
    return arr[:writer+1]
new_sort_arr = del_bub(sort_arr)
print(new_sort_arr)

НАХОЖДЕНИЕ СУММЫ ДВУХ ЧИСЕЛ С СУММОЙ TARGET
sort_arr = [2,4,7,10,11,14,18,23,24,30]
target = 22
def sum(arr,target):
    left,right = 0,len(arr)-1
    while left <= right:
        current = arr[left] + arr[right]
        if current == target:
            return left,right
        elif current < target:
            left += 1
        else:
            right -=1
    return -1
print(sum(sort_arr,target))

ОБЫЧНЫЙ БИНАРНЫЙ ПОИСК
sorted_numbers = [2,5,9,14,19,22,25,30,33]
target = 25
def search(arr,target):
    left, right = 0, len(arr)-1
    while left <= right:
        mid = (left+right)//2
        if target == arr[mid] :
            return mid
        elif target < arr[mid]:
            right = mid-1
        else:
            left = mid+1
    return -1
print(search(sorted_numbers,target))

sorted_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
sorted_numbers = [1,1,2,3,4,4,4,4,4,4,4,4,5,6,7,7]
sorted_numbers = [1,1,2,4,4,5,5,5,5,5,5,5,5,6,7,7]
sorted_numbers = [1, 2, 3, 4, 5, 7, 7, 7, 9, 10]
targett = 11
def left_bound_binary_search(arr, target):
    left, right = 0, len(arr)  # важно: right = len(arr), не len(arr)-1!

    while left < right:  # пока left не дойдет до right
        mid = (left + right) // 2

        if target > arr[mid]:
            left = mid + 1  # target где-то справа
        else:
            right = mid  # target здесь или левее

    # После цикла left == right
    return left  # индекс первого элемента >= target
print(left_bound_binary_search(sorted_numbers,targett))