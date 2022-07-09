class CamlError(Exception):
    def __init__(self, message):
        super(Exception, self).__init__(message)


class CamlConflictError(CamlError):
    def __init__(self, message):
        super(Exception, self).__init__(f"Conflict Error: {message}")


class CamlNotFoundError(CamlError):
    def __init__(self, message):
        super(Exception, self).__init__(message)


class CamlArgumentsError(CamlError):
    def __init__(self, message):
        super(Exception, self).__init__(message)
