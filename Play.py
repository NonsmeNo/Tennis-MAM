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


n = 1
l = 5
r = 3
court_x = 23.77
court_y = 8.23
agent_position = (0, court_y / 2)  # Подача агента
dummy_position = (court_x * 0.75, court_y / 2)  # Начальная позиция болванчика

dummy = Dummy(position=dummy_position, player_area=(court_x / 2, court_x, 0, court_y), length=l, radius=r)
agent = Agent(position=agent_position, player_area=(0, court_x / 2, 0, court_y / 2), length=l, radius=2 * r, n=n)
agent.divide_court(court_x, court_y)

tab_points = [0, 0]
winner = [0, 0]


play_points()
print(f"Общий счет игры {tab_points}")


