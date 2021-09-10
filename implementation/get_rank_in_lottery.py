def get_rank_in_lottery(numbers, matches):
    ranks = [6, 6, 5, 4, 3, 2, 1]

    match_count, zero_count = 0, 0
    for number in numbers:
        if number in matches:
            match_count += 1
        if number == 0:
            zero_count += 1

    return ranks[match_count], ranks[match_count + zero_count]


def main():
    numbers = [44, 1, 0, 3, 0, 21]
    matches = [31, 10, 3, 21, 11, 55]

    min_rank, max_rank = get_rank_in_lottery(numbers, matches)
    print(min_rank, max_rank)


if __name__ == '__main__':
    main()
