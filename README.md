#


# setup

## install

## prerequisite

- uv : https://astral.sh/blog/uv
- python: 3.11

## clone
```sh
git clone https://github.com/kimcharli/apstra-webtool.git
cd apstra-webtool
scripts/re-venv.sh
```

## generate self signed certificate
```sh
scripts/re-selfsigned.sh
```


# run


```sh
scripts/start.sh
```

Example
```
(apstra-webtool) ckim@ckim-mbp:apstra-webtool % scripts/start.sh
INFO:     Will watch for changes in these directories: ['/Users/ckim/Documents/Projects/apstra-webtool']
INFO:     Uvicorn running on https://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [78528] using WatchFiles
INFO:     Started server process [78530]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```


Open browser: <a href="https://127.0.0.1:8000" target="_blank">https://127.0.0.1:8000</a>



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


# initial setup

```sh
poetry init
poetry add ruff -G dev
```

## setup frontend with vite-react-swc

```sh
nvm use v20.13.1
npm create vite frontend -- template react-swc 
(create-vite@5.2.3, React, JavaScript + SWC)
cd frontend
npm install
npm run dev

npm run build
```
