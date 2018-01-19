"""My shelve.

This module is used to save the workspace (all variables).
And you can load these variables whenever you need them.

"""
import shelve
import types


def save_workspace(filename, names_of_spaces_to_save, dict_of_values_to_save):
    """Save the workspace.

    Args:
        filename (str): location to save workspace.
        names_of_spaces_to_save: use dir() from parent to save all variables in previous scope.
            - dir() = return the list of names in the current local scope
        dict_of_values_to_save: use globals() or locals() to save all variables.
            - globals() = Return a dictionary representing the current global symbol table.
            This is always the dictionary of the current module (inside a function or method,
            this is the module where it is defined, not the module from which it is called).
            - locals() = Update and return a dictionary representing the current local symbol table.
            Free variables are returned by locals() when it is called in function blocks, but not in class blocks.

    Returns:
        None

    Examples:
        An example to show how to save the workspace.

        >>> from io_helper import my_shelve
        >>> filename = 'shelve_file'
        >>> var1 = 'Is life always this hard, or just when you’re a kid?'
        >>> var2 = [i for i in range(10)]
        >>> my_shelve.save_workspace(filename, dir(), globals())

    """
    shelf_fp = shelve.open(filename, 'n')

    for key in names_of_spaces_to_save:
        try:
            if key[0:2] == '__':
                continue
            value = dict_of_values_to_save[key]
            if isinstance(value, types.FunctionType) or isinstance(value, types.ModuleType) or isinstance(value, type):
                continue
            else:
                shelf_fp[key] = value
        except TypeError:
            print('TypeError shelving: {0}'.format(key))
        except:
            print('Generic error shelving: {0}'.format(key))
    shelf_fp.close()


def load_workspace(filename, parent_globals):
    """Load the workspace.

    Args:
        filename (str): location to load workspace.
        parent_globals: use globals() to load the workspace saved in filename to current scope.

    Returns:
        None

    Examples:
        An example to show how to load the workspace.
        First, you need to save the workspace, and then you could load the workspace whenever you need it.

        >>> from io_helper import my_shelve
        >>> my_shelve.load_workspace(filename, globals())
        >>> print(var1)
        >>> print(var2)

    """
    shelf_fp = shelve.open(filename)
    for key in shelf_fp:
        parent_globals[key] = shelf_fp[key]
    shelf_fp.close()
