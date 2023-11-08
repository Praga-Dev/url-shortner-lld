class TinyURLResponseDTO:

    def __init__(self, is_success = False, message = 'FAILED', data: str = '') -> None:
        self.__is_success = is_success
        self.__message = message
        self.data = data

    def get_is_success(self):
        return self.__is_success
    
    def set_is_success(self, is_success: any) -> None:
        self.__is_success = is_success
    
    def get_message(self):
        return self.__message
    
    def set_message(self, message: any) -> None:
        self.__message = message
    
    def get_data(self):
        return self.data
    
    def set_data(self, data: any) -> None:
        self.data = data
    
    def print_response(self):
        print(self. __is_success, self.__message, str(self.data))