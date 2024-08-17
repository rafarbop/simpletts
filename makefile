SHELL := /bin/bash

venv:
	python3 -m venv venv
	source venv/bin/activate && pip3 install -r requirements.txt

install:
	pip3 install -r requirements.txt

clean:
	rm -rf venv