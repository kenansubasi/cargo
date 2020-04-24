#!/bin/sh

/code/docker/wait-for-it.sh db:27017
exec "$@"
