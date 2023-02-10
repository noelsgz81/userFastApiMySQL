from sqlalchemy import MetaData, create_engine

engine = create_engine("mysql+pymysql://root:123456@localhost:3306/storedb")

meta = MetaData()