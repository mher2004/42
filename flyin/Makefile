PY = python3
MAIN = main.py

run:
	$(PY) $(MAIN)

install:
	pip install -r requirements.txt

env:
	python3 -m venv venv

#activate:
#	source venv/bin/activate

lint:
	flake8 .
	mypy . \
	--warn-return-any \
	--warn-unused-ignores \
	--ignore-missing-imports \
	--disallow-untyped-defs \
	--check-untyped-defs

lint-strict:
	flake8 .
	mypy . --strict

debug:
	$(PY) -m pdb $(MAIN)

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type d -name ".mypy_cache" -exec rm -rf {} +

.PHONY: run install lint lint-strict clean debug

