from enum import Enum


class URLEnum(str, Enum):
    stats = "http://stats.nba.com/stats/"
    playtype = "http://stats.nba.com/js/data/playtype/"
    sportvu = "http://stats.nba.com/js/data/sportvu/"


class EndpointEnum(str, Enum):
    pass
