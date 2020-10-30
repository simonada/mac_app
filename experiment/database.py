import datetime
from experiment.wikiart_api_handler import WikiArtApi
from experiment.artist_class import Artist
import pickle
import os.path

class DataBase:
    def __init__(self, filename):
        self.filename = filename
        self.artists = None
        self.file = None
        self.added_last = None
        self.load()

    def load(self):
        #self.file = open(self.filename, "r")
        #self.artists = {}
        if os.path.isfile(self.filename):
            with open(self.filename, 'rb') as pickle_file:
                self.artists = pickle.load(pickle_file)
        else:
            self.artists = {}
        #for line in self.file:
        #    artist_name, location, created = line.strip().split(";")
        #    self.artists[artist_name] = (location, created)
        #self.file.close()

    def get_artist(self, artist_name):
        if artist_name in self.artists:
            return self.artists[artist_name]
        else:
            return -1

    def add_artist(self, artist_name, location):
        artist_name = artist_name.strip()
        if artist_name not in self.artists:
            #self.artists[artist_name] = (location.strip(), DataBase.get_date())
            artist_details_wikiart = WikiArtApi().get_artist_info(artist_name)
            if artist_details_wikiart == -1:
                return 0
            new_artist = Artist(artist_details_wikiart, "json", location)
            self.artists[artist_name] = new_artist
            self.added_last = new_artist
            self.save()
            return 1
        else:
            self.added_last = self.artists[artist_name]
            print("Artist exists already!")
            return -1

    def save(self):
        self.save_object_pickle(self.artists, "artists.pickle")

        #with open(self.filename, "w") as f:
        #    for artist in self.artists:
        #        artist_info = self.artists[artist]
        #        f.write(artist + ";" + artist_info.biography + ";" + self.artists[artist][1] + "\n")

    def save_object_pickle(self, obj, filename):
        with open(filename, 'wb') as output:  # Overwrites any existing file.
            pickle.dump(obj, output, pickle.HIGHEST_PROTOCOL)

    @staticmethod
    def get_date():
        return str(datetime.datetime.now()).split(" ")[0]