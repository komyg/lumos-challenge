# Lumos Backend Integrations Coding Challenge

## Installing Dependencies

This project uses [Poetry](https://python-poetry.org/) as its package manager.

To install the dependencies, please run: `poetry install` on your console.

## Running

### Environment Variables

To configure the environment variables locally, follow these steps:

1. Create a new _.env_ file in the project directory.
2. Copy and paste the values from the _.env.example_ file.
3. Update the `OKTA_URL` and `OKTA_TOKEN` variables with your own values.

### Running the Development Server

To run the development server execute these commands:

1. `poetry shell`
2. `make run`

### Running the Tests

To run the tests cases, execute these commands:

1. `poetry shell`
2. `make test`

## Additional Comments

### Handling API Throttling

There are a few different ways we could handle the case of API throttling in one of our integrations.

We could make all requests to third party APIs through a background worker such as [Celery](https://docs.celeryq.dev/en/stable/). This way we could add a retry logic with an exponential backoff strategy.

Another option would be to create a fully separated microservice for that particular integration. The service would then be responsible for retrying the requests also using an exponential backoff backoff strategy.

In both cases, we would have to keep the state of the API call inside a persistent store. This could be the application database in the case of Celery or the microservice database.
