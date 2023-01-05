from flask import Flask, request
import requests

app = Flask(__name__)

@app.route('/proxy')
def proxy():
  # Get the "url" query parameter
  url = request.args.get('url')

  # Send a GET request to the specified URL
  response = requests.get(url)

  # Return the response from the proxied request
  return response.text

if __name__ == '__main__':
  app.run()
