# coding: utf-8
# license: GPLv3

from solar_objects import Star, Planet


def read_space_objects_data_from_file(input_filename):
    """Cчитывает данные о космических объектах из файла, создаёт сами объекты
    и вызывает создание их графических образов

    Параметры:

    input_filename — имя входного файла
    """

    objects = []
    with open(input_filename, 'r') as input_file:
        for line in input_file:
            if len(line.strip()) == 0 or line[0] == '#':
                continue  # пустые строки и строки-комментарии пропускаем

            parts = line.split()
            object_type = parts[0].lower()

            if object_type == "star":
                star = Star()
                parse_star_parameters(line, star)
                objects.append(star)
            elif object_type == "planet":
                planet = Planet()
                parse_planet_parameters(line, planet)
                objects.append(planet)
            else:
                print(f"Unknown space object: {object_type}")

    return objects


def parse_star_parameters(line, star):
    """Считывает данные о звезде из строки.
    Входная строка должна иметь следующий формат:
    Star <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>

    Здесь (x, y) — координаты звезды, (Vx, Vy) — скорость.
    Пример строки:
    Star 10 red 1000 1 2 3 4

    Параметры:

    line — строка с описанием звезды.
    star — объект звезды.
    """
    parts = line.split()
    if len(parts) != 8:
        raise ValueError(f"Invalid star parameters count: {len(parts)}, expected 8")

    star.R = float(parts[1])
    star.color = parts[2]
    star.m = float(parts[3])
    star.x = float(parts[4])
    star.y = float(parts[5])
    star.Vx = float(parts[6])
    star.Vy = float(parts[7])


def parse_planet_parameters(line, planet):
    """Считывает данные о планете из строки.
    Входная строка должна иметь следующий формат:
    Planet <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>

    Здесь (x, y) — координаты планеты, (Vx, Vy) — скорость.
    Пример строки:
    Planet 10 red 1000 1 2 3 4

    Параметры:

    line — строка с описанием планеты.
    planet — объект планеты.
    """
    parts = line.split()
    if len(parts) != 8:
        raise ValueError(f"Invalid planet parameters count: {len(parts)}, expected 8")

    planet.R = float(parts[1])
    planet.color = parts[2]
    planet.m = float(parts[3])
    planet.x = float(parts[4])
    planet.y = float(parts[5])
    planet.Vx = float(parts[6])
    planet.Vy = float(parts[7])


def write_space_objects_data_to_file(output_filename, space_objects):
    """Сохраняет данные о космических объектах в файл.
    Строки должны иметь следующий формат:
    Star <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>
    Planet <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>

    Параметры:

    output_filename — имя выходного файла
    space_objects — список объектов планет и звёзд
    """
    with open(output_filename, 'w') as out_file:
        for obj in space_objects:
            if isinstance(obj, Star):
                obj_type = "Star"
            elif isinstance(obj, Planet):
                obj_type = "Planet"
            else:
                continue

            out_file.write(
                f"{obj_type} {obj.R} {obj.color} {obj.m} "
                f"{obj.x} {obj.y} {obj.Vx} {obj.Vy}\n"
            )


if __name__ == "__main__":
    print("This module is not for direct call!")
