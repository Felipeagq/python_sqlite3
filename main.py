from ast import Pass
from typing import Optional, Type
from abc import ABC,abstractmethod

import sqlite3
import os

from typing import TypeVar

T = TypeVar("T")


class User:
    __name: str
    __email: str
    __age: int
    
    def __init__(
        self,
        host: str,
        email: str  = None,
        age: int  = None
    ):
        self.__name = host
        self.__email = email
        self.__age = age
    
    def getName(self)->str:
        return self.__name
    
    def getEmail(self)->str:
        return self.__email
    
    def getAge(self)->str:
        return self.__age


class UserRepository(ABC):
    @abstractmethod
    def open(self)->None:
        pass
    @abstractmethod
    def store(self, user:User)->None:
        pass
    @abstractmethod
    def close(self)-> None:
        pass


class SqliteDatabase(UserRepository):
    __host: Optional[str]
    __username: Optional[str]
    __password: Optional[str]
    
    def __init__(
        self,
        host: str,
        username: Optional[str] = None,
        password: Optional[str] = None
    ):
        self.__host = host
        self.__username = username
        self.__password = password
    def open(self)-> None:
        conn = sqlite3.connect(self.__host)
        cursor = conn.cursor()
        self.conn = conn
        self.cursor = cursor
    def store(self, user: User) -> None:
        insertar = f"""insert into users (name,email,age) values ('{user.getName()}','{user.getEmail()}',{user.getAge()});"""
        print(insertar)
        self.cursor.execute(insertar)
        self.conn.commit()
    def close(self)->None:
        self.conn.close()


class MongoDB(UserRepository):
    def open(self) -> str:
        print("conectado")
    
    def store(self, user: User) -> str:
        print("guardado")
    
    def close(self) -> str:
        print("cerrado")

class StorageManager:
    @staticmethod
    def storageUser(
        user:T,
        userRepository: T
    )-> None:
        userRepository.open()
        userRepository.store(user)
        userRepository.close()

if __name__ == "__main__":
    ruta = os.path.dirname(os.path.abspath(__file__))
    db = os.path.join(ruta,"db_sqlite3.db")
    
    usuario = User("Sharon","Sharon@correo",21)
    
    sqliteDB = SqliteDatabase(db)
    StorageManager.storageUser(usuario,sqliteDB)
    
    mongodb = MongoDB()
    StorageManager.storageUser(usuario,mongodb)