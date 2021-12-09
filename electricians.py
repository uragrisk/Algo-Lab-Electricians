import math
from collections import Counter


class Electricians:
    def __init__(self, distance, pole_heights, pole_numbers):
        self.distance = distance
        self.pole_heights = pole_heights
        self.pole_numbers = pole_numbers
        self.wire_length = 0

    def calculate_wire_length(self, start_pole_height, end_pole_height, calculated_hypotenuses):
        calculated_hypotenuse = max(calculated_hypotenuses, key=lambda x: x[2] if (
                    start_pole_height in x[:2] and end_pole_height in x[:2]) else 0)
        if start_pole_height == end_pole_height:
            self.wire_length += self.distance
        elif calculated_hypotenuse:
            self.wire_length += calculated_hypotenuse[2]
        else:
            difference = end_pole_height - start_pole_height
            calculate = math.sqrt(math.pow(self.distance, 2) + math.pow(difference, 2))
            calculated_hypotenuses.append([start_pole_height, end_pole_height, calculate])
            self.wire_length += calculate
        return self.wire_length

    def get_wire_length(self):
        calculated_hypotenuses = [[]]
        pole_heights = self.pole_heights

        for i in range(1, self.pole_numbers):
            if i + 1 >= self.pole_numbers:
                if pole_heights[i] > pole_heights[i - 1]:
                    pole_heights[i - 1] = 1
                    break
                if pole_heights[i] < pole_heights[i - 1]:
                    pole_heights[i] = 1
                    break
                break

            if pole_heights[i - 1] <= pole_heights[i] and pole_heights[i + 1] <= pole_heights[i]:
                pole_heights[i - 1] = 1
                pole_heights[i + 1] = 1
            elif pole_heights[i - 1] > pole_heights[i]:
                pole_heights[i] = 1
            elif pole_heights[i + 1] > pole_heights[i] and pole_heights[i - 1] != 1:
                pole_heights[i] = 1

        for i in range(1, self.pole_numbers):
            self.calculate_wire_length(pole_heights[i - 1], pole_heights[i], calculated_hypotenuses)

        print(round(self.wire_length, 2))
        return round(self.wire_length, 2)
