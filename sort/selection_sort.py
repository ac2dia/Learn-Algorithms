import sys


# 시간 복잡도 => O(n^3)
def selection_sort(arr):
    for i in range(len(arr)):
        min_value = sys.maxsize
        index = 0
        for j in range(i, len(arr)):
            if min_value > arr[j]:
                min_value = arr[j]
                index = j

        arr[i], arr[index] = arr[index], arr[i]

    return arr


def main():
    arr = [1, 10, 5, 8, 7, 6, 4, 2, 3, 9]

    sorted_arr = selection_sort(arr)
    print(sorted_arr)


if __name__ == '__main__':
    main()
