import os

from pkg_resources import resource_filename, resource_string


def path(name: str, resource_dir: str = "images/") -> str:
    """
    Return the filename for the referenced image.

    Qt uses unix path conventions.
    """
    return resource_filename(__name__, resource_dir + name)


def load_css(name: str) -> str:
    """
    Return the contents of the referenced CSS file in the resources.
    """
    return resource_string(__name__, name).decode("utf-8")
