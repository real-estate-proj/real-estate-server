ENV_NAME=venv

install:
	python -m venv $(ENV_NAME)
	. $(ENV_NAME)/bin/activate && pip install -r requirements.txt

run:
	. $(ENV_NAME)/bin/activate && cd src && python main.py