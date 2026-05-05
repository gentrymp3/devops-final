install:
	pip install -r requirements.txt

test:
	PYTHONPATH=. pytest -v

run:
	python main.py