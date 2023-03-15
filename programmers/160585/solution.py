def solution(board):
    o_list = []
    x_list = []

    index = 0
    for i in board:
        for j in i:
            index += 1
            if j == 'O':
                o_list.append(index)
            elif j == 'X':
                x_list.append(index)

    if len(o_list) < len(x_list):
        return 0
    elif len(x_list) + 1 < len(o_list):
        return 0
    elif is_game_win_case(o_list) and is_game_win_case(x_list):
        return 0

    # @TODO 게임이 끝났는데도 계속 진행되는 케이스에 대해서 검사 필요

    return 1


def is_game_win_case(player_list):
    if 1 in player_list and 2 in player_list and 3 in player_list or \
            4 in player_list and 5 in player_list and 6 in player_list or \
            7 in player_list and 8 in player_list and 9 in player_list or \
            1 in player_list and 4 in player_list and 7 in player_list or \
            2 in player_list and 5 in player_list and 8 in player_list or \
            3 in player_list and 6 in player_list and 9 in player_list or \
            1 in player_list and 5 in player_list and 9 in player_list:
        return True

    return False
