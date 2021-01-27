import requests
from bs4 import BeautifulSoup


print('''
▀▀█▀▀ █▀▀█ █▀▀█ ▒█▀▀▀█ █▀▀█ █▀▀▄ █▀▀▀ █▀▀ 
░▒█░░ █░░█ █░░█ ░▀▀▀▄▄ █░░█ █░░█ █░▀█ ▀▀█ 
░▒█░░ ▀▀▀▀ █▀▀▀ ▒█▄▄▄█ ▀▀▀▀ ▀░░▀ ▀▀▀▀ ▀▀▀

░█▀▀▀█ █▀▀ █▀▀█ █▀▀█ █▀▀█ █▀▀ █▀▀█ 
─▀▀▀▄▄ █── █▄▄▀ █▄▄█ █──█ █▀▀ █▄▄▀ 
░█▄▄▄█ ▀▀▀ ▀─▀▀ ▀──▀ █▀▀▀ ▀▀▀ ▀─▀▀
      [+]Author: https://github.com/ShantanuRauthan

''')

print('''Chose an Option(1/2):
1. Official UK Top 40 by MTV
2. Official Singles Charts Top 100 by OfficialCharts
 ''')
result = input()


#for the first url (UkTop40)
def UK():
  url1= "http://www.mtv.co.uk/music/charts/the-official-uk-top-40-singles-chart"
  r = requests.get(url1)
  soup = BeautifulSoup(r.text,'html.parser')
  
  container = soup.find_all("li", class_ = 'swiper-slide')
 
  for item in container:
    data = {"Name": item.h3.text,
    "Artist": item.find("p",class_ = "item-subtitle").text  }
    print(data)
    with open("UkTop40.txt",'a') as f:
      f.write(str(data))
    f.close()
  print("\n")
  print("------------Data Successfully Saved on UkTop40.txt-------------")


#for the 2nd URL(Top 100 Singles)
def Single100():
  print("Do you want songs for a  specified date? If so pls input date in the format YYYYMMDD (Eg: 20210115) Otherwise Press Enter")
  str1 = input()
  url2="https://www.officialcharts.com/charts/singles-chart/"+''.join(str1)

  r = requests.get(url2)
  soup = BeautifulSoup(r.text,'html.parser')
  
  container = soup.find_all("div",class_='title-artist')
  
  for item in container:
    data = {"Name":item.find("div",class_ = "title").text,
    "Artist": item.find("div", class_ = "artist").text
    }
    print(data)
    with open("OfficialChart100.txt",'a') as f:
     f.write(str(data))
    f.close()
  print("\n")    
  print("------------Data Successfully Saved on OfficialChart100.txt-------------")

if (result == '1'):
  UK()
elif (result == '2'):
  Single100()
else:
  print("Please chose from the given options provided")

