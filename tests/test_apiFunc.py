# -*- coding: utf-8 -*-
import pytest

from goldsberry._apifunc import  *

test_data = [
(_nbaLeague, 'NBA', '00'),
(_nbaLeague, 'WNBA', '10'),
(_nbaLeague, 'NBADL', '20'),
(_nbaSeason, 1999, '1999-00'),
(_nbaSeason, 2000, '2000-01'),
(_seasonID, 1999, '21999'),
(_measureType, 1, 'Base'),
(_measureType, 2, 'Advanced'),
(_Scope, 1, ''),
(_PerModeSmall48, 1, 'Totals'),
(_PerModeSmall36, 1, 'Totals'),
(_PerModeMini, 1, 'Totals'),
(_PerModeLarge, 1, 'Totals'),
(_AheadBehind, 1, 'Ahead or Behind'),
(_ClutchTime, 1, 'Last 5 Minutes'),
(_GameScope, 2, 'Yesterday'),
(_PlayerExperience, 2, 'Rookie'),
(_PlayerPosition, 2, 'F'),
(_StarterBench, 2, 'Starters'),
(_PlusMinus, 2, 'Y'),
(_PaceAdjust, 2, 'Y'),
(_Rank, 2, 'Y'),
(_SeasonType, 1, 'Regular Season'),
(_SeasonType4, 1, 'Regular Season'),
(_Outcome, 2, 'W'),
(_Location, 2, 'Home'),
(_SeasonSegment, 2, 'Post All-Star'),
(_VsConference, 2, 'East'),
(_VsDivision, 2, 'Atlantic'),
(_GameSegment, 2, 'First Half'),
(_DistanceRange, 1, '5ft Range'),
(_valiDate, '', ''),
(_valiDate, '2015-01-02', '2015-01-02'),
(_ContextMeasure, 1, 'FGM'),
(_Position, 2, 'Guard'),
(_StatCategory, 1, 'MIN'),
]
@pytest.mark.parametrize("func,key,response", test_data)
def test_api_func(func, key, response):
    assert func(key) == response

@pytest.mark.parametrize('func,key', [
    (_nbaLeague, 'BAD VALUE'),
    (_nbaSeason, -1),
    (_seasonID, -1),
    (_measureType, -1),
    (_Scope, -1),
    (_PerModeSmall48, -1),
    (_PerModeSmall36, -1),
    (_PerModeMini, -1),
    (_PerModeLarge, -1),
    (_AheadBehind, -1),
    (_ClutchTime, -1),
    (_GameScope, -1),
    (_PlayerExperience, -1),
    (_PlayerPosition, -1),
    (_StarterBench, -1),
    (_PlusMinus, 0),
    (_PaceAdjust, 0),
    (_Rank, 0),
    (_SeasonType, 0),
    (_SeasonType4, 0),
    (_Outcome, 0),
    (_Location, 0),
    (_SeasonSegment, 0),
    (_VsConference, 0),
    (_VsDivision, 0),
    (_GameSegment, 0),
    (_DistanceRange, 0),
    (_valiDate, 'date'),
    (_ContextMeasure, 0),
    (_Position, 0),
    (_StatCategory, 0)
])
def test_api_func_raises_valueerror(func, key):
    with pytest.raises(ValueError):
        func(key)
