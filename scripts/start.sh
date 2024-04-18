#!/bin/bash

#python -m uvicorn webtool.main:app --reload
uvicorn webtool.main:app --reload --log-level debug --port 8000
