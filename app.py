from flask import Flask, render_template
import requests

app = Flask(__name__)

# Replace 'YOUR_API_KEY' with your NewsAPI key
NEWS_API_KEY = 'd1da0ac33bda4d1fabcd766208881585'

# Define the route for the homepage
@app.route('/')
def index():
    # Make a request to the NewsAPI
    url = f'https://newsapi.org/v2/top-headlines?country=us&apiKey={NEWS_API_KEY}'
    response = requests.get(url)
    data = response.json()

    # Extract the news articles from the response
    articles = data['articles']

    # Render the template with the news articles
    return render_template('index.html', articles=articles)

if __name__ == '__main__':
    app.run(debug=True)
