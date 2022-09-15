run:
	python app/app.py

test:
	pytest ./app

clean:
	rm -r -f __pycache__
	rm -r -f .pytest_cache
