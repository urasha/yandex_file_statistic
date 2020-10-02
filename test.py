import statistics
import sys
import string

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget


class MainForm(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('file_system.ui', self)
        self.pushButton.clicked.connect(self.count)

    def count(self):
        try:
            with open(f'{self.lineEdit.text()}', 'r') as file:
                # файл должен содержать только одну строку чисел, как я понял, да?
                f = list(filter(lambda x: x in string.digits, file.readline()))
                numbers = list(map(int, f))

                max_value = max(numbers)
                min_value = min(numbers)
                average_value = statistics.mean(numbers)

                self.lineEdit_3.setText(str(min_value))
                self.lineEdit_2.setText(str(average_value))
                self.lineEdit_4.setText(str(max_value))

                with open('output.txt', 'w') as file_1:
                    file_1.write('Max: ' + str(max_value) + '\n')
                    file_1.write('Min: ' + str(min_value) + '\n')
                    file_1.write('Average: ' + str(average_value) + '\n')

        except Exception:
            self.label_5.setText(f'Файла с именем {self.lineEdit.text()} нет, '
                                 f'или в нём содержаться некоректные данные')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_form = MainForm()
    main_form.show()
    sys.exit(app.exec())
