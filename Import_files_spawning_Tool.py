# Stand 11.01.2025 Bisher noch nicht implementiert oder getestet
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def extract_table_to_file(id):
    # Pfad zum WebDriver (passe den Pfad entsprechend an)
    driver_path = "C:\webdrivers"  # Ersetze "path/to/chromedriver" durch deinen tatsächlichen Pfad
    url = rf"https://lotv.spawningtool.com/build/{id}/"

    # Starte den WebDriver
    driver = webdriver.Chrome(driver_path)
    driver.get(url)

    # Gib dem Browser etwas Zeit, um die Seite zu laden
    time.sleep(5)

    try:
        # Finde das Table-Element mit dem angegebenen XPath
        table_element = driver.find_element(By.XPATH, '//*[@id="build-1"]')

        # Extrahiere den Text aus dem Table
        table_text = table_element.text

        # Speichere den Inhalt in eine Textdatei
        with open("table_content.txt", "w", encoding="utf-8") as file:
            file.write(table_text)

        print("Inhalt erfolgreich extrahiert und in 'table_content.txt' gespeichert.")

    except Exception as e:
        print(f"Fehler: {e}")

    finally:
        # Schließe den WebDriver
        driver.quit()

if __name__ == "__main__":
    extract_table_to_file()
