VENV = venv

ALEMBIC = alembic


run:
	uvicorn src.main:app --reload --host 0.0.0.0 --port 8085


migrate:
	$(ALEMBIC) revision --autogenerate -m "$(message)"

upgrade:
	$(ALEMBIC) upgrade head

downgrade:
	$(ALEMBIC) downgrade -1

history:
	$(ALEMBIC) history

current:
	$(ALEMBIC) current


install:
	pip install -r requirements.txt

lint:
	black ./src
	isort ./src
	flake8 ./src
