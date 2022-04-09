from pprint import pprint
from Google import create_service, convert_to_RFC_datetime

CLIENT_SECRET_FILE='clientSecret.json'
API_NAME='calendar'
API_VERSION='v3'
SCOPES=['https://www.googleapis.com/auth/calendar']

service = create_service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

#create an event 
colors = service.colors().get().execute()
request_body = {
	'summary':'txthw tasks'
}
def createEvent(inputDict,inputstr):
	print(inputDict['time'][:2])
	event_request_body = {
		'start':{
			'dateTime': convert_to_RFC_datetime(inputDict['year'],inputDict['month'],inputDict['date'],int(inputDict['time'][:2]),int(inputDict['time'][3:])),
			'timeZone':  'America/Chicago'
		},
		'end':{
			'dateTime': convert_to_RFC_datetime(inputDict['year'],inputDict['month'],inputDict['date'],int(inputDict['time'][:2]),int(inputDict['time'][3:])+1),
			'timeZone':  'America/Chicago'
		},
		'colorId': 5,
		'summary':inputstr
	}

	start_datetime =  convert_to_RFC_datetime(inputDict['year'],inputDict['month'],inputDict['date'],int(inputDict['time'][:2]),int(inputDict['time'][3:]))	
	end_datetime =  convert_to_RFC_datetime(inputDict['year'],inputDict['month'],inputDict['date'],int(inputDict['time'][:2]),int(inputDict['time'][3:])+1)	

	calendarID='efldnativihpigrme4da9bq19c@group.calendar.google.com'

	response = service.events().insert(calendarId=calendarID, maxAttendees=1,sendNotifications=True,sendUpdates='none',body=event_request_body).execute()
	eventID = response['id']

	response['start']['datetime'] = start_datetime
	response['end']['datetime'] = end_datetime
	response['summary'] = inputstr
	service.events().update(
		calendarId=calendarID, eventId = eventID, body=response
	).execute()