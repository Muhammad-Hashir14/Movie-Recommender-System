from flask import Flask, render_template, request, redirect, url_for
import pickle
import ast
app = Flask(__name__)
import requests

def fetch_poster(mid):
    response = requests.get(f"https://api.themoviedb.org/3/movie/{mid}?api_key=420ef4261c5783148647a0bcf4e60060")
    data = response.json()
    poster = data["poster_path"]
    path = "https://image.tmdb.org/t/p/original"+ poster
    return path

from Movies import routes





