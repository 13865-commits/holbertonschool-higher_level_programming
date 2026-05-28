#!/usr/bin/env python3
"""
This module defines a VerboseList class that extends the built-in list.
It prints notifications whenever items are added or removed.
"""


class VerboseList(list):
    """A custom list class that prints notifications on modification."""

    def append(self, item):
        """Add an item to the end of the list and print a notification."""
        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, iterable):
        """Extend the list with an iterable and print a notification."""
        items_added = len(iterable)
        super().extend(iterable)
        print("Extended the list with [{}] items.".format(items_added))

    def remove(self, item):
        """Remove an item from the list and print a notification."""
        # Edge case handling: print only if the item actually exists
        if item in self:
            print("Removed [{}] from the list.".format(item))
        super().remove(item)

    def pop(self, index=-1):
        """Pop an item at the given index and print a notification."""
        # Retrieve the item before popping to handle the notification
        # This also acts as an edge case handler (raises IndexError if invalid)
        item = self[index]
        print("Popped [{}] from the list.".format(item))
        return super().pop(index)
