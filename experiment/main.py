from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from experiment.database import DataBase
from kivy.uix.button import Button
from kivy.properties import NumericProperty, StringProperty, BooleanProperty,\
    ListProperty
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

class ActionOptionsWindow(Screen):

    def add_artist_btn(self):
        sm.current = "add_artist"

    def explore_btn(self):
        pass

    def ai_art_lab_btn(self):
        pass


class AddArtistWindow(Screen):
    artist_name = ObjectProperty(None)
    location = ObjectProperty(None)

    def submit(self):
        if self.artist_name.text != "" and self.location.text != "":
            response = db.add_artist(self.artist_name.text, self.location.text)
            if response == 0:
                artist_not_found_form()
            else:
                self.reset()
                sm.current = "show_artist"
        else:
            invalid_form()

    def reset(self):
        self.artist_name.text = ""
        self.location.text = ""

    def back_btn_pressed(self):
        sm.current = "options"

class CButton(Button):
    def exp_or_collapse(self, box):
        if box.height == self.height:
            # expand
            for child in box.children:
                child.height = 40
                child.opacity = 1
        else:
            # collapse
            for child in box.children:
                if child != self:
                    child.height = 0
                    child.opacity = 0

class ShowArtistWindow(Screen):
    artist_name = ObjectProperty(None)
    artist_bio = ObjectProperty(None)
    artist_born = ObjectProperty(None)
    artist_died = ObjectProperty(None)
    artist_themes = ObjectProperty(None)
    artist_image = ObjectProperty(None)
    bio_shown = False

    def on_enter(self, *args):
        artist_info = db.added_last
        self.artist_info = artist_info
        artist_name = artist_info.artist_name
        artist_born = artist_info.birth_day
        artist_died = artist_info.death_day
        artist_themes = artist_info.themes
        self.artist_image = artist_info.image_link
        self.artist_name.text = "Artist Name: " + artist_name
        self.artist_born.text = "Born: " + artist_born
        self.artist_died.text = "Died: " + artist_died
        if artist_info.periods_of_work[0] != '':
            self.artist_themes.text = "Periods: " + ", ".join(artist_info.periods_of_work)

    def update_bio(self):
        if not self.bio_shown:
            self.biography.text = self.artist_info.biography
            self.bio_shown = True
        else:
            self.biography.text = ""
            self.bio_shown = False

    def back_btn_pressed(self):
        sm.current = "add_artist"
        self.artist_themes.text = ""

class WindowManager(ScreenManager):
    pass

def artist_not_found_form():
    pop = Popup(title='Artist not found',
                content=Label(text='The artist name can not be recognized.'),
                size_hint=(None, None), size=(400, 400))

    pop.open()

def invalid_form():
    pop = Popup(title='Invalid Form',
                content=Label(text='Please fill in all inputs with valid information.'),
                size_hint=(None, None), size=(400, 400))

    pop.open()


kv = Builder.load_file("my.kv")
sm = WindowManager()
db = DataBase("db/artists.pickle")

available_screens = [ActionOptionsWindow(name="options"), AddArtistWindow(name="add_artist"), ShowArtistWindow(name="show_artist")]
for screen in available_screens:
    sm.add_widget(screen)


class MyMainApp(App):
    index = NumericProperty(-1)

    def build(self):
        self.screens = dict(zip(list(range(len(available_screens))), available_screens))
        #self.go_next_screen()
        return sm

    '''
    def load_screen(self, index):
        #if index in self.screens:
        return self.screens[index]
        #screen = Builder.load_file(self.available_screens[index])
        #self.screens[index] = screen
        #return screen

    def go_next_screen(self):
        self.index = (self.index + 1) % len(self.available_screens)
        screen = self.load_screen(self.index)
        sm = self.root.ids.sm
        sm.switch_to(screen, direction='left')

    def go_previous_screen(self):
        self.index = (self.index - 1) % len(self.available_screens)
        screen = self.load_screen(self.index)
        sm = self.root.ids.sm
        sm.switch_to(screen, direction='right')
        # self.current_title = screen.name
        # self.update_sourcecode()
'''

if __name__ == "__main__":
    MyMainApp().run()
