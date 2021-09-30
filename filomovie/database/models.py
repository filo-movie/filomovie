from sqlalchemy import Integer
from sqlalchemy.schema import Table, MetaData, Column

metadata = MetaData()

Table("testTable", metadata,
      Column('integer', Integer)
      )

