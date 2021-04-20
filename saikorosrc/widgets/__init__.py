from PySide6 import QtCore, QtWidgets, QtGui
from saikorosrc.resources import load_css


CSS = load_css("main.css")


class OptionsWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(OptionsWidget, self).__init__(parent)
        self.setMaximumWidth(200)
        self.parent = parent

        # Number of words
        self.nowWidget = QtWidgets.QSpinBox()
        self.nowWidget.setRange(3, 50)
        self.nowWidget.setSingleStep(1)
        self.nowWidget.setValue(6)
        self.nowWidget.valueChanged.connect(self.update_no_of_words)

        # Number of special characters
        self.spCharacterWidget = QtWidgets.QSpinBox()
        self.spCharacterWidget.setRange(0, 50)
        self.spCharacterWidget.setSingleStep(1)
        self.spCharacterWidget.setValue(0)
        self.spCharacterWidget.valueChanged.connect(self.update_spcharacters)

        # Delimiter
        self.delimiterWidget = QtWidgets.QLineEdit()
        self.delimiterWidget.textChanged.connect(self.update_delimiter)

        # Form layout
        formLayout = QtWidgets.QFormLayout()
        formLayout.addRow("&No. of words", self.nowWidget)
        formLayout.addRow("No. of &special characters", self.spCharacterWidget)
        formLayout.addRow("&Delimiter", self.delimiterWidget)
        formLayout.setRowWrapPolicy(QtWidgets.QFormLayout.WrapAllRows)
        formLayout.setVerticalSpacing(8)

        self.setLayout(formLayout)

    def update_no_of_words(self):
        self.parent.options.num = self.nowWidget.value()

    def update_spcharacters(self):
        self.parent.options.specials = self.spCharacterWidget.value()

    def update_delimiter(self):
        self.parent.options.delimiter = self.delimiterWidget.text()

    def paintEvent(self, evt):
        super(OptionsWidget, self).paintEvent(evt)
        opt = QtWidgets.QStyleOption()
        opt.initFrom(self)
        p = QtGui.QPainter(self)
        s = self.style()
        s.drawPrimitive(QtWidgets.QStyle.PE_Widget, opt, p, self)


class WrapAnywhereLabel(QtWidgets.QTextEdit):
    def __init__(self, text, parent=None):
        super(WrapAnywhereLabel, self).__init__(text, parent)
        self.setMaximumHeight(250)

        # Make it look like label
        self.setReadOnly(True)
        self.setFrameStyle(QtWidgets.QFrame.NoFrame)
        pal = QtGui.QPalette()
        pal.setColor(QtGui.QPalette.Base, QtCore.Qt.transparent)

        self.setLineWrapMode(QtWidgets.QTextEdit.WidgetWidth)
        self.setWordWrapMode(QtGui.QTextOption.WrapAnywhere)
