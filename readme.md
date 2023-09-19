### Pip install requirements.txt file
A requirements.txt file contains a simple list of dependencies, one per line. In its most simple form, it could look like this:

```
simplejson
chardet
```

## pipenv

### install 
```pip install pipenv```

### use for the first time
```pipenv install```

### activation
```pipenv shell```

### install
```
pipenv install django
pipenv uninstall django
pipenv install -r requirements.txt
```

### Pip freeze
Creating your requirements file using pip’s freeze option can make your life a little easier. First, write your software and install all the requirements you need as you go. Once you’re done and everything seems to work fine, use the following command:

```
pip freeze > requirements.txt
```

### Pip Install from a requirements.txt file

```
pip install -r requirements.txt
```

## Issues

### Resolve dependencies
Select interpreter from your env