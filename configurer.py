from __future__ import absolute_import, division, print_function, unicode_literals

try:
    from configparser import ConfigParser
except ImportError:
    from ConfigParser import ConfigParser
class Configurer(object):
    _BOOLEAN_STATES = {'yes': True, 'true': True, 'on': True,
        'no': False, 'false': False, 'off': False}

    def _detect_type_and_convert(self, value):
        v = value.lower()
        if value.isdigit():
            return int(value)
        elif v in ("true", "false", "yes", "no", "on", "off"):
            return self._BOOLEAN_STATES[v]
        else:
            return value

    def load(self, cfgfile, section=None):
        if not section:
            section = type(self).__name__ # Make the name of the class be the section name
        c = ConfigParser()
        c.read(cfgfile)
        items = {}
        for item, val in c.items(section):
            d = self._detect_type_and_convert(val)
            setattr(self, item, d)
            items[item] = d
        return items

    def save(self, cfgfile, options, section=None):
        if not section:
            section = type(self).__name__ # Make the name of the class be the section name
        c = ConfigParser()
        c.add_section(section)
        for o in options:
            val = getattr(self, o)
            c.set(section, o, str(val))
        f = open(cfgfile, "wt")
        return c.write(f)
