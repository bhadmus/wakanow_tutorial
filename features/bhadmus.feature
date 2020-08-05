Feature: Guest Shopping

    As a shopper,
    I should be able to shop on any site,
    So that I can checkout my item.

    Scenario: Guest Shopping on Amazon

    Given I am on "amazon" website

    And I search and click an item on "amazon"

    And I selected the "amazon" item

    And I added the "amazon" item to cart

    When I proceed to checkout on "amazon"

    Then I should be redirected to "amazon" Sign-in Page