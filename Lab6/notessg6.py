# We use modules to split up large programming tasks into smaller ones
# We use docstrings (denoted by """) to tell others what our modules are all about
# Top Down Design: We design our functions in a tree, with main at the top
# Followed by various modules which call other modules down the tree.
# Main modules are not meant to be imports

# Namespaces are used to avoid nameclashes, when two things have the same name
# When we use import [name] the namespace becomes avalable, but it needs to be qualified
# When we use from [name] import *, there's a chance for name clashes

# When changing a module while running code, you must reload(functionname) (pg261)

