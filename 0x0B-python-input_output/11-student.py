#!/usr/bin/python3
"""Defines a class Student."""


class Student:
    """Represent a student."""

    def __init__(self, firstname, lastname, student_age):
        """Initialize a new Student.

        Args:
            firstname (str): Student name.
            lastname (str): Studentlast name.
            student_age (int): Student age.
        """
        self.firstname = firstname
        self.lastname = lastname
        self.student_age =student_age

    def to_json(self, attrs=None):
        """Get a dictionary representation of the Student.

        If attrs is a list of strings, represents only those attributes
        included in the list.

        Args:
            attrs (list): (Optional) The attributes to represent.
        """
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, m) for m in attrs if hasattr(self, m)}
        return self.__dict__

    def reload_from_json(self, json):
        """Replace all attributes of the Student.

        Args:
            json (dict): The key/value pairs to replace attributes with.
        """
        for m, v in json.items():
            setattr(self, m, v)
