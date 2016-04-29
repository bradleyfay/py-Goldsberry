import goldsberry


class catch_and_shoot(goldsberry.masterclass.NbaDataProviderSportVu):
    def __init__(self, season=goldsberry.apiparams.default_season, team=False):
        url_modifier = 'catchShoot'
        goldsberry.masterclass.NbaDataProviderSportVu.__init__(self, url_modifier, year=season, team=team)


class defense(goldsberry.masterclass.NbaDataProviderSportVu):
    def __init__(self, season=goldsberry.apiparams.default_season, team=False):
        url_modifier = 'defense'
        goldsberry.masterclass.NbaDataProviderSportVu.__init__(self, url_modifier, year=season, team=team)


class drives(goldsberry.masterclass.NbaDataProviderSportVu):
    def __init__(self, season=goldsberry.apiparams.default_season, team=False):
        url_modifier = 'drives'
        goldsberry.masterclass.NbaDataProviderSportVu.__init__(self, url_modifier, year=season, team=team)


class passing(goldsberry.masterclass.NbaDataProviderSportVu):
    def __init__(self, season=goldsberry.apiparams.default_season, team=False):
        url_modifier = 'passing'
        goldsberry.masterclass.NbaDataProviderSportVu.__init__(self, url_modifier, year=season, team=team)


class touches(goldsberry.masterclass.NbaDataProviderSportVu):
    def __init__(self, season=goldsberry.apiparams.default_season, team=False):
        url_modifier = 'touches'
        goldsberry.masterclass.NbaDataProviderSportVu.__init__(self, url_modifier, year=season, team=team)


class pull_up_shooting(goldsberry.masterclass.NbaDataProviderSportVu):
    def __init__(self, season=goldsberry.apiparams.default_season, team=False):
        url_modifier = 'pullUpShoot'
        goldsberry.masterclass.NbaDataProviderSportVu.__init__(self, url_modifier, year=season, team=team)


class rebounding(goldsberry.masterclass.NbaDataProviderSportVu):
    def __init__(self, season=goldsberry.apiparams.default_season, team=False):
        url_modifier = 'rebounding'
        goldsberry.masterclass.NbaDataProviderSportVu.__init__(self, url_modifier, year=season, team=team)


class shooting(goldsberry.masterclass.NbaDataProviderSportVu):
    def __init__(self, season=goldsberry.apiparams.default_season, team=False):
        url_modifier = 'shooting'
        goldsberry.masterclass.NbaDataProviderSportVu.__init__(self, url_modifier, year=season, team=team)


class speed(goldsberry.masterclass.NbaDataProviderSportVu):
    def __init__(self, season=goldsberry.apiparams.default_season, team=False):
        url_modifier = 'speed'
        goldsberry.masterclass.NbaDataProviderSportVu.__init__(self, url_modifier, year=season, team=team)


__all__ = ['catch_and_shoot', 'defense', 'drives', 'passing',
           'touches', 'pull_up_shooting', 'rebounding', 'shooting',
           'speed']
