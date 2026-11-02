import sys
from PyQt6.QtWidgets import (
    QMainWindow, QApplication, QWidget, QVBoxLayout, QHBoxLayout, QFormLayout,
    QLabel, QLineEdit, QPushButton, QCheckBox, QComboBox, QSpinBox
)

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My first Window")
        self.setMinimumSize(400, 300)

        main_layout = QVBoxLayout()
        form_layout = QFormLayout()
        button_layout = QHBoxLayout()


        name_input = QLineEdit()
        name_input.setPlaceholderText("Введіть ім'я")
        form_layout.addRow("Ім'я: ", name_input)


        age_spin = QSpinBox()
        age_spin.setRange(1 , 100)
        age_spin.setValue(19)
        form_layout.addRow("Вік: ", age_spin)

        games_combo = QComboBox()
        games_combo.addItems(["Phantom blade zero", "Black Myth: Wukong", "Stellar blade", "Lies of P", "Dark souls"])
        form_layout.addRow("Гра: ", games_combo)

        terms_check = QCheckBox("Погоджуюсь з умовами")
        terms_check.setChecked(True)
        form_layout.addRow("", terms_check)

        btn_s = QPushButton("Зберегти")
        btn_s.setToolTip("Натисніть для збереження даних")
        
        btn_c = QPushButton("Відміна")
        btn_c.setToolTip("Закрити без збереження")

        button_layout.addWidget(btn_s)
        button_layout.addWidget(btn_c)

        
        main_layout.addLayout(form_layout)
        main_layout.addLayout(button_layout)

        self.setLayout(main_layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())