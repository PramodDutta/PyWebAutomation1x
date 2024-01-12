Feature: Google Search

  Scenario: Search for TheTestingAcademy on Google
    Given I am on the Google page
    When I search for "TheTestingAcademy"
    Then I should see "TheTestingAcademy" in the results
