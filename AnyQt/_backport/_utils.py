import warnings


def obsolete_rename(oldname, newfunc):
    """
    Simple obsolete/removed method decorator

    Parameters
    ----------
    oldname : str
        The name of the old obsolete name
    newfunc : FunctionType
        Replacement unbound member function.
    """
    newname = newfunc.__name__
    def __obsolete(*args, **kwargs):
        warnings.warn(
            "{oldname} is obsolete and is removed in PyQt5. "
            "Use {newname} instead.".format(oldname=oldname, newname=newname),
            DeprecationWarning,
            stacklevel=2
        )
        return newfunc(*args, **kwargs)
    __obsolete.__name__ = oldname
    return __obsolete

