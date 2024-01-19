Feature: Google Search for the TheTestingAcademy
  Scenario: Search for the TTA on Google
    Given I am on the Google Home Page
    When I search for "TheTestingAcademy"
    Then I should see the "TheTestingAcademy" in the results

  Scenario: Search for the TTAH on Google
    Given I am on the Google Home Page
    When I search for "TheTestingAcademy Hindi"
    Then I should see the "TheTestingAcademy Hindi" in the results




