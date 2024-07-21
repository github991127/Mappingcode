from PySide2.QtWidgets import QApplication, QWidget
from PySide2.QtUiTools import QUiLoader
from PySide2.QtGui import QIcon

from list_themes import *
import Mappingcode


class Stats:
    def __init__(self):
        # 从ui文件中加载UI定义,从UI定义中动态创建一个相应的窗口对象
        # 注意：里面的控件对象也成为窗口对象的属性了.比如 self.ui.button , self.ui.textEdit
        self.ui = QUiLoader().load('Mappingcode.ui')
        self.ui.lineEdit_1.returnPressed.connect(self.handleCalc)
        self.ui.lineEdit_2.returnPressed.connect(self.handleCalc)
        self.ui.lineEdit_3.returnPressed.connect(self.handleCalc)
        self.ui.toolButton_6.clicked.connect(self.handleCalc)

    def handleCalc(self):
        self.ui.textBrowser_1.clear()
        self.ui.textBrowser_2.clear()

        if self.ui.lineEdit_1.text() != '':
            a = float(self.ui.lineEdit_1.text())
        else:
            a = 0

        if self.ui.lineEdit_2.text() != '':
            b = float(self.ui.lineEdit_2.text())
        else:
            b = 0

        if self.ui.lineEdit_3.text() != '':
            c = float(self.ui.lineEdit_3.text())
        else:
            c = 0

        formula, x, list_index = Mappingcode.mappingcode(a, b, c)
        self.ui.textBrowser_1.setText(str(x))
        for i in range(len(list_index)):
            a = str(i) + '---' + str(list_index[i])
            self.ui.textBrowser_2.append(a)


if __name__ == '__main__':
    app = QApplication([])
    app.setWindowIcon(QIcon('image.png'))
    apply_stylesheet(app, theme[1], extra=extra, invert_secondary=True)  # 默认dark-False
    w = QWidget()
    w.setWindowIcon(QIcon('image.png'))
    stats = Stats()
    stats.ui.show()
    app.exec_()
