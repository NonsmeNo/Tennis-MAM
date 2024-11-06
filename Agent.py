import random
import math


class Agent:

    def __init__(self, position, player_area, length, radius, n):
        self.position = position
        self.player_area = player_area  # (x_min, x_max, y_min, y_max)
        self.length = length
        self.radius = radius

        self.n = n
        self.squares = []  # список координат n квадратов

    # проверка, отбил агент мяч или нет
    def hitting_check(self, ball_position):
        d = ((self.position[0] - ball_position[0]) ** 2 +
             (self.position[1] - ball_position[1]) ** 2) ** 0.5  # кратчайшее расстояние от точки до точки
        if ball_position[0] >= self.position[0]:
            return d <= self.length + self.radius
        else:
            return d <= self.length

    # деление половины корта болванчика на квадраты
    def divide_court(self, court_x, court_y):
        court_width = court_x / 2
        court_height = court_y

        # Вычисляем количество колонок и рядов
        num_cols = math.ceil(math.sqrt(self.n * court_width / court_height))
        num_rows = math.ceil(self.n / num_cols)

        step_x = court_width / num_cols
        step_y = court_height / num_rows

        # Заполняем список квадратов с координатами
        for i in range(num_rows):
            for j in range(num_cols):
                x_min = court_x / 2 + j * step_x
                x_max = min(court_x / 2 + (j + 1) * step_x, court_x)
                y_min = i * step_y
                y_max = min((i + 1) * step_y, court_y)

                self.squares.append(((x_min, x_max, y_min, y_max), (i, j)))  # Сохраняем также индексы (i, j)

                if len(self.squares) >= self.n:
                    return

    # время, которое потребуется болванчику, чтобы
    # достичь точки центра квадрата
    def time_to_reach(self, player_position, square_position):
        d = ((player_position[0] - square_position[0]) ** 2 +
             (player_position[1] - square_position[1]) ** 2) ** 0.5
        return d / self.length

    def algorithm(self, dummy):
        max_time_needed = 0
        best_square = None
        best_square_indices = None

        # Проходим по квадратам и находим лучший
        for square, (i, j) in self.squares:
            x = (square[0] + square[1]) / 2
            y = (square[2] + square[3]) / 2
            center_position = (x, y)

            time_needed = self.time_to_reach(dummy.position, center_position)

            if time_needed > max_time_needed:
                max_time_needed = time_needed
                best_square = square
                best_square_indices = (i, j)  # Сохраняем индексы лучшего квадрата

        # учитываем вероятность ошибки 5%
        # if random.random() < 0.05:
        #     print("попали сюда")

        return best_square

    # рандомный бросок
    def hit_random(self, player_area):  # отправление мяча в случайную точку определенной области
        x = random.uniform(player_area[0], player_area[1])
        y = random.uniform(player_area[2], player_area[3])
        return (x, y)
