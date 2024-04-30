#


# setup

## install
```sh
git clone https://github.com/kimcharli/apstra-webtool.git
cd apstra-webtool
scripts/re-venv.sh
```

## generated self signed certificate
```sh
scripts/re-selfsigned.sh
```


# run


```sh
scripts/start.sh
```


# TODO

One way
```sh
source .venv/bin/activate
webtool
```

Other way
```sh
source .venv/bin/activate
python -m webtool
```


# misc
```

poetry new rp-poetry [--name rp-poetry]
cd rp-poetry
poetry env info --path
poetry env list
poetry config --list
poetry add requests beautifulsoup4
poetry install
poetry run python -c "import requests"
poetry run python -q

```


# TODO:

```
[tool.poetry.env]
WEB_TITLE = "Apstra Webtool!"
```

