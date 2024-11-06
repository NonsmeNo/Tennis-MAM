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
        dummy.position = ball_position
    else:
        winner[0] += 1
        tab_points[0] += 1
        return

    # основной игровой цикл, где мяч переходит от одного игрока к другому
    while True:
        ball_position = dummy.hit_random(agent.player_area)
        if agent.hitting_check(ball_position):
            agent.position = ball_position
        else:
            winner[1] += 1
            tab_points[1] += 1
            return

        ball_position = agent.algorithm(dummy)
        if ball_position is None:
            winner[1] += 1
            tab_points[1] += 1
            return

        if dummy.hitting_check(ball_position):
            dummy.position = ball_position
        else:
            winner[0] += 1
            tab_points[0] += 1
            return


l = 5
r = 3

court_x = 23.77
court_y = 8.23
agent_position = (0, court_y / 2)  # Подача агента
dummy_position = (court_x * 0.75, court_y / 2)  # Начальная позиция болванчика

n = 1
for _ in range(10):
    n += 10

    dummy = Dummy(position=dummy_position, player_area=(court_x / 2, court_x, 0, court_y), length=l, radius=r)
    agent = Agent(position=agent_position, player_area=(0, court_x / 2, 0, court_y / 2), length=l, radius=2 * r, n=n)
    agent.divide_court(court_x, court_y)

    winner = [0, 0]
    tab_points = [0, 0]
    [play_points() for _ in range(10)]
    print(f"n = {n} Общий счет игры {tab_points}, вероятность победы агента: {tab_points[0] / (tab_points[0] + tab_points[1])}")
