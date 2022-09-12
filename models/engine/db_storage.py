#!/usr/bin/python
"""New database engine"""
from sqlalchemy import create_engine
from os import getenv
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
from models.city import City
from models.state import State
from models.user import User
from models.place import Place
from models.amenity import Amenity
from models.review import Review


Base = declarative_base()


class DBStorage():
    """new engine"""
    __engine = "None"
    __session = "None"

    def __init__(self):
        """Instantiation of DBStorage class
        """
        MySQL_user = getenv('HBNB_MYSQL_USER')
        MySQL_pwd = getenv('HBNB_MYSQL_PWD')
        MySQL_host = getenv('HBNB_MYSQL_HOST')
        MySQL_db = getenv('HBNB_MYSQL_DB')
        MySQL_env = getenv('HBNB_ENV')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            MySQL_user, MySQL_pwd, MySQL_host, MySQL_db), pool_pre_ping=True)
        Base.metadata.create_all(self.__engine)
        if MySQL_env == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """return all data objects"""
        if cls:
            data = self.__session.query(cls).all()
        else:
            classes = [User, State, City, Amenity, Place, Review]
            data = []
            for cl in classes:
                data.append(self.__session.query(cl))
        dict = {}
        for object in data:
            key = '{}.{}'.format(type(object).__name__, object.id)
            dict[key] = object
        return dict

    def new(self, obj):
        """Add obj to the current db"""
        if obj:
            self.__session.add(obj)

    def save(self):
        """save changes made to the db"""
        self.__session.commit()

    def delete(self, obj=None):
        """
        delete from the current database session obj if not None
        """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """create all tables in the database"""
        Base.metadata.create_all(self.__engine)
        self.__session = sessionmaker(bind=self.__engine,
                                      expire_on_commit=False)
        Session = scoped_session(self.__session)
        self.__session = Session()
        
    def close(self):
        """close session"""
        self.__session.close()
