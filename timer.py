import sys
from PyQt4 import QtGui, QtCore
 
from time import strftime
 
 
class Main(QtGui.QMainWindow):
 
    def __init__(self):
        super(Main, self).__init__()
        self.seconds = 0;
        self.timer_work = 0;
 
        
 
 
#---------Window settings --------------------------------
         
        self.setGeometry(300,300,250,100)
        self.setFixedSize(250, 100)
        self.setWindowTitle("Timer")


#---------Button settings---------------------------------
        btn = QtGui.QPushButton("start", self)
        btn.move(145, 60)
        btn.clicked.connect(self.StartTimer)

#---------Label settings----------------------------------        
        self.label = QtGui.QLabel(str(self.seconds), self)
        self.label.move(120, 22)

        newfont = QtGui.QFont("Times", 12, QtGui.QFont.Bold) 
        self.label.setFont(newfont)

    def StartTimer(self):
        self.timer_work =1 - self.timer_work
        print(self.timer_work)
        
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.Time)
        self.timer.start(1000)
        
  
    def Time(self):
        self.seconds += 1;
        self.label.setText(str(self.seconds))
        print(self.seconds)
        


         
def main():
    app = QtGui.QApplication(sys.argv)
    main = Main()
    main.show()
 
    sys.exit(app.exec_())
 
if __name__ == "__main__":
    main()
