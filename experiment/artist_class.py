import datetime

class Artist:

    def __init__(self, artist_info, input_format, location=None):
        if input_format == "json":
            self.artist_from_json(artist_info, location)
        else:
            self.artist_from_sting_line(artist_info)

    def artist_from_sting_line(self, line): # reading from the database
        self.artist_name, self.biography, self.birth_day, self.death_day, self.periods_of_work, self.themes, self.location_seen, self.date_seen = line.strip().split(
            ";")
        self.periods_of_work = self.periods_of_work.split(",")
        self.themes = self.themes.split(",")
        self.location_seen = self.location_seen.split(",")
        self.date_seen = self.date_seen.split(",")

    def artist_from_json(self, json_obj, location): # wikiart API results
        self.artist_name = json_obj["artistName"]
        self.biography = json_obj["biography"]
        self.birth_day = json_obj["birthDayAsString"]
        self.death_day = json_obj["deathDayAsString"]
        if not self.death_day:
            self.death_day = "n.a."
        self.image_link = json_obj["image"]

        self.periods_of_work = self.get_array_from_json(json_obj["periodsOfWork"])
        self.themes = self.get_array_from_json(json_obj["themes"])

        self.location_seen = [location]
        self.date_seen = [str(datetime.datetime.now()).split(" ")[0]]

    def get_array_from_json(self, json_arr):
        json_arr = json_arr.split("\r")
        if json_arr:
            return [ele.strip('\n') for ele in json_arr]
        else:
            return []

    def add_location(self, location):
        self.location_seen.append(location)