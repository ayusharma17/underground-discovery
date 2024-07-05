import requests
from bs4 import BeautifulSoup


artists_file = open('filtered_artists.txt', 'r') #change to base
artists = artists_file.readlines()
artists_file.close()
artist_song = {}
count = 0
for url in artists:
    print(count, url)
    try:
        html = requests.get(url.strip())
        soup = BeautifulSoup(html.text, "html.parser")
    except Exception as e:
        print(e)
    
    song_list = []
    for i in soup.find_all('p'):
        try:
            if "listrow-title-track-spotify" in (i.get('id')) and i.get('id') not in song_list:
                song_list.append(i.get('id')[34:56])
        except Exception as e:
            continue
    if len(song_list) > 0:
        artist_song[url] = song_list
        print(len(song_list))
            
    html.close()
    count+=1

song_file = open('songs.txt', 'w')
for key in artist_song:
    for track in artist_song[key]:
        song_file.write(key.strip() + " " + track + "\n")
song_file.close()
