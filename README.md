[![Build Status](https://travis-ci.org/ESSS/xml_factory.svg?branch=master)](https://travis-ci.org/ESSS/xml_factory) [![Coverage Status](https://coveralls.io/repos/ESSS/xml_factory/badge.svg?branch=master)](https://coveralls.io/r/ESSS/xml_factory?branch=master)

XML Factory
===========

About
-----
XMl Factory is a simple XMl writer that uses dict syntax to write files.


Example
------------
```python
# Create a root tag
factory = XmlFactory('root')
'''
<root>
</root>
'''

# Add elements using dict syntax
factory['elements/alpha'] = 'Alpha'
'''
<root>
  <elements>
    <alpha>Alpha</alpha>
  </elements>
</root>
'''

# Set tag fields using @
factory['elements@coding'] = 'utf8'
'''
<root>
  <elements coding="utf8">
    <alpha>Alpha</alpha>
  </elements>
</root>
'''

# Values can be overridden by using the same path twice
factory['elements/alpha'] = 'Overridden Alpha'
'''
<root>
  <elements coding="utf8">
    <alpha>Overridden Alpha</alpha>
  </elements>
</root>
'''

# New values can be added to a same path by ending a string with '+'
factory['elements/alpha+'] = 'New Alpha'
'''
<root>
  <elements coding="utf8">
    <alpha>Overridden Alpha</alpha>
    <alpha>New Alpha</alpha>
  </elements>
</root>
'''
```

Contributing
------------

This library follows Jeff Knupp's guide on Python open source projects:
http://www.jeffknupp.com/blog/2013/08/16/open-sourcing-a-python-project-the-right-way/
