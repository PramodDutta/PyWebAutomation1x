from behave import given, when, then



@given('open the app.vwo.com')
def step_impl(context):
    pass  # Setup, if necessary


@when('I enter the {username} and {password}')
def step_impl(context, username, password):
    print(username,password)
    # write a code to login to app.vwo.com


@then('I get this {message}')
def step_impl(context, message):
    print(message)
