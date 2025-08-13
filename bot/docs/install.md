# Installation Step By Step

## 1. Clone the repository

```sh
git clone https://github.com/TheAihopGG/Supports-Bot.git
cd Supports-Bot
```

## 2. Make sure you have python 3.13 installed.

```sh
python3 --version
```

## 3. Make sure you have poetry 2.1 installed.

```sh
poetry --version
```

## 4. Create virtual venv for any method and activate it

For example
```sh
python3.13 -m venv .venv
```

## 5. Create `.env` file

Copy `template.env` file, rename it to `.env`, and fill it out according to the [env file configuration](./env_configuration.md).

## 6. Build the project

Run
```sh
sudo docker build -t supports-bot
```

## 7. Launch the bot

Run
```sh
sudo docker compose up
```