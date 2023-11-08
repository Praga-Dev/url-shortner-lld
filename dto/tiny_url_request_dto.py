class TinyURLRequestDTO:

    def __init__(self, long_url: str) -> None:
        self.__long_url = long_url

    def get_long_url(self):
        return self.__long_url
    
    def set_long_url(self, long_url: any) -> None:
        self.__long_url = long_url
    
    