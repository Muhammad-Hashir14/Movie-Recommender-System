from Movies import app
from Movies import fetch_poster
import requests
import pickle
from flask import request, render_template
import ast

@app.route("/", methods = ["GET", "POST"])
def home():

    with open(r"Movies/model/similarity.pkl", 'rb') as f:
        similarity = pickle.load(f)

    with open(r"Movies/model/movies.pkl", 'rb') as f:
        loaded = pickle.load(f)

    data = loaded.to_json(orient='records')
    data = ast.literal_eval(data)

    action = request.form.get("action")
    select = request.form.get("select")  # Initialize 'select' with a default value

    recommendation = []
    poster_path = []
    if action == "Recommend":
        index = loaded[loaded['title'] == select].index[0]
        distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
        # recommendation = []
        # poster_path = []
        for i in distances[1:6]:
            recommendation.append(loaded.iloc[i[0]].title)
            poster_path.append(fetch_poster(loaded.iloc[i[0]].movie_id))
            print(poster_path)
    else:
        recommendation = []  # Set 'recommendation' to an empty list if action is not "Recommend"
    
    data1 = zip(recommendation, poster_path)

    return render_template("base.html", select = select, data=data, data1 = data1)