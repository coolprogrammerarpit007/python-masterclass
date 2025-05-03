"""
LEGB
LOCAL,ENCLOSING,GLOBAL,BUILT-IN
python first checks variale in the local,then Enclosing,then global then into built-in scope.
"""


def outer():
    x = 'outer x'

    def inner():
        """
        nonlocal keyword is used to change the enclosed scope variables.
        :return:
        """
        nonlocal x
        x = 'inner x'
        print(x)
    inner()
    print(x)

outer()