from goldsberry.masterclass import NbaDataProvider
from goldsberry.apiparams import *


class anthro(NbaDataProvider):
    def __init__(self, season=default_season):
        url_modifier = 'draftcombineplayeranthro'
        NbaDataProvider.__init__(self, url_modifier=url_modifier, default_params=p_draft, SeasonYear=season)

    def data(self):
        return self.object_manager.get_table_from_data(self.object_manager.data_tables, 0)


class agility(NbaDataProvider):
    def __init__(self, season=default_season):
        url_modifier = 'draftcombinedrillresults'
        NbaDataProvider.__init__(self, url_modifier=url_modifier, default_params=p_draft, SeasonYear=season)

    def data(self):
        return self.object_manager.get_table_from_data(self.object_manager.data_tables, 0)


class non_stationary_shooting(NbaDataProvider):
    def __init__(self, season=default_season):
        url_modifier = 'draftcombinenonstationaryshooting'
        NbaDataProvider.__init__(self, url_modifier=url_modifier, default_params=p_draft, SeasonYear=season)

    def data(self):
        return self.object_manager.get_table_from_data(self.object_manager.data_tables, 0)


class spot_up_shooting(NbaDataProvider):
    def __init__(self, season=default_season):
        url_modifier = 'draftcombinespotshooting'
        NbaDataProvider.__init__(self, url_modifier=url_modifier, default_params=p_draft, SeasonYear=season)

    def data(self):
        return self.object_manager.get_table_from_data(self.object_manager.data_tables, 0)


class combine(NbaDataProvider):
    def __init__(self, season=default_season):
        url_modifier = 'draftcombinestats'
        NbaDataProvider.__init__(self, url_modifier=url_modifier, default_params=p_draft, SeasonYear=season)

    def data(self):
        return self.object_manager.get_table_from_data(self.object_manager.data_tables, 0)


class draft_history(NbaDataProvider):
    def __init__(self):
        url_modifier = 'drafthistory'
        NbaDataProvider.__init__(self, url_modifier=url_modifier, default_params=p_league_only)

    def data(self):
        return self.object_manager.get_table_from_data(self.object_manager.data_tables, 0)


__all__ = ['anthro', 'agility', 'non_stationary_shooting', 'spot_up_shooting',
           'combine', 'draft_history']
