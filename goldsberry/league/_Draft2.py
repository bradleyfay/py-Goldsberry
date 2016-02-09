from goldsberry._masterclass import *
from goldsberry._apiparams import *

class anthro(NBA_datapull):
    def __init__(self):
        NBA_datapull.__init__(self)
        self.SET_parameters(**p_game_ids)
        self._url_modifier = 'draftcombineplayeranthro'
        self.GET_raw_data()
    def data(self):
        return self._get_table_from_data(self._datatables, 0)

class agility(NBA_datapull):
    def __init__(self):
        NBA_datapull.__init__(self)
        self.SET_parameters(**p_game_ids)
        self._url_modifier = 'draftcombinedrillresults'
        self.GET_raw_data()
    def data(self):
        return self._get_table_from_data(self._datatables, 0)

class non_stationary_shooting(NBA_datapull):
    def __init__(self):
        NBA_datapull.__init__(self)
        self.SET_parameters(**p_game_ids)
        self._url_modifier = 'draftcombinenonstationaryshooting'
        self.GET_raw_data()
    def data(self):
        return self._get_table_from_data(self._datatables, 0)

class spot_up_shooting(NBA_datapull):
    def __init__(self):
        NBA_datapull.__init__(self)
        self.SET_parameters(**p_game_ids)
        self._url_modifier = 'draftcombinespotshooting'
        self.GET_raw_data()
    def data(self):
        return self._get_table_from_data(self._datatables, 0)

class combine(NBA_datapull):
    def __init__(self):
        NBA_datapull.__init__(self)
        self.SET_parameters(**p_game_ids)
        self._url_modifier = 'draftcombinestats'
        self.GET_raw_data()
    def data(self):
        return self._get_table_from_data(self._datatables, 0)

__all__ = ['anthro', 'agility', 'non_stationary_shooting', 'spot_up_shooting',
           'combine']