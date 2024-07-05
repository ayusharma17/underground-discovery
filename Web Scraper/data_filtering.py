from bs4 import BeautifulSoup
import requests
base_file = open('unfiltered_artists.txt', 'r') 
artists = base_file.readlines()
base_file.close()
monthly_listener_class = "Type__TypeElement-sc-goli3j-0 dsbIME sMT6JaxLhI2QLVSevX_3 fjP8GyQyM5IWQvTxWk6W"
filtered_artists = []
count = 0
fcount = 0
for url in artists:
    print(count, fcount)
    if 'concert' in url:
        continue
    try:
        html = requests.get(url.strip())
        soup = BeautifulSoup(html.text, "html.parser")
    except Exception as e:
        print(url, e)
        continue
    try:
        x = soup.find(class_=monthly_listener_class).get_text().split()[0]
        y=""
        for i in x.split(","):
            y+=i
        y = int(y)
        if y >= 100000 and y<= 1000000:
            fcount +=1
            filtered_artists.append(url)
        html.close()
        

    except Exception as e:
        print(url, e)
        html.close()
        continue
    count+=1
print(len(filtered_artists))     
filtered_file = open('filtered_artists.txt', 'w') 
filtered_file.writelines(filtered_artists)
filtered_file.close() 

