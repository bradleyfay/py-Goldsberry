from goldsberry.masterclass import SportVuProvider


class catch_and_shoot(SportVuProvider):
    def __init__(self, **kwargs):
        url_modifier = 'catchShoot'
        SportVuProvider.__init__(self, url_modifier=url_modifier, **kwargs)


class defense(SportVuProvider):
    '''Sportvu specific data. Season totals'''
    def __init__(self, **kwargs):
        url_modifier = 'defense'
        SportVuProvider.__init__(self, url_modifier=url_modifier, **kwargs)

class drives(SportVuProvider):
    '''Sportvu specific data. Season totals'''
    def __init__(self, **kwargs):
        url_modifier = 'drives'
        SportVuProvider.__init__(self, url_modifier=url_modifier, **kwargs)

class passing(SportVuProvider):
    '''Sportvu specific data. Season totals'''
    def __init__(self, **kwargs):
        url_modifier = 'passing'
        SportVuProvider.__init__(self, url_modifier=url_modifier, **kwargs)

class touches(SportVuProvider):
    '''Sportvu specific data. Season totals'''
    def __init__(self, **kwargs):
        url_modifier = 'touches'
        SportVuProvider.__init__(self, url_modifier=url_modifier, **kwargs)

class pull_up_shooting(SportVuProvider):
    '''Sportvu specific data. Season totals'''
    def __init__(self, **kwargs):
        url_modifier = 'pullUpShoot'
        SportVuProvider.__init__(self, url_modifier=url_modifier, **kwargs)

class rebounding(SportVuProvider):
    '''Sportvu specific data. Season totals'''
    def __init__(self, **kwargs):
        url_modifier = 'rebounding'
        SportVuProvider.__init__(self, url_modifier=url_modifier, **kwargs)

class shooting(SportVuProvider):
    '''Sportvu specific data. Season totals'''
    def __init__(self, **kwargs):
        url_modifier = 'shooting'
        SportVuProvider.__init__(self, url_modifier=url_modifier, **kwargs)

class speed(SportVuProvider):
    '''Sportvu specific data. Season totals'''
    def __init__(self, **kwargs):
        url_modifier = 'speed'
        SportVuProvider.__init__(self, url_modifier=url_modifier, **kwargs)

__all__ = ['catch_and_shoot', 'defense', 'drives', 'passing',
           'touches', 'pull_up_shooting', 'rebounding', 'shooting',
           'speed']
