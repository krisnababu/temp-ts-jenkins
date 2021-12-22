Feature: Transtats Login

  Scenario Outline: Transtats login test with valid and invalid creds
    Given Launch browser
    When Open transtats homepage
    And Click on login
    And Enter username "<username>" and password "<password>"
    And Click on login button
    Then Successful login to the Transtats admin page.

    Examples:
      | username | password |
      | admin    | admin123 |
      | admin123 | admin    |
      | adminxyz | admin123 |
      | transtats| transtats|