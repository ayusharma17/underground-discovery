from bs4 import BeautifulSoup
import requests


# copy base artists
base_file = open('base_artists.txt', 'r') 
artists = base_file.readlines()
base_file.close()
count = 0
for url in artists: #remove array index
    print(count, len(artists), url)
    if count%10000 == 0:
        with open('data scraper/final_backup.txt', 'w') as unfiltered_file:
            unfiltered_file.writelines(artists)
    if(len(artists) >=5000000):
        break
    try: 
        html = requests.get(url.strip())
        soup = BeautifulSoup(html.text, "html.parser")
    except Exception as e:
        print(url.strip(), e)
    for link in soup.find_all('a'): 
        artist_link = "https://open.spotify.com" +link.get('href') + "\n"
        if ('artist' in artist_link) and (artist_link not in artists):
            artists.append(artist_link)
    html.close()
    count+=1

print(len(artists))     
unfiltered_file = open('unfiltered_artists.txt', 'w') 
unfiltered_file.writelines(artists)
unfiltered_file.close() 