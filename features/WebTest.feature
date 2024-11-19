Feature: Tests for firefox, chrome, edge drivers

  @tag_web @TAG_2
  Scenario: test selene1
   Given user open browser
   When user search valid solutions
   Then the system should display valid results

  @tag_web @TAG_3
  Scenario: test selene2
   Given user open browser
   When user search valid solutions
   Then the system should display valid results

  @tag_web @TAG_4
  Scenario: test selene3
   Given user open browser
   When user search valid solutions
   Then the system should display valid results

