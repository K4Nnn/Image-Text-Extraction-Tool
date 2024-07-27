from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget

def say_hello():
    label.setText("Hello, PyQt!")

app = QApplication([])
window = QWidget()
window.setWindowTitle('PyQt Example')

layout = QVBoxLayout()
label = QLabel('Click the button')
layout.addWidget(label)

button = QPushButton('Click Me')
button.clicked.connect(say_hello)
layout.addWidget(button)

window.setLayout(layout)
window.show()

app.exec_()
