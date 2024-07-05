import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import csv


client_credentials_manager = SpotifyClientCredentials(
    client_id="",
    client_secret="",
)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
tracks = [] 
track_ids = []
fields = [
    "acousticness",
    "artists",
    "danceability",
    "duration_ms",
    "energy",
    "explicit",
    "genres",
    "id",
    "instrumentalness",
    "key",
    "liveness",
    "loudness",
    "mode",
    "name",
    "popularity",
    "release_date",
    "speechiness",
    "tempo",
    "valence",
    "year",
]

filename = "song_data.csv"
csv_file = open(filename, "w", newline="")
writer = csv.DictWriter(csv_file, fieldnames=fields)
writer.writeheader()
tracks_file = open("songs.txt", "r")  # change to base
for i in tracks_file.readlines():
  track_ids.append(i.split()[1].strip())
tracks_file.close()
index = 101350
count = 0

while index <= 190000:
  print(index)
  genre_artists = []
  try:
    tracks_list = sp.tracks(track_ids[index:index+50])
    features_list = sp.audio_features(track_ids[index:index+50])
    for i in tracks_list['tracks']:
      genre_artists.append(i["artists"][0]["id"])
    genre_list = sp.artists(genre_artists)


  except Exception as e:
    print(e)
    continue
  index+=50
  

  for i in range(len(tracks_list['tracks'])):
    features = features_list[i]
    track = tracks_list['tracks'][i]
    artist_genre = genre_list['artists'][i]
    try:
      track_data = features
      genres = artist_genre["genres"]
      track_data["genres"] = genres
      name = track["name"]
      track_data["name"] = name
      popularity = track["popularity"]
      track_data["popularity"] = popularity
      artists = []
      for artist in track["artists"]:
          artists.append(artist["name"])
      track_data["artists"] = artists
      release_date = track["album"]["release_date"]
      track_data["release_date"] = release_date
      year = release_date[0:4]
      track_data["year"] = year
      del track_data["track_href"]
      del track_data["uri"]
      del track_data["analysis_url"]
      del track_data["type"]
      del track_data["time_signature"]
      tracks.append(track_data)
      writer.writerow(track_data)
      count+=1
    except Exception as e:
      print(e)
      continue

csv_file.close()

