# pytest-packagetree
Pytest plugin for package-tree

### Hooks

The following pytest hooks are available:

- pytest_packagetree_modules - Must return a list of directory names. Each directory is turned into a PackageTree and placed inside a pytest fixture of the same name.
By default, the `pages` directory is used.
