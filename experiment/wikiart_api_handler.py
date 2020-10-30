import requests
import json

class WikiArtApi:
    def get_request_name(self, artist_name_input):
        return artist_name_input.lower().replace(" ", "-")

    def get_artist_info(self, artist_name_input):
        artist_name = self.get_request_name(artist_name_input)
        response = requests.get("https://www.wikiart.org/en/{}?json=2".format(artist_name))
        if "200" in str(response):
            return response.json()
        else:
            print("Artist not found")
            return -1

def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)


if __name__ == "__main__":
    #response = requests.get("https://www.wikiart.org/en/pablo-picasso?json=2")
    api = WikiArtApi()
    artist_info = api.get_artist_info("Roni Horn")
    jprint(artist_info)
    if artist_info != -1:
        print(artist_info["periodsOfWork"])
        themes = artist_info["themes"].split("\r")
        themes = [theme.strip('\n') for theme in themes]
        print(themes)
