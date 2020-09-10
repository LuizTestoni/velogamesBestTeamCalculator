from bs4 import BeautifulSoup
import requests

import sys
sys.path.insert(1, "./model")

from rider import Rider

LIST_RIDERS_URL = "https://www.velogames.com/tirreno-adriatico/2020/riders.php"
#LIST_RIDERS_URL = "https://www.velogames.com/dauphine/2020/riders.php"
#LIST_RIDERS_URL = "https://www.velogames.com/tour-down-under/2020/riders.php"
# LIST_RIDERS_URL = "https://www.velogames.com/great-big-bike-game/2020/riders.php"

def getListOfRiders():
    html = requests.get(LIST_RIDERS_URL).content
    soup = BeautifulSoup(html, 'html.parser')

    listOfRiders = []

    for tableRows in soup.find_all('tr')[1:]:
        tableCels = tableRows.find_all('td')

        # Some games do not use the Class of the rider
        if (len(tableCels) > 5):
            listOfRiders.append(Rider(tableCels[1].text, tableCels[2].text, tableCels[3].text, int(tableCels[4].text), int(tableCels[5].text)))
        else:
            listOfRiders.append(Rider(tableCels[1].text, tableCels[2].text, "", int(tableCels[3].text), int(tableCels[4].text)))

    return listOfRiders
    