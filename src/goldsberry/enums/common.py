"""Common enums used across NBA API endpoints.

Provides type-safe enumerations for parameters that accept
specific string or numeric values.
"""

from enum import Enum


class LeagueID(str, Enum):
    """NBA League identifiers."""

    NBA = "00"
    ABA = "01"
    WNBA = "10"
    G_LEAGUE = "20"


class Season(str, Enum):
    """NBA Season identifiers.

    Format: YYYY-YY (e.g., "2024-25" for 2024-2025 season)
    """

    # Recent seasons
    SEASON_2024_25 = "2024-25"
    SEASON_2023_24 = "2023-24"
    SEASON_2022_23 = "2022-23"
    SEASON_2021_22 = "2021-22"
    SEASON_2020_21 = "2020-21"
    SEASON_2019_20 = "2019-20"
    SEASON_2018_19 = "2018-19"
    SEASON_2017_18 = "2017-18"
    SEASON_2016_17 = "2016-17"
    SEASON_2015_16 = "2015-16"

    # Convenience
    CURRENT = "2024-25"

    @classmethod
    def from_year(cls, year: int) -> "Season":
        """Create season from starting year.

        Args:
            year: Starting year (e.g., 2024 for 2024-25 season)

        Returns:
            Season enum

        Example:
            >>> Season.from_year(2024)
            Season.SEASON_2024_25
        """
        next_year = str(year + 1)[-2:]
        season_str = f"{year}-{next_year}"
        try:
            return cls(season_str)
        except ValueError:
            # Return as-is if not in enum (for older seasons)
            return season_str  # type: ignore


class SeasonType(str, Enum):
    """Season type identifiers."""

    REGULAR_SEASON = "Regular Season"
    PLAYOFFS = "Playoffs"
    PRE_SEASON = "Pre Season"
    ALL_STAR = "All Star"
    ALL = "All"


class PerMode(str, Enum):
    """Per-game statistics mode."""

    TOTALS = "Totals"
    PER_GAME = "PerGame"
    PER_36 = "Per36"
    PER_48 = "Per48"
    PER_40 = "Per40"
    PER_MINUTE = "PerMinute"
    PER_POSSESSION = "PerPossession"
    PER_100_POSSESSIONS = "Per100Possessions"
    PER_100_PLAYS = "Per100Plays"


class MeasureType(str, Enum):
    """Statistical measure type."""

    BASE = "Base"
    ADVANCED = "Advanced"
    MISC = "Misc"
    FOUR_FACTORS = "Four Factors"
    SCORING = "Scoring"
    OPPONENT = "Opponent"
    USAGE = "Usage"
    DEFENSE = "Defense"


class PaceAdjust(str, Enum):
    """Pace adjustment for statistics."""

    YES = "Y"
    NO = "N"


class PlusMinus(str, Enum):
    """Plus/minus adjustment."""

    YES = "Y"
    NO = "N"


class Rank(str, Enum):
    """Ranking display."""

    YES = "Y"
    NO = "N"


class Outcome(str, Enum):
    """Game outcome filter."""

    WIN = "W"
    LOSS = "L"
    ALL = ""


class Location(str, Enum):
    """Game location filter."""

    HOME = "Home"
    ROAD = "Road"
    ALL = ""


class SeasonSegment(str, Enum):
    """Season segment filter."""

    ENTIRE_SEASON = ""
    PRE_ALL_STAR = "Pre All-Star"
    POST_ALL_STAR = "Post All-Star"


class Month(int, Enum):
    """Month filter."""

    ALL = 0
    OCTOBER = 1
    NOVEMBER = 2
    DECEMBER = 3
    JANUARY = 4
    FEBRUARY = 5
    MARCH = 6
    APRIL = 7
    MAY = 8
    JUNE = 9
    JULY = 10
    AUGUST = 11
    SEPTEMBER = 12


class Period(int, Enum):
    """Game period filter."""

    ALL = 0
    FIRST_QUARTER = 1
    SECOND_QUARTER = 2
    THIRD_QUARTER = 3
    FOURTH_QUARTER = 4
    OVERTIME_1 = 5
    OVERTIME_2 = 6
    OVERTIME_3 = 7
    OVERTIME_4 = 8
    OVERTIME_5 = 9
    OVERTIME_6 = 10


class ShotClockRange(str, Enum):
    """Shot clock time range."""

    ALL = ""
    OFF = "ShotClock Off"
    VERY_LATE = "24-22"
    LATE = "22-18 Very Late"
    EARLY = "18-15 Late"
    VERY_EARLY = "15-7 Early"
    EARLY_SHOT = "7-4 Very Early"
    VERY_EARLY_SHOT = "4-0 Very Early"


class PlayerOrTeam(str, Enum):
    """Player or team scope."""

    PLAYER = "Player"
    TEAM = "Team"


class PlayerPosition(str, Enum):
    """Player position filter."""

    ALL = ""
    GUARD = "G"
    FORWARD = "F"
    CENTER = "C"
    POINT_GUARD = "PG"
    SHOOTING_GUARD = "SG"
    SMALL_FORWARD = "SF"
    POWER_FORWARD = "PF"


class StarterBench(str, Enum):
    """Starter vs bench filter."""

    ALL = ""
    STARTERS = "Starters"
    BENCH = "Bench"


class DraftYear(str, Enum):
    """Draft year filter."""

    ALL = ""


class DraftRound(str, Enum):
    """Draft round filter."""

    ALL = ""
    FIRST_ROUND = "1"
    SECOND_ROUND = "2"


class College(str, Enum):
    """College filter."""

    ALL = ""


class Country(str, Enum):
    """Country filter."""

    ALL = ""


class Height(str, Enum):
    """Height filter."""

    ALL = ""


class Weight(str, Enum):
    """Weight filter."""

    ALL = ""


class GameScope(str, Enum):
    """Game scope filter."""

    ALL = ""
    YESTERDAY = "Yesterday"
    LAST_10 = "Last 10"


class PlayerScope(str, Enum):
    """Player scope filter."""

    ALL_PLAYERS = "All Players"
    ROOKIES = "Rookies"


class IsOnlyCurrentSeason(int, Enum):
    """Filter for current season only."""

    ALL_TIME = 0
    CURRENT_SEASON_ONLY = 1


__all__ = [
    "LeagueID",
    "Season",
    "SeasonType",
    "PerMode",
    "MeasureType",
    "PaceAdjust",
    "PlusMinus",
    "Rank",
    "Outcome",
    "Location",
    "SeasonSegment",
    "Month",
    "Period",
    "ShotClockRange",
    "PlayerOrTeam",
    "PlayerPosition",
    "StarterBench",
    "DraftYear",
    "DraftRound",
    "College",
    "Country",
    "Height",
    "Weight",
    "GameScope",
    "PlayerScope",
    "IsOnlyCurrentSeason",
]
