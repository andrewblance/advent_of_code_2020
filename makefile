.ONESHELL:

# define the name of the virtual environment directory
VENV := venv

all: venv

$(VENV)/bin/activate: requirements.txt
	python3 -m venv $(VENV)
	./$(VENV)/bin/pip install -r requirements.txt

# venv is a shortcut target
venv: $(VENV)/bin/activate

lint: venv
	./$(VENV)/bin/python3 -m flake8 --exclude=venv,docs

mypy: venv
	./$(VENV)/bin/python3 -m mypy src/

test: venv
	./$(VENV)/bin/python3 -m pytest --ignore=venv,docs

sphinx: venv
	make html -C ./docs

# small run, only runs tests
small_run: venv
	./$(VENV)/bin/python3 -m pytest --ignore=venv,docs 
	./$(VENV)/bin/python3 -m src.main 

# this is the full run
# what you should use to do everything
run: venv
	./$(VENV)/bin/python3 -m flake8 --exclude=venv,docs
	./$(VENV)/bin/python3 -m pytest --ignore=venv,docs
	./$(VENV)/bin/python3 -m mypy src
	make html -C ./docs
	./$(VENV)/bin/python3 -m src.main


clean:
	make clean -C ./docs
	rm -rf $(VENV)
	find . -type f -name '*.pyc' -delete

