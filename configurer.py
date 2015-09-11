import ConfigParser
class Configurer(object):
    def load(self, cfgfile, section, ints, strings, booleans=[]):
        c=ConfigParser.ConfigParser()
        c.read(cfgfile)
        toparse = [] + ints + strings + booleans
        for o in toparse:
            try:
                if o in ints:
                    val=c.getint(section, o)
                elif o in strings:
                    val=c.get(section, o)
                elif o in booleans:
                    val=c.getboolean(section, o)
                setattr(self, o, val)
            except ConfigParser.NoOptionError:
                if not hasattr(self, o):
                    raise ValueError
        unknown_items = {}
        for item, val in c.items(section):
            if item in toparse:
                continue
            else:
                unknown_items[item] = val
        return unknown_items
