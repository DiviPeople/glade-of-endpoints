"""Module allowing configuration of the service via the environment variables. """

import os

HOST = os.getenv('HOST', 'localhost')

LOG_PATH = os.getenv('LOG_PATH', 'glade-of-endpoints.log')

PORT = os.getenv('PORT', '8000')

DB_HOST = os.getenv('DB_HOST', 'localhost')

DB_USER = os.getenv('DB_USER', 'root')

DB_PASSWORD = os.getenv('DB_PASSWORD', '')

DB_CHARSET = os.getenv('DB_CHARSET', 'utf8mb4')

DB_NAME = os.getenv('DB_NAME', 'webapi')
