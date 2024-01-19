Feature: Showing off behave with Scenario Outline

  Scenario Outline: Run a DDT on app.vwo.com
    Given open the app.vwo.com
    When I enter the <username> and <password>
    Then I get this <message>
    Examples:
      | username | password | message |
      | admin    | admin    | error   |
      | admin    | admin123 | error   |
      | admin    | password | error   |
