"""
What happens if you try to use a list as a dictionary key? Why?
"""
Lists cannot be dictionary keys because they are mutable and therefore unhashable. Dictionary keys must be immutable and hashable.
