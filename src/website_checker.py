import csv
import requests
from fake_useragent import UserAgent
from http import HTTPStatus


class WebsiteChecker():
    def __init__(self) -> None:
        pass
    
    def get_websites(self,csv_path: str) -> list[str]:
        websites: list[str] = []
        with open(csv_path, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if 'http://' in row[1]:
                    websites.append(row[1])
                elif 'https://' not in row[1]:
                    websites.append(f'https://{row[1]}')
                else:
                    websites.append(row[1])

            return websites

    def get_user_agent(self) -> str:
        user_agent = UserAgent()
        return user_agent.chrome

    def get_status_description(self,status_code: int) -> str:
        for value in HTTPStatus:
            if value == status_code:
                description: str = f'({value} {value.name}) {value.description}'
                return description
            
        return '(???) Unknown status code...'

    def check_website(self,website:str, user_agent) -> str:
        try:
            code:int = requests.get(website, headers={'User-Agent': user_agent}).status_code
            result = f"{website} {self.get_status_description(code)}"
            return result
        except Exception:
            result = f'**Could not get information for website: {website}'
            return result
