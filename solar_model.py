# coding: utf-8
# license: GPLv3

gravitational_constant = 6.67408E-11
"""Гравитационная постоянная Ньютона G"""


def calculate_force(body, space_objects):
    """Вычисляет силу, действующую на тело.

    Параметры:

    body — тело, для которого нужно вычислить действующую силу.
    space_objects — список объектов, которые воздействуют на тело.
    """

    body.Fx = body.Fy = 0.0
    for obj in space_objects:
        if body == obj:
            continue  # тело не действует гравитационной силой на само себя!

        # Вычисляем расстояние между телами
        dx = obj.x - body.x
        dy = obj.y - body.y
        r = (dx ** 2 + dy ** 2) ** 0.5

        # Вычисляем силу притяжения по закону Ньютона
        force = gravitational_constant * body.m * obj.m / (r ** 2)

        # Разлагаем силу на компоненты по осям
        body.Fx += force * dx / r
        body.Fy += force * dy / r


def move_space_object(body, dt):
    """Перемещает тело в соответствии с действующей на него силой.

    Параметры:

    **body — тело, которое нужно переместить.
    dt — шаг по времени.
    """

    # Вычисляем ускорение по второму закону Ньютона (a = F/m)
    ax = body.Fx / body.m
    ay = body.Fy / body.m

    # Обновляем скорость (v = v0 + a*dt)
    body.Vx += ax * dt
    body.Vy += ay * dt

    # Обновляем координаты (x = x0 + v*dt)
    body.x += body.Vx * dt
    body.y += body.Vy * dt


def recalculate_space_objects_positions(space_objects, dt):
    """Пересчитывает координаты объектов.

    Параметры:

    space_objects — список объектов, для которых нужно пересчитать координаты.
    dt — шаг по времени.
    """

    # Сначала вычисляем силы для всех тел
    for body in space_objects:
        calculate_force(body, space_objects)

    # Затем перемещаем все тела
    for body in space_objects:
        move_space_object(body, dt)


if __name__ == "__main__":
    print("This module is not for direct call!")
