import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, 
    QLineEdit, QSpinBox, QPushButton, QLabel, QGroupBox, QMainWindow
)
from PyQt6.QtCore import pyqtSignal


class ControlPanel(QWidget):
    message_sent = pyqtSignal(str)
    counter_upd = pyqtSignal(int, str)

    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        group = QGroupBox("Панель керування (Джерело даних)")
        group_layout = QVBoxLayout()

        self.text_input = QLineEdit()
        self.text_input.setPlaceholderText("Введіть повідомлення...")
        self.btn_send_text = QPushButton("Надіслати текст")

        self.spin_box = QSpinBox()
        self.spin_box.setRange(1, 100)
        self.spin_box.setValue(19)

        group_layout.addWidget(QLabel("Текстове повідомлення:"))
        group_layout.addWidget(self.text_input)
        group_layout.addWidget(self.btn_send_text)
        group_layout.addWidget(QLabel("Значення лічильника:"))
        group_layout.addWidget(self.spin_box)
        
        group.setLayout(group_layout)
        layout.addWidget(group)
        self.setLayout(layout)

        self.btn_send_text.clicked.connect(self.emit_message)
        self.spin_box.valueChanged.connect(self.emit_counter)

    def emit_message(self):
        text = self.text_input.text().strip()
        if text:
            self.message_sent.emit(text)

    def emit_counter(self, value):
        status = "Високий рівень" if value > 50 else "Нормальний рівень"
        self.counter_upd.emit(value, status)


class DisplayPanel(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        group = QGroupBox("Панель керування (Приймач даних)")
        group_layout = QVBoxLayout()

        self.msg_label = QLabel("Отримане повідомлення: (немає даних)")
        self.msg_label.setWordWrap(True)

        self.counter_label = QLabel("Стан лічильника: (немає даних)")

        group_layout.addWidget(self.msg_label)
        group_layout.addWidget(self.counter_label)

        group.setLayout(group_layout)
        layout.addWidget(group)
        self.setLayout(layout)

    def show_message(self, text: str):
        self.msg_label.setText(f"Отримане повідомлення:\n» {text}")

    def update_counter_display(self, val: int, status: str):
        self.counter_label.setText(f"Стан лічильника: {val} ({status})")


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Task 4 Window")
        self.resize(550, 450)

        central_widget = QWidget()
        main_layout = QVBoxLayout()

        self.control_panel = ControlPanel()
        self.display_panel = DisplayPanel()

        self.btn_toggle_signals = QPushButton("Злушити/Заблокувати сигнали (blockSignals)")
        self.btn_toggle_signals.setCheckable(True)
        self.btn_toggle_signals.toggled.connect(self.toggle_signal_blocking)

        main_layout.addWidget(self.control_panel)
        main_layout.addWidget(self.btn_toggle_signals)
        main_layout.addWidget(self.display_panel)

        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

        self.control_panel.message_sent.connect(self.display_panel.show_message)
        self.control_panel.counter_upd.connect(self.display_panel.update_counter_display)

    def toggle_signal_blocking(self, is_blocked):
        self.control_panel.blockSignals(is_blocked)
        
        if is_blocked:
            self.btn_toggle_signals.setText("Відновити передачу сигналів")
            self.statusBar().showMessage("Сигнали компонента ControlPanel заблоковано!")
        else:
            self.btn_toggle_signals.setText("Заглушити/Заблокувати сигнали (blockSignals)")
            self.statusBar().showMessage("Передачу сигналів відновлено.")



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())