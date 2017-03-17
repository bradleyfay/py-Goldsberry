import goldsberry


class transition(goldsberry.masterclass.NbaDataProviderPlayType):
    def __init__(self, season=goldsberry.apiparams.default_season, team=False):
        url_modifier = 'Transition'
        goldsberry.masterclass.NbaDataProviderPlayType.__init__(self, url_modifier, year=season, team=team)


class isolation(goldsberry.masterclass.NbaDataProviderPlayType):
    def __init__(self, season=goldsberry.apiparams.default_season, team=False):
        url_modifier = 'Isolation'
        goldsberry.masterclass.NbaDataProviderPlayType.__init__(self, url_modifier, year=season, team=team)


class pick_and_roll_ball_handler(goldsberry.masterclass.NbaDataProviderPlayType):
    def __init__(self, season=goldsberry.apiparams.default_season, team=False):
        url_modifier = 'PRBallHandler'
        goldsberry.masterclass.NbaDataProviderPlayType.__init__(self, url_modifier, year=season, team=team)


class pick_and_roll_man(goldsberry.masterclass.NbaDataProviderPlayType):
    def __init__(self, season=goldsberry.apiparams.default_season, team=False):
        url_modifier = 'PRRollMan'
        goldsberry.masterclass.NbaDataProviderPlayType.__init__(self, url_modifier, year=season, team=team)


class postup(goldsberry.masterclass.NbaDataProviderPlayType):
    def __init__(self, season=goldsberry.apiparams.default_season, team=False):
        url_modifier = 'Postup'
        goldsberry.masterclass.NbaDataProviderPlayType.__init__(self, url_modifier, year=season, team=team)


class spotup(goldsberry.masterclass.NbaDataProviderPlayType):
    def __init__(self, season=goldsberry.apiparams.default_season, team=False):
        url_modifier = 'Spotup'
        goldsberry.masterclass.NbaDataProviderPlayType.__init__(self, url_modifier, year=season, team=team)


class handoff(goldsberry.masterclass.NbaDataProviderPlayType):
    def __init__(self, season=goldsberry.apiparams.default_season, team=False):
        url_modifier = 'Handoff'
        goldsberry.masterclass.NbaDataProviderPlayType.__init__(self, url_modifier, year=season, team=team)


class cut(goldsberry.masterclass.NbaDataProviderPlayType):
    def __init__(self, season=goldsberry.apiparams.default_season, team=False):
        url_modifier = 'Cut'
        goldsberry.masterclass.NbaDataProviderPlayType.__init__(self, url_modifier, year=season, team=team)


class offscreen(goldsberry.masterclass.NbaDataProviderPlayType):
    def __init__(self, season=goldsberry.apiparams.default_season, team=False):
        url_modifier = 'OffScreen'
        goldsberry.masterclass.NbaDataProviderPlayType.__init__(self, url_modifier, year=season, team=team)


class offrebound(goldsberry.masterclass.NbaDataProviderPlayType):
    def __init__(self, season=goldsberry.apiparams.default_season, team=False):
        url_modifier = 'OffRebound'
        goldsberry.masterclass.NbaDataProviderPlayType.__init__(self, url_modifier, year=season, team=team)


class misc(goldsberry.masterclass.NbaDataProviderPlayType):
    def __init__(self, season=goldsberry.apiparams.default_season, team=False):
        url_modifier = 'Misc'
        goldsberry.masterclass.NbaDataProviderPlayType.__init__(self, url_modifier, year=season, team=team)


__all__ = ['transition', 'isolation', 'pick_and_roll_ball_handler',
           'pick_and_roll_man', 'postup', 'spotup', 'handoff', 'cut',
           'offscreen', 'offrebound', 'misc']
