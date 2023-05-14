from mask._common import mask_email, mask_string, randnum, znum


def test_mask_string():
    assert mask_string("k") == "k"
    assert mask_string("Jo") == "J*"
    assert mask_string("Ken") == "K**"
    assert mask_string("Kevin") == "K***n"
    assert mask_string("") == ""
    assert mask_string("Jack", fill="_") == "J__k"
    assert mask_string("Jen", fill="_") == "J__"
    assert mask_string(None) is None


def test_mask_emails():
    assert mask_email("e@email.com") == "e@e***l.com"
    assert mask_email("Jo@email.com") == "J*@e***l.com"
    assert mask_email("Jen@email.com") == "J**@e***l.com"
    assert mask_email("July@email.com") == "J**y@e***l.com"
    assert mask_email("proper@email.com") == "p****r@e***l.com"
    assert mask_email("proper@email.gov.ca") == "p****r@e***l.gov.ca"
    assert mask_email("improper email.com") == "improper email.com"
    assert mask_email("improper@email com") == "improper@email com"
    assert mask_email("") == ""
    assert mask_email(None) is None


def test_znum():
    assert znum("1234") == "0"
    assert znum(1234) == 0
    assert znum(1234.0) == 0.0
    assert znum(None) is None
    assert znum(False) is False


def test_randnum():
    assert randnum(1234) != 1234
    assert randnum("9000") != 9000
