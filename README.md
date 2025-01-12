![License](https://img.shields.io/badge/license-MIT-blue.svg)


##############################################
Python Programm für StarCraft 2 Buildorders
##############################################
Die Buildorders werden im Format entsprechend
https://lotv.spawningtool.com/build/184604/
als Textfile erzeugt

Bei Programmstart sollen alle Textdateien aus den Subordnern des aktuellen Verzeichnisses eingelesen und in Dictionaries gespeichert werden,
wobei der Name des Dictionaries dem Namen des jeweiligen Ordners entspricht.
Der Name der Textdateien wird als Schlüssel (key) und der Inhalt als Wert (value) im Dictionary gespeichert.

Das Programm soll Hauptfunktionen haben:
- Timer Start / Resume
- Timer Stop
- Timer Reset

Der Timer soll dabei eine Buildorder für die Klassen aus Star Craft 2 (Protoss, Zerg oder Terraner) darstellen können. Der Timer soll im Format <min:sek> gestartet werden.
Die Buildorder befindet sich in den Textdateien der jeweiligen Subordner des aktuellen Verzeichnisses.
Die Beschreibung der Buildorder soll in folgendem Format stattfinden:
"""
  14	  0:18	  Pylon	  
  15	  0:38	  Gateway	  
  16	  0:47	  Assimilator
"""

Die erste lesbare Zahl jeder Zeile Beschreibt die Anzahl der aktuellen im Spiel befindlichen "Probes" und dient als Vergleich
Die Zweite lesbare Zahl jeder Zeile entspricht dabei der Zeit im Format <min:sek>.
Der Text am Ende jeder Zeile beschreibt das Build-Objekt welches gebaut werden soll.
  
Nachdem der Timer gestartet wurde, soll die Buildorder Zeile für Zeile durchiteriert werden. Dabei soll die aktuelle Zeit des Timers mit der Zeit <min:sek> des Buildorders verglichen werden. 
Wenn die Zeit des Buildorders erreicht wurde soll die Anzahl der Probes der Zeit und der Text des Objektes in der Konsole angezeigt werden. 
Darüber hinaus soll erst das Erreichen der Zeit in der Buildorder dazu führen, dass die 

##############################################
			Anforderungen an GUI
##############################################
	
-Dropdownauswahl aus Protoss, Zerg und Terranerbuild
-Auflistung der gefundenen Builts in ausklappbaren Treeview. Bei Klick auf das Item im Treeview soll diese Builtorder geladen werden.
- Jeweils ein Button für 
	- Timer Start / Resume
	- Timer Stop
	- Timer Reset
- Es soll eine Timer Leiste geben bis zum nächsten Buildorder
- Außerdem soll es Zwei Ausgabe geben
	- die Erste soll die aktuelle Anweisung der "Probe | Zeit | Text" ausgeben
	- die Zweite soll die nächste Anweisung der "Probe | Zeit | Text" ausgeben

##############################################
			Zusatzanforderungen:
##############################################
- Favoritenliste für beliebteste Builds
- 2 Sekunden bevor eine neue  Buildanweisung stattfindet soll eine Audiosignal ertönen
- Das Audio Signal soll über Tastatureingabe gemutet werden können 
- Die Funktionen sollen über Tastatureingaben <Druck> <Pos1> und <Bild Up> als Makro gestartet werden können.
- Umwandlung in Windowsfähige Exe
	Installer Code
	
	GUI:
	pyuic5 .\GUI\GUI.ui -o GUI.py

	EXE:
	pyinstaller --onefile --noconsole --icon=your_icon.ico your_script.py
	pyinstaller --onefile --noconsole --icon=Logo.ico Main.py

##############################################
			Logfile:
##############################################
Version V 0.4.0
	Überarbeitung in function populate_table_view:
	- Spaltenbreit in table_view an breite des inhaltes anpassen

Version V 0.4.1
	Überarbeitung in function populate_table_view:
	- Orientierung der Grünen aktiven Zeile ab Objekt Nr. 3 immer an 3. Stelle scrollen

Konstruktor
	- Progressbar initialisiert auf 0

Version V.0.4.2 (Bisher nur Development Branch)
	- Hotkeys über Library "keyboard" und pytqt Modul QThread implementiert
