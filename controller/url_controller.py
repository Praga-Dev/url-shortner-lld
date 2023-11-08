from dto.tiny_url_request_dto import TinyURLRequestDTO
from dto.tiny_url_response_dto import TinyURLResponseDTO
from services.url_service import TinyURLService


class URLController:
    def __init__(self) -> None:
        self.__url_service = TinyURLService()

    def create_tiny_url(self, requestDTO: TinyURLRequestDTO) -> TinyURLResponseDTO:

        response = TinyURLResponseDTO()
        request = self.__url_service.generate_tiny_url(
            requestDTO.get_long_url()
        )

        if request:
            response = TinyURLResponseDTO(True, 'SUCCESS', request)

        return response    
    
    def redirectToLongUrl(self, tiny_url):
        response = TinyURLResponseDTO()
        request = self.__url_service.get_long_url(tiny_url)
        
        if request:
            response = TinyURLResponseDTO(True, 'SUCCESS', request)

        return response    

    
    def get_counter(self, tiny_url:str) -> TinyURLResponseDTO:

        response = TinyURLResponseDTO()
        request = self.__url_service.get_count(tiny_url)

        if request:
            response = TinyURLResponseDTO(True, 'SUCCESS', request)

        return response    
