import random

from models.tiny_url_info import TinyURLInfo


class TinyURLService:

    def __init__(self) -> None:
        self.__url_info:dict = {}

    def generate_tiny_url(self, long_url):
        if not self.__validate_long_url(long_url):
            raise Exception('INVALID URL')
        data = self.get_url_info(long_url)
        if not data:
            tiny_url = str(random.randint(100000, 10000000))
            data:TinyURLInfo = TinyURLInfo(tiny_url, long_url)
            self.__url_info[tiny_url] = data 
            return tiny_url
        else:
            return data.get_tiny_url()
            

    def get_url_info(self, long_url):
        for key, val in self.__url_info.items():
            if val and val.get_long_url() == long_url:
                return val   
    
    # For redirect
    def get_long_url(self, tiny_url):
        if tiny_url in self.__url_info:
            self.__url_info[tiny_url].increment_count()
            return self.__url_info[tiny_url]
        
        raise Exception('INVALID TINY URL')
        
    def get_count(self, tiny_url) -> int:
        if tiny_url in self.__url_info:
            return self.__url_info[tiny_url].get_count()
        
        raise Exception('INVALID TINY URL')
    
    def __validate_long_url(self, long_url):
        if long_url:
            return True 
        
