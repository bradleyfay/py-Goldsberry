from goldsberry._masterclass import *
from goldsberry._apiparams import *

class anthro(NbaDataProvider):
    def __init__(self):
        NbaDataProvider.__init__(self)
        self.set_default_api_parameters(**p_draft)
        self._url_modifier = 'draftcombineplayeranthro'
        self._set_class_data()
    def data(self):
        return self.get_table_from_data(self.data_tables, 0)

class agility(NbaDataProvider):
    def __init__(self):
        NbaDataProvider.__init__(self)
        self.set_default_api_parameters(**p_draft)
        self._url_modifier = 'draftcombinedrillresults'
        self._set_class_data()
    def data(self):
        return self.get_table_from_data(self.data_tables, 0)

class non_stationary_shooting(NbaDataProvider):
    def __init__(self):
        NbaDataProvider.__init__(self)
        self.set_default_api_parameters(**p_draft)
        self._url_modifier = 'draftcombinenonstationaryshooting'
        self._set_class_data()
    def data(self):
        return self.get_table_from_data(self.data_tables, 0)

class spot_up_shooting(NbaDataProvider):
    def __init__(self):
        NbaDataProvider.__init__(self)
        self.set_default_api_parameters(**p_draft)
        self._url_modifier = 'draftcombinespotshooting'
        self._set_class_data()
    def data(self):
        return self.get_table_from_data(self.data_tables, 0)

class combine(NbaDataProvider):
    def __init__(self):
        NbaDataProvider.__init__(self)
        self.set_default_api_parameters(**p_draft)
        self._url_modifier = 'draftcombinestats'
        self._set_class_data()
    def data(self):
        return self.get_table_from_data(self.data_tables, 0)

__all__ = ['anthro', 'agility', 'non_stationary_shooting', 'spot_up_shooting',
           'combine']