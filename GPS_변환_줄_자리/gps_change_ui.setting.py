import sys, os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5 import uic
import time

from gps_change import nav_change,changeint,zeroto,file_make,same_change,time_change,change_format

class qtApp(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('F.ui', self)
        self.pushButton_find_dir_button.clicked.connect(self.UpdateFileList)
        self.listwidget_file_list.itemDoubleClicked.connect(self.selectedchanged_listwidget)
    
    # def OnClickedFindFolder(self):
    #     self.dir_path = QFileDialog.getExistingDirectory(self.centralwidget, 'Find folder') # 폳더 찾는 기능

    #     self.lineEdit_dir_path.setText(self.dir_path) # 폴더의 경로를 적어준다

    #     self.UpdateFileList()

    def UpdateFileList(self): # 파일들의 리스트를 가져오게 해줌, 파일 형식에 맞는 거만 뜨게 해줌


        self.folder = QFileDialog.getExistingDirectory(self, "Select Directory") # 폴더 주소를 가져오는 함수
        if self.folder != '' :
            self.lineEdit_dir_path.setText(self.folder) # 라벨에 텍스트 넣어줌
            self.listwidget_file_list.clear() # 리스트위젯 클리어
            files = os.listdir(self.folder)
            fileExt = ".Nav"
            for file in files :
                if file.endswith(fileExt) :
                    self.listwidget_file_list.addItem(file)
        else :
            QMessageBox.about(self, "Error", "Not selected!")





    def selectedchanged_listwidget(self):
        lst_items = self.listwidget_file_list.selectedItems()
        if lst_items:
            # Get the file name from the selected item
            item = lst_items[0]
            file_name = str(item.text())
            file_path = os.path.join(self.folder, file_name)
            
            # Now you can use file_path for further processing
        try:
            nav_all = nav_change(file_path)
            changeint(nav_all)
            zeroto(nav_all)
            same_change(nav_all)
            time_change(nav_all)
            change_format(nav_all)
            file_make(file_name,nav_all)
            QMessageBox.information(self,'Success','변환완료')
        except:
            QMessageBox.warning(self,"Error",'오류')


            



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = qtApp()
    ex.show()
    sys.exit(app.exec_())
