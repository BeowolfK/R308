"""
@author: meylan
Question 9 TP2
classe
"""

import math

class Time:
    def __init__(self, timestamp):
        self.timestamp = timestamp
    
    def affiche_heure(self):
        heure = math.floor(self.timestamp % 86400 / 3600)
        minute = math.floor(self.timestamp % 3600 / 60)
        seconds = self.timestamp % 60
        print(f"Timestamp : {self.timestamp}\nSeconds : {seconds}\nMinute : {minute}\nHeure : {heure}\n")
