import sys
import collections.abc
if not hasattr(collections, "Iterator"):
    collections.Iterator = collections.abc.Iterator
