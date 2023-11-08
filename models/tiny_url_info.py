# class TinyURL:

#     def __init__(self, long_url) -> None:
#         self.__tiny_url = fetch_tiny_url(long_url)


class TinyURLInfo:

    def __init__(self, tiny_url, long_url) -> None:
        self.__tiny_url = tiny_url
        self.__long_url = long_url
        self.__count = 0

    def get_tiny_url(self):
        return self.__tiny_url
    
    def set_tiny_url(self, tiny_url: any) -> None:
        self.__tiny_url = tiny_url
    
    def get_long_url(self):
        return self.__long_url
    
    def set_long_url(self, long_url: any) -> None:
        self.__long_url = long_url
    
    def get_count(self):
        return self.__count
    
    def increment_count(self) -> None:
        self.__count += 1

    def __str__(self) -> str:
        return f'TINY_URL : {self.__tiny_url}, LONG_URL : {self.__long_url}, COUNTER: {self.__count}'
    
    