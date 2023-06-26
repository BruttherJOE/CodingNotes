# Venv (Linux)

### Setup

```
sudo add-apt-repository ppa:jonathonf/python-3.6
sudo apt-get update
sudo apt-get install python3.6
```



### Create venv in the current directory

```
virtualenv --python python3.6 venv_name_here
```



### Activate venv

```
source venv/bin/activate
```

### Deactivate venv

```
deactivate
```



### Create description of libraries

```
pip freeze > requirements.txt
```



### Install all dependencies from `requirements.txt`

```
pip install -r requirements.txt
```





[cr https://mothergeo-py.readthedocs.io/en/latest/development/how-to/venv.html]
