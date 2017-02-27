from __future__ import division
from PyQt4 import QtCore, QtGui
from ui_mainwindow import Ui_MainWindow
from ui_logindlg import Ui_LoginDialog

class myLoginDialog(QtGui.QDialog, Ui_LoginDialog):
	def __init__(self, mainWindow, parent=None):
		super(myLoginDialog, self).__init__(parent)
		self.setupUi(self)
		self.mainWindow = mainWindow

	@QtCore.pyqtSlot()
	def on_pushButton_clicked(self):
		self.hide()
		self.mainWindow.show()


class myMainWindow(QtGui.QMainWindow, Ui_MainWindow):

	def __init__(self, parent=None):
		super(myMainWindow, self).__init__(parent)
		self.setupUi(self)
        #self.updateUi()

	@QtCore.pyqtSlot()
	def on_pushButton_clicked(self):
		if self.tabWidget.currentIndex() == 0:
			self.caculate_bh()

		else:
			self.caculate_wy()

	def caculate_bh(self):
		A = self.spinBox_1.value()
		B = A / 800 + 4
		self.doubleSpinBox_2.setValue(B)
		C = self.spinBox_3.value()
		D = self.spinBox_4.value()
		E = self.doubleSpinBox_5.value()
		F = E * 2
		G = (F / 2 / D) ** (1 / 3.0) * A
		H = G + 2
		self.doubleSpinBox_6.setValue(F)
		self.doubleSpinBox_7.setValue(G)
		self.doubleSpinBox_8.setValue(H)
		I = self.doubleSpinBox_9.value()
		J = I * A / 2.0 / 0.9 / 0.85 / 235
		K = J + 2
		L = max(B, C, H, K)
		self.doubleSpinBox_10.setValue(J)
		self.doubleSpinBox_11.setValue(K)
		self.doubleSpinBox_12.setValue(L)

	def caculate_wy(self):
		A = self.spinBox_13.value()
		B = self.spinBox_14.value()
		C = self.spinBox_15.value()
		D = C - 2
		self.spinBox_16.setValue(D)
		E = int(round(1.63 * (A / B) ** 0.5 * (A / D) ** 0.25))
		self.spinBox_17.setValue(E)
		F = self.spinBox_18.value()
		G = self.spinBox_19.value()
		H = self.doubleSpinBox_20.value()
		I = G/(F**2-1)/(1+(F*B/3.14159/A*2)**2)**2*D/A*2+G/12/(1-H**2)*(F**2-1+(2*F**2-1-H)/(1+(F*B/3.14159/A*2)**2))*(D/A*2)**3
		self.doubleSpinBox_21.setValue(I)
		J = self.doubleSpinBox_22.value()
		K = I / J
		self.doubleSpinBox_23.setValue(K)


if __name__ == "__main__":
 	import sys
 	app = QtGui.QApplication(sys.argv)
 	mw = myMainWindow()
 	dlg = myLoginDialog(mw)
	dlg.show()
	sys.exit(app.exec_())