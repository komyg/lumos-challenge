run:
	export DEBUG=true
	export FLASK_APP=app.py
	export FLASK_ENV=development
	flask --debug run --port=5000

test:
	pytest .

clean:
	rm -r -f __pycache__
	rm -r -f .pytest_cache
