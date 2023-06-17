#HuRe ©
#By Reda telegram: @rd0r0

from telethon.tl.custom import Button
from cryptography.fernet import Fernet
import requests
from html_telegraph_poster.upload_images import upload_image
import random
from HuRe import l313l
import asyncio
from ..core.managers import edit_delete, edit_or_reply

valid_extensions = [".jpg", ".jpeg", ".png", ".gif"]

ek = "kSa3Wm6B2RcR_-7A3bHqw0AquOKwaZjP6HvK_WQPD28="
ea = "gAAAAABkjWzgEQUUyMxIeTnRVCY3kcNOhIy6RYiQnFm9CCrfZFNcJJyIBbUJPsahTXyOIjCPkDsoo1hkmScQwt9Yi0taZX8id7sH6AtvGCeFl9-UgAOGjVMfpZTVOypPOk0yw240Jhp6"

@l313l.ar_cmd(pattern="فلم")
async def rfilm(event):
    await event.edit("يرجى الانتظار جاري البحث عن فيلم...")
    dk = ek.encode()
    nk = ea.encode()
    cipher_suite = Fernet(dk)
    api_key = cipher_suite.decrypt(nk).decode()
    url = f"https://api.themoviedb.org/3/movie/top_rated?api_key={api_key}"
    response = requests.get(url)
    top_movies = response.json()["results"]
    random_movie = random.choice(top_movies)
    movie_id = random_movie["id"]
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&language=ar"
    response = requests.get(url)
    movie = response.json()
    movied = movie["overview"]
    movien = random_movie["title"]
    rating = movie["vote_average"]
    year = movie["release_date"][:4]
    poster_path = movie["poster_path"]
    moviep = f"https://image.tmdb.org/t/p/w500{poster_path}"
    if movied is None:
        movied = "-"
    if any(moviep.endswith(ext) for ext in valid_extensions):
        try:
            moviep = upload_image(moviep)
        except BaseException:
            moviep = None
    else:
        moviep = "https://telegra.ph/file/15480332b663adae49205.jpg"

    moviet = f"الاسم: {movien}\nالسنة: {year}\nالتقييم: {rating}\nالقصة:\n{movied}"
    
    url = f"https://api.themoviedb.org/3/movie/{movie_id}/videos?api_key={api_key}"
    response = requests.get(url)
    movie_data = response.json()
    buttonss = []
    if 'results' in movie_data:
        for video in movie_data["results"]:
            x = [Button.url("مشاهدة الفيديو", f"https://www.youtube.com/watch?v={video['key']}")]
            print(x)
            buttonss.append(x)

    await event.delete()
    print(buttonss)
    await event.answer(
        moviet,
        buttons=buttonss,
        file=moviep,
        force_document=Fallse,
        link_preview=False,
    )


    
#Reda

@l313l.ar_cmd(pattern="مسلسل")
async def rfilm(event):
    await event.edit("يرجى الانتضار جاري البحث على مسلسل...")
    dk = ek.encode()
    nk = ea.encode()
    cipher_suite = Fernet(dk)
    api_key = cipher_suite.decrypt(nk).decode()
    url = f"https://api.themoviedb.org/3/tv/top_rated?api_key={api_key}"
    response = requests.get(url)
    top_series = response.json()["results"]
    random_series = random.choice(top_series)
    series_id = random_series["id"]
    url = f"https://api.themoviedb.org/3/tv/{series_id}?api_key={api_key}&language=ar"
    response = requests.get(url)
    series = response.json()
    sern = random_series["name"]
    serr = series["vote_average"]
    sers = series["overview"]
    sersn = series["number_of_seasons"]
    poster_path = random_series["poster_path"]
    serp = f"https://image.tmdb.org/t/p/w500{poster_path}"
    if any(serp.endswith(ext) for ext in valid_extensions):
        try:
            serp = upload_image(serp) 
        except BaseException:
            serp = None
    else:
        serp = "https://telegra.ph/file/15480332b663adae49205.jpg"
    if serp is None:
        serp = "https://telegra.ph/file/15480332b663adae49205.jpg"
    sm = f"الاسم: {sern}\nالتقييم: {serr}\nعدد المواسم: {sersn}\nالقصة:\n{sers}"
    await event.delete()
    await l313l.send_file(
                event.chat_id,
                serp,
                caption=sm,
                )