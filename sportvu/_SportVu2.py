from goldsberry.masterclass import *

class catch_and_shoot(SPORTVU):
    _url_modifier = 'catchShoot'

class defense(SPORTVU):
    _url_modifier = 'defense'

class drives(SPORTVU):
    _url_modifier = 'drives'

class passing(SPORTVU):
    _url_modifier = 'passing'

class touches(SPORTVU):
    _url_modifier = 'touches'

class pull_up_shooting(SPORTVU):
    _url_modifier = 'pullUpShoot'

class rebounding(SPORTVU):
    _url_modifier = 'rebounding'

class shooting(SPORTVU):
    _url_modifier = 'shooting'

class speed(SPORTVU):
    _url_modifier = 'speed'

__all__ = ['catch_and_shoot', 'defense', 'drives', 'passing', 
    'touches', 'pull_up_shooting', 'rebounding', 'shooting', 
    'speed']