import subprocess
import os
import shutil


def convert_ui_to_py():
    """Konvertiert die .ui-Datei in eine .py-Datei."""
    ui_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "GUI", "GUI.ui")
    output_py_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "GUI.py")

    if not os.path.exists(ui_file):
        print(f"UI-Datei nicht gefunden: {ui_file}")
        return

    try:
        command = ["pyuic5", ui_file, "-o", output_py_file]
        subprocess.run(command, check=True)
        print(f"UI-Datei erfolgreich konvertiert: {output_py_file}")
    except subprocess.CalledProcessError as e:
        print(f"Fehler beim Konvertieren der UI-Datei: {e}")
    except FileNotFoundError:
        print("pyuic5 ist nicht installiert oder nicht im PATH verfügbar. Bitte installiere PyQt5.")


def build_exe():
    """Erstellt eine ausführbare Datei mit PyInstaller."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    command = [
        "pyinstaller",
        "--onefile",
        "--noconsole",
        f"--icon={os.path.join(script_dir, 'Data', 'Icons', 'sc2_thumbnail.ico')}",
        "Main.py"
    ]

    try:
        subprocess.run(command, check=True)
        print("Build erfolgreich abgeschlossen.")
    except subprocess.CalledProcessError as e:
        print(f"Fehler beim Build: {e}")
    except FileNotFoundError:
        print("PyInstaller ist nicht installiert. Bitte installiere es mit 'pip install pyinstaller'.")


def clean_up():
    """Verschiebt die .exe-Datei ins Hauptverzeichnis, löscht Build-Ordner und Spezifikationsdateien."""
    base_dir = os.path.dirname(os.path.abspath(__file__))
    dist_dir = os.path.join(base_dir, "dist")
    build_dir = os.path.join(base_dir, "build")

    # Verschiebe die .exe-Datei ins Hauptverzeichnis
    if os.path.exists(dist_dir):
        for file in os.listdir(dist_dir):
            if file.endswith(".exe"):
                exe_file = os.path.join(dist_dir, file)
                target_path = os.path.join(base_dir, file)
                try:
                    shutil.move(exe_file, target_path)
                    print(f"Exe-Datei verschoben nach: {target_path}")
                except Exception as e:
                    print(f"Fehler beim Verschieben der .exe-Datei: {e}")
                    return

    # Lösche Build- und Dist-Ordner
    for folder in [build_dir, dist_dir]:
        if os.path.exists(folder):
            try:
                shutil.rmtree(folder)
                print(f"Ordner gelöscht: {folder}")
            except Exception as e:
                print(f"Fehler beim Löschen des Ordners {folder}: {e}")

    # Lösche alle .spec-Dateien im Hauptverzeichnis
    for file in os.listdir(base_dir):
        if file.endswith(".spec"):
            spec_file = os.path.join(base_dir, file)
            try:
                os.remove(spec_file)
                print(f"Spezifikationsdatei gelöscht: {spec_file}")
            except Exception as e:
                print(f"Fehler beim Löschen der Spezifikationsdatei {spec_file}: {e}")


if __name__ == "__main__":

    # Schritt 1: UI-Datei konvertieren
    convert_ui_to_py()

    # Schritt 2: Exe-Datei erstellen
    build_exe()

    # Schritt 3: Aufräumen
    clean_up()
