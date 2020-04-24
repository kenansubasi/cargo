#!/bin/sh

/code/docker/wait-for-it.sh db:27017 -- python -c 'from cargo.utils import load_data; load_data()'
exec "$@"
