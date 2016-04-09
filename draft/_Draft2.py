from goldsberry._masterclass import *
from goldsberry._apiparams import *

class anthro(NbaDataProvider):
    def __init__(self):
        url_modifier = 'draftcombineplayeranthro'
        NbaDataProvider.__init__(self, url_modifier=url_modifier, default_params=p_draft)
    def data(self):
        return self.get_table_from_data(self.data_tables, 0)

class agility(NbaDataProvider):
    def __init__(self):
        url_modifier = 'draftcombinedrillresults'
        NbaDataProvider.__init__(self, url_modifier=url_modifier, default_params=p_draft)
    def data(self):
        return self.get_table_from_data(self.data_tables, 0)

class non_stationary_shooting(NbaDataProvider):
    def __init__(self):
        url_modifier = 'draftcombinenonstationaryshooting'
        NbaDataProvider.__init__(self, url_modifier=url_modifier, default_params=p_draft)
    def data(self):
        return self.get_table_from_data(self.data_tables, 0)

class spot_up_shooting(NbaDataProvider):
    def __init__(self):
        url_modifier = 'draftcombinespotshooting'
        NbaDataProvider.__init__(self, url_modifier=url_modifier, default_params=p_draft)
    def data(self):
        return self.get_table_from_data(self.data_tables, 0)

class combine(NbaDataProvider):
    def __init__(self):
        url_modifier = 'draftcombinestats'
        NbaDataProvider.__init__(self, url_modifier=url_modifier, default_params=p_draft)
    def data(self):
        return self.get_table_from_data(self.data_tables, 0)

__all__ = ['anthro', 'agility', 'non_stationary_shooting', 'spot_up_shooting',
           'combine']