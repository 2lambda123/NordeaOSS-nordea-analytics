# Nordea Analytics

## Install
```commandline
python -m pip install nordea-analytics
```


## Development steps
1. Make sure you have the required Python version installed (the following command should list all the versions)
```commandline
py --list
```
2. Create a virtual environment, e.g. for python3.9 and activate
```commandline
py -3.9 -m venv venv
venv39\Scripts\activate
```

3. Install pip-tools if you're creating the environment for the first time
```commandline
python -m pip install --index-url https://artifactory.itcm.oneadr.net/api/pypi/pypi-remote/simple pip-tools
```

4. Synchronise your dependencies (do this after pulling as well since someone might have updated dependencies)
```commandline
python -m piptools sync requirements\py39\requirements.txt requirements\py39\requirements-dev.txt
```

5. Install the package in editable mode (you need to do this after syncing because syncing will remove nordea-analytics
   since it is not in the requirements files)
```commandline
python -m pip install --no-deps --index-url https://artifactory.itcm.oneadr.net/api/pypi/pypi-remote/simple -e .
```
   
6. Write your code and run black to format the code
 ```commandline
 nox -rs black
 ```
   
7. Run the CI steps locally and fix the errors. The --no-install flag is used if the dependencies versions are unchanged
   in order to speed up the process. Don't pass the flag if one of the dependency versions changed.
 ```commandline
 nox -r -p 3.9 --no-install
 ```
   
8. Commit and push your code, and deactivate the environment.
 ```commandline
 deactivate
 ```
## Release
Development should be done on the develop branch. When new version of the library should be published, the version should
be bumped and develop branch merged with master branch. This is done with the following steps:
1. Go into nordea-analytics bitbucket and bump the version (see Versioning below) in src/nordea_analytics/__init__.py
2. Go into Pull request - Create Pull Request
3. Select to merge develop branch to master. Make sure both branches are built in bamboo.
 
## Versioning
Developers need to keep track of the library version.
The version of the library is single sourced from `src/nordea_analytics/__init__.py`.
The version number follows the [semantic versioning](https://semver.org/) scheme.
Read about semantic versioning carefully before determining whether your change should come in the form of
incrementing the major, minor or patch version number.


## Documentation
The docstrings used within the library should follow the
[Google docstyle](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html).

## Update requirements
The requirements are maintained separately for each Python version (3.6, 3.7, 3.8, 3.9).
1. Create and activate the virtual environment for each Python version
```commandline
py -<major_version>.<minorversion> -m venv venv<major_version><minor_version>
```
2. Delete the production and development requirement files
```commandline
del requirements\py<major_version><minor_version>\requirements.txt requirements\py<major_version><minor_version>\requirements-dev.txt
```
3. Recreate the production and development requirement files using pip-compile
```commandline
python -m piptools compile --strip-extras --index-url https://artifactory.itcm.oneadr.net/api/pypi/pypi-remote/simple requirements\py<major_version><minor_version>\requirements.in
python -m piptools compile --strip-extras --index-url https://artifactory.itcm.oneadr.net/api/pypi/pypi-remote/simple requirements\py<major_version><minor_version>\requirements-dev.in
```
4. Synchronise your virtual environment with the new requirement files (if you want to run something with this environment).
```commandline
python -m piptools sync requirements\py<major_version><minor_version>\requirements.txt requirements\py<major_version><minor_version>\requirements-dev.txt
```

5. Install the package in editable mode (if you want to run something with this environment).
```commandline
python -m pip install --no-deps --index-url https://artifactory.itcm.oneadr.net/api/pypi/pypi-remote/simple -e .
```