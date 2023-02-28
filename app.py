from flask import Flask, render_template, request
import openai
import os
from dotenv import load_dotenv
load_dotenv()  # Load environment variables from .env file

app = Flask(__name__)

openai.api_key = os.environ.get("OPENAI_API_KEY")


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/game", methods=["POST"])
def game():
    prompt = request.form["prompt"]
    round_num = int(request.form.get("round", 1))
    image_url = request.form.get("image_url", "")

    if round_num > 5:
        return render_template("game_over.html", image_urls=image_urls)

    response = openai.Image.create(
        prompt=prompt,
        n=1,
        size="1024x1024"
    )

    image_url = response['data'][0]['url']
    image_urls = [image_url] if round_num == 1 else image_urls + [image_url]

    return render_template("game.html", round=round_num, image_url=image_url)

@app.route("/404")
def page_not_found():
    return render_template("404.html"), 404

@app.route("/500")
def server_error():
    return render_template("500.html"), 500
