from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog, QLabel
from design4 import Ui_MainWindow
from PyQt5.QtGui import QPixmap
import sys
import functions


class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.encrypt_image = ''
        self.encrypt_image_big = ''
        self.decrypt_image = ''
        self.encrypt_image_orig = ''
        self.encrypt_image_orig_big = ''
        self.decrypt_image_orig = ''
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.open_encrypt_3.clicked.connect(self.open_encrypt_img)
        self.ui.encrypt_2.clicked.connect(self.encrypt_img_func)
        self.ui.open_decrypt.clicked.connect(self.open_decrypt_img)
        self.ui.open_encrypt_2.clicked.connect(self.open_encrypt_img_small)
        self.ui.decrypt.clicked.connect(self.decrypt_img_func)
        self.number = 1
        self.usable_pixels = 0
        self.usable_pixels_arr = 0

    def open_encrypt_img_small(self):
        options = QFileDialog.Options()
        self.encrypt_image = QFileDialog.getOpenFileName(self,"Выберете изображение", "","Image Files (*.png *.jpg)", options=options)[0]
        self.encrypt_image_orig = self.encrypt_image
        self.encrypt_image = functions.image_resize(self.encrypt_image)
        if not QPixmap(self.encrypt_image).isNull():
            self.ui.encrypt_img_2.setPixmap(QPixmap(self.encrypt_image))
            self.usable_pixels_arr, self.usable_pixels = functions.make_usable_pixels_array(self.encrypt_image_orig)
        else:
            self.ui.encryption_2.setText('Некорректное изображение')

    def open_encrypt_img(self):
        options = QFileDialog.Options()
        self.encrypt_image_big = QFileDialog.getOpenFileName(self,"Выберете изображение", "","Image Files (*.png *.jpg )", options=options)[0]
        self.encrypt_image_orig_big = self.encrypt_image_big
        self.encrypt_image_big = functions.image_resize_big(self.encrypt_image_big)
        if not QPixmap(self.encrypt_image_big).isNull():
            self.ui.encrypt_img_3.setPixmap(QPixmap(self.encrypt_image_big))
            self.usable_pixels_arr, self.usable_pixels = functions.make_usable_pixels_array(self.encrypt_image_orig_big)
            self.ui.output_2.setText(
                f'Вы можете зашифровать {self.usable_pixels} символов(буквы, пробелы и прочие знаки)')
        else:
            self.ui.output_2.setText('Некорректное изображение')

    def encrypt_img_func(self):
        text = self.ui.encryption_2.toPlainText()
        text = functions.check_simbols(text)
        if (len(text) < self.usable_pixels):
            functions.encrypt(self.encrypt_image_orig_big,text,self.usable_pixels_arr,self.number)
            self.ui.output_2.setText(
                f'Текст успешно зашифрован. Изображение с зашифрованным текстом находится в папке программы')
            self.number += 1
        else:
            self.ui.output_2.setText(
                f'Изображение слишокм маленькое. Для шифрования текста вам предположительно понадобится картинка '
                f'{int(round((len(text)*4*1.3)**0.5,-1))} на {int(round((len(text)*4*1.3)**0.5,-1))} пикселей')


    def open_decrypt_img(self):
        options = QFileDialog.Options()
        self.decrypt_image = QFileDialog.getOpenFileName(self, "Выберете изображение", "", "Image Files (*.png *.jpg )", options=options)[0]
        self.decrypt_image_orig = self.decrypt_image
        self.decrypt_image = functions.image_resize(self.decrypt_image)
        if not QPixmap(self.decrypt_image).isNull():
            self.ui.decrypt_img.setPixmap(QPixmap(self.decrypt_image))
        else:
            self.ui.decruption.setText('Некорректное изображение')

    def decrypt_img_func(self):
        try:
            text = functions.decrypt(self.encrypt_image_orig,self.decrypt_image_orig)
            self.ui.decruption.setText(text)
        except Exception:
            self.ui.decruption.setText('Ошибка. Возможно вы загрузили не оригинальное изображение или неправильное изображение с шифром')
            print(Exception)



app = QtWidgets.QApplication([])
application = mywindow()
application.show()

sys.exit(app.exec())