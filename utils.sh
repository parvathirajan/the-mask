#!/bin/sh
echo $0 $1
if [ $1 = "report" ]
then
    pipenv run pytest --cov=. --cov-report=html tests
elif [ $1 = "format" ]
then
    pipenv run black .
elif [ $1 = "test" ]
then
    pipenv run pytest -vvv tests/
elif [ $1 = "build" ]
then
    rm -frv ./dist/*
    echo "Previous Dist removed"
    python3 -m build
    echo "New Dist Created"
    python3 -m twine upload --repository testpypi dist/*
fi
