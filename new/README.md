

# Gary Notes
`export PIPENV_VENV_IN_PROJECT=1`
`pipenv install`
or
`pipenv install --python 3.10.10`

# check .venv folder is not exist ?
`source .venv/bin/activate`
best command is
`pipenv shell`

## export packages depends
pipenv graph
pipenv graph --reverse

## install package
`pipenv install -d fastapi `
`pipenv install fastapi==0.109.0`

pipenv install "fastapi[all]"ex
pipenv install "uvicorn[standard]"

uvicorn main:app --reload

# create other folder use python 3.10
export PIPENV_IGNORE_VIRTUALENVS=1
pipenv install --python 3.10
