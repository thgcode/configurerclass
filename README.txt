Configurer class

This class is intended to be a mixin to your classes.
It has, at the moment, only one function.

load(file, section, ints, strings, booleans)
This function, when called, will set all configuration options written
in the file to your class (see the included example).
Ints, strings and booleans are lists of strings, each element containing option
names. These lists will convert the variables to the proper types when
setting the class attributes.

I'll later write a save function so you'll be hable to save a
dictionary in the configuration file.
