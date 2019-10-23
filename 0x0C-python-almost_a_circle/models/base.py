#!/usr/bin/python3
import json
"""begin program - python3"""


class Base:
    """begin program - python3"""

    __nb_objects = 0

    def __init__(self, id=None):
    	"""begin program - python3"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
    	"""begin program - python3"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        if not isinstance(list_dictionaries, list):
            raise TypeError("list_dictionaries must be a list")
        if isinstance(list_dictionaries, list):
            for i in range(len(list_dictionaries)):
                if not isinstance(list_dictionaries[i], dict):
                    m = "list_dictionaries must contain dictionaries"
                    raise TypeError(m)
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
    	"""begin program - python3"""
        if not isinstance(list_objs, list):
            raise TypeError("list_objs must be list")
        if list_objs is None or list_objs == []:
            emptyList = []
        else:
            output = [c.to_dictionary() for c in list_objs]
            file = cls.__name__ + ".json"
            with open(file, mode='w', encoding='utf-8') as myFile:
                myFile.write(cls.to_json_string(output))

    @staticmethod
    def from_json_string(json_string):
    	"""begin program - python3"""
        if not isinstance(json_string, str):
            raise TypeError("json_string must be a string")
        if json_string is None or json_string == "":
            output = []
            return output
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
    	"""begin program - python3"""
        if cls.__name__ == "Rectangle":
            a = cls(2, 4, 6, 8, 10)
            a.update(**dictionary)
            return a
        if cls.__name__ == "Square":
            a = cls(2, 2, 6, 8, 10)
            a.update(**dictionary)
            return a

    @classmethod
    def load_from_file(cls):
        """Return a list of instances."""
        filename = str(cls).split(".")[-1][:-2] + ".json"
        if not os.path.exists(filename):
            return []
        res = []
        with open(filename, "r") as f:
            dicts = cls.from_json_string(f.readline())
        for d in dicts:
            res.append(cls.create(**d))
        return res
