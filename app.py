
from PySide2.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QComboBox, QLineEdit, QPushButton
from PySide2.QtGui import QIcon
from PySide2.QtCore import QTimer
import time

from utils import get_date, extract_data, save_data, save_backup, add_set, get_data, get_all_exercices, get_types, get_exercices, get_save

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.data = extract_data("./data.json")
        self.date = get_date()
        self.setWindowTitle("Workout Tracker")
        self.setIcon()
        self.left = 900
        self.top = 300
        self.width = 500
        self.height = 700
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setup_ui()
        self.set_connections()
        self.set_types_choice()
        
    def setup_ui(self):
        # Layout creation
        self.layout = QVBoxLayout(self)
        
        # Widget creation
        self.label_title_part1 = QLabel("Voir les dernières séances")
        self.cb_choice_seance = QComboBox()
        self.label_data = QLabel("")
        self.label_title_part2 = QLabel("Ajouter des données")
        self.label_message = QLabel("")
        self.date_input = QLineEdit()
        self.date_input.setText(self.date)
        self.cb_choice_seance2 = QComboBox()
        self.cb_choice_exercice = QComboBox()
        self.label_reps = QLabel("Répétitions")
        self.rep_input = QLineEdit()
        self.label_weight = QLabel("Poids")
        self.weight_input = QLineEdit()
        self.btn_add = QPushButton("Ajouter")
        
        
        # setting widgets css
        self.label_title_part1.setStyleSheet("font-size: 20px")
        self.label_title_part2.setStyleSheet("font-size: 20px")
        self.label_data.setStyleSheet("font-size: 15px")
        self.label_reps.setStyleSheet("font-size: 15px")
        self.label_weight.setStyleSheet("font-size: 15px")
        
        
        
        
        # adding widgets to layout
        self.layout.addWidget(self.label_title_part1)
        self.layout.addWidget(self.cb_choice_seance)
        self.layout.addWidget(self.label_data)
        self.layout.addWidget(self.label_title_part2)
        self.layout.addWidget(self.label_message)
        self.layout.addWidget(self.date_input)
        self.layout.addWidget(self.cb_choice_seance2)
        self.layout.addWidget(self.cb_choice_exercice)
        self.layout.addWidget(self.label_reps)
        self.layout.addWidget(self.rep_input)
        self.layout.addWidget(self.label_weight)
        self.layout.addWidget(self.weight_input)
        self.layout.addWidget(self.btn_add)
        
        
        
    def set_connections(self):
        self.cb_choice_seance.activated.connect(self.display_data)
        self.cb_choice_seance2.activated.connect(self.display_exercices)
        self.btn_add.clicked.connect(self.add_data)
        
    def reset_message(self):
        self.label_message.setText("")
        
    def set_message(self, message, color):
        self.label_message.setStyleSheet(f"color: {color}")
        self.label_message.setText(message)
        QTimer.singleShot(2000, self.reset_message)    
        
    
    
    def add_data(self):
        date = self.date_input.text()
        seance_type = self.cb_choice_seance2.currentText()
        exercice = self.cb_choice_exercice.currentText()
        reps = int(self.rep_input.text())
        weight = float(self.weight_input.text())
        try:
            add_set(self.data, date, seance_type, exercice, reps, weight)
            self.set_message(f"Données ajoutées pour l'exercice {exercice}", "green")
            
        except Exception as e:
            self.set_message(f"Erreur lors de l'ajout : {e}", "red")
            return
        save_data(self.data, "./data.json")
        save_backup(self.data, date)
        self.rep_input.clear()
        self.weight_input.clear()
        self.display_data()
        
    def display_exercices(self):
        seance_type = self.cb_choice_seance2.currentText()
        exercices = get_exercices(self.data, seance_type)
        self.cb_choice_exercice.clear()
        for exercice in exercices:
            self.cb_choice_exercice.addItem(exercice)
        
    def display_data(self):
        seance_type = self.cb_choice_seance.currentText()
        text = "-"* 10 + "\n"
        save = get_save(self.data, seance_type)
        for exercice in save:
            text += exercice + "\n" + "\n"
            for info in save[exercice]:
                text += f"{info} : {save[exercice][info]}\n"
            text += "-"* 10 + "\n"
                
        self.label_data.setText(text)
        
        
    def setIcon(self):
        appIcon = QIcon("./images/icon.png")
        self.setWindowIcon(appIcon)
        
    def set_types_choice(self):
        types = get_types(self.data)
        for type in types:
            self.cb_choice_seance.addItem(type)
            self.cb_choice_seance2.addItem(type)
        
        

if __name__ == '__main__':
    app = QApplication([])
    win = App()
    win.show()
    app.exec_()