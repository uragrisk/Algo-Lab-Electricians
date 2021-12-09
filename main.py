from electricians import Electricians


def main():
    try:
        electricians_input = open("data/electricians.in")
        distance = int(electricians_input.readline())
        pole_heights_line = electricians_input.readline()
        pole_heights = [int(x) for x in pole_heights_line.split()]
        print(pole_heights)
        pole_numbers = len(pole_heights)

        e = Electricians(distance, pole_heights, pole_numbers)

        electricians_output = open("data/electricians.out", "w")
        electricians_output.write(f'You need {e.get_wire_length()} meters of wire')
    except FileNotFoundError as e:
        print(e)


if __name__ == '__main__':
    main()

