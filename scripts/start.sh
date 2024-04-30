#!/bin/bash

uvicorn webtool.main:app --reload --ssl-keyfile certs/key.pem --ssl-certfile certs/cert.pem
