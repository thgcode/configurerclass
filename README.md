## Configurer class

This class is intended to be used as a mixin to your classes.
It reads and writes configuration files based on attributes present in
an INI file and your classes.

#### List of functions in the class


### load(cfgfile, section=None)

> This function, when called, will set all configuration options provided in
the configuration file to your class (see the ```example.py```).

The attributes are converted to their correct types automatically.

> Only integers, strings and booleans are supported for now).

**cfgfile**: file that contains the class' configuration options.

**section**: the section to look up the options on the configuration
file.

> If section is None it will default to the name of the class.

### save(cfgfile, options, section=None)

> This function will get all attributes described in the options list and save them to the configuration file.

**cfgfile**: file that will be written with data within class.

**options**: attributes from origin class (attributes that should be created
in the configuration file).

**section**: the section to set the attributes on the configuration
file.

> If section is None it will default to the name of the class.

If you want to look right away in the code, there is an example and the
module itself.

**Contributions are very appreciated.**

If you want to install the module globally, a setup script is provided.

```
$ python setup.py install
```
