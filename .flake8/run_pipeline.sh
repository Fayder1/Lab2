#!/bin/bash

echo "Running pytest..."
pytest --html=report.html --self-contained-html

echo "Running flake8..."
flake8 app tests --format=html --htmldir=flake8-report
