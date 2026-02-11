class HomeLibraryException(Exception):
    pass

class BookAlreadyExistsException(HomeLibraryException):
    pass

class BookNotFoundException(HomeLibraryException):
    pass