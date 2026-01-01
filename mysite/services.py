from models import Stat, Car
from content import SITE_CONTENT

def get_stats():
    return [Stat(s["label"], s["value"]) for s in SITE_CONTENT["stats"]]

def get_cars():
    return [Car(c["name"], c["description"]) for c in SITE_CONTENT["cars"]]
