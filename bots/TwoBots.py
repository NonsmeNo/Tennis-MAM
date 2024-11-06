import random
class Player:
    def __init__(self, position, radius, length, player_area, points):
        self.position = position
        self.radius = radius
        self.length = length
        self.player_area = player_area # (x_min, x_max, y_min, y_max)
        self.points = points

    def hit_random(self, player_area): # отправление мяча в случайную точку определенной области
        x = random.uniform(player_area[0], player_area[1])
        y = random.uniform(player_area[2], player_area[3])
        pitch_coordinate = (x, y)
        return pitch_coordinate

class Agent(Player):
    def __init__(self, position, radius, length, player_area, n, points):
        super().__init__(position, radius, length, player_area, points)
        self.n = n

    def algorithm(self, player_area): # алгоритм отбивания мяча для агента
        x = random.uniform(player_area[0], player_area[1])
        y = random.uniform(player_area[2], player_area[3])
        pitch_coordinate = (x, y)
        return pitch_coordinate

    def hitting_check(self, ball_position):  # проверка, отбил агент мяч или нет
        d = ((self.position[0] - ball_position[0]) ** 2 +
             (self.position[1] - ball_position[1]) ** 2) ** 0.5  # кратчайшее расстояние от точки до точки
        print(d)
        if ball_position[0] >= self.position[0]:
            return d <= self.length + self.radius
        else:
            return d <= self.length




class Dummy(Player):
    def __init__(self, position, radius, length, player_area, points):
        super().__init__(position, radius, length, player_area, points)

    def hitting_check(self, ball_position):  # проверка, отбил болванчик мяч или нет
        d = ((self.position[0] - ball_position[0]) ** 2 +
             (self.position[1] - ball_position[1]) ** 2) ** 0.5 # кратчайшее расстояние от точки до точки
        print(d)
        return d <= self.length + self.radius



def play_points(points): # одна игра до потери мяча
    agent.position = agent_position
    dummy.position = dummy_position

    #подача мяча

    player_area_EF = (court_x / 2, court_x * 0.75, 0, court_y) #подача совершается только в сектор E или F
    ball_position = agent.hit_random(player_area_EF)
    print(f"ball_position {ball_position}")
    print(f"dummy.position {dummy.position}")
    if dummy.hitting_check(ball_position):
        print("болванчик отбил")
        dummy.position = ball_position
    else:
        print("болванчик не отбил")
        agent.points += points
        return

    while True:
        ball_position = dummy.hit_random(agent.player_area)
        print(f"ball_position {ball_position}")
        print(f"agent.position {agent.position}")
        if agent.hitting_check(ball_position):
            print("агент отбил")
            agent.position = ball_position
        else:
            print("агент не отбил")
            dummy.points += points
            return

        ball_position = agent.algorithm(dummy.player_area)
        print(f"ball_position {ball_position}")
        print(f"dummy.position {dummy.position}")
        if dummy.hitting_check(ball_position):
            print("болванчик отбил")
            dummy.position = ball_position
        else:
            print("болванчик не отбил")
            agent.points += points
            return

n = 40
l = 5
r = 5

court_x = 23.77
court_y = 8.23
agent_position = (0, court_y/2)  # Подача агента
dummy_position = (court_x*0.75, court_y/2)  # Начальная позиция болванчика

agent = Agent(position=agent_position, radius=2*r, length=l, player_area=(0, court_x/2, 0, court_y/2), n=n, points=0)
dummy = Dummy(position=dummy_position, radius=r, length=l, player_area=(court_x/2, court_x, 0, court_y), points=0)


play_points(3)
