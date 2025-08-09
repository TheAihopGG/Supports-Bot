"""
The package contains files with class inherits from `sqlalchemy.Model` inside.
"""

from .base import Base
from .guild_settings import GuildSettings

__all__ = ("Base", "GuildSettings")
