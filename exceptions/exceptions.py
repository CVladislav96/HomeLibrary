class HomeLiberyException(Exception):
    pass

class BookAlreadyExistsException(HomeLiberyException):
    pass

class BookNotFoundException(HomeLiberyException):
    pass