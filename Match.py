from Agent import Agent
from Dummy import Dummy


def play_points():  # одна игра до потери мяча
    winner[:] = [0, 0]
    agent.position = agent_position
    dummy.position = dummy_position

    # подача мяча
    start_player_area = (court_x / 2, court_x * 0.75, 0, court_y)  # подача совершается только в сектор E или F
    ball_position = agent.hit_random(start_player_area)
    if dummy.hitting_check(ball_position):
        print("болванчик отбил")
        dummy.position = ball_position
    else:
        winner[0] += 1
        tab_points[0] += 1
        print(f"болванчик не отбил")
        return

    # основной игровой цикл, где мяч переходит от одного игрока к другому
    while True:
        ball_position = dummy.hit_random(agent.player_area)
        if agent.hitting_check(ball_position):
            print("агент отбил")
            agent.position = ball_position
        else:
            winner[1] += 1
            tab_points[1] += 1
            print(f"агент не отбил")
            return

        ball_position = agent.algorithm(dummy)
        if ball_position is None:
            winner[1] += 1
            tab_points[1] += 1
            print(f"мяч попал в аут")
            return

        if dummy.hitting_check(ball_position):
            print("болванчик отбил")
            dummy.position = ball_position
        else:
            winner[0] += 1
            tab_points[0] += 1
            print(f"болванчик не отбил")
            return


def play_game():
    points_sequence = [0, 15, 30, 40]
    score = [0, 0]

    while True:
        play_points()
        if winner[0] > winner[1]:  # Агент выиграл очко
            if score[0] < 3:
                score[0] += 1
            elif score[0] == 3 and score[1] < 3:
                return 0
            elif score[0] == 3 and score[1] == 3:
                score[0] = 4
            elif score[0] == 4:
                return 0
            else:
                score[1] = 3

        else:  # Болванчик выиграл очко
            if score[1] < 3:
                score[1] += 1
            elif score[1] == 3 and score[0] < 3:
                return 1
            elif score[1] == 3 and score[0] == 3:
                score[1] = 4
            elif score[1] == 4:
                return 1
            else:
                score[0] = 3
        print(f"Счет в гейме: Агент {points_sequence[score[0]]} - Болванчик {points_sequence[score[1]]} \n")


def play_set():
    set_score = [0, 0]

    while True:
        game_winner = play_game()
        set_score[game_winner] += 1

        print(f"\nСчет в сете: Агент {set_score[0]} - Болванчик {set_score[1]} \n \n \n")

        # Проверка на победу в сете
        if set_score[game_winner] >= 6 and abs(set_score[0] - set_score[1]) >= 2:
            return game_winner

        # Тай-брейк при счете 6-6
        if set_score[0] == 6 and set_score[1] == 6:
            return play_tiebreak()


def play_tiebreak():
    tiebreak_score = [0, 0]

    while True:
        play_points()
        if winner[0] > winner[1]:
            tiebreak_score[0] += 1
        else:
            tiebreak_score[1] += 1

        print(f"Тай-брейк: Агент {tiebreak_score[0]} - Болванчик {tiebreak_score[1]}")

        # Проверка на победу в тай-брейке
        if (tiebreak_score[0] >= 7 or tiebreak_score[1] >= 7) and abs(tiebreak_score[0] - tiebreak_score[1]) >= 2:
            return 0 if tiebreak_score[0] > tiebreak_score[1] else 1


def play_match():
    match_score = [0, 0]

    while match_score[0] < 2 and match_score[1] < 2:
        set_winner = play_set()
        match_score[set_winner] += 1
        print(f"Счет в матче: Агент {match_score[0]} - Болванчик {match_score[1]}")

    if match_score[0] > match_score[1]:
        print("Агент выиграл матч!")
    else:
        print("Болванчик выиграл матч!")


n = 20
l = 5
r = 3

court_x = 23.77
court_y = 8.23
agent_position = (0, court_y / 2)  # Подача агента
dummy_position = (court_x * 0.75, court_y / 2)  # Начальная позиция болванчика

dummy = Dummy(position=dummy_position, player_area=(court_x / 2, court_x, 0, court_y), length=l, radius=r)
agent = Agent(position=agent_position, player_area=(0, court_x / 2, 0, court_y / 2), length=l, radius=2 * r, n=n)
agent.divide_court(court_x, court_y)

winner = [0, 0]
tab_points = [0, 0]

print(f"Начало матча!!! \n")
play_match()
print(f"Общий счет игры {tab_points}")
