# This script checks for the current time period to report.
# It asks until when time needs to be tracked and based on that
# information it will shuffle activities and report them in excel.

import datetime
import os
import random
import time
import pandas as pd

# Get the file context
file = os.path.join(os.path.dirname(__file__), 'activities.xlsx') #TODO: select Niklas Reiter

# Set the user config

my_workdays = ['Monday', 'Tuesday', 'Wednesday']

my_workhours = {
    'Monday': ['08:00', '18:00'],
    'Tuesday': ['08:00', '16:00'],
    'Wednesday': ['09:00', '13:00']
}

activity_blocks = {
    'Monday': ['08:00', '10:00'],
    'Monday': ['10:00', '12:00'],
    'Monday': ['12:00', '14:00'],
    'Monday': ['14:00', '16:00'],
    'Monday': ['16:00', '18:00'],
    'Tuesday': ['08:00', '10:00'],
    'Tuesday': ['10:00', '12:00'],
    'Tuesday': ['12:00', '14:00'],
    'Tuesday': ['14:00', '16:00'],
    'Wednesday': ['09:00', '11:00'],
    'Wednesday': ['11:00', '13:00'] 
}
my_activities = [
    'Konzeption Framework',
    'Durchführung Experimente',
    'Dokumentation Experimente',
    'Implementierung Showcase Applikation',
    'Literatur Recherche',
    'Research Demo Applikation'
]
# Scan the file for the period to report and ask the user via cli
def getTimePeriod():

    today = datetime.datetime.now()
    last_reported = excel.getLastReported(file)
    new_period = last_reported + datetime.timedelta(days=1)
    new_date_range = new_period.strftime('%d.%m.%Y') + ' - ' + new_period.strftime('%d.%m.%Y')

def getLastReported(file):

    df = pd.read_excel(file)
    date_column = df['Datum (TT.MM.JJJJ)']
    date_column = pd.to_datetime(date_column, errors='coerce')

# def validateTimePeriod(new_date_range):
#     userPrompt = 'Please verify the time period to report : + new_date_range + ' (y/n) : 
#     userResponse = input(userPrompt)
#     return userResponse.lower() == 'y'

# def trackTime():


if __name__ == '__main__':

    getTimePeriod()
    print(getLastReported(file))
