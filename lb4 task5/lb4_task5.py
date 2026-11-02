import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QDialog, 
    QVBoxLayout, QFormLayout, QLineEdit, 
    QDialogButtonBox, QPushButton, QLabel, 
    QMessageBox, QInputDialog
)


STYLE_SHEET = """
    QWidget {
        background-color: #1e1e1e;
        color: #f5f5f5;
        font-family: 'Segoe UI', sans-serif;
        font-size: 14px;
    }

    
    QLabel {
        color: #ffffff;
        font-weight: bold;
        padding: 12px;
        background-color: #252526;
        border: 1px solid #d63031;
        border-radius: 6px;
    }

    
    QLineEdit {
        background-color: #2d2d30;
        color: #ffffff;
        border: 1px solid #444444;
        border-radius: 4px;
        padding: 6px;
    }
    QLineEdit:focus {
        border: 2px solid #ff7675;
    }

    
    QPushButton {
        background-color: #d63031;
        color: #ffffff;
        border: none;
        border-radius: 5px;
        padding: 9px 16px;
        font-weight: bold;
    }
    QPushButton:hover {
        background-color: #ff7675;
    }
    QPushButton:pressed {
        background-color: #b22222;
    }

    
    QPushButton#DangerButton {
        background-color: #2d2d30;
        color: #ff7675;
        border: 2px solid #d63031;
    }
    QPushButton#DangerButton:hover {
        background-color: #d63031;
        color: #ffffff;
    }
    QPushButton#DangerButton:pressed {
        background-color: #b22222;
    } """


class UserProfileDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Task 5 Window")

        layout = QVBoxLayout()
        form_layout = QFormLayout()

        self.name_ipt = QLineEdit()
        self.role_ipt = QLineEdit()

        form_layout.addRow("Ім'я користувача: ", self.name_ipt)
        form_layout.addRow("Роль: ", self.role_ipt)

        self.button_box = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel)
        self.button_box.accepted.connect(self.accept)
        self.button_box.rejected.connect(self.reject)

        layout.addLayout(form_layout)
        layout.addWidget(self.button_box)
        self.setLayout(layout)

    def get_data(self):
        return {
            "name": self.name_ipt.text().strip(),
            "role": self.role_ipt.text().strip()
        }



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Task 5 Window!")
        self.resize(570, 450)

        central_widget = QWidget()
        self.main_layout = QVBoxLayout()
        central_widget.setLayout(self.main_layout)
        self.setCentralWidget(central_widget)

        self.inf_label = QLabel("Профіль порожній")
        self.main_layout.addWidget(self.inf_label)

        self.btn_msg = QPushButton("Підтвердити дію")
        self.btn_msg.setObjectName("DangerButton")
        self.main_layout.addWidget(self.btn_msg)


        self.btn_inp = QPushButton("Змінити статус (QInputDialog)")
        self.main_layout.addWidget(self.btn_inp)

        self.btn_cus = QPushButton("Редагувати профіль (QDialog)")
        self.main_layout.addWidget(self.btn_cus)

        self.btn_msg.clicked.connect(self.show_confirm_dialog)
        self.btn_inp.clicked.connect(self.show_inp_dialog)
        self.btn_cus.clicked.connect(self.show_custom_dialog)

    def show_confirm_dialog(self):
        rep = QMessageBox.question(self,"Підтвердження",  "Ви дійсно хочете виконати дію?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        if rep == QMessageBox.StandardButton.Yes:
            self.inf_label.setText("Дію підтверджено")
        else:
            self.inf_label.setText("Дію скасовано")


    def show_inp_dialog(self):
        text, ok = QInputDialog.getText(self, "Зміна статусу", "Введіть новий статус")
        if ok and text:
            self.inf_label.setText(f"Новий статус: {text}")

    def show_custom_dialog(self):
        dialog = UserProfileDialog(self)
        if dialog.exec() == QDialog.DialogCode.Accepted:
            data = dialog.get_data()
            self.inf_label.setText(f"Профіль: {data['name']} ({data['role']})")



if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet(STYLE_SHEET)  
    window = MainWindow()
    window.show()
    sys.exit(app.exec())