#!/bin/bash
SHELL=/bin/bash

include .env
export

init:
	python -m venv .venv && source .venv/bin/activate && python -m pip install -r requirements.txt

run:
	source .venv/bin/activate; export FLASK_APP=main; flask run --port=8080 --host=0.0.0.0

debug:
	source .venv/bin/activate; export FLASK_APP=main; export FLASK_DEBUG=true; flask run --port=8080

requirements:
	python -m pip freezy > requirements.txt