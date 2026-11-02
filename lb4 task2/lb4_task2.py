import sys
from PyQt6.QtWidgets import (
    QMainWindow, QApplication, QWidget, QVBoxLayout, QHBoxLayout, QFormLayout,
    QLabel, QLineEdit, QPushButton, QCheckBox, QComboBox, QSpinBox, QMessageBox
)


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Interactive Window")
        self.setMinimumSize(400, 300)

        main_layout = QVBoxLayout()
        form_layout = QFormLayout()
        button_layout = QHBoxLayout()


        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Введіть ім'я")
        

        self.age_spin = QSpinBox()
        self.age_spin.setRange(1 , 100)
        self.age_spin.setValue(19)
        

        self.terms_check = QCheckBox("Погоджуюсь з умовами")
        
        self.status_label = QLabel("Заповніть форму")

        self.btn_s = QPushButton("Підтвердити")
        self.btn_s.setEnabled(False)



        self.btn_r = QPushButton("Скинути")
       

        form_layout.addRow("Ім'я:", self.name_input)
        form_layout.addRow("Вік:", self.age_spin)
        form_layout.addRow("", self.terms_check)
        form_layout.addRow("Статус:", self.status_label)

        button_layout.addWidget(self.btn_s)
        button_layout.addWidget(self.btn_r)

        
        main_layout.addLayout(form_layout)
        main_layout.addLayout(button_layout)
        self.setLayout(main_layout)

        self.terms_check.toggled.connect(self.btn_s.setEnabled)

        self.name_input.textChanged.connect(lambda text: self.status_label.setText(f"Вводиться ім'я: {text}") )

        self.age_spin.valueChanged.connect(lambda age: self.status_label.setText(f"Вводиться вік: {age}"))

        self.btn_s.clicked.connect(self.on_sub)

        self.btn_r.clicked.connect(self.reset)

    def validate_inp(self):
        name = self.name_input.text().strip()
        if not name:
            return False, "Поле 'Ім'я' не може бути порожнім!"
        if len(name) < 2:
            return False, "Ім'я повинно містити щонайменше 2 символа!"
        return True, "Дані успішно перевірено!"

    def on_sub(self):
        is_valid, message = self.validate_inp()

        if is_valid:
            QMessageBox.information(self, "Успіх", f"Форму відправлено!\n{message}")
            self.status_label.setText("Статус: Форму успішно відправлено!")
        else:
            QMessageBox.warning(self, "Помилка валідації", message)
            self.status_label.setText(f"Помилка: {message}")


    def reset(self):
        self.name_input.clear()
        self.age_spin.setValue(19)
        self.terms_check.setChecked(False)
        self.status_label.setText("Заповніть форму")



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
