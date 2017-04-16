from __future__ import (absolute_import, division,
                        print_function, unicode_literals)
from builtins import *
import six
from abc import ABCMeta, abstractmethod, abstractproperty


@six.add_metaclass(ABCMeta)
class AbstractWorld:
    @abstractmethod
    def step(self):
        pass

    @abstractproperty
    def state(self):
        pass