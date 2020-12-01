# define the name of the virtual environment directory
VENV := venv

all: venv

$(VENV)/bin/activate: requirements.txt
	python3 -m venv $(VENV)
	./$(VENV)/bin/pip install -r requirements.txt

# venv is a shortcut target
venv: $(VENV)/bin/activate

lint: venv
	flake8 --exclude=venv

test: venv
	pytest --ignore=venv

run: venv
	flake8 --exclude=venv
	pytest --ignore=venv


clean:
	rm -rf $(VENV)
	find . -type f -name '*.pyc' -delete
