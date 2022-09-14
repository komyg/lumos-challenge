run:
	export DEBUG=true
	export FLASK_APP=app.py
	export FLASK_ENV=development
	flask --debug run --port=5000

test:
	pytest .