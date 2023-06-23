#!/usr/bin/env python3
# vim: sw=4 ts=4 et si:

import sys

class ValidationError(Exception):
    pass

class PatchException(Exception):
    def __init__(self, errors):
        Exception.__init__(self, "Validation Error")
        self._errors = errors

    def errors(self, error=None):
        if error is None:
            return len(self._errors)
        return sum(1 for err in self._errors if isinstance(err, error))

    def __str__(self):
        return "\n".join(f"** {str(x)}" for x in self._errors)

    def __repr__(self):
        ret = "%d errors:\n" % len(self._errors)
        ret += "\n".join(self._errors)
        return ret

    def error_message(self, fn):
        ret = "ERROR: Problems encountered in "
        ret += "`%s'\n" % fn if fn else "input\n"
        ret += str(self)

        return ret

class PatchChecker:
    def __init__(self):
        pass

    def do_patch(self):
        pass
