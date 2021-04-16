# 시간 복잡도 => O(n^2)
# 어느정도 정렬이 되어 있다는 가정에서 빠른 속도를 자랑한다!
def insert_sort(arr):
    for i in range(len(arr) - 1):
        j = i
        while arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
            j -= 1

    return arr


def main():
    arr = [1, 10, 5, 8, 7, 6, 4, 2, 3, 9]

    sorted_arr = insert_sort(arr)
    print(sorted_arr)


if __name__ == '__main__':
    main()
