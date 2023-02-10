from sqlalchemy import Column, Table
from sqlalchemy.sql.sqltypes import String, Integer
from config.db import meta, engine

users = Table("users", meta,
              Column("id", Integer, primary_key=True),
              Column("name", String(255), nullable=False),
              Column("username", String(255), nullable=False),
              Column("user_password", String(255), nullable=False))

meta.create_all(engine)