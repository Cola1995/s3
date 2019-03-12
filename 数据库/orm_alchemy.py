

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint, Index
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import create_engine

#engine = create_engine("mysql+pymysql://root:123456@127.0.0.1:3306/db4", max_overflow=5)

Base = declarative_base()


class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True,autoincrement=True)
    name = Column(String(32),nullable=True)
    email = Column(String(16),nullable=True)
    user_tid=Column(Integer, ForeignKey("userstype.id"))

    user_type = relationship("Userstype", backref='xxoo')
    # __table_args__ = (
    #     UniqueConstraint('id', 'name', name='uix_id_name'),
    #     Index('ix_id_name', 'name', 'extra'),
    # )

class Userstype(Base):
    __tablename__ = 'userstype'
    id = Column(Integer, primary_key=True,autoincrement=True)
    caption = Column(String(32),nullable=True)

def create_db():
    engine = create_engine("mysql+pymysql://root:@127.0.0.1:3306/s4day62db?charset=utf8", max_overflow=5)
    Base.metadata.create_all(engine)

def insert():
    '''
    insert 插入类

    :return:
    '''
    engine = create_engine("mysql+pymysql://root:123456@127.0.0.1:3306/db4", max_overflow=5)

    Session=sessionmaker(bind=engine)
    session=Session()
    objs=[
        Userstype(caption="市场部"),
        Userstype(caption="财务部"),
        Userstype(caption="运营部"),


    ]
    # obj1=Userstype(caption="市场部")
    session.add_all(objs)  #多条数据提交
    #session.add(obj1)  单条数据提交
    session.commit()
    session.close()

def select():
    '''
    查询类
    :return:
    '''


    engine = create_engine("mysql+pymysql://root:123456@127.0.0.1:3306/db4", max_overflow=5)

    Session = sessionmaker(bind=engine)
    session = Session()

    # user_type=session.query(Userstype).all()
    # for row in user_type:
    #     print(row.id,row.caption)

    user_type=session.query(Userstype).filter(Userstype.id>2)
    for row in user_type:
        print(row.id,row.caption)

def delete():
    '''
    删除/修改
    :return:
    '''
    engine = create_engine("mysql+pymysql://root:123456@127.0.0.1:3306/db4", max_overflow=5)

    Session = sessionmaker(bind=engine)
    session = Session()

    #session.query(Userstype).filter(Userstype.id > 1).delete()
    session.query(Userstype).filter(Userstype.id > 0).update({"caption":"财务部"})
    session.commit()
    session.close()

def select_all():
    engine = create_engine("mysql+pymysql://root:123456@127.0.0.1:3306/db4", max_overflow=5)

    Session = sessionmaker(bind=engine)
    session = Session()
    list=session.query(Users,Userstype).join(Userstype,isouter=True).all()
    for row in list:
        print(row[0].name,row[0].email,row[1].caption)

def s1():
    engine = create_engine("mysql+pymysql://root:123456@127.0.0.1:3306/db4", max_overflow=5)

    Session = sessionmaker(bind=engine)
    session = Session()

    type_list = session.query(Userstype)
    for row in type_list:
        print(row.id,row.caption,session.query(Users).filter(Users.user_tid == row.id).all())

    # type_list = session.query(Userstype)
    # for row in type_list:
    #     print(row.id,row.caption,row.xxoo)
s1()