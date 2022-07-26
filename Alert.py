import email
import smtplib
from email.message import EmailMessage
import random
import math
import tkinter as tk 
import time
import requests
from bs4 import BeautifulSoup
#https://www.phonecarriercheck.com/   to look up carrier of phone numbers
# 
# #Quotes
quotes=["Let them win?","Ya just be wasteful","They have you beat","Ugly people are doing better than you"," Do not let them win","Don't dissapoint your family","DO NOT LET THEM WIN","People are getting stuff done and you are not don't allow it"]
txt= random.choice(quotes) 
gov="Alert!"
threat="The Person you tried to no caller id is done with your SHENNENIGANS that it made a bot to spam you"
apologize="Apologize accordingly by texting the individual or suffer the consequences.... do not respond to this text message"
notxt="This user does not recieve text messages.(1800 usr error)"



#Ap web scraper

source = requests.get("https://apnews.com/")
soup = BeautifulSoup(source.text,"html.parser")
#print(soup.prettify())
tables = soup.find_all(class_="featured-link")
#Gets the trending links and text from AP
  
  #From Weather api
api = "http://api.openweathermap.org/data/2.5/weather?q=Fairfax&appid=413bd3297369e8a7924ae10cf4d30a6a" #Uses website link plus city 
json_data = requests.get(api).json()
condition = json_data['weather'][0]['main']
temp = int((json_data['main']['temp'] - 273.15)*(9/5)+32) #Temp curently
min_temp = int((json_data['main']['temp_min'] - 273.15)*(9/5)+32) # Low
max_temp = int((json_data['main']['temp_max'] - 273.15)*(9/5)+32) #High
feels_temp = int((json_data['main']['feels_like'] - 273.15)*(9/5)+32) #What it feels like
humidity = json_data['main']['humidity'] #Humidity
pressure = json_data['main']['pressure'] #Didn't include it but pressure
wind = (json_data['wind']['speed']*2.23694) #Converted mps to mph
#Need to add sunset/rise but don't know how w daylight savings

final_info = condition + "\n" + str(temp)+ " Degrees"
final_data = "\n"+ "Max Temp: " + str(max_temp)+ " Degrees" + "\n" + "Min Temp: " + str(min_temp)+" Degrees" + "\n" + "Feels Like: " + str(feels_temp)+" Degrees" + "\n" + "Humidity: "+ str(humidity)+"%" +"\n" + "Wind Speed: " + str(wind)[0:4] + "mph"


def email_alert(body, to):
    msg = EmailMessage()
    msg.set_content(body)
   # msg['subject'] = subject 
    msg['to'] = to

    user = " "  #email that sends message (Blank for security purposes)
    msg['from']=user      
    password = ""   #App given password (Blank for security purposes)

    server = smtplib.SMTP("smtp.gmail.com", 587) 
    server.starttls()
    server.login(user,password)
    server.send_message(msg)
    server.quit()

  
if __name__ == '__main__':
  email_alert(txt,#Phonenumber email)
  email_alert(final_data,#Phonenumber email)
  for t in tables:
    email_alert(t.text,#Phonenumber email)
    email_alert(t["href"],#Phonenumber email)
    time.sleep(3)
    
#tmomail.net is tmobile
#@vtext.com is verizon
#https://www.phonecarriercheck.com/   to look up carriers
