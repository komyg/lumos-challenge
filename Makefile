run:
	flask --debug --app app run --port=5000

test:
	pytest ./app

clean:
	find . -type f -name '*.py[co]' -delete -o -type d -name __pycache__ -delete
	rm -r -f .pytest_cache
