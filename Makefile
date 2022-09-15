run:
	python app/app.py

test:
	pytest ./app

clean:
	find . -type f -name '*.py[co]' -delete -o -type d -name __pycache__ -delete
	rm -r -f .pytest_cache
