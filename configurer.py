from __future__ import absolute_import, division, print_function, unicode_literals

try:
    from configparser import ConfigParser, NoOptionError
except ImportError:
    from ConfigParser import ConfigParser, NoOptionError
class Configurer(object):
    def load(self, cfgfile, section, ints, strings, booleans=[]):
        c = ConfigParser()
        c.read(cfgfile)
        toparse = [] + ints + strings + booleans
        for o in toparse:
            try:
                if o in ints:
                    val = c.getint(section, o)
                elif o in strings:
                    val = c.get(section, o)
                elif o in booleans:
                    val = c.getboolean(section, o)
                setattr(self, o, val)
            except NoOptionError:
                if not hasattr(self, o):
                    raise ValueError("Missing option in the configuration file: %s" % o)
        unknown_items = {}
        for item, val in c.items(section):
            if item in toparse:
                continue
            else:
                unknown_items[item] = val
        return unknown_items

    def save(self, cfgfile, section, ints, strings, booleans):
        c = ConfigParser()
        c.add_section(section)
        options = [] + ints + strings + booleans
        for o in options:
            val = getattr(self, o)
            c.set(section, o, str(val))
        f = open(cfgfile, "wt")
        return c.write(f)
