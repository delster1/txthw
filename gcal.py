from __future__ import print_function

import datetime
import os.path
from pprint import pprint
from Google import create_service, convert_to_RFC_datetime
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
SCOPES=['https://www.googleapis.com/auth/calendar']

creds = None
if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
if not creds or not creds.valid:
	if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
	else:
		flow = InstalledAppFlow.from_client_secrets_file(
			'credentials.json', SCOPES)
		creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
	with open('token.json', 'w') as token:
		token.write(creds.to_json())

CLIENT_SECRET_FILE='clientSecret.json'
API_NAME='calendar'
API_VERSION='v3'

service = build('calendar', 'v3', credentials=creds)
hourAdjustment = +5
#create an event
# colors = service.colors().get().execute()
# google calendar name
request_body = {
	'summary':'txthw tasks'
}
# code for creating events
def createEvent(inputDict,inputstr):
	minute = int(inputDict['time'][3:])

	# tests if hour is over 20 b/c of stupid gcal time functions
	hour = int(inputDict['time'][:2])
	print("Hour: ", hour, " \n")
	if hour > 20 and hour != 24:

		hour = hour - 19
		inputDict['date'] += 1
	elif hour == 24:

		hour = 5
		
		
	else:
		hour += hourAdjustment
	# setting up event w times etc
	event_request_body = {
		'start':{
			'dateTime': convert_to_RFC_datetime(inputDict['year'],inputDict['month'],inputDict['date'],hour,minute),
			'timeZone': 'America/Chicago'
		},
		'end':{
			'dateTime': convert_to_RFC_datetime(inputDict['year'],inputDict['month'],inputDict['date'],hour,minute+1),
			'timeZone': 'America/Chicago'

		},
		'colorId': 5,
		'summary':inputstr
	}
	start_datetime =  convert_to_RFC_datetime(inputDict['year'],inputDict['month'],inputDict['date'],hour,int(inputDict['time'][3:]))
	end_datetime =  convert_to_RFC_datetime(inputDict['year'],inputDict['month'],inputDict['date'],hour,int(inputDict['time'][3:])+1)
	calendarID='efldnativihpigrme4da9bq19c@group.calendar.google.com'

	response = service.events().insert(calendarId=calendarID, maxAttendees=1,sendNotifications=True,sendUpdates='none',body=event_request_body).execute()
	eventID = response['id']

	response['start']['datetime'] = start_datetime
	print(response['start']['datetime'])
	response['end']['datetime'] = end_datetime
	response['summary'] = inputstr
	print(response)
	service.events().update(
		calendarId=calendarID, eventId = eventID, body=response
	).execute()

