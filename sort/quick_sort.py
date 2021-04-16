# 시간 복잡도 => O(N * logN)
def quick_sort(arr):
    def sort(low, high):
        if high <= low:
            return

        mid = partition(low, high)
        sort(low, mid - 1)
        sort(mid, high)

    def partition(low, high):
        pivot = arr[(low + high) // 2]
        while low <= high:
            while arr[low] < pivot:
                low += 1
            while arr[high] > pivot:
                high -= 1
            if low <= high:
                arr[low], arr[high] = arr[high], arr[low]
                low, high = low + 1, high - 1
        return low

    return sort(0, len(arr) - 1)


def main():
    arr = [3, 7, 8, 1, 5, 9, 6, 10, 2, 4]

    quick_sort(arr)
    print(arr)


if __name__ == '__main__':
    main()
