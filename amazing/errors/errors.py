class ConfigFormatError(Exception):
    def __init__(self, msg: str = "Invalid config format!"):
        super().__init__("ConfigFormatError:" + msg)


class LineFormatError(ConfigFormatError):
    def __init__(self, msg: str = "Invalid config line format!"):
        super().__init__("LineFormatError:" + msg)
