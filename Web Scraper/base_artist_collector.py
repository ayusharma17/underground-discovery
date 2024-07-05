from selenium import webdriver 
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()


# Base Artist links Collecting
playlists = [
    "https://open.spotify.com/playlist/37i9dQZF1DX0XUsuxWHRQd",
    "https://open.spotify.com/playlist/37i9dQZF1DWXRqgorJj26U",
    "https://open.spotify.com/playlist/37i9dQZF1DX9GRpeH4CL0S",
    "https://open.spotify.com/playlist/0kz78XchNmM9aKwDHQhi0t",
    "https://open.spotify.com/playlist/37i9dQZF1DX7HOk71GPfSw",
    "https://open.spotify.com/playlist/3EyB7nH0Gt1CSLtgeT1cNw",
    "https://open.spotify.com/playlist/1Vtq5pePI2g6p0MpAB2gDt",
    "https://open.spotify.com/playlist/6TxuoHMx9qLTePZGS1CasY",
    "https://open.spotify.com/playlist/37i9dQZEVXbJiZcmkrIHGU",
    "https://open.spotify.com/playlist/44zrIqtaK4EIwyrE62yQ6o",
    "https://open.spotify.com/playlist/5zZDVkuWyO3hdjckJHHv40",
    "https://open.spotify.com/playlist/37i9dQZF1DX0XUfTFmNBRM",
    "https://open.spotify.com/playlist/08VCxXZsk7jkzqfHupsL61",
    "https://open.spotify.com/playlist/5TDtuKDbOhrfW7C58XnriZ",
    "https://open.spotify.com/playlist/1h0CEZCm6IbFTbxThn6Xcs",
    "https://open.spotify.com/playlist/7m1C1eHUC2kJQL69dGMjaz",
    "https://open.spotify.com/playlist/1LD6W0yUGghEu193n2OOJy",
    "https://open.spotify.com/playlist/0rh4JRWo3tSRBYNM3i4XXa",
    "https://open.spotify.com/playlist/2YE8ziv26B6ZIon7iSTrcQ",
    "https://open.spotify.com/playlist/0xev9Iu5toHJc1L1PthrpW",
    "https://open.spotify.com/playlist/3AfMvO7Ha5m06dJl51eeEy",
    "https://open.spotify.com/playlist/65M0woJ8PIdm5KmAesnZhr",
    "https://open.spotify.com/playlist/2otQLmbi8QWHjDfq3eL0DC",
    "https://open.spotify.com/playlist/37i9dQZF1EQqkOPvHGajmW",
    "https://open.spotify.com/playlist/37i9dQZF1DXd8cOUiye1o2",
    "https://open.spotify.com/playlist/37i9dQZF1DX5cZuAHLNjGz",
    "https://open.spotify.com/playlist/37i9dQZF1DWVo4cdnikh7Z",
    "https://open.spotify.com/playlist/37i9dQZF1DWU8quswnFt3c",
    "https://open.spotify.com/playlist/37i9dQZF1DWY0DyDKedRYY",
    "https://open.spotify.com/playlist/37i9dQZF1DX4sWSpwq3LiO",
    "https://open.spotify.com/playlist/37i9dQZF1DX10zKzsJ2jva",
    "https://open.spotify.com/playlist/69fEt9DN5r4JQATi52sRtq",
    'https://open.spotify.com/playlist/4ibx3N0OdTyTFZTRX1zEQQ',
    "https://open.spotify.com/playlist/7eybPwcFDYDzw1KYGqHiQo",
    "https://open.spotify.com/playlist/5d6HDkkTouObGKeQOg39gk",
    "https://open.spotify.com/playlist/2HUpNZLoYHe0Sa9dglqQOg",
    "https://open.spotify.com/playlist/4jr1tvvMa8bYtXGQZPFn3T",
    "https://open.spotify.com/playlist/7kDOjv4aQuo4lFBDq9F6Rw",
    "https://open.spotify.com/playlist/6V2kpfvd5y48VjOq2CFwuv",
    "https://open.spotify.com/playlist/1C49yxU1XBkoq5yaVDbJwx",
    "https://open.spotify.com/playlist/04ZwFco4KsjgPlVMtzwfgS"
]
base_artists = []
for link in playlists:
    driver.get(link)
    html = driver.find_elements(By.TAG_NAME, "a")
    for i in html:
        try:
            url = i.get_attribute("href") + "\n"
            if 'artist' in url and url not in base_artists:
                base_artists.append(url)
        except:
            continue
print(len(base_artists))     
base_file = open('base_artists.txt', 'w') 
base_file.writelines(base_artists)
base_file.close()
    