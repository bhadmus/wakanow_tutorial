from behave import *
from pages.page_objects import GuestShopper
from file import ref

use_step_matcher("parse")
driver = GuestShopper()

@given(u'I am on "{text}" website')
def step_impl(context, text):
    if text == "amazon":
        driver.setup(ref.amazon_url)
    elif text == "konga":
        driver.setup(ref.konga_url)


@step(u'I search and click an item on "{text}"')
def step_impl(context, text):
    if text == "amazon":
        driver.search_and_click(ref.amazon_search_box, ref.amazon_search_item, ref.amazon_search_button)
    elif text == "konga":
        driver.search_and_click(ref.konga_search_box, ref.konga_search_item, ref.konga_search_button)


@step(u'I selected the "{text}" item')
def step_impl(context, text):
    if text == "amazon":
        driver.scroll_page()
        driver.select_item(ref.amazon_item)
    elif text == "konga":
        driver.select_item(ref.konga_item)


@step(u'I added the "{text}" item to cart')
def step_impl(context, text):
    if text == "amazon":
        driver.buy_option()
        driver.add_to_cart(ref.amazon_add_button)
    elif text == "konga":
        driver.add_to_cart(ref.konga_add_button)


@when(u'I proceed to checkout on "{text}"')
def step_impl(context, text):
    if text == "amazon":
        driver.proceed_to_checkout(ref.amazon_checkout_button)
    elif text == "konga":
        driver.proceed_to_checkout(ref.konga_checkout_button)


@then(u'I should be redirected to "{text}" Sign-in Page')
def step_impl(context, text):
    if text == "amazon":
        driver.verify_page(ref.amazon_phrase)
    elif text == "konga":
        driver.verify_page(ref.konga_phrase)