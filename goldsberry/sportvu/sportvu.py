from goldsberry.masterclass import SportVuProvider


class catch_and_shoot(SportVuProvider):
    def __init__(self, **kwargs):
        url_modifier = 'catchShoot'
        SportVuProvider.__init__(self, url_modifier=url_modifier,**kwargs)


class defense(SportVuProvider):
    _url_modifier = 'defense'


class drives(SportVuProvider):
    _url_modifier = 'drives'


class passing(SportVuProvider):
    _url_modifier = 'passing'


class touches(SportVuProvider):
    _url_modifier = 'touches'


class pull_up_shooting(SportVuProvider):
    _url_modifier = 'pullUpShoot'


class rebounding(SportVuProvider):
    _url_modifier = 'rebounding'


class shooting(SportVuProvider):
    _url_modifier = 'shooting'


class speed(SportVuProvider):
    _url_modifier = 'speed'


__all__ = ['catch_and_shoot', 'defense', 'drives', 'passing',
           'touches', 'pull_up_shooting', 'rebounding', 'shooting',
           'speed']
