import math


def sphere_curvature(r):  # Кривизна сферы (r - радиус сферы)
    return 1 / (r ** 2)


def riemann_triangle_p(r, a, b, c):  # Периметр сферического треугольника (r - радиус плоскости)
    return (r * (a + b + c)) / 2


def lobachevsky_triangle_p(r, a, b, c):  # Периметр гиперболического треугольника (r - радиус плоскости)
    return (4 * (math.pi ** 2) * r) / (a + b + c)


def riemann_triangle_s(r, a, b, c):  # Площадь сферического треугольника (r - радиус сферы / полусферы)
    return (r ** 2) * (math.pi - a - b - c)


def lobachevsky_triangle_s(r, a, b, c):  # Площадь гиперболического треугольника (r - радиус сферы / полусферы)
    return (r ** 2) * (a + b + c - math.pi)


def n_eucl_tetrahedron_v(r, a, h):  # Объем сферического / гиперболического тетраэдра (h — высота сегмента, R — радиус сферы, а - ребро тетраэдра)
    return math.pi * (h ** 2) * (r - 1 / 3 * h) + ((a ** 3) * math.sqrt(2) / 3)


def r_from_curvature(k):	# Радиус сферы через кривизну сферы (k - кривизна сферы)
    return math.sqrt(1 / k)


def r_from_r_t_p(p, a, b, c):	# Радиус плоскости через периметр сферического треугольника
    return 2 * p / (a + b + c)


def r_from_l_t_p(p, a, b, c):	# Радиус плоскости через периметр гиперболического треугольника
    return (p * (a + b + c)) / (4 * math.pi ** 2)


def r_from_r_t_s(s, a, b, c):	# Радиус сферы через площадь сферического треугольника
    return math.sqrt(s / (math.pi - a - b - c))


def r_from_l_t_s(s, a, b, c):	# Радиус сферы через площадь гиперболического треугольника
    return math.sqrt(s / (a + b + c - math.pi))


def r_from_v(v, a, h):	# Радиус сферы через объем неевклидова тетраэдра
    return -((-math.pi * h ** 3 + math.sqrt(2) * a ** 3 - 3 * v) / (3 * math.pi * h ** 2))


def s_angle_sum_from_r_t_p(p, r):	# Сумма углов сферического треугольника через его периметр
    return 2 * p / r


def h_angle_sum_from_l_t_p(p, r):	# Сумма углов гиперболического треугольника через его периметр
    return (4 * math.pi ** 2 * r) / p


def s_angle_sum_from_r_t_s(s, r):	# Сумма углов сферического треугольника через его площадь
    return abs((s / r ** 2) - math.pi)


def h_angle_sum_from_l_t_s(s, r):	# Сумма углов гиперболического треугольника через его площадь
    return (s / r ** 2) + math.pi
