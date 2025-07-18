ENV_NAME=venv

install:
	python -m venv $(ENV_NAME)
	. $(ENV_NAME)\Scripts\activate && pip install -r requirements.txt

vr:
	$(ENV_NAME)\Scripts\activate

run:
	$(ENV_NAME)\Scripts\activate && cd src && python main.py

up:
	docker-compose up

down:
	docker-compose down

