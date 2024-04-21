from abc import ABC, abstractmethod
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from google.oauth2.service_account import Credentials
import gspread
from dicPrefectures import prefectures as pref
from dicPrefectures2 import prefectures as pref2


def main():
    options = Options()
    options.add_argument('--headless')
    browser = webdriver.Chrome(options=options)

def authentificate():
    scopes = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']

    credentials = Credentials.from_service_account_file(
        R"jobsearchforsandt-d92cda930b99.json",
        scopes=scopes
    )
    gc = gspread.authorize(credentials)

    spreadsheet_url = "https://docs.google.com/spreadsheets/d/1RQW1ryYM3FhrKRNVXYChjnIhCjNdw7bYk5GBM-uB1GY/edit#gid=386239817"

    sheet1 = gc.open_by_url(spreadsheet_url).worksheet("ビューティーワークス")
    sheet2 = gc.open_by_key("1RQW1ryYM3FhrKRNVXYChjnIhCjNdw7bYk5GBM-uB1GY").worksheet("リクエストQJ")
    return sheet1, sheet2


class abstractRecruitReader(ABC):
    @abstractmethod
    def shopAccessWeb(self):
        pass
    
    @abstractmethod
    def shopSalaryMonth(self):
        pass
    
    @abstractmethod
    def shopAddress(self):
        pass

    @abstractmethod
    def shopName(self):
        pass

class concreteRecruitReader(abstractRecruitReader):
    def __init__(self, url):
        self.url = url