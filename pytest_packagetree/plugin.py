import itertools
import sys

import pytest

from packagetree import PackageTree
from pytest_packagetree import hooks


def _build_packagetree(module_name):
    def build():
        return PackageTree(module=module_name)
    return build


def pytest_configure(config):
    modules = config.hook.pytest_packagetree_modules()
    # Hook collection will cause a list of lists to be collected.
    # Flatten them to make life easier.
    flattened_modules = itertools.chain.from_iterable(modules)
    for item in flattened_modules:
        fixture = pytest.fixture(
            scope='session', name=item)(_build_packagetree(item))

        setattr(sys.modules[__name__], f"{item}_func", fixture)


def pytest_addhooks(pluginmanager):
    pluginmanager.add_hookspecs(hooks)


def pytest_packagetree_modules():
    """Default Implementation."""
    return ['pages']
