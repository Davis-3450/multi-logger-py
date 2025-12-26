from enum import Enum


class Level(str, Enum):
    """Emojis for different log levels."""

    DEBUG = "🐛"
    INFO = "ℹ️"
    WARNING = "⚠️"
    ERROR = "❌"
    SUCCESS = "✅"
    CRITICAL = "🔥"

    @staticmethod
    def use_emoji(level_string: str) -> str:
        """Get the emoji representation of a log level.

        Args:
            level_string (str): Log level as a string.

        Returns:
            str: Emoji corresponding to the log level.
        """
        level_string = level_string.upper()
        if level_string in Level.__members__:
            return Level[level_string].value
        return level_string
