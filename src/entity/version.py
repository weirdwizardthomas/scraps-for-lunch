from datetime import datetime


class Version:
    def __init__(self, version, year, month, day):
        self.version = version
        self.timestamp = datetime(year, month, day)

    def __repr__(self):
        return f'v{self.version} | {self.timestamp}'
