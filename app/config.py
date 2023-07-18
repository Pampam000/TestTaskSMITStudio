import os

from dotenv import load_dotenv

load_dotenv()

# Database
POSTGRES_USER = os.getenv('POSTGRES_USER')
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD')
POSTGRES_DB = os.getenv('POSTGRES_DB')
POSTRGES_HOST = os.getenv('POSTRGES_HOST')
POSTGRES_PORT = os.getenv('POSTGRES_PORT')

DATABASE_URL = f'postgres://{POSTGRES_USER}:{POSTGRES_PASSWORD}@' \
               f'{POSTRGES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}'

TORTOISE_ORM = {
    "connections": {"default": DATABASE_URL},
    "apps": {
        "models": {
            "models": ["app.insurance_cost.models", "aerich.models"],
            "default_connection": "default",
        },
    },
}
