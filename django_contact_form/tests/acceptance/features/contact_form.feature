Feature: contact form
    Scenario: User submit contact form successfully
        Given User is on contact form page
         When User fill the fields
          And User click submit button
         Then User submit form succussfully

    Scenario: User for get to fill required fileds
        Given User is on contact form page
         When User click submit button
         Then User get error message
