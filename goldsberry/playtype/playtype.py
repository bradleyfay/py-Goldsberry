from goldsberry.masterclass import PlayTypeProvider


class transition(PlayTypeProvider):
    def __init__(self):
        url_modifier = 'Transition'
        PlayTypeProvider.__init__(self, url_modifier)


class isolation(PlayTypeProvider):
    def __init__(self):
        url_modifier = 'Isolation'
        PlayTypeProvider.__init__(self, url_modifier)


class pick_and_roll_ball_handler(PlayTypeProvider):
    def __init__(self):
        url_modifier = 'PRBallHandler'
        PlayTypeProvider.__init__(self, url_modifier)


class pick_and_roll_man(PlayTypeProvider):
    def __init__(self):
        url_modifier = 'PRRollMan'
        PlayTypeProvider.__init__(self, url_modifier)


class postup(PlayTypeProvider):
    def __init__(self):
        url_modifier = 'Postup'
        PlayTypeProvider.__init__(self, url_modifier)


class spotup(PlayTypeProvider):
    def __init__(self):
        url_modifier = 'Spotup'
        PlayTypeProvider.__init__(self, url_modifier)


class handoff(PlayTypeProvider):
    def __init__(self):
        url_modifier = 'Handoff'
        PlayTypeProvider.__init__(self, url_modifier)


class cut(PlayTypeProvider):
    def __init__(self):
        url_modifier = 'Cut'
        PlayTypeProvider.__init__(self, url_modifier)


class offscreen(PlayTypeProvider):
    def __init__(self):
        url_modifier = 'Offscreen'
        PlayTypeProvider.__init__(self, url_modifier)


class offrebound(PlayTypeProvider):
    def __init__(self):
        url_modifier = 'OffRebound'
        PlayTypeProvider.__init__(self, url_modifier)


class misc(PlayTypeProvider):
    def __init__(self):
        url_modifier = 'Misc'
        PlayTypeProvider.__init__(self, url_modifier)


__all__ = ['transition', 'isolation', 'pick_and_roll_ball_handler',
           'pick_and_roll_man', 'postup', 'spotup', 'handoff', 'cut',
           'offscreen', 'offrebound', 'misc']