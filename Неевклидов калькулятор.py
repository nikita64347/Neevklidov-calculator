import sys
import math

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtWidgets import *


class Main_window(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Неевклидов калькулятор - Главное меню')
        self.resize(600, 400)
        self.setWindowIcon(QIcon(
            "3700470-drawing-geometry-measure-measuring-rulers-set-square_108760.ico"))

        label = QLabel('Выберите действие:')
        self.button_1 = QPushButton('Определить кривизну сферы')
        self.button_2 = QPushButton('Определить периметр сферического треугольника')
        self.button_3 = QPushButton('Определить периметр гиперболического треугольника')
        self.button_4 = QPushButton('Определить площадь сферического треугольника')
        self.button_5 = QPushButton('Определить площадь гиперболического треугольника')
        self.button_6 = QPushButton('Определить объем сферического / гиперболического тетраэдра')
        self.button_7 = QPushButton('Определить радиус')
        self.button_8 = QPushButton('Определить сумму углов треугольника')

        label.setFont(QFont('Arial', 12, QFont.Bold))
        self.button_1.setFont(QFont('Arial', 10))
        self.button_2.setFont(QFont('Arial', 10))
        self.button_3.setFont(QFont('Arial', 10))
        self.button_4.setFont(QFont('Arial', 10))
        self.button_5.setFont(QFont('Arial', 10))
        self.button_6.setFont(QFont('Arial', 10))
        self.button_7.setFont(QFont('Arial', 10))
        self.button_8.setFont(QFont('Arial', 10))

        self.button_1.setFixedWidth(400)
        self.button_2.setFixedWidth(400)
        self.button_3.setFixedWidth(400)
        self.button_4.setFixedWidth(400)
        self.button_5.setFixedWidth(400)
        self.button_6.setFixedWidth(400)
        self.button_7.setFixedWidth(400)
        self.button_8.setFixedWidth(400)

        main_layout = QVBoxLayout()

        main_layout.addWidget(label, alignment=Qt.AlignCenter)
        main_layout.addWidget(self.button_1, alignment=Qt.AlignCenter)
        main_layout.addWidget(self.button_2, alignment=Qt.AlignCenter)
        main_layout.addWidget(self.button_3, alignment=Qt.AlignCenter)
        main_layout.addWidget(self.button_4, alignment=Qt.AlignCenter)
        main_layout.addWidget(self.button_5, alignment=Qt.AlignCenter)
        main_layout.addWidget(self.button_6, alignment=Qt.AlignCenter)
        main_layout.addWidget(self.button_7, alignment=Qt.AlignCenter)
        main_layout.addWidget(self.button_8, alignment=Qt.AlignCenter)

        self.setLayout(main_layout)

        self.button_1.clicked.connect(self.open_win_1)
        self.button_2.clicked.connect(self.open_win_2)
        self.button_3.clicked.connect(self.open_win_3)
        self.button_4.clicked.connect(self.open_win_4)
        self.button_5.clicked.connect(self.open_win_5)
        self.button_6.clicked.connect(self.open_win_6)
        self.button_7.clicked.connect(self.open_win_7)
        self.button_8.clicked.connect(self.open_win_8)

    def open_win_1(self):
        self.win_1 = Window_1()
        self.win_1.show()

    def open_win_2(self):
        self.win_2 = Window_2()
        self.win_2.show()

    def open_win_3(self):
        self.win_3 = Window_3()
        self.win_3.show()

    def open_win_4(self):
        self.win_4 = Window_4()
        self.win_4.show()

    def open_win_5(self):
        self.win_5 = Window_5()
        self.win_5.show()

    def open_win_6(self):
        self.win_6 = Window_6()
        self.win_6.show()

    def open_win_7(self):
        self.win_7 = Window_7()
        self.win_7.show()

    def open_win_8(self):
        self.win_8 = Window_8()
        self.win_8.show()


class Window_1(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Определение кривизны сферы')
        self.resize(450, 400)
        self.setWindowIcon(QIcon("shape_geometry_geometric_d_sphere_round_icon_149664.ico"))

        label_win_1 = QLabel('Введите значения величин:')
        label_win_1.setFont(QFont('Arial', 10))
        label_r_win_1 = QLabel('R = ')
        label_r_win_1.setFont(QFont('Arial', 12))
        self.line_r_1 = QLineEdit()
        self.line_r_1.setFixedWidth(400)
        self.line_r_1.setPlaceholderText('Радиус сферы (см)')
        self.ready_button_1 = QPushButton('Рассчитать')
        round_label_1 = QLabel('Округление:')
        self.round_choice_box_1 = QComboBox()
        self.round_choice_box_1.addItem('нет')
        self.round_choice_box_1.addItem('до сотых')
        self.round_choice_box_1.addItem('до десятых')
        self.round_choice_box_1.addItem('до целого')

        main_layout_1 = QVBoxLayout()
        layout_1_1 = QHBoxLayout()
        layout_1_2 = QHBoxLayout()
        layout_1_1.addWidget(label_r_win_1, alignment=Qt.AlignRight)
        layout_1_1.addWidget(self.line_r_1, alignment=Qt.AlignLeft)
        layout_1_2.addWidget(round_label_1, alignment=Qt.AlignRight)
        layout_1_2.addWidget(self.round_choice_box_1, alignment=Qt.AlignLeft)
        main_layout_1.addWidget(label_win_1, alignment=Qt.AlignCenter)
        main_layout_1.addLayout(layout_1_1)
        main_layout_1.addLayout(layout_1_2)
        main_layout_1.addWidget(self.ready_button_1, alignment=Qt.AlignCenter)

        self.setLayout(main_layout_1)

        self.ready_button_1.clicked.connect(self.get_result_1)

    def get_result_1(self):
        def sphere_curvature(r):
            return 1 / (r ** 2)

        try:
            match self.round_choice_box_1.currentText():
                case 'до сотых':
                    r = float(self.line_r_1.text())
                    message_result_1 = QMessageBox()
                    message_result_1.setWindowIcon(
                        QIcon("Tick_Mark_icon-icons.com_69146.ico"))
                    message_result_1.setWindowTitle('Готово')
                    message_result_1.setText('Результат: ' + str(round(sphere_curvature(r), 2)))
                    message_result_1.exec_()
                case 'до десятых':
                    r = float(self.line_r_1.text())
                    message_result_1 = QMessageBox()
                    message_result_1.setWindowIcon(
                        QIcon("Tick_Mark_icon-icons.com_69146.ico"))
                    message_result_1.setWindowTitle('Готово')
                    message_result_1.setText('Результат: ' + str(round(sphere_curvature(r), 1)))
                    message_result_1.exec_()
                case 'до целого':
                    r = float(self.line_r_1.text())
                    message_result_1 = QMessageBox()
                    message_result_1.setWindowIcon(
                        QIcon("Tick_Mark_icon-icons.com_69146.ico"))
                    message_result_1.setWindowTitle('Готово')
                    message_result_1.setText('Результат: ' + str(round(sphere_curvature(r))))
                    message_result_1.exec_()
                case _:
                    r = float(self.line_r_1.text())
                    message_result_1 = QMessageBox()
                    message_result_1.setWindowIcon(
                        QIcon("Tick_Mark_icon-icons.com_69146.ico"))
                    message_result_1.setWindowTitle('Готово')
                    message_result_1.setText('Результат: ' + str(sphere_curvature(r)))
                    message_result_1.exec_()
        except:
            message_error_1 = QMessageBox()
            message_error_1.setWindowIcon(QIcon("crossregular_106296.ico"))
            message_error_1.setWindowTitle('Ошибка')
            message_error_1.setText('Не удалось расчитать величину')
            message_error_1.exec_()


class Window_2(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Определение периметра сферического треугольника')
        self.resize(450, 400)
        self.setWindowIcon(QIcon("stroke_pyramid_geometry_triangle_icon_259998.ico"))

        label_win_2 = QLabel('Введите значения величин:')
        label_win_2.setFont(QFont('Arial', 10))
        label_r_win_2 = QLabel('R = ')
        label_a_win_2 = QLabel('α = ')
        label_b_win_2 = QLabel('β = ')
        label_c_win_2 = QLabel('γ = ')
        label_r_win_2.setFont(QFont('Arial', 12))
        label_a_win_2.setFont(QFont('Arial', 12))
        label_b_win_2.setFont(QFont('Arial', 12))
        label_c_win_2.setFont(QFont('Arial', 12))
        self.line_r_2 = QLineEdit()
        self.line_a_2 = QLineEdit()
        self.line_b_2 = QLineEdit()
        self.line_c_2 = QLineEdit()
        self.line_r_2.setFixedWidth(400)
        self.line_a_2.setFixedWidth(400)
        self.line_b_2.setFixedWidth(400)
        self.line_c_2.setFixedWidth(400)
        self.line_r_2.setPlaceholderText('Радиус плоскости (см)')
        self.line_a_2.setPlaceholderText('Угол 1 (в градусах)')
        self.line_b_2.setPlaceholderText('Угол 2 (в градусах)')
        self.line_c_2.setPlaceholderText('Угол 3 (в градусах)')
        self.ready_button_2 = QPushButton('Рассчитать')
        round_label_2 = QLabel('Округление:')
        self.round_choice_box_2 = QComboBox()
        self.round_choice_box_2.addItem('нет')
        self.round_choice_box_2.addItem('до сотых')
        self.round_choice_box_2.addItem('до десятых')
        self.round_choice_box_2.addItem('до целого')

        main_layout_2 = QVBoxLayout()
        layout_2_1 = QHBoxLayout()
        layout_2_2 = QHBoxLayout()
        layout_2_3 = QHBoxLayout()
        layout_2_4 = QHBoxLayout()
        layout_2_5 = QHBoxLayout()
        layout_2_1.addWidget(label_r_win_2, alignment=Qt.AlignRight)
        layout_2_1.addWidget(self.line_r_2, alignment=Qt.AlignLeft)
        layout_2_2.addWidget(label_a_win_2, alignment=Qt.AlignRight)
        layout_2_2.addWidget(self.line_a_2, alignment=Qt.AlignLeft)
        layout_2_3.addWidget(label_b_win_2, alignment=Qt.AlignRight)
        layout_2_3.addWidget(self.line_b_2, alignment=Qt.AlignLeft)
        layout_2_4.addWidget(label_c_win_2, alignment=Qt.AlignRight)
        layout_2_4.addWidget(self.line_c_2, alignment=Qt.AlignLeft)
        layout_2_5.addWidget(round_label_2, alignment=Qt.AlignRight)
        layout_2_5.addWidget(self.round_choice_box_2, alignment=Qt.AlignLeft)
        main_layout_2.addWidget(label_win_2, alignment=Qt.AlignCenter)
        main_layout_2.addLayout(layout_2_1)
        main_layout_2.addLayout(layout_2_2)
        main_layout_2.addLayout(layout_2_3)
        main_layout_2.addLayout(layout_2_4)
        main_layout_2.addLayout(layout_2_5)
        main_layout_2.addWidget(self.ready_button_2, alignment=Qt.AlignCenter)

        self.setLayout(main_layout_2)

        self.ready_button_2.clicked.connect(self.get_result_2)

    def get_result_2(self):
        def riemann_triangle_p(r, a, b, c):
            return (r * (a + b + c)) / 2

        try:
            match self.round_choice_box_2.currentText():
                case 'до сотых':
                    r = float(self.line_r_2.text())
                    a = float(self.line_a_2.text())
                    b = float(self.line_b_2.text())
                    c = float(self.line_c_2.text())
                    message_result_2 = QMessageBox()
                    message_result_2.setWindowIcon(
                        QIcon("Tick_Mark_icon-icons.com_69146.ico"))
                    message_result_2.setWindowTitle('Готово')
                    message_result_2.setText('Результат: ' + str(round(riemann_triangle_p(r, a, b, c), 2)))
                    message_result_2.exec_()
                case 'до десятых':
                    r = float(self.line_r_2.text())
                    a = float(self.line_a_2.text())
                    b = float(self.line_b_2.text())
                    c = float(self.line_c_2.text())
                    message_result_2 = QMessageBox()
                    message_result_2.setWindowIcon(
                        QIcon("Tick_Mark_icon-icons.com_69146.ico"))
                    message_result_2.setWindowTitle('Готово')
                    message_result_2.setText('Результат: ' + str(round(riemann_triangle_p(r, a, b, c), 1)))
                    message_result_2.exec_()
                case 'до целого':
                    r = float(self.line_r_2.text())
                    a = float(self.line_a_2.text())
                    b = float(self.line_b_2.text())
                    c = float(self.line_c_2.text())
                    message_result_2 = QMessageBox()
                    message_result_2.setWindowIcon(
                        QIcon("Tick_Mark_icon-icons.com_69146.ico"))
                    message_result_2.setWindowTitle('Готово')
                    message_result_2.setText('Результат: ' + str(round(riemann_triangle_p(r, a, b, c))))
                    message_result_2.exec_()
                case _:
                    r = float(self.line_r_2.text())
                    a = float(self.line_a_2.text())
                    b = float(self.line_b_2.text())
                    c = float(self.line_c_2.text())
                    message_result_2 = QMessageBox()
                    message_result_2.setWindowIcon(
                        QIcon("Tick_Mark_icon-icons.com_69146.ico"))
                    message_result_2.setWindowTitle('Готово')
                    message_result_2.setText('Результат: ' + str(riemann_triangle_p(r, a, b, c)))
                    message_result_2.exec_()
        except:
            message_error_2 = QMessageBox()
            message_error_2.setWindowIcon(QIcon("crossregular_106296.ico"))
            message_error_2.setWindowTitle('Ошибка')
            message_error_2.setText('Не удалось расчитать величину')
            message_error_2.exec_()


class Window_3(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Определение периметра гиперболического треугольника')
        self.resize(450, 400)
        self.setWindowIcon(QIcon("stroke_pyramid_geometry_triangle_icon_259998.ico"))

        label_win_3 = QLabel('Введите значения величин:')
        label_win_3.setFont(QFont('Arial', 10))
        label_r_win_3 = QLabel('R = ')
        label_a_win_3 = QLabel('α = ')
        label_b_win_3 = QLabel('β = ')
        label_c_win_3 = QLabel('γ = ')
        label_r_win_3.setFont(QFont('Arial', 12))
        label_a_win_3.setFont(QFont('Arial', 12))
        label_b_win_3.setFont(QFont('Arial', 12))
        label_c_win_3.setFont(QFont('Arial', 12))
        self.line_r_3 = QLineEdit()
        self.line_a_3 = QLineEdit()
        self.line_b_3 = QLineEdit()
        self.line_c_3 = QLineEdit()
        self.line_r_3.setFixedWidth(400)
        self.line_a_3.setFixedWidth(400)
        self.line_b_3.setFixedWidth(400)
        self.line_c_3.setFixedWidth(400)
        self.line_r_3.setPlaceholderText('Радиус плоскости (см)')
        self.line_a_3.setPlaceholderText('Угол 1 (в градусах)')
        self.line_b_3.setPlaceholderText('Угол 2 (в градусах)')
        self.line_c_3.setPlaceholderText('Угол 3 (в градусах)')
        self.ready_button_3 = QPushButton('Рассчитать')
        round_label_3 = QLabel('Округление:')
        self.round_choice_box_3 = QComboBox()
        self.round_choice_box_3.addItem('нет')
        self.round_choice_box_3.addItem('до сотых')
        self.round_choice_box_3.addItem('до десятых')
        self.round_choice_box_3.addItem('до целого')

        main_layout_3 = QVBoxLayout()
        layout_3_1 = QHBoxLayout()
        layout_3_2 = QHBoxLayout()
        layout_3_3 = QHBoxLayout()
        layout_3_4 = QHBoxLayout()
        layout_3_5 = QHBoxLayout()
        layout_3_1.addWidget(label_r_win_3, alignment=Qt.AlignRight)
        layout_3_1.addWidget(self.line_r_3, alignment=Qt.AlignLeft)
        layout_3_2.addWidget(label_a_win_3, alignment=Qt.AlignRight)
        layout_3_2.addWidget(self.line_a_3, alignment=Qt.AlignLeft)
        layout_3_3.addWidget(label_b_win_3, alignment=Qt.AlignRight)
        layout_3_3.addWidget(self.line_b_3, alignment=Qt.AlignLeft)
        layout_3_4.addWidget(label_c_win_3, alignment=Qt.AlignRight)
        layout_3_4.addWidget(self.line_c_3, alignment=Qt.AlignLeft)
        layout_3_5.addWidget(round_label_3, alignment=Qt.AlignRight)
        layout_3_5.addWidget(self.round_choice_box_3, alignment=Qt.AlignLeft)
        main_layout_3.addWidget(label_win_3, alignment=Qt.AlignCenter)
        main_layout_3.addLayout(layout_3_1)
        main_layout_3.addLayout(layout_3_2)
        main_layout_3.addLayout(layout_3_3)
        main_layout_3.addLayout(layout_3_4)
        main_layout_3.addLayout(layout_3_5)
        main_layout_3.addWidget(self.ready_button_3, alignment=Qt.AlignCenter)

        self.setLayout(main_layout_3)

        self.ready_button_3.clicked.connect(self.get_result_3)

    def get_result_3(self):
        def lobachevsky_triangle_p(r, a, b, c):
            return (4 * (math.pi ** 2) * r) / (a + b + c)

        try:
            match self.round_choice_box_3.currentText():
                case 'до сотых':
                    r = float(self.line_r_3.text())
                    a = float(self.line_a_3.text())
                    b = float(self.line_b_3.text())
                    c = float(self.line_c_3.text())
                    message_result_3 = QMessageBox()
                    message_result_3.setWindowIcon(
                        QIcon("Tick_Mark_icon-icons.com_69146.ico"))
                    message_result_3.setWindowTitle('Готово')
                    message_result_3.setText('Результат: ' + str(round(lobachevsky_triangle_p(r, a, b, c), 2)))
                    message_result_3.exec_()
                case 'до десятых':
                    r = float(self.line_r_3.text())
                    a = float(self.line_a_3.text())
                    b = float(self.line_b_3.text())
                    c = float(self.line_c_3.text())
                    message_result_3 = QMessageBox()
                    message_result_3.setWindowIcon(
                        QIcon("Tick_Mark_icon-icons.com_69146.ico"))
                    message_result_3.setWindowTitle('Готово')
                    message_result_3.setText('Результат: ' + str(round(lobachevsky_triangle_p(r, a, b, c), 1)))
                    message_result_3.exec_()
                case 'до целого':
                    r = float(self.line_r_3.text())
                    a = float(self.line_a_3.text())
                    b = float(self.line_b_3.text())
                    c = float(self.line_c_3.text())
                    message_result_3 = QMessageBox()
                    message_result_3.setWindowIcon(
                        QIcon("Tick_Mark_icon-icons.com_69146.ico"))
                    message_result_3.setWindowTitle('Готово')
                    message_result_3.setText('Результат: ' + str(round(lobachevsky_triangle_p(r, a, b, c))))
                    message_result_3.exec_()
                case _:
                    r = float(self.line_r_3.text())
                    a = float(self.line_a_3.text())
                    b = float(self.line_b_3.text())
                    c = float(self.line_c_3.text())
                    message_result_3 = QMessageBox()
                    message_result_3.setWindowIcon(
                        QIcon("Tick_Mark_icon-icons.com_69146.ico"))
                    message_result_3.setWindowTitle('Готово')
                    message_result_3.setText('Результат: ' + str(lobachevsky_triangle_p(r, a, b, c)))
                    message_result_3.exec_()
        except:
            message_error_3 = QMessageBox()
            message_error_3.setWindowIcon(QIcon("crossregular_106296.ico"))
            message_error_3.setWindowTitle('Ошибка')
            message_error_3.setText('Не удалось расчитать величину')
            message_error_3.exec_()


class Window_4(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Определение площади сферического треугольника')
        self.resize(450, 400)
        self.setWindowIcon(QIcon("stroke_pyramid_geometry_triangle_icon_259998.ico"))

        label_win_4 = QLabel('Введите значения величин:')
        label_win_4.setFont(QFont('Arial', 10))
        label_r_win_4 = QLabel('R = ')
        label_a_win_4 = QLabel('α = ')
        label_b_win_4 = QLabel('β = ')
        label_c_win_4 = QLabel('γ = ')
        label_r_win_4.setFont(QFont('Arial', 12))
        label_a_win_4.setFont(QFont('Arial', 12))
        label_b_win_4.setFont(QFont('Arial', 12))
        label_c_win_4.setFont(QFont('Arial', 12))
        self.line_r_4 = QLineEdit()
        self.line_a_4 = QLineEdit()
        self.line_b_4 = QLineEdit()
        self.line_c_4 = QLineEdit()
        self.line_r_4.setFixedWidth(400)
        self.line_a_4.setFixedWidth(400)
        self.line_b_4.setFixedWidth(400)
        self.line_c_4.setFixedWidth(400)
        self.line_r_4.setPlaceholderText('Радиус сферы / полусферы (см)')
        self.line_a_4.setPlaceholderText('Угол 1 (в градусах)')
        self.line_b_4.setPlaceholderText('Угол 2 (в градусах)')
        self.line_c_4.setPlaceholderText('Угол 3 (в градусах)')
        self.ready_button_4 = QPushButton('Рассчитать')
        round_label_4 = QLabel('Округление:')
        self.round_choice_box_4 = QComboBox()
        self.round_choice_box_4.addItem('нет')
        self.round_choice_box_4.addItem('до сотых')
        self.round_choice_box_4.addItem('до десятых')
        self.round_choice_box_4.addItem('до целого')

        main_layout_4 = QVBoxLayout()
        layout_4_1 = QHBoxLayout()
        layout_4_2 = QHBoxLayout()
        layout_4_3 = QHBoxLayout()
        layout_4_4 = QHBoxLayout()
        layout_4_5 = QHBoxLayout()
        layout_4_1.addWidget(label_r_win_4, alignment=Qt.AlignRight)
        layout_4_1.addWidget(self.line_r_4, alignment=Qt.AlignLeft)
        layout_4_2.addWidget(label_a_win_4, alignment=Qt.AlignRight)
        layout_4_2.addWidget(self.line_a_4, alignment=Qt.AlignLeft)
        layout_4_3.addWidget(label_b_win_4, alignment=Qt.AlignRight)
        layout_4_3.addWidget(self.line_b_4, alignment=Qt.AlignLeft)
        layout_4_4.addWidget(label_c_win_4, alignment=Qt.AlignRight)
        layout_4_4.addWidget(self.line_c_4, alignment=Qt.AlignLeft)
        layout_4_5.addWidget(round_label_4, alignment=Qt.AlignRight)
        layout_4_5.addWidget(self.round_choice_box_4, alignment=Qt.AlignLeft)
        main_layout_4.addWidget(label_win_4, alignment=Qt.AlignCenter)
        main_layout_4.addLayout(layout_4_1)
        main_layout_4.addLayout(layout_4_2)
        main_layout_4.addLayout(layout_4_3)
        main_layout_4.addLayout(layout_4_4)
        main_layout_4.addLayout(layout_4_5)
        main_layout_4.addWidget(self.ready_button_4, alignment=Qt.AlignCenter)

        self.setLayout(main_layout_4)

        self.ready_button_4.clicked.connect(self.get_result_4)

    def get_result_4(self):
        def riemann_triangle_s(r, a, b, c):
            return (r ** 2) * (math.pi - a - b - c)

        try:
            match self.round_choice_box_4.currentText():
                case 'до сотых':
                    r = float(self.line_r_4.text())
                    a = float(self.line_a_4.text())
                    b = float(self.line_b_4.text())
                    c = float(self.line_c_4.text())
                    message_result_4 = QMessageBox()
                    message_result_4.setWindowIcon(
                        QIcon("Tick_Mark_icon-icons.com_69146.ico"))
                    message_result_4.setWindowTitle('Готово')
                    message_result_4.setText('Результат: ' + str(round(riemann_triangle_s(r, a, b, c), 2)))
                    message_result_4.exec_()
                case 'до десятых':
                    r = float(self.line_r_4.text())
                    a = float(self.line_a_4.text())
                    b = float(self.line_b_4.text())
                    c = float(self.line_c_4.text())
                    message_result_4 = QMessageBox()
                    message_result_4.setWindowIcon(
                        QIcon("Tick_Mark_icon-icons.com_69146.ico"))
                    message_result_4.setWindowTitle('Готово')
                    message_result_4.setText('Результат: ' + str(round(riemann_triangle_s(r, a, b, c), 1)))
                    message_result_4.exec_()
                case 'до целого':
                    r = float(self.line_r_4.text())
                    a = float(self.line_a_4.text())
                    b = float(self.line_b_4.text())
                    c = float(self.line_c_4.text())
                    message_result_4 = QMessageBox()
                    message_result_4.setWindowIcon(
                        QIcon("Tick_Mark_icon-icons.com_69146.ico"))
                    message_result_4.setWindowTitle('Готово')
                    message_result_4.setText('Результат: ' + str(round(riemann_triangle_s(r, a, b, c))))
                    message_result_4.exec_()
                case _:
                    r = float(self.line_r_4.text())
                    a = float(self.line_a_4.text())
                    b = float(self.line_b_4.text())
                    c = float(self.line_c_4.text())
                    message_result_4 = QMessageBox()
                    message_result_4.setWindowIcon(
                        QIcon("Tick_Mark_icon-icons.com_69146.ico"))
                    message_result_4.setWindowTitle('Готово')
                    message_result_4.setText('Результат: ' + str(riemann_triangle_s(r, a, b, c)))
                    message_result_4.exec_()
        except:
            message_error_4 = QMessageBox()
            message_error_4.setWindowIcon(QIcon("crossregular_106296.ico"))
            message_error_4.setWindowTitle('Ошибка')
            message_error_4.setText('Не удалось расчитать величину')
            message_error_4.exec_()


class Window_5(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Определение площади гиперболического треугольника')
        self.resize(450, 400)
        self.setWindowIcon(QIcon("stroke_pyramid_geometry_triangle_icon_259998.ico"))

        label_win_5 = QLabel('Введите значения величин:')
        label_win_5.setFont(QFont('Arial', 10))
        label_r_win_5 = QLabel('R = ')
        label_a_win_5 = QLabel('α = ')
        label_b_win_5 = QLabel('β = ')
        label_c_win_5 = QLabel('γ = ')
        label_r_win_5.setFont(QFont('Arial', 12))
        label_a_win_5.setFont(QFont('Arial', 12))
        label_b_win_5.setFont(QFont('Arial', 12))
        label_c_win_5.setFont(QFont('Arial', 12))
        self.line_r_5 = QLineEdit()
        self.line_a_5 = QLineEdit()
        self.line_b_5 = QLineEdit()
        self.line_c_5 = QLineEdit()
        self.line_r_5.setFixedWidth(400)
        self.line_a_5.setFixedWidth(400)
        self.line_b_5.setFixedWidth(400)
        self.line_c_5.setFixedWidth(400)
        self.line_r_5.setPlaceholderText('Радиус сферы / полусферы (см)')
        self.line_a_5.setPlaceholderText('Угол 1 (в градусах)')
        self.line_b_5.setPlaceholderText('Угол 2 (в градусах)')
        self.line_c_5.setPlaceholderText('Угол 3 (в градусах)')
        self.ready_button_5 = QPushButton('Рассчитать')
        round_label_5 = QLabel('Округление:')
        self.round_choice_box_5 = QComboBox()
        self.round_choice_box_5.addItem('нет')
        self.round_choice_box_5.addItem('до сотых')
        self.round_choice_box_5.addItem('до десятых')
        self.round_choice_box_5.addItem('до целого')

        main_layout_5 = QVBoxLayout()
        layout_5_1 = QHBoxLayout()
        layout_5_2 = QHBoxLayout()
        layout_5_3 = QHBoxLayout()
        layout_5_4 = QHBoxLayout()
        layout_5_5 = QHBoxLayout()
        layout_5_1.addWidget(label_r_win_5, alignment=Qt.AlignRight)
        layout_5_1.addWidget(self.line_r_5, alignment=Qt.AlignLeft)
        layout_5_2.addWidget(label_a_win_5, alignment=Qt.AlignRight)
        layout_5_2.addWidget(self.line_a_5, alignment=Qt.AlignLeft)
        layout_5_3.addWidget(label_b_win_5, alignment=Qt.AlignRight)
        layout_5_3.addWidget(self.line_b_5, alignment=Qt.AlignLeft)
        layout_5_4.addWidget(label_c_win_5, alignment=Qt.AlignRight)
        layout_5_4.addWidget(self.line_c_5, alignment=Qt.AlignLeft)
        layout_5_5.addWidget(round_label_5, alignment=Qt.AlignRight)
        layout_5_5.addWidget(self.round_choice_box_5, alignment=Qt.AlignLeft)
        main_layout_5.addWidget(label_win_5, alignment=Qt.AlignCenter)
        main_layout_5.addLayout(layout_5_1)
        main_layout_5.addLayout(layout_5_2)
        main_layout_5.addLayout(layout_5_3)
        main_layout_5.addLayout(layout_5_4)
        main_layout_5.addLayout(layout_5_5)
        main_layout_5.addWidget(self.ready_button_5, alignment=Qt.AlignCenter)

        self.setLayout(main_layout_5)

        self.ready_button_5.clicked.connect(self.get_result_5)

    def get_result_5(self):
        def lobachevsky_triangle_s(r, a, b, c):
            return (r ** 2) * (a + b + c - math.pi)

        try:
            match self.round_choice_box_5.currentText():
                case 'до сотых':
                    r = float(self.line_r_5.text())
                    a = float(self.line_a_5.text())
                    b = float(self.line_b_5.text())
                    c = float(self.line_c_5.text())
                    message_result_5 = QMessageBox()
                    message_result_5.setWindowIcon(
                        QIcon("Tick_Mark_icon-icons.com_69146.ico"))
                    message_result_5.setWindowTitle('Готово')
                    message_result_5.setText('Результат: ' + str(round(lobachevsky_triangle_s(r, a, b, c), 2)))
                    message_result_5.exec_()
                case 'до десятых':
                    r = float(self.line_r_5.text())
                    a = float(self.line_a_5.text())
                    b = float(self.line_b_5.text())
                    c = float(self.line_c_5.text())
                    message_result_5 = QMessageBox()
                    message_result_5.setWindowIcon(
                        QIcon("Tick_Mark_icon-icons.com_69146.ico"))
                    message_result_5.setWindowTitle('Готово')
                    message_result_5.setText('Результат: ' + str(round(lobachevsky_triangle_s(r, a, b, c), 1)))
                    message_result_5.exec_()
                case 'до целого':
                    r = float(self.line_r_5.text())
                    a = float(self.line_a_5.text())
                    b = float(self.line_b_5.text())
                    c = float(self.line_c_5.text())
                    message_result_5 = QMessageBox()
                    message_result_5.setWindowIcon(
                        QIcon("Tick_Mark_icon-icons.com_69146.ico"))
                    message_result_5.setWindowTitle('Готово')
                    message_result_5.setText('Результат: ' + str(round(lobachevsky_triangle_s(r, a, b, c))))
                    message_result_5.exec_()
                case _:
                    r = float(self.line_r_5.text())
                    a = float(self.line_a_5.text())
                    b = float(self.line_b_5.text())
                    c = float(self.line_c_5.text())
                    message_result_5 = QMessageBox()
                    message_result_5.setWindowIcon(
                        QIcon("Tick_Mark_icon-icons.com_69146.ico"))
                    message_result_5.setWindowTitle('Готово')
                    message_result_5.setText('Результат: ' + str(lobachevsky_triangle_s(r, a, b, c)))
                    message_result_5.exec_()
        except:
            message_error_5 = QMessageBox()
            message_error_5.setWindowIcon(QIcon("crossregular_106296.ico"))
            message_error_5.setWindowTitle('Ошибка')
            message_error_5.setText('Не удалось расчитать величину')
            message_error_5.exec_()


class Window_6(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Определение объема сферического / гиперболического тетраэдра')
        self.resize(450, 400)
        self.setWindowIcon(QIcon("shape_geometry_geometric_d_pyramid_icon_149669.ico"))

        label_win_6 = QLabel('Введите значения величин:')
        label_win_6.setFont(QFont('Arial', 10))
        label_r_win_6 = QLabel('R = ')
        label_a_win_6 = QLabel('a = ')
        label_h_win_6 = QLabel('h = ')
        label_r_win_6.setFont(QFont('Arial', 12))
        label_a_win_6.setFont(QFont('Arial', 12))
        label_h_win_6.setFont(QFont('Arial', 12))
        self.line_r_6 = QLineEdit()
        self.line_a_6 = QLineEdit()
        self.line_h_6 = QLineEdit()
        self.line_r_6.setFixedWidth(400)
        self.line_a_6.setFixedWidth(400)
        self.line_h_6.setFixedWidth(400)
        self.line_r_6.setPlaceholderText('Радиус сферы (см)')
        self.line_a_6.setPlaceholderText('Ребро тетраэдра (см)')
        self.line_h_6.setPlaceholderText('Высота сегмента (см)')
        self.ready_button_6 = QPushButton('Рассчитать')
        round_label_6 = QLabel('Округление:')
        self.round_choice_box_6 = QComboBox()
        self.round_choice_box_6.addItem('нет')
        self.round_choice_box_6.addItem('до сотых')
        self.round_choice_box_6.addItem('до десятых')
        self.round_choice_box_6.addItem('до целого')

        main_layout_6 = QVBoxLayout()
        layout_6_1 = QHBoxLayout()
        layout_6_2 = QHBoxLayout()
        layout_6_3 = QHBoxLayout()
        layout_6_4 = QHBoxLayout()
        layout_6_1.addWidget(label_r_win_6, alignment=Qt.AlignRight)
        layout_6_1.addWidget(self.line_r_6, alignment=Qt.AlignLeft)
        layout_6_2.addWidget(label_a_win_6, alignment=Qt.AlignRight)
        layout_6_2.addWidget(self.line_a_6, alignment=Qt.AlignLeft)
        layout_6_3.addWidget(label_h_win_6, alignment=Qt.AlignRight)
        layout_6_3.addWidget(self.line_h_6, alignment=Qt.AlignLeft)
        layout_6_4.addWidget(round_label_6, alignment=Qt.AlignRight)
        layout_6_4.addWidget(self.round_choice_box_6, alignment=Qt.AlignLeft)
        main_layout_6.addWidget(label_win_6, alignment=Qt.AlignCenter)
        main_layout_6.addLayout(layout_6_1)
        main_layout_6.addLayout(layout_6_2)
        main_layout_6.addLayout(layout_6_3)
        main_layout_6.addLayout(layout_6_4)
        main_layout_6.addWidget(self.ready_button_6, alignment=Qt.AlignCenter)

        self.setLayout(main_layout_6)

        self.ready_button_6.clicked.connect(self.get_result_6)

    def get_result_6(self):
        def n_eucl_tetrahedron_v(r, a, h):
            return math.pi * (h ** 2) * (r - 1 / 3 * h) + ((a ** 3) * math.sqrt(2) / 3)

        try:
            match self.round_choice_box_6.currentText():
                case 'до сотых':
                    r = float(self.line_r_6.text())
                    a = float(self.line_a_6.text())
                    h = float(self.line_h_6.text())
                    message_result_6 = QMessageBox()
                    message_result_6.setWindowIcon(
                        QIcon("Tick_Mark_icon-icons.com_69146.ico"))
                    message_result_6.setWindowTitle('Готово')
                    message_result_6.setText('Результат: ' + str(round(n_eucl_tetrahedron_v(r, a, h), 2)))
                    message_result_6.exec_()
                case 'до десятых':
                    r = float(self.line_r_6.text())
                    a = float(self.line_a_6.text())
                    h = float(self.line_h_6.text())
                    message_result_6 = QMessageBox()
                    message_result_6.setWindowIcon(
                        QIcon("Tick_Mark_icon-icons.com_69146.ico"))
                    message_result_6.setWindowTitle('Готово')
                    message_result_6.setText('Результат: ' + str(round(n_eucl_tetrahedron_v(r, a, h), 1)))
                    message_result_6.exec_()
                case 'до целого':
                    r = float(self.line_r_6.text())
                    a = float(self.line_a_6.text())
                    h = float(self.line_h_6.text())
                    message_result_6 = QMessageBox()
                    message_result_6.setWindowIcon(
                        QIcon("Tick_Mark_icon-icons.com_69146.ico"))
                    message_result_6.setWindowTitle('Готово')
                    message_result_6.setText('Результат: ' + str(round(n_eucl_tetrahedron_v(r, a, h))))
                    message_result_6.exec_()
                case _:
                    r = float(self.line_r_6.text())
                    a = float(self.line_a_6.text())
                    h = float(self.line_h_6.text())
                    message_result_6 = QMessageBox()
                    message_result_6.setWindowIcon(
                        QIcon("Tick_Mark_icon-icons.com_69146.ico"))
                    message_result_6.setWindowTitle('Готово')
                    message_result_6.setText('Результат: ' + str(n_eucl_tetrahedron_v(r, a, h)))
                    message_result_6.exec_()
        except:
            message_error_6 = QMessageBox()
            message_error_6.setWindowIcon(QIcon("crossregular_106296.ico"))
            message_error_6.setWindowTitle('Ошибка')
            message_error_6.setText('Не удалось расчитать величину')
            message_error_6.exec_()


class Window_7(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Определение радиуса')
        self.resize(450, 400)
        self.setWindowIcon(QIcon("radius_outline_icon_139237.ico"))

        label_win_7 = QLabel('Определить радиус через:')
        self.button_choice_7_1 = QPushButton('кривизну сферы')
        self.button_choice_7_2 = QPushButton('периметр сферического треугольника')
        self.button_choice_7_3 = QPushButton('периметр гиперболического треугольника')
        self.button_choice_7_4 = QPushButton('площадь сферического треугольника')
        self.button_choice_7_5 = QPushButton('площадь гиперболического треугольника')
        self.button_choice_7_6 = QPushButton('объем неевклидова тетраэдра')

        label_win_7.setFont(QFont('Arial', 10, QFont.Bold))
        self.button_choice_7_1.setFont(QFont('Arial', 10))
        self.button_choice_7_2.setFont(QFont('Arial', 10))
        self.button_choice_7_3.setFont(QFont('Arial', 10))
        self.button_choice_7_4.setFont(QFont('Arial', 10))
        self.button_choice_7_5.setFont(QFont('Arial', 10))
        self.button_choice_7_6.setFont(QFont('Arial', 10))

        self.button_choice_7_1.setFixedWidth(300)
        self.button_choice_7_2.setFixedWidth(300)
        self.button_choice_7_3.setFixedWidth(300)
        self.button_choice_7_4.setFixedWidth(300)
        self.button_choice_7_5.setFixedWidth(300)
        self.button_choice_7_6.setFixedWidth(300)

        main_layout_7 = QVBoxLayout()
        main_layout_7.addWidget(label_win_7, alignment=Qt.AlignCenter)
        main_layout_7.addWidget(self.button_choice_7_1, alignment=Qt.AlignCenter)
        main_layout_7.addWidget(self.button_choice_7_2, alignment=Qt.AlignCenter)
        main_layout_7.addWidget(self.button_choice_7_3, alignment=Qt.AlignCenter)
        main_layout_7.addWidget(self.button_choice_7_4, alignment=Qt.AlignCenter)
        main_layout_7.addWidget(self.button_choice_7_5, alignment=Qt.AlignCenter)
        main_layout_7.addWidget(self.button_choice_7_6, alignment=Qt.AlignCenter)

        self.setLayout(main_layout_7)

        self.button_choice_7_1.clicked.connect(self.open_win_7_1)
        self.button_choice_7_2.clicked.connect(self.open_win_7_2)
        self.button_choice_7_3.clicked.connect(self.open_win_7_3)
        self.button_choice_7_4.clicked.connect(self.open_win_7_4)
        self.button_choice_7_5.clicked.connect(self.open_win_7_5)
        self.button_choice_7_6.clicked.connect(self.open_win_7_6)

    def open_win_7_1(self):
        self.win_7_1 = Window_7_1()
        self.win_7_1.show()

    def open_win_7_2(self):
        self.win_7_2 = Window_7_2()
        self.win_7_2.show()

    def open_win_7_3(self):
        self.win_7_3 = Window_7_3()
        self.win_7_3.show()

    def open_win_7_4(self):
        self.win_7_4 = Window_7_4()
        self.win_7_4.show()

    def open_win_7_5(self):
        self.win_7_5 = Window_7_5()
        self.win_7_5.show()

    def open_win_7_6(self):
        self.win_7_6 = Window_7_6()
        self.win_7_6.show()


class Window_7_1(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Определение радиуса сферы через кривизну сферы')
        self.resize(450, 400)
        self.setWindowIcon(QIcon("radius_outline_icon_139237.ico"))

        label_win_7_1 = QLabel('Введите значения величин:')
        label_win_7_1.setFont(QFont('Arial', 10))
        label_k_win_7_1 = QLabel('k = ')
        label_k_win_7_1.setFont(QFont('Arial', 12))
        self.line_k_7_1 = QLineEdit()
        self.line_k_7_1.setFixedWidth(400)
        self.line_k_7_1.setPlaceholderText('Кривизна сферы')
        self.ready_button_7_1 = QPushButton('Рассчитать')
        round_label_7_1 = QLabel('Округление:')
        self.round_choice_box_7_1 = QComboBox()
        self.round_choice_box_7_1.addItem('нет')
        self.round_choice_box_7_1.addItem('до сотых')
        self.round_choice_box_7_1.addItem('до десятых')
        self.round_choice_box_7_1.addItem('до целого')

        main_layout_7_1 = QVBoxLayout()
        layout_7_1_1 = QHBoxLayout()
        layout_7_1_2 = QHBoxLayout()
        layout_7_1_1.addWidget(label_k_win_7_1, alignment=Qt.AlignRight)
        layout_7_1_1.addWidget(self.line_k_7_1, alignment=Qt.AlignLeft)
        layout_7_1_2.addWidget(round_label_7_1, alignment=Qt.AlignRight)
        layout_7_1_2.addWidget(self.round_choice_box_7_1, alignment=Qt.AlignLeft)
        main_layout_7_1.addWidget(label_win_7_1, alignment=Qt.AlignCenter)
        main_layout_7_1.addLayout(layout_7_1_1)
        main_layout_7_1.addWidget(self.ready_button_7_1, alignment=Qt.AlignCenter)
        main_layout_7_1.addLayout(layout_7_1_2)

        self.setLayout(main_layout_7_1)

        self.ready_button_7_1.clicked.connect(self.get_result_7_1)

    def get_result_7_1(self):
        def r_from_curvature(k):
            return math.sqrt(1 / k)

        try:
            match self.round_choice_box_7_1.currentText():
                case 'до сотых':
                    k = float(self.line_k_7_1.text())
                    message_result_7_1 = QMessageBox()
                    message_result_7_1.setWindowIcon(
                        QIcon("Tick_Mark_icon-icons.com_69146.ico"))
                    message_result_7_1.setWindowTitle('Готово')
                    message_result_7_1.setText('Результат: ' + str(round(r_from_curvature(k), 2)))
                    message_result_7_1.exec_()
                case 'до десятых':
                    k = float(self.line_k_7_1.text())
                    message_result_7_1 = QMessageBox()
                    message_result_7_1.setWindowIcon(
                        QIcon("Tick_Mark_icon-icons.com_69146.ico"))
                    message_result_7_1.setWindowTitle('Готово')
                    message_result_7_1.setText('Результат: ' + str(round(r_from_curvature(k), 1)))
                    message_result_7_1.exec_()
                case 'до целого':
                    k = float(self.line_k_7_1.text())
                    message_result_7_1 = QMessageBox()
                    message_result_7_1.setWindowIcon(
                        QIcon("Tick_Mark_icon-icons.com_69146.ico"))
                    message_result_7_1.setWindowTitle('Готово')
                    message_result_7_1.setText('Результат: ' + str(round(r_from_curvature(k))))
                    message_result_7_1.exec_()
                case _:
                    k = float(self.line_k_7_1.text())
                    message_result_7_1 = QMessageBox()
                    message_result_7_1.setWindowIcon(
                        QIcon("Tick_Mark_icon-icons.com_69146.ico"))
                    message_result_7_1.setWindowTitle('Готово')
                    message_result_7_1.setText('Результат: ' + str(r_from_curvature(k)))
                    message_result_7_1.exec_()
        except:
            message_error_7_1 = QMessageBox()
            message_error_7_1.setWindowIcon(QIcon("crossregular_106296.ico"))
            message_error_7_1.setWindowTitle('Ошибка')
            message_error_7_1.setText('Не удалось расчитать величину')
            message_error_7_1.exec_()


class Window_7_2(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Определение радиуса плоскости через периметр сферического треугольника')
        self.resize(450, 400)
        self.setWindowIcon(QIcon("radius_outline_icon_139237.ico"))

        label_win_7_2 = QLabel('Введите значения величин:')
        label_win_7_2.setFont(QFont('Arial', 10))
        label_p_win_7_2 = QLabel('p = ')
        label_a_win_7_2 = QLabel('α = ')
        label_b_win_7_2 = QLabel('β = ')
        label_c_win_7_2 = QLabel('γ = ')
        label_p_win_7_2.setFont(QFont('Arial', 12))
        label_a_win_7_2.setFont(QFont('Arial', 12))
        label_b_win_7_2.setFont(QFont('Arial', 12))
        label_c_win_7_2.setFont(QFont('Arial', 12))
        self.line_p_7_2 = QLineEdit()
        self.line_a_7_2 = QLineEdit()
        self.line_b_7_2 = QLineEdit()
        self.line_c_7_2 = QLineEdit()
        self.line_p_7_2.setFixedWidth(400)
        self.line_a_7_2.setFixedWidth(400)
        self.line_b_7_2.setFixedWidth(400)
        self.line_c_7_2.setFixedWidth(400)
        self.line_p_7_2.setPlaceholderText('Периметр сферического треугольника')
        self.line_a_7_2.setPlaceholderText('Угол 1 (в градусах)')
        self.line_b_7_2.setPlaceholderText('Угол 2 (в градусах)')
        self.line_c_7_2.setPlaceholderText('Угол 3 (в градусах)')
        self.ready_button_7_2 = QPushButton('Рассчитать')
        round_label_7_2 = QLabel('Округление:')
        self.round_choice_box_7_2 = QComboBox()
        self.round_choice_box_7_2.addItem('нет')
        self.round_choice_box_7_2.addItem('до сотых')
        self.round_choice_box_7_2.addItem('до десятых')
        self.round_choice_box_7_2.addItem('до целого')

        main_layout_7_2 = QVBoxLayout()
        layout_7_2_1 = QHBoxLayout()
        layout_7_2_2 = QHBoxLayout()
        layout_7_2_3 = QHBoxLayout()
        layout_7_2_4 = QHBoxLayout()
        layout_7_2_5 = QHBoxLayout()
        layout_7_2_1.addWidget(label_p_win_7_2, alignment=Qt.AlignRight)
        layout_7_2_1.addWidget(self.line_p_7_2, alignment=Qt.AlignLeft)
        layout_7_2_2.addWidget(label_a_win_7_2, alignment=Qt.AlignRight)
        layout_7_2_2.addWidget(self.line_a_7_2, alignment=Qt.AlignLeft)
        layout_7_2_3.addWidget(label_b_win_7_2, alignment=Qt.AlignRight)
        layout_7_2_3.addWidget(self.line_b_7_2, alignment=Qt.AlignLeft)
        layout_7_2_4.addWidget(label_c_win_7_2, alignment=Qt.AlignRight)
        layout_7_2_4.addWidget(self.line_c_7_2, alignment=Qt.AlignLeft)
        layout_7_2_5.addWidget(round_label_7_2, alignment=Qt.AlignRight)
        layout_7_2_5.addWidget(self.round_choice_box_7_2, alignment=Qt.AlignLeft)
        main_layout_7_2.addWidget(label_win_7_2, alignment=Qt.AlignCenter)
        main_layout_7_2.addLayout(layout_7_2_1)
        main_layout_7_2.addLayout(layout_7_2_2)
        main_layout_7_2.addLayout(layout_7_2_3)
        main_layout_7_2.addLayout(layout_7_2_4)
        main_layout_7_2.addLayout(layout_7_2_5)
        main_layout_7_2.addWidget(self.ready_button_7_2, alignment=Qt.AlignCenter)

        self.setLayout(main_layout_7_2)

        self.ready_button_7_2.clicked.connect(self.get_result_7_2)

    def get_result_7_2(self):
        def r_from_r_t_p(p, a, b, c):
            return 2 * p / (a + b + c)

        try:
            match self.round_choice_box_7_2.currentText():
                case 'до сотых':
                    p = float(self.line_p_7_2.text())
                    a = float(self.line_a_7_2.text())
                    b = float(self.line_b_7_2.text())
                    c = float(self.line_c_7_2.text())
                    message_result_7_2 = QMessageBox()
                    message_result_7_2.setWindowIcon(
                        QIcon("Tick_Mark_icon-icons.com_69146.ico"))
                    message_result_7_2.setWindowTitle('Готово')
                    message_result_7_2.setText('Результат: ' + str(round(r_from_r_t_p(p, a, b, c), 2)))
                    message_result_7_2.exec_()
                case 'до десятых':
                    p = float(self.line_p_7_2.text())
                    a = float(self.line_a_7_2.text())
                    b = float(self.line_b_7_2.text())
                    c = float(self.line_c_7_2.text())
                    message_result_7_2 = QMessageBox()
                    message_result_7_2.setWindowIcon(
                        QIcon("Tick_Mark_icon-icons.com_69146.ico"))
                    message_result_7_2.setWindowTitle('Готово')
                    message_result_7_2.setText('Результат: ' + str(round(r_from_r_t_p(p, a, b, c), 1)))
                    message_result_7_2.exec_()
                case 'до целого':
                    p = float(self.line_p_7_2.text())
                    a = float(self.line_a_7_2.text())
                    b = float(self.line_b_7_2.text())
                    c = float(self.line_c_7_2.text())
                    message_result_7_2 = QMessageBox()
                    message_result_7_2.setWindowIcon(
                        QIcon("Tick_Mark_icon-icons.com_69146.ico"))
                    message_result_7_2.setWindowTitle('Готово')
                    message_result_7_2.setText('Результат: ' + str(round(r_from_r_t_p(p, a, b, c))))
                    message_result_7_2.exec_()
                case _:
                    p = float(self.line_p_7_2.text())
                    a = float(self.line_a_7_2.text())
                    b = float(self.line_b_7_2.text())
                    c = float(self.line_c_7_2.text())
                    message_result_7_2 = QMessageBox()
                    message_result_7_2.setWindowIcon(
                        QIcon("Tick_Mark_icon-icons.com_69146.ico"))
                    message_result_7_2.setWindowTitle('Готово')
                    message_result_7_2.setText('Результат: ' + str(r_from_r_t_p(p, a, b, c)))
                    message_result_7_2.exec_()
        except:
            message_error_7_2 = QMessageBox()
            message_error_7_2.setWindowIcon(QIcon("crossregular_106296.ico"))
            message_error_7_2.setWindowTitle('Ошибка')
            message_error_7_2.setText('Не удалось расчитать величину')
            message_error_7_2.exec_()


class Window_7_3(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Определение радиуса плоскости через периметр гиперболического треугольника')
        self.resize(450, 400)
        self.setWindowIcon(QIcon("radius_outline_icon_139237.ico"))

        label_win_7_3 = QLabel('Введите значения величин:')
        label_win_7_3.setFont(QFont('Arial', 10))
        label_p_win_7_3 = QLabel('p = ')
        label_a_win_7_3 = QLabel('α = ')
        label_b_win_7_3 = QLabel('β = ')
        label_c_win_7_3 = QLabel('γ = ')
        label_p_win_7_3.setFont(QFont('Arial', 12))
        label_a_win_7_3.setFont(QFont('Arial', 12))
        label_b_win_7_3.setFont(QFont('Arial', 12))
        label_c_win_7_3.setFont(QFont('Arial', 12))
        self.line_p_7_3 = QLineEdit()
        self.line_a_7_3 = QLineEdit()
        self.line_b_7_3 = QLineEdit()
        self.line_c_7_3 = QLineEdit()
        self.line_p_7_3.setFixedWidth(400)
        self.line_a_7_3.setFixedWidth(400)
        self.line_b_7_3.setFixedWidth(400)
        self.line_c_7_3.setFixedWidth(400)
        self.line_p_7_3.setPlaceholderText('Периметр гиперболического треугольника')
        self.line_a_7_3.setPlaceholderText('Угол 1 (в градусах)')
        self.line_b_7_3.setPlaceholderText('Угол 2 (в градусах)')
        self.line_c_7_3.setPlaceholderText('Угол 3 (в градусах)')
        self.ready_button_7_3 = QPushButton('Рассчитать')
        round_label_7_3 = QLabel('Округление:')
        self.round_choice_box_7_3 = QComboBox()
        self.round_choice_box_7_3.addItem('нет')
        self.round_choice_box_7_3.addItem('до сотых')
        self.round_choice_box_7_3.addItem('до десятых')
        self.round_choice_box_7_3.addItem('до целого')

        main_layout_7_3 = QVBoxLayout()
        layout_7_3_1 = QHBoxLayout()
        layout_7_3_2 = QHBoxLayout()
        layout_7_3_3 = QHBoxLayout()
        layout_7_3_4 = QHBoxLayout()
        layout_7_3_5 = QHBoxLayout()
        layout_7_3_1.addWidget(label_p_win_7_3, alignment=Qt.AlignRight)
        layout_7_3_1.addWidget(self.line_p_7_3, alignment=Qt.AlignLeft)
        layout_7_3_2.addWidget(label_a_win_7_3, alignment=Qt.AlignRight)
        layout_7_3_2.addWidget(self.line_a_7_3, alignment=Qt.AlignLeft)
        layout_7_3_3.addWidget(label_b_win_7_3, alignment=Qt.AlignRight)
        layout_7_3_3.addWidget(self.line_b_7_3, alignment=Qt.AlignLeft)
        layout_7_3_4.addWidget(label_c_win_7_3, alignment=Qt.AlignRight)
        layout_7_3_4.addWidget(self.line_c_7_3, alignment=Qt.AlignLeft)
        layout_7_3_5.addWidget(round_label_7_3, alignment=Qt.AlignRight)
        layout_7_3_5.addWidget(self.round_choice_box_7_3, alignment=Qt.AlignLeft)
        main_layout_7_3.addWidget(label_win_7_3, alignment=Qt.AlignCenter)
        main_layout_7_3.addLayout(layout_7_3_1)
        main_layout_7_3.addLayout(layout_7_3_2)
        main_layout_7_3.addLayout(layout_7_3_3)
        main_layout_7_3.addLayout(layout_7_3_4)
        main_layout_7_3.addLayout(layout_7_3_5)
        main_layout_7_3.addWidget(self.ready_button_7_3, alignment=Qt.AlignCenter)

        self.setLayout(main_layout_7_3)

        self.ready_button_7_3.clicked.connect(self.get_result_7_3)

    def get_result_7_3(self):
        def r_from_l_t_p(p, a, b, c):
            return (p * (a + b + c)) / (4 * math.pi ** 2)

        try:
            match self.round_choice_box_7_3.currentText():
                case 'до сотых':
                    p = float(self.line_p_7_3.text())
                    a = float(self.line_a_7_3.text())
                    b = float(self.line_b_7_3.text())
                    c = float(self.line_c_7_3.text())
                    message_result_7_3 = QMessageBox()
                    message_result_7_3.setWindowIcon(
                        QIcon("Tick_Mark_icon-icons.com_69146.ico"))
                    message_result_7_3.setWindowTitle('Готово')
                    message_result_7_3.setText('Результат: ' + str(round(r_from_l_t_p(p, a, b, c), 2)))
                    message_result_7_3.exec_()
                case 'до десятых':
                    p = float(self.line_p_7_3.text())
                    a = float(self.line_a_7_3.text())
                    b = float(self.line_b_7_3.text())
                    c = float(self.line_c_7_3.text())
                    message_result_7_3 = QMessageBox()
                    message_result_7_3.setWindowIcon(
                        QIcon("Tick_Mark_icon-icons.com_69146.ico"))
                    message_result_7_3.setWindowTitle('Готово')
                    message_result_7_3.setText('Результат: ' + str(round(r_from_l_t_p(p, a, b, c), 1)))
                    message_result_7_3.exec_()
                case 'до целого':
                    p = float(self.line_p_7_3.text())
                    a = float(self.line_a_7_3.text())
                    b = float(self.line_b_7_3.text())
                    c = float(self.line_c_7_3.text())
                    message_result_7_3 = QMessageBox()
                    message_result_7_3.setWindowIcon(
                        QIcon("Tick_Mark_icon-icons.com_69146.ico"))
                    message_result_7_3.setWindowTitle('Готово')
                    message_result_7_3.setText('Результат: ' + str(round(r_from_l_t_p(p, a, b, c))))
                    message_result_7_3.exec_()
                case _:
                    p = float(self.line_p_7_3.text())
                    a = float(self.line_a_7_3.text())
                    b = float(self.line_b_7_3.text())
                    c = float(self.line_c_7_3.text())
                    message_result_7_3 = QMessageBox()
                    message_result_7_3.setWindowIcon(
                        QIcon("Tick_Mark_icon-icons.com_69146.ico"))
                    message_result_7_3.setWindowTitle('Готово')
                    message_result_7_3.setText('Результат: ' + str(r_from_l_t_p(p, a, b, c)))
                    message_result_7_3.exec_()
        except:
            message_error_7_3 = QMessageBox()
            message_error_7_3.setWindowIcon(QIcon("crossregular_106296.ico"))
            message_error_7_3.setWindowTitle('Ошибка')
            message_error_7_3.setText('Не удалось расчитать величину')
            message_error_7_3.exec_()


class Window_7_4(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Определение радиуса сферы через площадь сферического треугольника')
        self.resize(450, 400)
        self.setWindowIcon(QIcon("radius_outline_icon_139237.ico"))

        label_win_7_4 = QLabel('Введите значения величин:')
        label_win_7_4.setFont(QFont('Arial', 10))
        label_s_win_7_4 = QLabel('s = ')
        label_a_win_7_4 = QLabel('α = ')
        label_b_win_7_4 = QLabel('β = ')
        label_c_win_7_4 = QLabel('γ = ')
        label_s_win_7_4.setFont(QFont('Arial', 12))
        label_a_win_7_4.setFont(QFont('Arial', 12))
        label_b_win_7_4.setFont(QFont('Arial', 12))
        label_c_win_7_4.setFont(QFont('Arial', 12))
        self.line_s_7_4 = QLineEdit()
        self.line_a_7_4 = QLineEdit()
        self.line_b_7_4 = QLineEdit()
        self.line_c_7_4 = QLineEdit()
        self.line_s_7_4.setFixedWidth(400)
        self.line_a_7_4.setFixedWidth(400)
        self.line_b_7_4.setFixedWidth(400)
        self.line_c_7_4.setFixedWidth(400)
        self.line_s_7_4.setPlaceholderText('Площадь сферического треугольника')
        self.line_a_7_4.setPlaceholderText('Угол 1 (в градусах)')
        self.line_b_7_4.setPlaceholderText('Угол 2 (в градусах)')
        self.line_c_7_4.setPlaceholderText('Угол 3 (в градусах)')
        self.ready_button_7_4 = QPushButton('Рассчитать')
        round_label_7_4 = QLabel('Округление:')
        self.round_choice_box_7_4 = QComboBox()
        self.round_choice_box_7_4.addItem('нет')
        self.round_choice_box_7_4.addItem('до сотых')
        self.round_choice_box_7_4.addItem('до десятых')
        self.round_choice_box_7_4.addItem('до целого')

        main_layout_7_4 = QVBoxLayout()
        layout_7_4_1 = QHBoxLayout()
        layout_7_4_2 = QHBoxLayout()
        layout_7_4_3 = QHBoxLayout()
        layout_7_4_4 = QHBoxLayout()
        layout_7_4_5 = QHBoxLayout()
        layout_7_4_1.addWidget(label_s_win_7_4, alignment=Qt.AlignRight)
        layout_7_4_1.addWidget(self.line_s_7_4, alignment=Qt.AlignLeft)
        layout_7_4_2.addWidget(label_a_win_7_4, alignment=Qt.AlignRight)
        layout_7_4_2.addWidget(self.line_a_7_4, alignment=Qt.AlignLeft)
        layout_7_4_3.addWidget(label_b_win_7_4, alignment=Qt.AlignRight)
        layout_7_4_3.addWidget(self.line_b_7_4, alignment=Qt.AlignLeft)
        layout_7_4_4.addWidget(label_c_win_7_4, alignment=Qt.AlignRight)
        layout_7_4_4.addWidget(self.line_c_7_4, alignment=Qt.AlignLeft)
        layout_7_4_5.addWidget(round_label_7_4, alignment=Qt.AlignRight)
        layout_7_4_5.addWidget(self.round_choice_box_7_4, alignment=Qt.AlignLeft)
        main_layout_7_4.addWidget(label_win_7_4, alignment=Qt.AlignCenter)
        main_layout_7_4.addLayout(layout_7_4_1)
        main_layout_7_4.addLayout(layout_7_4_2)
        main_layout_7_4.addLayout(layout_7_4_3)
        main_layout_7_4.addLayout(layout_7_4_4)
        main_layout_7_4.addLayout(layout_7_4_5)
        main_layout_7_4.addWidget(self.ready_button_7_4, alignment=Qt.AlignCenter)

        self.setLayout(main_layout_7_4)

        self.ready_button_7_4.clicked.connect(self.get_result_7_4)

    def get_result_7_4(self):
        def r_from_r_t_s(s, a, b, c):
            return math.sqrt(s / (math.pi - a - b - c))

        try:
            match self.round_choice_box_7_4.currentText():
                case 'до сотых':
                    s = float(self.line_s_7_4.text())
                    a = float(self.line_a_7_4.text())
                    b = float(self.line_b_7_4.text())
                    c = float(self.line_c_7_4.text())
                    message_result_7_4 = QMessageBox()
                    message_result_7_4.setWindowIcon(
                        QIcon("Tick_Mark_icon-icons.com_69146.ico"))
                    message_result_7_4.setWindowTitle('Готово')
                    message_result_7_4.setText('Результат: ' + str(round(r_from_r_t_s(s, a, b, c), 2)))
                    message_result_7_4.exec_()
                case 'до десятых':
                    s = float(self.line_s_7_4.text())
                    a = float(self.line_a_7_4.text())
                    b = float(self.line_b_7_4.text())
                    c = float(self.line_c_7_4.text())
                    message_result_7_4 = QMessageBox()
                    message_result_7_4.setWindowIcon(
                        QIcon("Tick_Mark_icon-icons.com_69146.ico"))
                    message_result_7_4.setWindowTitle('Готово')
                    message_result_7_4.setText('Результат: ' + str(round(r_from_r_t_s(s, a, b, c), 1)))
                    message_result_7_4.exec_()
                case 'до целого':
                    s = float(self.line_s_7_4.text())
                    a = float(self.line_a_7_4.text())
                    b = float(self.line_b_7_4.text())
                    c = float(self.line_c_7_4.text())
                    message_result_7_4 = QMessageBox()
                    message_result_7_4.setWindowIcon(
                        QIcon("Tick_Mark_icon-icons.com_69146.ico"))
                    message_result_7_4.setWindowTitle('Готово')
                    message_result_7_4.setText('Результат: ' + str(round(r_from_r_t_s(s, a, b, c))))
                    message_result_7_4.exec_()
                case _:
                    s = float(self.line_s_7_4.text())
                    a = float(self.line_a_7_4.text())
                    b = float(self.line_b_7_4.text())
                    c = float(self.line_c_7_4.text())
                    message_result_7_4 = QMessageBox()
                    message_result_7_4.setWindowIcon(
                        QIcon("Tick_Mark_icon-icons.com_69146.ico"))
                    message_result_7_4.setWindowTitle('Готово')
                    message_result_7_4.setText('Результат: ' + str(r_from_r_t_s(s, a, b, c)))
                    message_result_7_4.exec_()
        except:
            message_error_7_4 = QMessageBox()
            message_error_7_4.setWindowIcon(QIcon("crossregular_106296.ico"))
            message_error_7_4.setWindowTitle('Ошибка')
            message_error_7_4.setText('Не удалось расчитать величину')
            message_error_7_4.exec_()


class Window_7_5(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Определение радиуса сферы через площадь гиперболического треугольника')
        self.resize(450, 400)
        self.setWindowIcon(QIcon("radius_outline_icon_139237.ico"))

        label_win_7_5 = QLabel('Введите значения величин:')
        label_win_7_5.setFont(QFont('Arial', 10))
        label_s_win_7_5 = QLabel('s = ')
        label_a_win_7_5 = QLabel('α = ')
        label_b_win_7_5 = QLabel('β = ')
        label_c_win_7_5 = QLabel('γ = ')
        label_s_win_7_5.setFont(QFont('Arial', 12))
        label_a_win_7_5.setFont(QFont('Arial', 12))
        label_b_win_7_5.setFont(QFont('Arial', 12))
        label_c_win_7_5.setFont(QFont('Arial', 12))
        self.line_s_7_5 = QLineEdit()
        self.line_a_7_5 = QLineEdit()
        self.line_b_7_5 = QLineEdit()
        self.line_c_7_5 = QLineEdit()
        self.line_s_7_5.setFixedWidth(400)
        self.line_a_7_5.setFixedWidth(400)
        self.line_b_7_5.setFixedWidth(400)
        self.line_c_7_5.setFixedWidth(400)
        self.line_s_7_5.setPlaceholderText('Площадь гиперболического треугольника')
        self.line_a_7_5.setPlaceholderText('Угол 1 (в градусах)')
        self.line_b_7_5.setPlaceholderText('Угол 2 (в градусах)')
        self.line_c_7_5.setPlaceholderText('Угол 3 (в градусах)')
        self.ready_button_7_5 = QPushButton('Рассчитать')
        round_label_7_5 = QLabel('Округление:')
        self.round_choice_box_7_5 = QComboBox()
        self.round_choice_box_7_5.addItem('нет')
        self.round_choice_box_7_5.addItem('до сотых')
        self.round_choice_box_7_5.addItem('до десятых')
        self.round_choice_box_7_5.addItem('до целого')

        main_layout_7_5 = QVBoxLayout()
        layout_7_5_1 = QHBoxLayout()
        layout_7_5_2 = QHBoxLayout()
        layout_7_5_3 = QHBoxLayout()
        layout_7_5_4 = QHBoxLayout()
        layout_7_5_5 = QHBoxLayout()
        layout_7_5_1.addWidget(label_s_win_7_5, alignment=Qt.AlignRight)
        layout_7_5_1.addWidget(self.line_s_7_5, alignment=Qt.AlignLeft)
        layout_7_5_2.addWidget(label_a_win_7_5, alignment=Qt.AlignRight)
        layout_7_5_2.addWidget(self.line_a_7_5, alignment=Qt.AlignLeft)
        layout_7_5_3.addWidget(label_b_win_7_5, alignment=Qt.AlignRight)
        layout_7_5_3.addWidget(self.line_b_7_5, alignment=Qt.AlignLeft)
        layout_7_5_4.addWidget(label_c_win_7_5, alignment=Qt.AlignRight)
        layout_7_5_4.addWidget(self.line_c_7_5, alignment=Qt.AlignLeft)
        layout_7_5_5.addWidget(round_label_7_5, alignment=Qt.AlignRight)
        layout_7_5_5.addWidget(self.round_choice_box_7_5, alignment=Qt.AlignLeft)
        main_layout_7_5.addWidget(label_win_7_5, alignment=Qt.AlignCenter)
        main_layout_7_5.addLayout(layout_7_5_1)
        main_layout_7_5.addLayout(layout_7_5_2)
        main_layout_7_5.addLayout(layout_7_5_3)
        main_layout_7_5.addLayout(layout_7_5_4)
        main_layout_7_5.addLayout(layout_7_5_5)
        main_layout_7_5.addWidget(self.ready_button_7_5, alignment=Qt.AlignCenter)

        self.setLayout(main_layout_7_5)

        self.ready_button_7_5.clicked.connect(self.get_result_7_5)

    def get_result_7_5(self):
        def r_from_l_t_s(s, a, b, c):
            return math.sqrt(s / (a + b + c - math.pi))

        try:
            match self.round_choice_box_7_5.currentText():
                case 'до сотых':
                    s = float(self.line_s_7_5.text())
                    a = float(self.line_a_7_5.text())
                    b = float(self.line_b_7_5.text())
                    c = float(self.line_c_7_5.text())
                    message_result_7_5 = QMessageBox()
                    message_result_7_5.setWindowIcon(
                        QIcon("Tick_Mark_icon-icons.com_69146.ico"))
                    message_result_7_5.setWindowTitle('Готово')
                    message_result_7_5.setText('Результат: ' + str(round(r_from_l_t_s(s, a, b, c), 2)))
                    message_result_7_5.exec_()
                case 'до десятых':
                    s = float(self.line_s_7_5.text())
                    a = float(self.line_a_7_5.text())
                    b = float(self.line_b_7_5.text())
                    c = float(self.line_c_7_5.text())
                    message_result_7_5 = QMessageBox()
                    message_result_7_5.setWindowIcon(
                        QIcon("Tick_Mark_icon-icons.com_69146.ico"))
                    message_result_7_5.setWindowTitle('Готово')
                    message_result_7_5.setText('Результат: ' + str(round(r_from_l_t_s(s, a, b, c), 1)))
                    message_result_7_5.exec_()
                case 'до целого':
                    s = float(self.line_s_7_5.text())
                    a = float(self.line_a_7_5.text())
                    b = float(self.line_b_7_5.text())
                    c = float(self.line_c_7_5.text())
                    message_result_7_5 = QMessageBox()
                    message_result_7_5.setWindowIcon(
                        QIcon("Tick_Mark_icon-icons.com_69146.ico"))
                    message_result_7_5.setWindowTitle('Готово')
                    message_result_7_5.setText('Результат: ' + str(round(r_from_l_t_s(s, a, b, c))))
                    message_result_7_5.exec_()
                case _:
                    s = float(self.line_s_7_5.text())
                    a = float(self.line_a_7_5.text())
                    b = float(self.line_b_7_5.text())
                    c = float(self.line_c_7_5.text())
                    message_result_7_5 = QMessageBox()
                    message_result_7_5.setWindowIcon(
                        QIcon("Tick_Mark_icon-icons.com_69146.ico"))
                    message_result_7_5.setWindowTitle('Готово')
                    message_result_7_5.setText('Результат: ' + str(r_from_l_t_s(s, a, b, c)))
                    message_result_7_5.exec_()
        except:
            message_error_7_5 = QMessageBox()
            message_error_7_5.setWindowIcon(QIcon("crossregular_106296.ico"))
            message_error_7_5.setWindowTitle('Ошибка')
            message_error_7_5.setText('Не удалось расчитать величину')
            message_error_7_5.exec_()


class Window_7_6(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Определение радиуса сферы через объем неевклидова тетраэдра')
        self.resize(450, 400)
        self.setWindowIcon(QIcon("radius_outline_icon_139237.ico"))

        label_win_7_6 = QLabel('Введите значения величин:')
        label_win_7_6.setFont(QFont('Arial', 10))
        label_v_win_7_6 = QLabel('v = ')
        label_a_win_7_6 = QLabel('a = ')
        label_h_win_7_6 = QLabel('h = ')
        label_v_win_7_6.setFont(QFont('Arial', 12))
        label_a_win_7_6.setFont(QFont('Arial', 12))
        label_h_win_7_6.setFont(QFont('Arial', 12))
        self.line_v_7_6 = QLineEdit()
        self.line_a_7_6 = QLineEdit()
        self.line_h_7_6 = QLineEdit()
        self.line_v_7_6.setFixedWidth(400)
        self.line_a_7_6.setFixedWidth(400)
        self.line_h_7_6.setFixedWidth(400)
        self.line_v_7_6.setPlaceholderText('Объем неевклидова тетраэдра')
        self.line_a_7_6.setPlaceholderText('Ребро тетраэдра (см)')
        self.line_h_7_6.setPlaceholderText('Высота сегмента (см)')
        self.ready_button_7_6 = QPushButton('Рассчитать')
        round_label_7_6 = QLabel('Округление:')
        self.round_choice_box_7_6 = QComboBox()
        self.round_choice_box_7_6.addItem('нет')
        self.round_choice_box_7_6.addItem('до сотых')
        self.round_choice_box_7_6.addItem('до десятых')
        self.round_choice_box_7_6.addItem('до целого')

        main_layout_7_6 = QVBoxLayout()
        layout_7_6_1 = QHBoxLayout()
        layout_7_6_2 = QHBoxLayout()
        layout_7_6_3 = QHBoxLayout()
        layout_7_6_4 = QHBoxLayout()
        layout_7_6_1.addWidget(label_v_win_7_6, alignment=Qt.AlignRight)
        layout_7_6_1.addWidget(self.line_v_7_6, alignment=Qt.AlignLeft)
        layout_7_6_2.addWidget(label_a_win_7_6, alignment=Qt.AlignRight)
        layout_7_6_2.addWidget(self.line_a_7_6, alignment=Qt.AlignLeft)
        layout_7_6_3.addWidget(label_h_win_7_6, alignment=Qt.AlignRight)
        layout_7_6_3.addWidget(self.line_h_7_6, alignment=Qt.AlignLeft)
        layout_7_6_4.addWidget(round_label_7_6, alignment=Qt.AlignRight)
        layout_7_6_4.addWidget(self.round_choice_box_7_6, alignment=Qt.AlignLeft)
        main_layout_7_6.addWidget(label_win_7_6, alignment=Qt.AlignCenter)
        main_layout_7_6.addLayout(layout_7_6_1)
        main_layout_7_6.addLayout(layout_7_6_2)
        main_layout_7_6.addLayout(layout_7_6_3)
        main_layout_7_6.addLayout(layout_7_6_4)
        main_layout_7_6.addWidget(self.ready_button_7_6, alignment=Qt.AlignCenter)

        self.setLayout(main_layout_7_6)

        self.ready_button_7_6.clicked.connect(self.get_result_7_6)

    def get_result_7_6(self):
        def r_from_v(v, a, h):
            return -((-math.pi * h ** 3 + math.sqrt(2) * a ** 3 - 3 * v) / (3 * math.pi * h ** 2))

        try:
            match self.round_choice_box_7_6.currentText():
                case 'до сотых':
                    v = float(self.line_v_7_6.text())
                    a = float(self.line_a_7_6.text())
                    h = float(self.line_h_7_6.text())
                    message_result_7_6 = QMessageBox()
                    message_result_7_6.setWindowIcon(
                        QIcon("Tick_Mark_icon-icons.com_69146.ico"))
                    message_result_7_6.setWindowTitle('Готово')
                    message_result_7_6.setText('Результат: ' + str(round(r_from_v(v, a, h), 2)))
                    message_result_7_6.exec_()
                case 'до десятых':
                    v = float(self.line_v_7_6.text())
                    a = float(self.line_a_7_6.text())
                    h = float(self.line_h_7_6.text())
                    message_result_7_6 = QMessageBox()
                    message_result_7_6.setWindowIcon(
                        QIcon("Tick_Mark_icon-icons.com_69146.ico"))
                    message_result_7_6.setWindowTitle('Готово')
                    message_result_7_6.setText('Результат: ' + str(round(r_from_v(v, a, h), 1)))
                    message_result_7_6.exec_()
                case 'до целого':
                    v = float(self.line_v_7_6.text())
                    a = float(self.line_a_7_6.text())
                    h = float(self.line_h_7_6.text())
                    message_result_7_6 = QMessageBox()
                    message_result_7_6.setWindowIcon(
                        QIcon("Tick_Mark_icon-icons.com_69146.ico"))
                    message_result_7_6.setWindowTitle('Готово')
                    message_result_7_6.setText('Результат: ' + str(round(r_from_v(v, a, h))))
                    message_result_7_6.exec_()
                case _:
                    v = float(self.line_v_7_6.text())
                    a = float(self.line_a_7_6.text())
                    h = float(self.line_h_7_6.text())
                    message_result_7_6 = QMessageBox()
                    message_result_7_6.setWindowIcon(
                        QIcon("Tick_Mark_icon-icons.com_69146.ico"))
                    message_result_7_6.setWindowTitle('Готово')
                    message_result_7_6.setText('Результат: ' + str(r_from_v(v, a, h)))
                    message_result_7_6.exec_()
        except:
            message_error_7_6 = QMessageBox()
            message_error_7_6.setWindowIcon(QIcon("crossregular_106296.ico"))
            message_error_7_6.setWindowTitle('Ошибка')
            message_error_7_6.setText('Не удалось расчитать величину')
            message_error_7_6.exec_()


class Window_8(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Определение суммы сторон треугольника')
        self.resize(450, 400)
        self.setWindowIcon(QIcon("angle_acute_icon_138939.ico"))

        label_win_8 = QLabel('Определить радиус через:')
        self.button_choice_8_1 = QPushButton('кривизну сферы')
        self.button_choice_8_2 = QPushButton('периметр сферического треугольника')
        self.button_choice_8_3 = QPushButton('периметр гиперболического треугольника')
        self.button_choice_8_4 = QPushButton('площадь сферического треугольника')

        label_win_8.setFont(QFont('Arial', 10, QFont.Bold))
        self.button_choice_8_1.setFont(QFont('Arial', 10))
        self.button_choice_8_2.setFont(QFont('Arial', 10))
        self.button_choice_8_3.setFont(QFont('Arial', 10))
        self.button_choice_8_4.setFont(QFont('Arial', 10))

        self.button_choice_8_1.setFixedWidth(300)
        self.button_choice_8_2.setFixedWidth(300)
        self.button_choice_8_3.setFixedWidth(300)
        self.button_choice_8_4.setFixedWidth(300)

        main_layout_8 = QVBoxLayout()
        main_layout_8.addWidget(label_win_8, alignment=Qt.AlignCenter)
        main_layout_8.addWidget(self.button_choice_8_1, alignment=Qt.AlignCenter)
        main_layout_8.addWidget(self.button_choice_8_2, alignment=Qt.AlignCenter)
        main_layout_8.addWidget(self.button_choice_8_3, alignment=Qt.AlignCenter)
        main_layout_8.addWidget(self.button_choice_8_4, alignment=Qt.AlignCenter)

        self.setLayout(main_layout_8)

        self.button_choice_8_1.clicked.connect(self.open_win_8_1)
        self.button_choice_8_2.clicked.connect(self.open_win_8_2)
        self.button_choice_8_3.clicked.connect(self.open_win_8_3)
        self.button_choice_8_4.clicked.connect(self.open_win_8_4)

    def open_win_8_1(self):
        self.win_8_1 = Window_8_1()
        self.win_8_1.show()

    def open_win_8_2(self):
        self.win_8_2 = Window_8_2()
        self.win_8_2.show()

    def open_win_8_3(self):
        self.win_8_3 = Window_8_3()
        self.win_8_3.show()

    def open_win_8_4(self):
        self.win_8_4 = Window_8_4()
        self.win_8_4.show()


class Window_8_1(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Определение суммы углов сферического треугольника через его периметр')
        self.resize(450, 400)
        self.setWindowIcon(QIcon("angle_acute_icon_138939.ico"))

        label_win_8_1 = QLabel('Введите значения величин:')
        label_win_8_1.setFont(QFont('Arial', 10))
        label_p_win_8_1 = QLabel('p = ')
        label_r_win_8_1 = QLabel('r = ')
        label_p_win_8_1.setFont(QFont('Arial', 12))
        label_r_win_8_1.setFont(QFont('Arial', 12))
        self.line_p_8_1 = QLineEdit()
        self.line_r_8_1 = QLineEdit()
        self.line_p_8_1.setFixedWidth(400)
        self.line_r_8_1.setFixedWidth(400)
        self.line_p_8_1.setPlaceholderText('Периметр сферического треугольника')
        self.line_r_8_1.setPlaceholderText('Радиус плоскости (см)')
        self.ready_button_8_1 = QPushButton('Рассчитать')
        round_label_8_1 = QLabel('Округление:')
        self.round_choice_box_8_1 = QComboBox()
        self.round_choice_box_8_1.addItem('нет')
        self.round_choice_box_8_1.addItem('до сотых')
        self.round_choice_box_8_1.addItem('до десятых')
        self.round_choice_box_8_1.addItem('до целого')

        main_layout_8_1 = QVBoxLayout()
        layout_8_1_1 = QHBoxLayout()
        layout_8_1_2 = QHBoxLayout()
        layout_8_1_3 = QHBoxLayout()
        layout_8_1_1.addWidget(label_p_win_8_1, alignment=Qt.AlignRight)
        layout_8_1_1.addWidget(self.line_p_8_1, alignment=Qt.AlignLeft)
        layout_8_1_2.addWidget(label_r_win_8_1, alignment=Qt.AlignRight)
        layout_8_1_2.addWidget(self.line_r_8_1, alignment=Qt.AlignLeft)
        layout_8_1_3.addWidget(round_label_8_1, alignment=Qt.AlignRight)
        layout_8_1_3.addWidget(self.round_choice_box_8_1, alignment=Qt.AlignLeft)
        main_layout_8_1.addWidget(label_win_8_1, alignment=Qt.AlignCenter)
        main_layout_8_1.addLayout(layout_8_1_1)
        main_layout_8_1.addLayout(layout_8_1_2)
        main_layout_8_1.addLayout(layout_8_1_3)
        main_layout_8_1.addWidget(self.ready_button_8_1, alignment=Qt.AlignCenter)

        self.setLayout(main_layout_8_1)

        self.ready_button_8_1.clicked.connect(self.get_result_8_1)

    def get_result_8_1(self):
        def s_angle_sum_from_r_t_p(p, r):
            return 2 * p / r

        try:
            match self.round_choice_box_8_1.currentText():
                case 'до сотых':
                    p = float(self.line_p_8_1.text())
                    r = float(self.line_r_8_1.text())
                    message_result_8_1 = QMessageBox()
                    message_result_8_1.setWindowIcon(
                        QIcon("Tick_Mark_icon-icons.com_69146.ico"))
                    message_result_8_1.setWindowTitle('Готово')
                    message_result_8_1.setText('Результат: ' + str(round(s_angle_sum_from_r_t_p(p, r), 2)))
                    message_result_8_1.exec_()
                case 'до десятых':
                    p = float(self.line_p_8_1.text())
                    r = float(self.line_r_8_1.text())
                    message_result_8_1 = QMessageBox()
                    message_result_8_1.setWindowIcon(
                        QIcon("Tick_Mark_icon-icons.com_69146.ico"))
                    message_result_8_1.setWindowTitle('Готово')
                    message_result_8_1.setText('Результат: ' + str(round(s_angle_sum_from_r_t_p(p, r), 1)))
                    message_result_8_1.exec_()
                case 'до целого':
                    p = float(self.line_p_8_1.text())
                    r = float(self.line_r_8_1.text())
                    message_result_8_1 = QMessageBox()
                    message_result_8_1.setWindowIcon(
                        QIcon("Tick_Mark_icon-icons.com_69146.ico"))
                    message_result_8_1.setWindowTitle('Готово')
                    message_result_8_1.setText('Результат: ' + str(round(s_angle_sum_from_r_t_p(p, r))))
                    message_result_8_1.exec_()
                case _:
                    p = float(self.line_p_8_1.text())
                    r = float(self.line_r_8_1.text())
                    message_result_8_1 = QMessageBox()
                    message_result_8_1.setWindowIcon(
                        QIcon("Tick_Mark_icon-icons.com_69146.ico"))
                    message_result_8_1.setWindowTitle('Готово')
                    message_result_8_1.setText('Результат: ' + str(s_angle_sum_from_r_t_p(p, r)))
                    message_result_8_1.exec_()
        except:
            message_error_8_1 = QMessageBox()
            message_error_8_1.setWindowIcon(QIcon("crossregular_106296.ico"))
            message_error_8_1.setWindowTitle('Ошибка')
            message_error_8_1.setText('Не удалось расчитать величину')
            message_error_8_1.exec_()


class Window_8_2(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Определение суммы углов гиперболического треугольника через его периметр')
        self.resize(450, 400)
        self.setWindowIcon(QIcon("angle_acute_icon_138939.ico"))

        label_win_8_2 = QLabel('Введите значения величин:')
        label_win_8_2.setFont(QFont('Arial', 10))
        label_p_win_8_2 = QLabel('p = ')
        label_r_win_8_2 = QLabel('r = ')
        label_p_win_8_2.setFont(QFont('Arial', 12))
        label_r_win_8_2.setFont(QFont('Arial', 12))
        self.line_p_8_2 = QLineEdit()
        self.line_r_8_2 = QLineEdit()
        self.line_p_8_2.setFixedWidth(400)
        self.line_r_8_2.setFixedWidth(400)
        self.line_p_8_2.setPlaceholderText('Периметр гиперболического треугольника')
        self.line_r_8_2.setPlaceholderText('Радиус плоскости (см)')
        self.ready_button_8_2 = QPushButton('Рассчитать')
        round_label_8_2 = QLabel('Округление:')
        self.round_choice_box_8_2 = QComboBox()
        self.round_choice_box_8_2.addItem('нет')
        self.round_choice_box_8_2.addItem('до сотых')
        self.round_choice_box_8_2.addItem('до десятых')
        self.round_choice_box_8_2.addItem('до целого')

        main_layout_8_2 = QVBoxLayout()
        layout_8_2_1 = QHBoxLayout()
        layout_8_2_2 = QHBoxLayout()
        layout_8_2_3 = QHBoxLayout()
        layout_8_2_1.addWidget(label_p_win_8_2, alignment=Qt.AlignRight)
        layout_8_2_1.addWidget(self.line_p_8_2, alignment=Qt.AlignLeft)
        layout_8_2_2.addWidget(label_r_win_8_2, alignment=Qt.AlignRight)
        layout_8_2_2.addWidget(self.line_r_8_2, alignment=Qt.AlignLeft)
        layout_8_2_3.addWidget(round_label_8_2, alignment=Qt.AlignRight)
        layout_8_2_3.addWidget(self.round_choice_box_8_2, alignment=Qt.AlignLeft)
        main_layout_8_2.addWidget(label_win_8_2, alignment=Qt.AlignCenter)
        main_layout_8_2.addLayout(layout_8_2_1)
        main_layout_8_2.addLayout(layout_8_2_2)
        main_layout_8_2.addLayout(layout_8_2_3)
        main_layout_8_2.addWidget(self.ready_button_8_2, alignment=Qt.AlignCenter)

        self.setLayout(main_layout_8_2)

        self.ready_button_8_2.clicked.connect(self.get_result_8_2)

    def get_result_8_2(self):
        def h_angle_sum_from_l_t_p(p, r):
            return (4 * math.pi ** 2 * r) / p

        try:
            match self.round_choice_box_8_2.currentText():
                case 'до сотых':
                    p = float(self.line_p_8_2.text())
                    r = float(self.line_r_8_2.text())
                    message_result_8_2 = QMessageBox()
                    message_result_8_2.setWindowIcon(
                        QIcon("Tick_Mark_icon-icons.com_69146.ico"))
                    message_result_8_2.setWindowTitle('Готово')
                    message_result_8_2.setText('Результат: ' + str(round(h_angle_sum_from_l_t_p(p, r), 2)))
                    message_result_8_2.exec_()
                case 'до десятых':
                    p = float(self.line_p_8_2.text())
                    r = float(self.line_r_8_2.text())
                    message_result_8_2 = QMessageBox()
                    message_result_8_2.setWindowIcon(
                        QIcon("Tick_Mark_icon-icons.com_69146.ico"))
                    message_result_8_2.setWindowTitle('Готово')
                    message_result_8_2.setText('Результат: ' + str(round(h_angle_sum_from_l_t_p(p, r), 1)))
                    message_result_8_2.exec_()
                case 'до целого':
                    p = float(self.line_p_8_2.text())
                    r = float(self.line_r_8_2.text())
                    message_result_8_2 = QMessageBox()
                    message_result_8_2.setWindowIcon(
                        QIcon("Tick_Mark_icon-icons.com_69146.ico"))
                    message_result_8_2.setWindowTitle('Готово')
                    message_result_8_2.setText('Результат: ' + str(round(h_angle_sum_from_l_t_p(p, r))))
                    message_result_8_2.exec_()
                case _:
                    p = float(self.line_p_8_2.text())
                    r = float(self.line_r_8_2.text())
                    message_result_8_2 = QMessageBox()
                    message_result_8_2.setWindowIcon(
                        QIcon("Tick_Mark_icon-icons.com_69146.ico"))
                    message_result_8_2.setWindowTitle('Готово')
                    message_result_8_2.setText('Результат: ' + str(h_angle_sum_from_l_t_p(p, r)))
                    message_result_8_2.exec_()
        except:
            message_error_8_2 = QMessageBox()
            message_error_8_2.setWindowIcon(QIcon("crossregular_106296.ico"))
            message_error_8_2.setWindowTitle('Ошибка')
            message_error_8_2.setText('Не удалось расчитать величину')
            message_error_8_2.exec_()


class Window_8_3(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Определение суммы углов сферического треугольника через его площадь')
        self.resize(450, 400)
        self.setWindowIcon(QIcon("angle_acute_icon_138939.ico"))

        label_win_8_3 = QLabel('Введите значения величин:')
        label_win_8_3.setFont(QFont('Arial', 10))
        label_s_win_8_3 = QLabel('s = ')
        label_r_win_8_3 = QLabel('r = ')
        label_s_win_8_3.setFont(QFont('Arial', 12))
        label_r_win_8_3.setFont(QFont('Arial', 12))
        self.line_s_8_3 = QLineEdit()
        self.line_r_8_3 = QLineEdit()
        self.line_s_8_3.setFixedWidth(400)
        self.line_r_8_3.setFixedWidth(400)
        self.line_s_8_3.setPlaceholderText('Площадь сферического треугольника')
        self.line_r_8_3.setPlaceholderText('Радиус сферы (см)')
        self.ready_button_8_3 = QPushButton('Рассчитать')
        round_label_8_3 = QLabel('Округление:')
        self.round_choice_box_8_3 = QComboBox()
        self.round_choice_box_8_3.addItem('нет')
        self.round_choice_box_8_3.addItem('до сотых')
        self.round_choice_box_8_3.addItem('до десятых')
        self.round_choice_box_8_3.addItem('до целого')

        main_layout_8_3 = QVBoxLayout()
        layout_8_3_1 = QHBoxLayout()
        layout_8_3_2 = QHBoxLayout()
        layout_8_3_3 = QHBoxLayout()
        layout_8_3_1.addWidget(label_s_win_8_3, alignment=Qt.AlignRight)
        layout_8_3_1.addWidget(self.line_s_8_3, alignment=Qt.AlignLeft)
        layout_8_3_2.addWidget(label_r_win_8_3, alignment=Qt.AlignRight)
        layout_8_3_2.addWidget(self.line_r_8_3, alignment=Qt.AlignLeft)
        layout_8_3_3.addWidget(round_label_8_3, alignment=Qt.AlignRight)
        layout_8_3_3.addWidget(self.round_choice_box_8_3, alignment=Qt.AlignLeft)
        main_layout_8_3.addWidget(label_win_8_3, alignment=Qt.AlignCenter)
        main_layout_8_3.addLayout(layout_8_3_1)
        main_layout_8_3.addLayout(layout_8_3_2)
        main_layout_8_3.addLayout(layout_8_3_3)
        main_layout_8_3.addWidget(self.ready_button_8_3, alignment=Qt.AlignCenter)

        self.setLayout(main_layout_8_3)

        self.ready_button_8_3.clicked.connect(self.get_result_8_3)

    def get_result_8_3(self):
        def s_angle_sum_from_r_t_s(s, r):
            return abs((s / r ** 2) - math.pi)

        try:
            match self.round_choice_box_8_3.currentText():
                case 'до сотых':
                    s = float(self.line_s_8_3.text())
                    r = float(self.line_r_8_3.text())
                    message_result_8_3 = QMessageBox()
                    message_result_8_3.setWindowIcon(
                        QIcon("Tick_Mark_icon-icons.com_69146.ico"))
                    message_result_8_3.setWindowTitle('Готово')
                    message_result_8_3.setText('Результат: ' + str(round(s_angle_sum_from_r_t_s(s, r), 2)))
                    message_result_8_3.exec_()
                case 'до десятых':
                    s = float(self.line_s_8_3.text())
                    r = float(self.line_r_8_3.text())
                    message_result_8_3 = QMessageBox()
                    message_result_8_3.setWindowIcon(
                        QIcon("Tick_Mark_icon-icons.com_69146.ico"))
                    message_result_8_3.setWindowTitle('Готово')
                    message_result_8_3.setText('Результат: ' + str(round(s_angle_sum_from_r_t_s(s, r), 1)))
                    message_result_8_3.exec_()
                case 'до целого':
                    s = float(self.line_s_8_3.text())
                    r = float(self.line_r_8_3.text())
                    message_result_8_3 = QMessageBox()
                    message_result_8_3.setWindowIcon(
                        QIcon("Tick_Mark_icon-icons.com_69146.ico"))
                    message_result_8_3.setWindowTitle('Готово')
                    message_result_8_3.setText('Результат: ' + str(round(s_angle_sum_from_r_t_s(s, r))))
                    message_result_8_3.exec_()
                case _:
                    s = float(self.line_s_8_3.text())
                    r = float(self.line_r_8_3.text())
                    message_result_8_3 = QMessageBox()
                    message_result_8_3.setWindowIcon(
                        QIcon("Tick_Mark_icon-icons.com_69146.ico"))
                    message_result_8_3.setWindowTitle('Готово')
                    message_result_8_3.setText('Результат: ' + str(s_angle_sum_from_r_t_s(s, r)))
                    message_result_8_3.exec_()
        except:
            message_error_8_3 = QMessageBox()
            message_error_8_3.setWindowIcon(QIcon("crossregular_106296.ico"))
            message_error_8_3.setWindowTitle('Ошибка')
            message_error_8_3.setText('Не удалось расчитать величину')
            message_error_8_3.exec_()


class Window_8_4(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Определение суммы углов гиперболического треугольника через его площадь')
        self.resize(450, 400)
        self.setWindowIcon(QIcon("angle_acute_icon_138939.ico"))

        label_win_8_4 = QLabel('Введите значения величин:')
        label_win_8_4.setFont(QFont('Arial', 10))
        label_s_win_8_4 = QLabel('s = ')
        label_r_win_8_4 = QLabel('r = ')
        label_s_win_8_4.setFont(QFont('Arial', 12))
        label_r_win_8_4.setFont(QFont('Arial', 12))
        self.line_s_8_4 = QLineEdit()
        self.line_r_8_4 = QLineEdit()
        self.line_s_8_4.setFixedWidth(400)
        self.line_r_8_4.setFixedWidth(400)
        self.line_s_8_4.setPlaceholderText('Площадь гиперболического треугольника')
        self.line_r_8_4.setPlaceholderText('Радиус сферы (см)')
        self.ready_button_8_4 = QPushButton('Рассчитать')
        round_label_8_4 = QLabel('Округление:')
        self.round_choice_box_8_4 = QComboBox()
        self.round_choice_box_8_4.addItem('нет')
        self.round_choice_box_8_4.addItem('до сотых')
        self.round_choice_box_8_4.addItem('до десятых')
        self.round_choice_box_8_4.addItem('до целого')

        main_layout_8_4 = QVBoxLayout()
        layout_8_4_1 = QHBoxLayout()
        layout_8_4_2 = QHBoxLayout()
        layout_8_4_3 = QHBoxLayout()
        layout_8_4_1.addWidget(label_s_win_8_4, alignment=Qt.AlignRight)
        layout_8_4_1.addWidget(self.line_s_8_4, alignment=Qt.AlignLeft)
        layout_8_4_2.addWidget(label_r_win_8_4, alignment=Qt.AlignRight)
        layout_8_4_2.addWidget(self.line_r_8_4, alignment=Qt.AlignLeft)
        layout_8_4_3.addWidget(round_label_8_4, alignment=Qt.AlignRight)
        layout_8_4_3.addWidget(self.round_choice_box_8_4, alignment=Qt.AlignLeft)
        main_layout_8_4.addWidget(label_win_8_4, alignment=Qt.AlignCenter)
        main_layout_8_4.addLayout(layout_8_4_1)
        main_layout_8_4.addLayout(layout_8_4_2)
        main_layout_8_4.addLayout(layout_8_4_3)
        main_layout_8_4.addWidget(self.ready_button_8_4, alignment=Qt.AlignCenter)

        self.setLayout(main_layout_8_4)

        self.ready_button_8_4.clicked.connect(self.get_result_8_4)

    def get_result_8_4(self):
        def h_angle_sum_from_l_t_s(s, r):
            return (s / r ** 2) + math.pi

        try:
            match self.round_choice_box_8_4.currentText():
                case 'до сотых':
                    s = float(self.line_s_8_4.text())
                    r = float(self.line_r_8_4.text())
                    message_result_8_4 = QMessageBox()
                    message_result_8_4.setWindowIcon(
                        QIcon("Tick_Mark_icon-icons.com_69146.ico"))
                    message_result_8_4.setWindowTitle('Готово')
                    message_result_8_4.setText('Результат: ' + str(round(h_angle_sum_from_l_t_s(s, r), 2)))
                    message_result_8_4.exec_()
                case 'до десятых':
                    s = float(self.line_s_8_4.text())
                    r = float(self.line_r_8_4.text())
                    message_result_8_4 = QMessageBox()
                    message_result_8_4.setWindowIcon(
                        QIcon("Tick_Mark_icon-icons.com_69146.ico"))
                    message_result_8_4.setWindowTitle('Готово')
                    message_result_8_4.setText('Результат: ' + str(round(h_angle_sum_from_l_t_s(s, r), 1)))
                    message_result_8_4.exec_()
                case 'до целого':
                    s = float(self.line_s_8_4.text())
                    r = float(self.line_r_8_4.text())
                    message_result_8_4 = QMessageBox()
                    message_result_8_4.setWindowIcon(
                        QIcon("Tick_Mark_icon-icons.com_69146.ico"))
                    message_result_8_4.setWindowTitle('Готово')
                    message_result_8_4.setText('Результат: ' + str(round(h_angle_sum_from_l_t_s(s, r))))
                    message_result_8_4.exec_()
                case _:
                    s = float(self.line_s_8_4.text())
                    r = float(self.line_r_8_4.text())
                    message_result_8_4 = QMessageBox()
                    message_result_8_4.setWindowIcon(
                        QIcon("Tick_Mark_icon-icons.com_69146.ico"))
                    message_result_8_4.setWindowTitle('Готово')
                    message_result_8_4.setText('Результат: ' + str(h_angle_sum_from_l_t_s(s, r)))
                    message_result_8_4.exec_()
        except:
            message_error_8_4 = QMessageBox()
            message_error_8_4.setWindowIcon(QIcon("crossregular_106296.ico"))
            message_error_8_4.setWindowTitle('Ошибка')
            message_error_8_4.setText('Не удалось расчитать величину')
            message_error_8_4.exec_()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    main_win = Main_window()
    main_win.show()
    sys.exit(app.exec_())
