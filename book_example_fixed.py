#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Book Code

class Book(object):
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        if not price >= 0.00:
            price = 0.00
        self.price = price

    def __unicode__(self):
        return u"%s by %s ($%s)" % (self.title, self.author, self.price)

    def __repr__(self):
        return self.__unicode__().encode("utf-8")


# Property-based Test

from hypothesis import given
import hypothesis.strategies as st

books = st.builds(
        Book,
        title=st.text(),
        author=st.text(),
        price=st.floats(),
        )

@given(books)
def test_unicode(book):
    print(book)

@given(books)
def test_never_negative(book):
    assert book.price >= 0.00
