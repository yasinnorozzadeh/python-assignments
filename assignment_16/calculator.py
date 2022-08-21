import math
from PySide6.QtWidgets import *
from PySide6.QtUiTools import *
from PySide6.QtCore import *

class HelloWorld(QMainWindow):
    def __init__(self):
        self.chek_op = 0
        super().__init__()
        loader = QUiLoader()
        self.ui = loader.load('form.ui',None)
        self.ui.show()
        self.ui.btn_sum.clicked.connect(self.sum)
        self.ui.btn_sub.clicked.connect(self.sub)
        self.ui.btn_mul.clicked.connect(self.mul)
        self.ui.btn_div.clicked.connect(self.div)
        self.ui.btn_num_1.clicked.connect(self.f_n_1)
        self.ui.btn_num_2.clicked.connect(self.f_n_2)
        self.ui.btn_num_3.clicked.connect(self.f_n_3)
        self.ui.btn_num_4.clicked.connect(self.f_n_4)
        self.ui.btn_num_5.clicked.connect(self.f_n_5)
        self.ui.btn_num_6.clicked.connect(self.f_n_6)
        self.ui.btn_num_7.clicked.connect(self.f_n_7)
        self.ui.btn_num_8.clicked.connect(self.f_n_8)
        self.ui.btn_num_9.clicked.connect(self.f_n_9)
        self.ui.btn_num_0.clicked.connect(self.f_n_0)
        self.ui.btn_tan.clicked.connect(self.tan_n)
        self.ui.btn_cot.clicked.connect(self.cot_n)
        self.ui.btn_sin.clicked.connect(self.sin_n)
        self.ui.btn_cos.clicked.connect(self.cos_n)
        self.ui.btn_sqrt.clicked.connect(self.sqrt_n)
        self.ui.btn_log.clicked.connect(self.log_n)
        self.ui.btn_AC.clicked.connect(self.AC_n)
        self.ui.btn_abc.clicked.connect(self.abc_n)
        self.ui.btn_dot.clicked.connect(self.dot)
        self.ui.btn_equal.clicked.connect(self.equal)

    def f_n_1(self):
        self.ui.text_box.setText(self.ui.text_box.text() + "1")
    def f_n_2(self):
        self.ui.text_box.setText(self.ui.text_box.text() + "2")
    def f_n_3(self):
        self.ui.text_box.setText(self.ui.text_box.text() + "3")
    def f_n_4(self):
        self.ui.text_box.setText(self.ui.text_box.text() + "4")
    def f_n_5(self):
        self.ui.text_box.setText(self.ui.text_box.text() + "5")
    def f_n_6(self):
        self.ui.text_box.setText(self.ui.text_box.text() + "6")
    def f_n_7(self):
        self.ui.text_box.setText(self.ui.text_box.text() + "7")
    def f_n_8(self):
        self.ui.text_box.setText(self.ui.text_box.text() + "8")
    def f_n_9(self):
        self.ui.text_box.setText(self.ui.text_box.text() + "9")
    def f_n_0(self):
        self.ui.text_box.setText(self.ui.text_box.text() + "0")
    def dot(self):
        if "." not in self.ui.text_box.text():
            self.ui.text_box.setText(self.ui.text_box.text() + ".")

    def sum(self):
        self.num_1 = float(self.ui.text_box.text())
        self.ui.text_box.setText("")
        self.chek_op = "+"
    def equl_sum(self):
        self.num_2 = float(self.ui.text_box.text())
        self.ui.text_box.setText("")
        result = self.num_1 + self.num_2
        self.ui.text_box.setText(str(result))
    def sub(self):
        self.num_1 = float(self.ui.text_box.text())
        self.ui.text_box.setText("")
        self.chek_op = "-"
    def equl_sub(self):
        self.num_2 = float(self.ui.text_box.text())
        self.ui.text_box.setText("")
        result = self.num_1 - self.num_2
        self.ui.text_box.setText(str(result))
    def div(self):
        self.num_1 = float(self.ui.text_box.text())
        self.ui.text_box.setText("")
        self.chek_op = "/"
    def equl_div(self):
        self.num_2 = float(self.ui.text_box.text())
        self.ui.text_box.setText("")
        if self.num_1 == 0 or self.num_2 == 0:
            self.ui.text_box.setText("not / becuse 0")
        else:
            result = self.num_1 / self.num_2
            self.ui.text_box.setText(str(result))
    def mul(self):
        self.num_1 = float(self.ui.text_box.text())
        self.ui.text_box.setText("")
        self.chek_op = "*"
    def equl_mul(self):
        self.num_2 = float(self.ui.text_box.text())
        self.ui.text_box.setText("")
        result = self.num_1 * self.num_2
        self.ui.text_box.setText(str(result))
    def equal(self):
        if self.chek_op == "+":
            self.equl_sum()
        elif self.chek_op == "-":
            self.equl_sub()
        elif self.chek_op == "*":
            self.equl_mul()
        elif self.chek_op == "/":
            self.equl_div()
        else:
            self.ui.text_box.setText(self.ui.text_box.text())
    
    def AC_n(self):
        self.ui.text_box.setText("")
    def tan_n(self):
        self.num_1 = int(self.ui.text_box.text())
        self.ui.text_box.setText(str(math.tan(self.num_1)))
    def cot_n(self):
        self.num_1 = int(self.ui.text_box.text())
        self.ui.text_box.setText(str(math.cos(self.num_1)))
    def sin_n(self):
        self.num_1 = int(self.ui.text_box.text())
        self.ui.text_box.setText(str(math.sin(self.num_1)))
    def cos_n(self):
        self.num_1 = int(self.ui.text_box.text())
        self.ui.text_box.setText(str(math.cos(self.num_1)))
    def sqrt_n(self):
        self.num_1 = int(self.ui.text_box.text())
        self.ui.text_box.setText(str(math.sqrt(self.num_1)))
    def log_n(self):
        self.num_1 = int(self.ui.text_box.text())
        self.ui.text_box.setText(str(math.log(self.num_1)))
    def abc_n(self):
        self.num_1 = int(self.ui.text_box.text())
        self.abc = self.num_1 - self.num_1*2
        self.ui.text_box.setText(str(self.abc))

app = QApplication([])
window = HelloWorld()

app.exec()
