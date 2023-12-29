#!/bin/bash

# Migrate the database
flask db init
flask db migrate
flask db upgrade

# Start the application
exec "$@"
