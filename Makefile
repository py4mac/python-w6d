.PHONY: init
init:
	python -m poetry config virtualenvs.in-project true
	python -m poetry config virtualenvs.path env/
	python -m poetry install --no-root