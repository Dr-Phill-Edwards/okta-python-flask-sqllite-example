# Build a website with Python, Flask, and SQLite

This repository contains an example web application written in Python using the Flask and SQLite libraries. Please read [Build a website with Python, Flask, and SQLite]() to see how it was created.

### Prerequsites

- Python 3
* Okta CLI 0.8.0+

## Getting Started

To run this example, run the following commands:

```bash
git clone https://github.com/oktadev/okta-python-flask-sqllite-example.git
cd okta-python-flask-sqllite-example
python3 -m venv .venv
. .venv/bin/activate
pip install --upgrade pip
pip install flask okta okta-jwt
```

## Create the OIDC Application in Okta

Register for a free developer account with the following simple commands using the [Okta CLI](https://github.com/okta/okta-cli), in the project root folder:

```bash
okta register
```

Provide the required information. Once you register, create a client application in Okta with the following command:

```bash
okta apps create
```

You will be prompted to select the following options:
* Type of Application: 2: SPA
* Redirect URI: http://localhost:8080
* Logout Redirect URI: http://localhost:8080

The application configuration will be printed to your screen:

```
Okta application configuration:
Issuer:    https://dev-123456.okta.com/oauth2/default
Client ID: 0o...7
```

Set the following environment variables using the values printed out:

```bash
export OKTA_DOMAIN=https://dev-123456.okta.com
export OKTA_ISSUER_ID=https://$OKTA_DOMAIN/oauth2/default
export OKTA_CLIENT_ID=0...5
```

Start your app and you should be able to log in.

```bash
python Server.py
```

## Links

This example uses the following open source libraries from Okta:

* [Okta SignIn Widget](https://github.com/okta/okta-signin-widget)
* [Okta CLI](https://github.com/okta/okta-cli)

## Help

Please post any questions as comments on the [blog post](https://developer.okta.com/blog/...), or visit our [Okta Developer Forums](https://devforum.okta.com/).

## License

Apache 2.0, see [LICENSE](LICENSE).
