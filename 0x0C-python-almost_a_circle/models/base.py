#!/usr/bin/python3
"""Module for base class of all other classes for this project."""
import json
import csv
import turtle


class Base:
    """
        This class will manage the id attribute for all the classes.
        Arguments:
            @id: The id for a specific instance.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Converting a dict into a json string."""
        if list_dictionaries is None:
            return '[]'
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """Returns a dict from a string."""
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the string representation of an object of a class to file."""
        file_name = cls.__name__ + ".json"

        content = []
        if list_objs is not None:
            for item in list_objs:
                item = item.to_dictionary()
                json_dict = json.loads(cls.to_json_string(item))
                content.append(json_dict)

        with open(file_name, mode="w") as fd:
            json.dump(content, fd)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all the attributes already set."""
        from models.rectangle import Rectangle
        from models.square import Square

        if cls.__name__ == "Rectangle":
            r2 = Rectangle(3, 8)
        elif cls.__name__ == "Square":
            r2 = Square(5)
        r2.update(**dictionary)
        return (r2)

    @classmethod
    def load_from_file(cls):
        """load dict for  the params  of instance and creating instances"""
        file_name = cls.__name__ + ".json"

        try:
            with open(file_name, encoding="UTF8") as fd:
                content = cls.from_json_string(fd.read())
        except IOError:
            return []

        instances = []

        for instance in content:
            tmp = cls.create(**instance)
            instances.append(tmp)

        return instances

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Open a window to draw all squares and rectangles"""
        turt = turtle.Turtle()
        turt.screen.bgcolor("#b7312c")
        turt.pensize(3)
        turt.shape("turtle")

        turt.color("#ffffff")
        for rect in list_rectangles:
            turt.showturtle()
            turt.up()
            turt.goto(rect.x, rect.y)
            turt.down()
            for i in range(2):
                turt.forward(rect.width)
                turt.left(90)
                turt.forward(rect.height)
                turt.left(90)
            turt.hideturtle()

        turt.color("#b5e3d8")
        for sq in list_squares:
            turt.showturtle()
            turt.up()
            turt.goto(sq.x, sq.y)
            turt.down()
            for i in range(2):
                turt.forward(sq.width)
                turt.left(90)
                turt.forward(sq.height)
                turt.left(90)
            turt.hideturtle()

        turtle.exitonclick()

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """save to csv file."""
        file_name = cls.__name__ + ".csv"

        with open(file_name, mode="w", newline='', encoding="UTF8") as fd:
            write_this = csv.writer(fd, delimiter=" ")

            if cls.__name__ == "Rectangle":
                for item in list_objs:
                    string = ""
                    item = item.to_dictionary()
                    string += (str(item["id"]) + "," +
                               str(item["width"]) + "," +
                               str(item["height"]) + "," +
                               str(item["x"]) + "," + str(item["y"]))
                    write_this.writerow(string)

            if cls.__name__ == "Square":
                for item in list_objs:
                    string = ""
                    item = item.to_dictionary()
                    string += (str(item["id"]) + "," +
                               str(item["size"]) + "," +
                               str(item["x"]) + "," + str(item["y"]))
                    write_this.writerow(string)

    @classmethod
    def load_from_file_csv(cls):
        """loads csv."""
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(csvfile, fieldnames=fieldnames)
                list_dicts = [dict([k, int(v)] for k, v in d.items())
                              for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []
