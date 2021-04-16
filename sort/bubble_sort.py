# 시간 복잡도 => O(n^2)
# 가장 작은 수를 찾고 스왑하는 과정도 있음!
def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(0, len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


def main():
    arr = [1, 10, 5, 8, 7, 6, 4, 2, 3, 9]

    sorted_arr = bubble_sort(arr)
    print(sorted_arr)


if __name__ == '__main__':
    main()
