.PHONY: all clean test

date=$(shell date +%F)

help:
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z0-9._-]+:.*?## / {printf "\033[1m\033[36m%-38s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

test: ## run pytest
	pytest -vvs

install: ## install for testing
	pip install -e .

lint: ## run flake8 to check the code
	flake8 src tests

fmt: ## run black to format the code
	black src tests
