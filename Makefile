.PHONY: clean coverage test tox-test

test:
	py.test tests/

tox-test:
	tox

coverage:
	coverage run --source goldsberry -m py.test
	coverage report

clean:
	find . -name '*.pyc' -exec rm -f {} +
	rm -rf .tox/
