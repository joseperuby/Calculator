""" 
This is a simple calculator application using PyQt6. 🧮


Author: Joseperuby
"""

import sys
from PyQt6.QtWidgets import QApplication, QWidget, QTextEdit, QPushButton, QGridLayout
import operator

operation = {
    '+' : operator.add,
    '-' : operator.sub,
    '*' : operator.mul,
    '/' : operator.truediv
}

class MainWindow(QWidget):
    """
    The main window of the calculator application.

    Attributes:
        m_screen (QTextEdit): The text edit field for displaying input and results.
        main_grid_layout (QGridLayout): The grid layout for organizing buttons.
    """

    def __init__(self):
        """
        Initialize the main calculator window.
        """
        super().__init__()
        self.build_interface()
        self.first_number = ''
        self.second_number = ''
        self.operator = ''
        self.pointer_flag = '1'
        self.after_equal = False
        self.after_operator = False

    def build_interface(self):
        """
        Build the user interface for the calculator.
        """
        self.setGeometry(700, 300, 100, 100)
        self.setWindowTitle("Pepe's Calculator")

        # Main Screen
        self.m_screen = QTextEdit()
        self.m_screen.setDisabled(True)

        # Buttons
        button_ce = QPushButton("CE")
        button_c = QPushButton("C")
        button_res = QPushButton("=")

        button_1 = QPushButton("1")
        button_2 = QPushButton("2")
        button_3 = QPushButton("3")
        button_4 = QPushButton("4")
        button_5 = QPushButton("5")
        button_6 = QPushButton("6")
        button_7 = QPushButton("7")
        button_8 = QPushButton("8")
        button_9 = QPushButton("9")
        button_0 = QPushButton("0")
        button_00 = QPushButton("00")
        button_point = QPushButton(".")
        button_add = QPushButton("+")
        button_sub = QPushButton("-")
        button_div = QPushButton("/")
        button_mul = QPushButton("*")

        # Slots and Signals (SLOTS)
        button_c.clicked.connect(self.clear_one)
        button_ce.clicked.connect(self.clear_everything)
        button_res.clicked.connect(self.enter_result)

        button_1.clicked.connect(self.enter_values)
        button_2.clicked.connect(self.enter_values)
        button_3.clicked.connect(self.enter_values)
        button_4.clicked.connect(self.enter_values)
        button_5.clicked.connect(self.enter_values)
        button_6.clicked.connect(self.enter_values)
        button_7.clicked.connect(self.enter_values)
        button_8.clicked.connect(self.enter_values)
        button_9.clicked.connect(self.enter_values)
        button_0.clicked.connect(self.enter_values)
        button_00.clicked.connect(self.enter_values)
        button_point.clicked.connect(self.enter_values)
        button_add.clicked.connect(self.enter_operator)
        button_sub.clicked.connect(self.enter_operator)
        button_div.clicked.connect(self.enter_operator)
        button_mul.clicked.connect(self.enter_operator)

        # Layout (Grid)
        self.main_grid_layout = QGridLayout()
        self.main_grid_layout.addWidget(self.m_screen, 0, 0, 2, 4) 

        self.main_grid_layout.addWidget(button_ce, 2, 0, 1, 2)
        self.main_grid_layout.addWidget(button_c, 2, 2)
        self.main_grid_layout.addWidget(button_add, 2, 3)

        self.main_grid_layout.addWidget(button_7, 3, 0)
        self.main_grid_layout.addWidget(button_8, 3, 1)
        self.main_grid_layout.addWidget(button_9, 3, 2)
        self.main_grid_layout.addWidget(button_div, 3, 3)

        self.main_grid_layout.addWidget(button_4, 4, 0)
        self.main_grid_layout.addWidget(button_5, 4, 1)
        self.main_grid_layout.addWidget(button_6, 4, 2)
        self.main_grid_layout.addWidget(button_mul, 4, 3)

        self.main_grid_layout.addWidget(button_1, 5, 0)
        self.main_grid_layout.addWidget(button_2, 5, 1)
        self.main_grid_layout.addWidget(button_3, 5, 2)
        self.main_grid_layout.addWidget(button_sub, 5, 3)

        self.main_grid_layout.addWidget(button_0, 6, 0)
        self.main_grid_layout.addWidget(button_00, 6, 1)
        self.main_grid_layout.addWidget(button_point, 6, 2)
        self.main_grid_layout.addWidget(button_res, 6, 3)

        self.setLayout(self.main_grid_layout)
        self.show()

    # Class methods
    def enter_values(self):
        button_c = self.sender().text()
        if self.after_equal:
            self.first_number = ''
            self.m_screen.setText(self.first_number)
            self.after_equal = False
            self.pointer_flag == '1'

        if self.pointer_flag == '1':
            self.first_number += button_c
            self.m_screen.setText(self.first_number)
        else:
            self.second_number += button_c
            self.m_screen.setText(self.m_screen.toPlainText() + button_c)
    
    def enter_operator(self):
        button_c = self.sender().text()
        self.operator = button_c
        self.pointer_flag = '2'

        if self.after_operator == True:
            self.enter_result()
            self.m_screen.setText(self.first_number + '' + self.operator + '')
            self.after_operator = False
        else:
            self.m_screen.setText(self.m_screen.toPlainText() + '' + self.operator + '')

        self.after_operator = True
        self.after_equal = False

    def clear_everything(self):
        self.first_number = ''
        self.second_number = ''
        self.operator = ''
        self.pointer_flag = '1'
        self.after_equal = False
        self.after_operator = False
        self.m_screen.setText("")

    def clear_one(self):
        if self.after_equal:
            self.clear_everything()
        
        if self.pointer_flag == '1':
            self.first_number = self.first_number[:-1]
            self.m_screen.setText(self.first_number)
        else:
            self.second_number = self.second_number[:-1]
            self.m_screen.setText(self.second_number)
    
    def enter_result(self):
        result = str(operation[self.operator](float(self.first_number), float(self.second_number)))
        self.m_screen.setText(result)
        self.first_number = result
        self.second_number = ''
        self.after_equal = True
        self.after_operator = False
        
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())