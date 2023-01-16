#!/bin/bash
SHELL=/bin/bash

include .env
export

run:
	source .venv/bin/activate; export FLASK_APP=main; flask run --port=8080

debug:
	source .venv/bin/activate; export FLASK_APP=main; export FLASK_DEBUG=true; flask run --port=8080