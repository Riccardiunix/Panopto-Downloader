import pickle
import utils
import sys

if len(sys.argv) == 1:
    print("Aggiungi almeno una URL del video che vuoi scaricare")

#-- Login
driver = utils.get_driver()

#-- Analizzo i link delle lezione per estrarre gli stream
utils.get_links_video(driver, sys.argv[1:])

driver.quit()
