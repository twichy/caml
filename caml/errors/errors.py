from errors.error_messages import AUTHENTICATION_ERROR


class LibhubError(Exception):
    def __init__(self, message):
        super(Exception, self).__init__(message)


class LibhubRetryError(LibhubError):
    def __init__(self, message):
        super(LibhubError, self).__init__(message)


class LibhubHttpError(LibhubError):
    def __init__(self, status_code, message):
        self.status_code = status_code
        super(LibhubError, self).__init__(message)


class LibhubAuthenticationError(LibhubError):
    def __init__(self):
        super(LibhubError, self).__init__(AUTHENTICATION_ERROR)
