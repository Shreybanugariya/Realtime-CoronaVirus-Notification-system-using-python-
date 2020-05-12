from plyer import notification
import requests
from bs4 import BeautifulSoup
import time

def notifyMe(title, message):
	notification.notify(
		title = title,
		message = message,
		app_icon = None,
		timeout =5
		)

def getData(url):
	r = requests.get(url)
	return r.text

if __name__  ==  "__main__":
	notifyMe("Shrey", "Hey, Updates in Corona Data")
	myHtmlData = getData('https://www.mohfw.gov.in/')

	soup = BeautifulSoup(myHtmlData, 'html.parser')

	myDataStr = ""
	for tr in soup.find_all('tbody')[0].find_all('tr'):
		myDataStr += tr.get_text()

	myDataStr = myDataStr[1:]
	itemList = myDataStr.split("\n\n")
    
	#states = [ 'Gujarat','Uttar Pradesh']
	for item in itemList[0:33]:
		dataList = item.split("\n")
		#if dataList[1] in states:	
		print(dataList)
		nTitle = 'Cases of Covid-19'
		nText = f"{dataList[1]}- Total Cases : {dataList[2]}"
		notifyMe(nTitle, nText)

	#To get notificaton every hour, write time.sleep(3600) 
	#while(true){body}
  # To get details for any specific state remove the comment of line 31 and 34,
  #tab out the following lines. 