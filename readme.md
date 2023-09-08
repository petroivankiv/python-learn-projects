## venv

### Install

```python -m venv venv```

### venv activation

```
# In git bash
./venv/Scripts/activate.bat
# In cmd.exe
venv\Scripts\activate.bat
# In PowerShell
venv\Scripts\Activate.ps1
```

### Deactivate the Python venv
If you want to delete this virtualenv, deactivate it first and then remove the directory with all its content

```
deactivate
# If your virtual environment is in a directory called 'venv':
rm -r venv
```

### Install Python packages in a venv

```pip install simplejson```

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

### Pip uninstall

```
pip uninstall simplejson
pip uninstall -r requirements.txt
```

### Other Pip command

```
pip list
pip show
```

## Issues

### Resolve dependencies
Select interpreter from your env