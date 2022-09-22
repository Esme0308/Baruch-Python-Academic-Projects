#Import libaries
from bs4 import BeautifulSoup
import requests


#The Baruch's sports team websites
Baruch_sports_teams = {'mens volleyball team' : 'https://athletics.baruch.cuny.edu/sports/mens-volleyball/roster',
                'mens swim team': 'https://athletics.baruch.cuny.edu/sports/mens-swimming-and-diving/roster',
                'womens volleyball team': 'https://athletics.baruch.cuny.edu/sports/womens-volleyball/roster',
                'womens swim team': 'https://athletics.baruch.cuny.edu/sports/womens-swimming-and-diving/roster'
                }
                
               
#Scrape the website
def scraping_data(team_type, url):

#My two lists  
  raw_height = []
  height_1 =0

#Making my request to the server
  page =requests.get(url)

#Importing the raw html into beautiful soup
  soup = BeautifulSoup(page.content, 'html.parser')

#Collection all of the td tags with a class of height into a single list
  all_relevant_td_tags = soup.find_all('td', class_ ='height' )

#Extracting the contents of the td tags using get_text()
  for height in all_relevant_td_tags:
    raw_height.append(height.get_text())

#Doing the split of height to inches 
  for x in raw_height:
    feet_to_inches = float(x.split('-')[0]) * 12 

#Converting the inches and split 
    inches = float(x.split('-')[1])

#Calculating the total height in inches
    total_height_in_inches_meters =  (feet_to_inches + inches)
    height_1 +=total_height_in_inches_meters
  
  average_height_team =height_1 / len(raw_height )
  print('The average for the'" "+str(team_type)+" is "+str(round(average_height_team, 2)) + " Inches ")

for key, value in Baruch_sports_teams.items():
  #print(f'{key} {value}')
  scraping_data(key, value)
