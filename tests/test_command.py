from pas_man.validate import validate_email

def test_validate_email(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "tushar@gmail.com")

    assert validate_email() == "tushar@gmail.com"