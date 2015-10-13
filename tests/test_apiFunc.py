# -*- coding: utf-8 -*-
import pytest

import goldsberry


test_data = [
(goldsberry._nbaLeague, 'NBA', '00'),
(goldsberry._nbaLeague, 'WNBA', '10'),
(goldsberry._nbaLeague, 'NBADL', '20'),
(goldsberry._nbaSeason, 1999, '1999-00'),
(goldsberry._nbaSeason, 2000, '2000-01'),
(goldsberry._seasonID, 1999, '21999'),
(goldsberry._measureType, 1, 'Base'),
(goldsberry._measureType, 2, 'Advanced'),
(goldsberry._Scope, 1, ''),
(goldsberry._PerModeSmall48, 1, 'Totals'),
(goldsberry._PerModeSmall36, 1, 'Totals'),
(goldsberry._PerModeMini, 1, 'Totals'),
(goldsberry._PerModeLarge, 1, 'Totals'),
(goldsberry._AheadBehind, 1, 'Ahead or Behind'),
(goldsberry._ClutchTime, 1, 'Last 5 Minutes'),
(goldsberry._GameScope, 2, 'Yesterday'),
(goldsberry._PlayerExperience, 2, 'Rookie'),
(goldsberry._PlayerPosition, 2, 'F'),
(goldsberry._StarterBench, 2, 'Starters'),
(goldsberry._PlusMinus, 2, 'Y'),
(goldsberry._PaceAdjust, 2, 'Y'),
(goldsberry._Rank, 2, 'Y'),
(goldsberry._SeasonType, 1, 'Regular Season'),
(goldsberry._SeasonType4, 1, 'Regular Season'),
(goldsberry._Outcome, 2, 'W'),
(goldsberry._Location, 2, 'Home'),
(goldsberry._SeasonSegment, 2, 'Post All-Star'),
(goldsberry._VsConference, 2, 'East'),
(goldsberry._VsDivision, 2, 'Atlantic'),
(goldsberry._GameSegment, 2, 'First Half'),
(goldsberry._DistanceRange, 1, '5ft Range'),
(goldsberry._valiDate, '', ''),
(goldsberry._valiDate, '2015-01-02', '2015-01-02'),
(goldsberry._ContextMeasure, 1, 'FGM'),
(goldsberry._Position, 2, 'Guard'),
(goldsberry._StatCategory, 1, 'MIN'),
]
@pytest.mark.parametrize("func,key,response", test_data)
def test_api_func(func, key, response):
    assert func(key) == response

@pytest.mark.parametrize('func,key', [
    (goldsberry._nbaLeague, 'BAD VALUE'),
    (goldsberry._nbaSeason, -1),
    (goldsberry._seasonID, -1),
    (goldsberry._measureType, -1),
    (goldsberry._Scope, -1),
    (goldsberry._PerModeSmall48, -1),
    (goldsberry._PerModeSmall36, -1),
    (goldsberry._PerModeMini, -1),
    (goldsberry._PerModeLarge, -1),
    (goldsberry._AheadBehind, -1),
    (goldsberry._ClutchTime, -1),
    (goldsberry._GameScope, -1),
    (goldsberry._PlayerExperience, -1),
    (goldsberry._PlayerPosition, -1),
    (goldsberry._StarterBench, -1),
    (goldsberry._PlusMinus, 0),
    (goldsberry._PaceAdjust, 0),
    (goldsberry._Rank, 0),
    (goldsberry._SeasonType, 0),
    (goldsberry._SeasonType4, 0),
    (goldsberry._Outcome, 0),
    (goldsberry._Location, 0),
    (goldsberry._SeasonSegment, 0),
    (goldsberry._VsConference, 0),
    (goldsberry._VsDivision, 0),
    (goldsberry._GameSegment, 0),
    (goldsberry._DistanceRange, 0),
    (goldsberry._valiDate, 'date'),
    (goldsberry._ContextMeasure, 0),
    (goldsberry._Position, 0),
    (goldsberry._StatCategory, 0)
])
def test_api_func_raises_valueerror(func, key):
    with pytest.raises(ValueError):
        func(key)
