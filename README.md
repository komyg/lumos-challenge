# Lumos Backend Integrations Coding Challenge

## Introduction 👋

- For this challenge, you will build out an API integration that has a few capabilities.
- The high-level objectives are, roughly in the following order:

    1. Build a working system
    2. Implement as many features as you're able to
    3. Build with software development principles in mind — try to keep your
       code modular and readable (we look at it!), and use git commits to
       checkpoint progress.

- You are also welcome to bring in any libraries or tools (even replacing our
  starter code) that help you better achieve the objectives above. Don't worry
  about dependencies or reproducibility for the time being. We'll do the demo
  only on your computer at the end of the challenge.

## Getting Started 📈

There is just one component for this challenge: a simple python backend server
using flask to handle requests.

### Setup 🏗
- You can run the following commands to create an isolated
  python env containing just the dependencies of this project! 🎉
  ```shell
  python3 -m venv venv
  . venv/bin/activate
  pip install -r requirements.txt
  ```

### Running the server 🏃
To run the server, you just need to run this in your shell:
```shell
./run.sh
```

Once your server is running, you can make sure it is working by making a
couple of local HTTP requests to it:
```shell
curl http://127.0.0.1:5000/capabilities/okta
curl http://127.0.0.1:5000/okta/list_users
```

If you have it installed already, you might find
[Postman](https://www.postman.com/) helpful when testing out the different API
calls.

### Running the unit tests
You might find it helpful to write unit tests as you work on your task. You can run unit tests using `pytest` by running this in your shell:
```shell
./test.sh
```

## Your Task ✨
The existing starter code in `app.py` contains a basic API that has endpoints
for the following functionality:
- return a set of capabilities for a specified integration (ex: for Okta)
- run read operations based on specified capabilities
- run write operations based on specified capabilities

Your task is to first extend the API to support the following capabilities for
Okta:
- `list_users`: https://developer.okta.com/docs/reference/api/users/#list-users
- `suspend_user`: https://developer.okta.com/docs/reference/api/users/#suspend-user
- `delete_user`: https://developer.okta.com/docs/reference/api/users/#delete-user

NOTE: the starter code provides some structure, but it is intentionally
open-ended and underspecified. Please implement the above functionality as you
see fit!

### Additional Features 🔥

Afterwards, you can choose to extend the project in a direction that you find
interesting! Here is a list of features that you can pick and choose from:
- Build an extensible system so that it's easy to add a new integration with a different set of capabilities. Imagine if you had to write 100 integrations, how would you rewrite the code structure?
- Build an extensible system so that it's easy to swap out authentication methods to call APIs
- Build a module that securely stores and retrieves the API keys / tokens. Think proper interfaces so that you can swap them out later on with a cloud-based secrets management service.
- Write a test suite that can test out the API integrations capabilities (unit tests and/or integration tests)
- Write a small design doc on how you would API throttling and retries when doing integration operations

## Tips 💡
- Remember the order of the priorities:
  1. Build a working system
  2. Keep in mind we have multiple customers, and which customer has a different Okta instance to integrate, it's a nice idea to implement something that could work in this case
  3. Implement as many features as you're able to
  4. Build with good software engineering principles in mind

- Remember that you are welcome to use any tools, techniques, libraries to make
  you productive and help with the stated goals!
