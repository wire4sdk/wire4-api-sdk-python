# wire4-authenticator
Referencia de la herramienta de autenticación para el API de Wire4

This Python package is make and sopported by Wire4:

- API version: 1.0.0
- Package version: 1.0.0

## Requirements.

Python 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/wire4/wire4-api-sdk-python#subdirectory=authenticator
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import wire4_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import wire4_auth
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from wire4_auth import OAuthWire4, EnvironmentEnum
from wire4_auth.webhook_verification_signature.utils_compute import UtilsCompute
from wire4_client import SaldoApi
from wire4_client.rest import ApiException

# Build OAuth2 access token for get authorization tokens
oauth_wire = OAuthWire4("FxUWmqYGZuv8O1qjxstvIyJothMa", "kjwbkrPVgXsnaUGzthj55dsFhx4a", EnvironmentEnum.SANDBOX)

# Token App User
oauth_token_user = oauth_wire.obtain_access_token_app_user("071e2b59b354186b3a0158de493536@sandbox.wire4.mx",
                                                           "0d1e33e94604f01b4e00d2fcb6b48f", "spei_admin")

"""Test Balance"""
# create an instance of the API class
api_instance = SaldoApi(OAuthWire4.get_default_api_client(oauth_token_user))
try:

    # Query balance
    api_response = api_instance.get_balance_using_get("f1504fea-3a8f-475a-a50a-90d3c40efc59")
    print(api_response)
except ApiException as e:

    print("Exception when calling SaldoApi->get_balance_using_get: %s\n" % e)
```

## Author

Wire4
