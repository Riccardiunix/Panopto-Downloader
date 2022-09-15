import pickle
import core
import sys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
num_videos = 500

if len(sys.argv) == 1:
    print("Aggiungi almeno una URL del video che vuoi scaricare")

#-- Login
driver = core.get_driver()

#-- Accdo e prendo i link dei video delle lezioni nella pagina
list_videos = core.get_lesson_links(driver, num_videos, sys.argv[1])

#-- Analizzo i link delle lezione per estrarre gli stream
core.get_links_video(driver, list_videos)

driver.quit()