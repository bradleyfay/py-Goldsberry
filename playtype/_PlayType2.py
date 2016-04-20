import goldsberry.masterclass


class transition(goldsberry.masterclass.PlayTypeProvider):
    def __init__(self, team=False):
        url_modifier = 'Transition'
        goldsberry.masterclass.PlayTypeProvider.__init__(self, url_modifier, team=team)


class isolation(goldsberry.masterclass.PlayTypeProvider):
    def __init__(self, team=False):
        url_modifier = 'Isolation'
        goldsberry.masterclass.PlayTypeProvider.__init__(self, url_modifier, team=team)


class pick_and_roll_ball_handler(goldsberry.masterclass.PlayTypeProvider):
    def __init__(self, team=False):
        url_modifier = 'PRBallHandler'
        goldsberry.masterclass.PlayTypeProvider.__init__(self, url_modifier, team=team)


class pick_and_roll_man(goldsberry.masterclass.PlayTypeProvider):
    def __init__(self, team=False):
        url_modifier = 'PRRollMan'
        goldsberry.masterclass.PlayTypeProvider.__init__(self, url_modifier, team=team)


class postup(goldsberry.masterclass.PlayTypeProvider):
    def __init__(self, team=False):
        url_modifier = 'Postup'
        goldsberry.masterclass.PlayTypeProvider.__init__(self, url_modifier, team=team)


class spotup(goldsberry.masterclass.PlayTypeProvider):
    def __init__(self, team=False):
        url_modifier = 'Spotup'
        goldsberry.masterclass.PlayTypeProvider.__init__(self, url_modifier, team=team)


class handoff(goldsberry.masterclass.PlayTypeProvider):
    def __init__(self, team=False):
        url_modifier = 'Handoff'
        goldsberry.masterclass.PlayTypeProvider.__init__(self, url_modifier, team=team)


class cut(goldsberry.masterclass.PlayTypeProvider):
    def __init__(self, team=False):
        url_modifier = 'Cut'
        goldsberry.masterclass.PlayTypeProvider.__init__(self, url_modifier, team=team)


class offscreen(goldsberry.masterclass.PlayTypeProvider):
    def __init__(self, team=False):
        url_modifier = 'OffScreen'
        goldsberry.masterclass.PlayTypeProvider.__init__(self, url_modifier, team=team)


class offrebound(goldsberry.masterclass.PlayTypeProvider):
    def __init__(self, team=False):
        url_modifier = 'OffRebound'
        goldsberry.masterclass.PlayTypeProvider.__init__(self, url_modifier, team=team)


class misc(goldsberry.masterclass.PlayTypeProvider):
    def __init__(self, team=False):
        url_modifier = 'Misc'
        goldsberry.masterclass.PlayTypeProvider.__init__(self, url_modifier, team=team)


__all__ = ['transition', 'isolation', 'pick_and_roll_ball_handler',
           'pick_and_roll_man', 'postup', 'spotup', 'handoff', 'cut',
           'offscreen', 'offrebound', 'misc']
