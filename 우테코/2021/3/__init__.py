def solution(ings, menu, sell):
    answer = 0

    ings_dict = {}
    for idx in range(0, len(ings)):
        ings_dict[ings[idx].split(" ")[0]] = ings[idx].split(" ")[1]

    sell_dict = {}
    for idx in range(0, len(sell)):
        sell_dict[sell[idx].split(" ")[0]] = sell[idx].split(" ")[1]

    for food in menu:
        menu_name = food.split(" ")[0]
        menu_price = food.split(" ")[2]

        if menu_name not in sell_dict.keys():
            continue

        price = 0
        for ing in food.split(" ")[1]:
            price += int(ings_dict[ing])

        answer += int(sell_dict[menu_name]) * (int(menu_price) - price)

    return answer


if __name__ == '__main__':
    ings = ["r 10", "a 23", "t 124", "k 9"]
    menu = ["PIZZA arraak 145", "HAMBURGER tkar 180", "BREAD kkk 30", "ICECREAM rar 50", "SHAVEDICE rar 45",
            "JUICE rra 55", "WATER a 20"]
    sell = ["BREAD 5", "ICECREAM 100", "PIZZA 7", "JUICE 10", "WATER 1"]
    print(solution(ings, menu, sell))
