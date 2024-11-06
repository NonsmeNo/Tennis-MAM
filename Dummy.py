import random


class Dummy:
    def __init__(self, position, player_area, length, radius):
        self.position = position
        self.player_area = player_area  # (x_min, x_max, y_min, y_max)
        self.length = length
        self.radius = radius

    # проверка, отбил болванчик мяч или нет
    def hitting_check(self, ball_position):
        d = ((self.position[0] - ball_position[0]) ** 2 +
             (self.position[1] - ball_position[1]) ** 2) ** 0.5  # кратчайшее расстояние от точки до точки
        return d <= self.length + self.radius

    # отправление мяча в случайную точку определенной области
    def hit_random(self, player_area):  # отправление мяча в случайную точку определенной области
        x = random.uniform(player_area[0], player_area[1])
        y = random.uniform(player_area[2], player_area[3])
        return (x, y)
