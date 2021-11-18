import math


def cockroach_speed(kmh_speed: float) -> int:
    result = (kmh_speed * 1000 / 36)
    x = math.floor(result)
    return x


if __name__ == '__main__':
    speed_val = float(input('Введите скорость таракана в км/ч: '))
    print(f'Скорость таракана в см/с: {cockroach_speed(speed_val)}')
