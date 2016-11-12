#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Inventory Code

import hypothesis.strategies as st

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

books = st.builds(
        Book,
        title=st.text(),
        author=st.text(),
        price=st.floats(allow_infinity=False),
        )


# Shopping Cart Code

class ShoppingCart(object):
    def __init__(self):
        self.cart = {}
        self.total = 0.00

    def add(self, item):
        if item in self.cart:
            self.cart[item] += 1
        else:
            self.cart[item] = 1
        self.total += item.price

    def remove(self, item):
        if item in self.cart:
            self.cart[item] -= 1
            if self.cart[item] == 0:
                del self.cart[item]
            self.total -= item.price


# Property-based Test(s)

from hypothesis import given
import hypothesis.strategies as st

@given(st.lists(books))
def test_add(list_of_books):
    cart = ShoppingCart()
    for book in list_of_books:
        cart.add(book)
    assert cart.total == sum(book.price for book in list_of_books)

@given(st.lists(books))
def test_remove(list_of_books):
    cart = ShoppingCart()
    for book in list_of_books:
        cart.remove(book)
    assert cart.total == 0.00

@given(st.lists(books))
def test_add_remove(list_of_books):
    cart = ShoppingCart()
    for book in list_of_books:
        cart.add(book)
        cart.remove(book)
    assert cart.total == 0.00
