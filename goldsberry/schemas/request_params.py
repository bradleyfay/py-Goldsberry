from typing import Dict, List, Optional, Union

from pydantic import BaseModel
from typing_extensions import Literal


class ResultSet(BaseModel):
    name: str
    headers: List[str]
    rowSet: List[List[Union[str, int, float]]]


class NBAResponse(BaseModel):
    resource: str  # This matches the EndpointEnum
    parameters: Dict  # These match API Parameters conditional on resource
    resultSet: ResultSet


class LeagueLeaders(BaseModel):
    LeagueID: Literal["00"]
    PerMode: Literal["PerGame"]
    StatCategory: str
    Season: str
    SeasonType: Literal['Regular Season']
    Scope: Literal["S"]
    ActiveFlag: Optional[str] = None
