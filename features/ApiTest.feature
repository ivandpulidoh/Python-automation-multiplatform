Feature: Scenarios for api testing

  @tag_api @TAG_5
  Scenario Outline: Test get character goku
   Given the user set the base url and headers
   When the user send the GET request to <api>
   Then the service should return goku character 
   Examples:
    |     api    |
    |characters/1|

  @tag_api @TAG_6
  Scenario Outline: Test get character vegeta
   Given the user set the base url and headers
   When the user send the GET request to <api>
   Then the service should return vegeta character
   Examples:
    |     api    |
    |characters/2|
