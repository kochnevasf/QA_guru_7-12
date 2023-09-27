import allure
from allure import step

@step("test_pass1")
def test_pass1():
    pass


@step("test_pass2")
def test_pass2():
    pass

@step("test_pass3")
def test_pass3():
    pass

@step("test_pass4")
def test_pass4():
    pass

@step("test_pass5")
def test_pass5():
    pass

@step("test_pass6")
def test_pass6():
    pass

@allure.tag('web')
@allure.severity(severity_level='Critical')
@allure.feature("Issues")
@allure.story("тесты пройдены")
@allure.link("https://github.com/", name='Testing')
@allure.label('owner', 'github')
def test_pass7():
    pass
