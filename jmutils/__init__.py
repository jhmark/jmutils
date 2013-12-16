# jmutils/__init__.py
# Copyright (c) 2013 by Jonathan Mark
# This file is distributed under the MIT License. See LICENSE.txt for details.
""" jmutils

This module provides some useful Python functions and classes:

Struct - allows 1-line definition of lightweight objects
"""

def Struct(name, field_names):  # pylint: disable=C0103

    """ Define a lightweight class having the specified name and field names.
    """
    num_fields = len(field_names)

    def obj_init(self, *positional_args, **keyword_args):
        """ __init__ function for the new class """
        # Set fields from positional args, filling in None for missing fields.
        iarg = -1
        for iarg, val in enumerate(positional_args):
            setattr(self, field_names[iarg], val)
        while iarg < num_fields - 1:
            iarg += 1
            setattr(self, field_names[iarg], None)

        # Set fields from keyword args.
        for arg_name, val in keyword_args.items():
            setattr(self, arg_name, val)

    def obj_repr(self):
        """ __repr__ function for the new class """
        return '%s(%s)' % (name, ', '.join(
                ('%s=%r' % (field_name, getattr(self, field_name))
                 for field_name in field_names)))

    return type(name, (object,), {'__slots__': field_names,
                                  '__init__': obj_init,
                                  '__repr__': obj_repr})
