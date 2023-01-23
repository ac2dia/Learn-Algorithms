def reverse(alphabet):
    # 공백 체크
    if alphabet == " ":
        return " "

    return chr(ord('Z') - ord(alphabet) + ord('A')) if alphabet.isupper() else chr(ord('z') - ord(alphabet) + ord('a'))


def solve():
    reverse_word = ""

    word = input()
    for alphabet in word:
        reverse_word += reverse(alphabet)

    print(reverse_word)


if __name__ == '__main__':
    solve()
