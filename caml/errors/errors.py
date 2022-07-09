
class CamlError(Exception):
    def __init__(self, message):
        super(Exception, self).__init__(message)


class CamlArgumentsError(CamlError):
    def __init__(self, message):
        super(Exception, self).__init__(message)