Feature: Google Search

  Scenario: Search for TheTestingAcademy on Google
    Given I am on the Google page
    When I search for "TheTestingAcademy"
    Then I should see "TheTestingAcademy" in the results


#    Scenario: VWO Negative Test
#    Given I am on the App.vwo.com
#    When I enter email "admin" and "admin" password
#    Then I should see "error" message on page.
