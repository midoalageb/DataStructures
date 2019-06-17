from pympler import muppy
from LinkedList import Node


def mem_analysis():
    all_objects = muppy.get_objects()
    my_types = muppy.filter(all_objects, Type=Node)
    print(len(my_types))
