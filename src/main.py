import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from file_manager import file_manager

from website_checker import WebsiteChecker

#Load the kv file
Builder.load_file('main.kv')

class MainLayout(Widget):
    def __init__(self, **kwargs):
        super(self,MainLayout).__init__(**kwargs)
        self.manager = file_manager.FileManager()
        self.websitechecker = WebsiteChecker()
        self.file = ''

    
    #Data biding of the kv files
    url = ObjectProperty(None)
    def choose_csv_file(self):
        self.file = self.manager.get_path_file()
        print(self.file)

    def check_sites(self):
        if self.file:
            sites: list[str] = self.websitechecker.get_websites(self.file)
            user_agent: str = self.websitechecker.get_user_agent()
            for site in sites:
                self.websitechecker.check_website(site,user_agent)
            self.file = ''
        else:
            url = self.url.text
            user_agent: str = self.websitechecker.get_user_agent()
            if 'http://' in url:
                self.websitechecker.check_website(url,user_agent)
            elif 'https://' not in url:
                self.websitechecker.check_website(f'https://{url}',user_agent)
            else:
                self.websitechecker.check_website(url,user_agent)
            self.file = ''
            self.url.text = ''







class WebsiteCheckerApp(App):
    def build(self):
        return MainLayout()

if __name__ == "__main__":
    app = WebsiteCheckerApp()
    app.run()