Feature: Test for mobile platform

  @tag_mobile @TAG_1
  Scenario: test mobile selene
    Given user open app wikipedia
    When user search appium
    Then the system should display appium results