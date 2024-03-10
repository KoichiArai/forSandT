from abc import ABC, abstractmethod

def main():
    pass

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