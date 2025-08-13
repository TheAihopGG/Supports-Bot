# Project Configuration

- `ENV_FILENAME: Path`

  Path to `.env` file

- `IS_DEV_MODE: bool`

  Is bot in product or develop. If `True`, prod database will be used, else dev database.

- `LOGGING_FILENAME`

  Path to logs file. Example: `./bot/logs/logs.log`

- `LOGGING_FILEMODE`

  Log`s file mode. "w" or "a"

- `PROD_SQLALCHEMY_URL`

  The URL that sqlalchemy will connect to. If `IS_DEV_MODE` == `False`

- `DEV_SQLALCHEMY_URL`

  The URL that sqlalchemy will connect to. If `IS_DEV_MODE` == `True`

- `BOT_TOKEN`

  Bot token from `.env` file.
