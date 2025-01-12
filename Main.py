import sys
import GUI  # Importiert GUI
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QLineEdit, QPushButton, QVBoxLayout, QWidget, QComboBox, QLabel, QTextBrowser, QMessageBox, QShortcut, QHeaderView
from PyQt5.QtGui import QKeySequence, QStandardItem, QStandardItemModel, QColor
from PyQt5.QtCore import QTimer
from functools import partial
import os
import time


#Imports aus anderen .py Skripten
# from modul_1 import function_Beispiel_1

#######################################################
#                   Load your GUI
########################################################
class UI(QMainWindow, GUI.Ui_MainWindow):
    def __init__(self, parent=None):
        super(UI, self).__init__(parent)
        self.setupUi(self)

        #######################################################
        #           Connect Buttons, Text, Widgets etc.
        ########################################################
        # Überschrift
        version = "V.0.4.0"
        self.setWindowTitle(f"Star Craft II Build Timer {version}")  # Fenstertitel

        # Tool Tab
        self.btn_Timer_Start.clicked.connect(self.function_start)
        self.btn_Timer_Stop.clicked.connect(self.function_stop)
        self.btn_Timer_Reset.clicked.connect(self.function_reset)
        self.comboBox_Races.currentIndexChanged.connect(self.update_list)
        self.listWidget_builds.itemClicked.connect(self.on_item_selected)

        self.btn_Timer_Start.setEnabled(False)  # Button initial deaktivieren
        self.btn_Timer_Stop.setEnabled(False)  # Button initial deaktivieren
        self.btn_Timer_Reset.setEnabled(False)  # Button initial deaktivieren

        # ProgressBar initialisieren
        self.progressBar_TimeSinceStart.setMinimum(0)
        self.progressBar_TimeSinceStart.setMaximum(100) # Placeholder, wird in function_start aktualisiert

        # Übergabevariablen initialisieren
        self.current_built = None

        # Initialisierung - Laden aller verfügbaren Builds in ComboBox und Liste
        self.data = self.read_textfiles_from_subfolders()
        self.comboBox_Races.addItems(self.data.keys())

        # Timer initialisieren
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_timer)
        self.time_elapsed = 0  # Zeit in Sekunden

        # Shortcuts Start / Stop / Reset
        shortcut_start = QShortcut(QKeySequence("F9"), self)
        shortcut_start.activated.connect(self.function_start)
        shortcut_stop = QShortcut(QKeySequence("F10"), self)
        shortcut_stop.activated.connect(self.function_stop)
        shortcut_reset = QShortcut(QKeySequence("F11"), self)
        shortcut_reset .activated.connect(self.function_reset)
    ########################################################
    #                   Declare Function
    ########################################################

    def on_item_selected(self, item):
        # Wenn ein Item aus der Liste ausgewählt wird
        self.selected_item = item.text()
        # Hole den Wert aus dem Dictionary für den aktuell ausgewählten Eintrag
        self.current_built = self.data[self.selected_value][self.selected_item]
        self.btn_Timer_Start.setEnabled(True)
        self.label_loaded_built.setText(self.selected_item)
        #print(self.selected_item)
        #print(self.current_built)

    def update_list(self):
        # Bei Wechsel des Dropdown -> Liste leeren und mit neuen Einträgen der jeweiligen Rasse hinzufügen
        self.selected_value = self.comboBox_Races.currentText()
        self.listWidget_builds.clear()
        self.listWidget_builds.addItems(self.data[self.selected_value].keys())  # bei jede

    def update_timer(self):
        # Zeit aktualisieren
        self.time_elapsed += 1
        minutes = self.time_elapsed // 60
        seconds = self.time_elapsed % 60
        current_time_str = f"{minutes}:{seconds:02}"  # Formatierte Zeit <min:sec>

        # Vergleich der aktuellen Zeit mit der Liste
        if self.current_index < len(self.timer_min_sec):  # Sicherstellen, dass der Index gültig ist
            next_time = self.timer_min_sec[self.current_index]
            next_minutes, next_seconds = map(int, next_time.split(":"))
            next_total_seconds = next_minutes * 60 + next_seconds

            # Differenzzeit berechnen
            remaining_seconds = max(next_total_seconds - self.time_elapsed, 0)
            remaining_minutes = remaining_seconds // 60
            remaining_seconds %= 60
            remaining_time_str = f"{remaining_minutes}:{remaining_seconds:02}"

            # Update TextBrowser für Differenzzeit
            self.textBrowser_timer.setText(remaining_time_str)

            # Nächstes zu bauendes Objekt anzeigen
            self.textBrowser_object.setText(self.built_object[self.current_index])

            # Aktion ausführen, wenn die aktuelle Zeit das nächste Bau-Event erreicht
            if self.time_elapsed == next_total_seconds:
                print(f"Zeit erreicht: {current_time_str}. Ausführen: {self.built_object[self.current_index]}")

                # Update der Anzeige des gerade erreichten Objekts
                self.textBrowser_probe_nr.setText(f"{self.worker_nr[self.current_index]}")

                # Index für das nächste Event erhöhen
                self.current_index += 1

        else:  # Wenn das Ende der Liste erreicht ist, stoppe den Timer
            self.function_stop()

        # Update ProgressBar
        self.progressBar_TimeSinceStart.setValue(self.time_elapsed)
        self.label_current_time.setText(current_time_str)

        # Aktualisiere das TableView mit der grünen Markierung
        self.populate_table_view()

    def function_start(self):
        # Timer Start/Resume
        print("Funktion function_start aktiv")

        # Sichtbarkeit der Buttons aktivieren/deaktivieren
        self.btn_Timer_Start.setEnabled(False)
        self.btn_Timer_Stop.setEnabled(True)
        self.btn_Timer_Reset.setEnabled(True)

        print(rf"Starte Timer für Built: {self.selected_item}")

        # Listen zur Speicherung der Ergebnisse aus self.current_built
        self.worker_nr = []
        self.timer_min_sec = []
        self.built_object = []

        # Daten verarbeiten
        lines = self.current_built.strip().split("\n")  # Entfernt überflüssige Leerzeilen und splittet die Zeilen
        for line in lines:
            parts = line.split("\t")  # Teile die Zeile anhand von Tabulatoren auf
            if len(parts) >= 3:  # Sicherstellen, dass die Zeile mindestens 3 Spalten hat
                self.worker_nr.append(int(parts[0].strip()))  # Erste Zahl in die Liste #worker
                self.timer_min_sec.append(parts[1].strip())  # Entfernt Leerzeichen vor der Zeit
                self.built_object.append(parts[2].lstrip())  # Entfernt Leerzeichen vor dem Objekt

        # Index initialisieren
        self.current_index = 0

        # Ergebnisse ausgeben
        print("Worker nr:", self.worker_nr)
        print("timer_min_sec:", self.timer_min_sec)
        print("built_object:", self.built_object)

        # Set maximum value for ProgressBar
        last_time = self.timer_min_sec[-1]
        minutes, seconds = map(int, last_time.split(":"))
        self.progressBar_TimeSinceStart.setMaximum(minutes * 60 + seconds + 1)

        # Initialanzeige des nächsten Bau-Objekts, der Differenzzeit und der Worker-Zahl
        if self.timer_min_sec:
            # Nächste Zeit berechnen
            next_minutes, next_seconds = map(int, self.timer_min_sec[0].split(":"))
            next_total_seconds = next_minutes * 60 + next_seconds
            remaining_seconds = max(next_total_seconds - self.time_elapsed, 0)
            remaining_minutes = remaining_seconds // 60
            remaining_seconds %= 60
            remaining_time_str = f"{remaining_minutes}:{remaining_seconds:02}"

            # Anzeigen
            self.textBrowser_timer.setText(remaining_time_str)  # Differenzzeit bis zum nächsten Objekt anzeigen
            self.textBrowser_object.setText(self.built_object[0])  # Erstes Bau-Objekt anzeigen
            self.textBrowser_probe_nr.setText(str(self.worker_nr[0]))  # Anzahl der Worker anzeigen

        # Neuer Code: Fülle das TableView mit den Daten
        self.populate_table_view()

        # Timer starten
        self.timer.start(1000)  # Timer alle 1000 ms (1 Sekunde) auslösen
        self.time_elapsed = 0  # Zurücksetzen der Zeit

    def function_stop(self):
        # Timer Stop
        print("Funktion function_stop aktiv")
        # Sichtbarkeit der buttons aktivieren / deaktivieren
        self.btn_Timer_Start.setEnabled(True)
        self.btn_Timer_Stop.setEnabled(False)
        self.btn_Timer_Reset.setEnabled(True)

        # Timer stoppen
        self.timer.stop()

    def function_reset(self):
        # Timer Reset
        print("Funktion function_reset aktiv")
        # Sichtbarkeit der buttons aktivieren / deaktivieren
        self.btn_Timer_Start.setEnabled(True)
        self.btn_Timer_Stop.setEnabled(False)
        self.btn_Timer_Reset.setEnabled(False)

        # Timer stoppen und Zeit zurücksetzen
        self.timer.stop()
        self.time_elapsed = 0
        self.textBrowser_timer.clear()  # TextBrowser zurücksetzen

    def read_textfiles_from_subfolders(self):
        data = {}

        # Durchläuft alle Unterordner im aktuellen Verzeichnis
        for foldername in os.listdir('.'):
            if os.path.isdir(foldername):
                folder_data = {}
                # Durchläuft alle Dateien im Unterordner
                for filename in os.listdir(foldername):
                    if filename.endswith(".txt"):
                        file_path = os.path.join(foldername, filename)
                        try:
                            with open(file_path, 'r', encoding='utf-8') as file:
                                folder_data[filename] = file.read()
                        except Exception as e:
                            print(f"Fehler beim Lesen der Datei {file_path}: {e}")
                # Wenn im Ordner Textdateien vorhanden sind, wird das Dictionary gespeichert
                if folder_data:
                    data[foldername] = folder_data

        if data:
            #self.btn_Timer_Start.setEnabled(True)
            print("Builds Available")
        else:
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Warning)
            msg_box.setWindowTitle("Warnung")
            msg_box.setText("Keine Buildfiles gefunden")
            msg_box.setStandardButtons(QMessageBox.Ok)
            msg_box.exec_() # Fenster anzeigen
        return data

    def populate_table_view(self):
        # Neues Model für das TableView erstellen
        model = QStandardItemModel()

        # Setze die Header (Spaltenüberschriften)
        model.setHorizontalHeaderLabels(["Time", "Worker", "Objekt"])

        # Füge die Daten in das Model ein
        for i in range(len(self.timer_min_sec)):
            row = [
                QStandardItem(self.timer_min_sec[i]),
                QStandardItem(str(self.worker_nr[i])),
                QStandardItem(self.built_object[i])
            ]
            model.appendRow(row)

            # Wenn diese Zeile die aktuelle Zeile ist, grün markieren
            if i == self.current_index:
                for column in range(3):  # Wir haben 3 Spalten (Zeit, Worker, Bau-Objekt)
                    item = model.item(i, column)
                    item.setBackground(QColor(0, 255, 0))  # Setze Hintergrund auf grün

        # Setze das Model in das TableView
        self.tableView.setModel(model)
        # Zugriff auf den horizontalen Header
        header = self.tableView.horizontalHeader()

        # Passe die Breite der Spalten an
        header.setSectionResizeMode(0, QHeaderView.ResizeToContents)  # "Time" Spalte
        header.setSectionResizeMode(1, QHeaderView.ResizeToContents)  # "Worker #" Spalte
        header.setSectionResizeMode(2, QHeaderView.Stretch)          # "Objekt" Spalte

#######################################################
#                   Main Function
########################################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    PyWindow = UI()
    PyWindow.show()
    app.exec_()
