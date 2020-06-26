#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Creation date: June 26, 2020
Authors: Robinson Montes
        Carlos Murcia
"""
import uuid
import datetime


class BaseModel():
    """
    base_model that defines all common attributes/methods for other classes
    """
    def __init__(self, *args, **kwargs):
        """init method for BaseModel Class

        Attributes:
            args (list): inputted arguments as a list.
            kwargs (dict): inputted arguments as a dict.
            id (str) - assign with an uuid when an instance is created.
            created_at (time): datetime - assign with the current datetime when
                an instance is created.
            updated_at (time): datetime - assign with the current datetime when
                n instance is created and it will be updated every time you
                change your object.
        """
        if len(kwargs) > 0:
            for k, v in kwargs.items():
                if k in ['created_at', 'updated_at']:
                    self.__dict__[k] = datetime.datetime\
                        .strptime(v, '%Y-%m-%dT%H:%M:%S.%f')
            else:
                    self.__dict__[k] = v
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()

    def __str__(self):
        """str method for BaseModel Class

            Return:
                string (str): string descriptor for BaseModel Class
        """
        string = "[" + str(self.__class__.__name__) + "] ("
        string += str(self.id) + ") " + str(self.__dict__)
        return string

    def save(self):
        """
        updates the public instance attribute updated_at with the
        current datetime
        """
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """returns a dictionary containing all keys/values of __dict__
        of the instance

        Return:
            dictionary (dict): Dictionary object that contains __dict__
        """
        dictionary = self.__dict__.copy()
        dictionary["created_at"] = self.created_at.isoformat()
        dictionary["updated_at"] = self.updated_at.isoformat()
        dictionary["__class__"] = self.__class__.__name__
        return dictionary
