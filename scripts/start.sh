#!/bin/bash

poetry run uvicorn webtool.main:app --host 0.0.0.0 --port 8083 --reload --ssl-keyfile certs/key.pem --ssl-certfile certs/cert.pem
