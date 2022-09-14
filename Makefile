run:
	export FLASK_ENV=development
	flask --debug --app ./app/app.py run --port=5000

test:
	pytest ./app

clean:
	rm -r -f __pycache__
	rm -r -f .pytest_cache
