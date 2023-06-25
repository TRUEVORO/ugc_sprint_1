#!/bin/sh

cd src || exit

gunicorn -c gunicorn/gunicorn.py main:app
