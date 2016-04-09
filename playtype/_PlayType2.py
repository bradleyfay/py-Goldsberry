from goldsberry._masterclass import PLAYTYPE
from goldsberry._apiparams import *


class transition(PLAYTYPE):
    _url_modifier = 'Transition'


class isolation(PLAYTYPE):
    _url_modifier = 'Isolation'


class pick_and_roll_ball_handler(PLAYTYPE):
    _url_modifier = 'PRBallHandler'


class pick_and_roll_man(PLAYTYPE):
    _url_modifier = 'PRRollMan'


class postup(PLAYTYPE):
    _url_modifier = 'Postup'


class spotup(PLAYTYPE):
    _url_modifier = 'Spotup'


class handoff(PLAYTYPE):
    _url_modifier = 'Handoff'


class cut(PLAYTYPE):
    _url_modifier = 'Cut'


class offscreen(PLAYTYPE):
    _url_modifier = 'Offscreen'


class offrebound(PLAYTYPE):
    _url_modifier = 'OffRebound'


class misc(PLAYTYPE):
    _url_modifier = 'Misc'


__all__ = ['transition', 'isolation', 'pick_and_roll_ball_handler',
           'pick_and_roll_man', 'postup', 'spotup', 'handoff', 'cut',
           'offscreen', 'offrebound', 'misc']
