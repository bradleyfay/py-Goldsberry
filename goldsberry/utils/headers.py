from pydantic import BaseModel
from random_user_agent.params import OperatingSystem, SoftwareName
from random_user_agent.user_agent import UserAgent

# you can also import SoftwareEngine, HardwareType, SoftwareType, Popularity from random_user_agent.params
# you can also set number of user agents required by providing `limit` as parameter

software_names = [SoftwareName.CHROME.value, SoftwareName.FIREFOX.value]
operating_systems = [OperatingSystem.WINDOWS.value,
                     OperatingSystem.LINUX.value,
                     OperatingSystem.ANDROID.value,
                     OperatingSystem.IOS.value]

user_agent_rotator = UserAgent(
    software_names=software_names, operating_systems=operating_systems, limit=100)


def aliaser(name: str) -> str:
    names = [n.title() for n in name.split('_')]
    return '-'.join(names)


class Header(BaseModel):
    user_agent: str
    accept: str = "text/html,application/xhtml+xml,application/xml;q=0.9"

    class Config:
        allow_population_by_field_name = True
        alias_generator = aliaser


def get_header() -> Header:

    return Header(user_agent=user_agent_rotator.get_random_user_agent()).dict(by_alias=True)
