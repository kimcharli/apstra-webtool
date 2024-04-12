#


# setup

```sh
uv venv
source .venv/bin/activate
uv pip install -e .
```


# run


```sh
source .venv/bin/activate
uvicorn webtool.main:app
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

