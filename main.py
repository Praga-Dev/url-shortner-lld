from controller.url_controller import URLController
from dto.tiny_url_request_dto import TinyURLRequestDTO


def main():
    url_controller = URLController()
    url = 'www.google.com'
    
    request: TinyURLRequestDTO = TinyURLRequestDTO(url)
    response = url_controller.create_tiny_url(request)
    response.print_response()
    tiny_url = response.get_data()
    print('THE TINY URL : ', tiny_url)
    print('---------------------------------')

    response = url_controller.redirectToLongUrl(tiny_url)
    response.print_response()
    print('---------------------------------')
    
    response = url_controller.get_counter(tiny_url)
    response.print_response()

main()