import os
from dotenv import load_dotenv
from peewee import PostgresqlDatabase, Model, IntegerField, FloatField, TextField, DateTimeField, BooleanField, \
    AutoField
from peewee_migrate import Router
from playhouse.postgres_ext import ArrayField
from playhouse.postgres_ext import JSONField

load_dotenv()
PG_USER = os.getenv("pg_user")
PG_PASSWORD = os.getenv("pg_password")

# Initialize the database
db = PostgresqlDatabase('mydatabase', user=PG_USER, password=PG_PASSWORD, host='localhost')


class BaseModel(Model):
    class Meta:
        database = db


class ImageLabel(BaseModel):
    id = AutoField(primary_key=True)

    # Section 2 changes
    invalidated_by_user_id = IntegerField()  # Ideally, a reference to a USER table

    class Meta:
        table_name = 'IMAGE_LABELS'


if __name__ == '__main__':
    db.connect()
    db.create_tables([ImageLabel])

    router = Router(db, migrate_dir='migrations')

    # To create the base state
    # router.create('base', auto='model')

    # To implement requirements in section2
    # router.create('section2', auto='model')

    # Run all unapplied migrations
    router.run()

    db.close()
