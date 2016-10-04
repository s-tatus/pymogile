#! coding: utf-8
# pylint: disable-msg=W0311
from __future__ import absolute_import, print_function, unicode_literals


class MogileFSError(Exception):

    def __init__(self, err_str, err=None):
        self.err_str = err_str
        self.err = err

    def __str__(self):
        return self.err_str

    def __repr__(self):
        return '<pymogile.exceptions.MogileFSError: %s>' % self.err_str


class HTTPError(Exception):

    def __init__(self, code, content):
        self.code = code
        self.content = content

    def __repr__(self):
        return '<pymogile.exceptions.HTTPError status:%s>' % self.code

    def __str__(self):
        return 'HTTP Error %d, %s' % (self.code, self.content)
