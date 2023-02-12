from flask import render_template, request, flash, redirect
import os
from datetime import datetime
from core import app, db
from core.models import ShortUrls
from random import choice
import string
import requests
import json


def importFromImgur(albumID):
    if albumID == None:
        albumID = "MJXmbUp"
    url = "https://api.imgur.com/3/album/" + albumID + "/images"

    payload = {}
    files = {}
    headers = {
        'Authorization': 'Client-ID **************'
    }

    response = requests.request("GET", url, headers=headers, data=payload, files=files)
    data = json.loads(response.text)
    images = data['data']
    imageList = []

    for image in images:
        imageList.append(image['link'])
    return imageList


def generate_short_id(num_of_chars: int):
    """Function to generate short_id of specified number of characters"""
    return ''.join(choice(string.ascii_letters + string.digits) for _ in range(num_of_chars))


@app.route('/')
def index():
    return render_template('landing.html')


@app.route("/longString")
def longString():
    url = request.args.get('long')
    short_id = generate_short_id(8)

    new_link = ShortUrls(
        original_url=url, short_id=short_id, created_at=datetime.now())
    db.session.add(new_link)
    db.session.commit()
    short_url = request.host_url + "short?short=" + short_id
    return render_template('longtest.html', short_url=short_url)


@app.route('/short')
def redirect_url():
    short_id = request.args.get('short')
    link = ShortUrls.query.filter_by(short_id=short_id).first()
    if link:
        # print(link.original_url)
        return redirect(link.original_url)
    else:
        flash('Invalid URL')
        return render_template("landing.html")


@app.route("/mobile-build")
def mobile_build():
    # Read all the images in the cards directory
    images = []
    for file in os.listdir("static/cards"):
        # print(file)
        if file.endswith(".jpg"):
            # Remove the file extension
            card = file

            # Add the card to the list of images
            images.append(card)

    # Render the desktop building page template

    return render_template("mobile-build.html", images=images)


@app.route("/desktop-build", methods=["GET", "POST"])
def desktop_build():
    # Read all the images in the cards directory
    images = []
    for file in os.listdir("static/cards"):
        # print(file)
        if file.endswith(".jpg"):
            # Remove the file extension
            card = file
            # print(card)
            # Add the card to the list of images
            images.append(card)

    # Render the desktop building page template

    return render_template("desktop-build.html", images=images)


@app.route("/desktop-build-imgur", methods=["GET", "POST"])
def desktop_build_imgur():
    albumId = request.args.get('albumID')
    # import from imgur
    images = importFromImgur(albumId)

    return render_template("desktop-build-imgur.html", images=images)


@app.route("/mobile-play")
def mobile_play():
    # Render the mobile playing page template

    return render_template("mobile-play.html")


@app.route("/desktop-play")
def desktop_play():
    # Read all the images in the cards directory
    # images = []
    deck = []
    deckInput = request.args.get('deck')

    for image in deckInput.split(','):
        # images.append(image)
        deck.append(image)
    # Render the desktop playing page template
    # print(deck)
    return render_template("desktop-play.html", deck=deck)
