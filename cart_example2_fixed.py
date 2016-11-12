#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Inventory Code

from collections import namedtuple
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
        price=st.floats(min_value=0.00, max_value=1000.00),
        )

COUPONS = []
Coupon = namedtuple("Coupon", ["name", "percent"])
for n in range(10, 100, 10):
    c = Coupon("%sOFF" % n, (100 - n) / 100.00)
    COUPONS.append(c)


# Shopping Cart Code

class ShoppingCart(object):
    def __init__(self):
        self.cart = {}
        self.discounts = {}

    @property
    def total(self):
        subtotal = 0.00
        for item, num in self.cart.items():
            subtotal += item.price * num
        for discount in self.discounts.values():
            subtotal *= discount
        return subtotal

    def add(self, item):
        if item in self.cart:
            self.cart[item] += 1
        else:
            self.cart[item] = 1

    def remove(self, item):
        if item in self.cart:
            self.cart[item] -= 1
            if self.cart[item] == 0:
                del self.cart[item]

    def add_discount(self, coupon):
        if self.total >= 0 and coupon not in self.discounts:
            self.discounts[coupon] = coupon.percent

    def remove_discount(self, coupon):
        if coupon in self.discounts:
            del self.discounts[coupon]


# Test(s)

from hypothesis.stateful import rule, RuleBasedStateMachine, Bundle
import hypothesis.strategies as st

class CartMachine(RuleBasedStateMachine):
    Carts = Bundle("carts")
    BOOKS = st.lists(books, min_size=10).example()

    @rule(target=Carts)
    def new_cart(self):
        return ShoppingCart()

    @rule(cart=Carts, item=st.sampled_from(BOOKS))
    def add_item(self, cart, item):
        cart.add(item)
        assert cart.total >= 0.00

    @rule(cart=Carts, item=st.sampled_from(BOOKS))
    def remove_item(self, cart, item):
        cart.remove(item)
        assert cart.total >= 0.00

    @rule(cart=Carts, coupon=st.sampled_from(COUPONS))
    def add_coupon(self, cart, coupon):
        cart.add_discount(coupon)
        assert cart.total >= 0.00

    @rule(cart=Carts, coupon=st.sampled_from(COUPONS))
    def remove_discount(self, cart, coupon):
        cart.remove_discount(coupon)
        assert cart.total >= 0.00

TestCarts = CartMachine.TestCase

