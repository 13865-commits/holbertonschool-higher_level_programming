#!/usr/bin/env python3
"""
This module defines the CountedIterator class that wraps an iterable
and keeps track of the iteration count.
"""


class CountedIterator:
    """A custom iterator that counts how many items have been fetched."""

    def __init__(self, some_iterable):
        """Initialize the iterator and the count."""
        self.iterator = iter(some_iterable)
        self.counter = 0

    def get_count(self):
        """Return the current count of iterated items."""
        return self.counter

    def __next__(self):
        """
        Return the next item from the iterator and increment the counter.
        Raises StopIteration when no more items are left.
        """
        # Növbəti elementi çəkirik. Əgər bitibsə, avtomatik StopIteration verəcək.
        item = next(self.iterator)
        
        # Əgər yuxarıdakı sətir xəta vermədisə, deməli element var. Sayğacı artırırıq.
        self.counter += 1
        return item
