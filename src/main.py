import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty, StringProperty
from kivy.lang import Builder
from file_manager import file_manager
from shared.popup.popup import *
from website_checker import WebsiteChecker

#Load the kv file
Builder.load_file('main.kv')
Builder.load_file("shared/popup/popup.kv")

class MainLayout(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.manager = file_manager.FileManager()
        self.websitechecker = WebsiteChecker()
        self.file = ''

    success_popup = MessageSuccessPopup()
    message_error = MessageErrorPopup()
    #file_error = FileErrorPopup()    
    #Data biding of the kv files
    url = ObjectProperty(None)
    def choose_csv_file(self):
        self.file = self.manager.get_path_file()

    def check_sites(self):
        if self.file:
            result: str = ''
            sites: list[str] = self.websitechecker.get_websites(self.file)
            user_agent: str = self.websitechecker.get_user_agent()
            for site in sites:
                result += self.websitechecker.check_website(site,user_agent) + '\n'
            self.success_popup.result_text.text = result
            self.success_popup.open()
            self.file = ''
        else:
            url = self.url.text
            user_agent: str = self.websitechecker.get_user_agent()
            if 'http://' in url:
                result: str = self.websitechecker.check_website(url,user_agent)
                if result:
                    self.success_popup.result_text.text = result
                    self.success_popup.open()
                else:
                    self.message_error.result_text.text = result
                    self.message_error.open()
            elif 'https://' not in url:
                result: str = self.websitechecker.check_website(f'https://{url}',user_agent)
                if result:
                    self.success_popup.result_text.text = result
                    self.success_popup.open()
                else:
                    self.message_error.result_text.text = result
                    self.message_error.open()
            else:
                result: str = self.websitechecker.check_website(url,user_agent)
                if result:
                    self.success_popup.result_text.text = result
                    self.success_popup.open()
                else:
                    self.message_error.result_text.text = result
                    self.message_error.open()
            self.file = ''
            self.url.text = ''







class WebsiteCheckerApp(App):
    def build(self):
        return MainLayout()

if __name__ == "__main__":
    app = WebsiteCheckerApp()
    app.run()