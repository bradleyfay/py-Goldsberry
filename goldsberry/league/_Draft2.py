from goldsberry._masterclass import *
from goldsberry._apiparams import *

class anthro(NBA_datapull):
    _url_modifier = 'draftcombineplayeranthro'
    def data(self):
        return self._get_table_from_data(self._datatables, 0)

class agility(NBA_datapull):
    _url_modifier = 'draftcombinedrillresults'
    def data(self):
        return self._get_table_from_data(self._datatables, 0)

class non_stationary_shooting(NBA_datapull):
    _url_modifier = 'draftcombinenonstationaryshooting'
    def data(self):
        return self._get_table_from_data(self._datatables, 0)

class spot_up_shooting(NBA_datapull):
    _url_modifier = 'draftcombinespotshooting'
    def data(self):
        return self._get_table_from_data(self._datatables, 0)

class combine(NBA_datapull):
    _url_modifier = 'draftcombinestats'
    def data(self):
        return self._get_table_from_data(self._datatables, 0)

__all__ = ['anthro', 'agility', 'non_stationary_shooting', 'spot_up_shooting',
           'combine']