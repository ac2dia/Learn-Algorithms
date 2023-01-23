from collections import deque

def main():
    queue = deque()

    queue.append(5)
    queue.append(2)
    queue.append(3)
    queue.append(7)
    queue.popleft()
    queue.append(1)
    queue.append(4)
    queue.popleft()

    print(queue)
    queue.reverse()
    print(queue)

if __name__ == '__main__':
    main()
