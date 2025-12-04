import pytest

from exasol.tdbp.dialects.exasol.exasol_identifier import ExasolIdentifier


@pytest.mark.parametrize(
    "valid_identifier",
    [
        "foo",  # Simple ASCII
        "foo_bar",  # With underscore
        "Köln",  # Uppercase with umlaut (Lu)
        "αβγ",  # Lowercase Greek (Ll)
        "ǅword",  # Title case letter (Lt)
        "ᵃword",  # Modifier letter (Lm)
        "սword",  # Other letter (Lo)
        "ⅥII",  # Letter number (Nl)
        "name·name",  # With middle dot (U+00B7)
        "name︳name",  # With connector punctuation (Pc)
        "nañme",  # With non-spacing mark (Mn)
        "naྲme",  # With spacing mark (Mc)
        "name٢",  # With decimal number (Nd)
        "naמּe",  # With format control (Cf)
    ],
)
def test_validate_identifier(valid_identifier: str):
    ExasolIdentifier.of(valid_identifier)


@pytest.mark.parametrize(
    "invalid_identifier",
    [
        "foo bar",  # Space not allowed
        "foo.bar",  # Dot not allowed
        "'foo'",  # Quotes not allowed
        "123name",  # Cannot start with number
        "·name",  # Cannot start with middle dot
        "@name",  # Cannot start with symbol
        "",  # Empty string not allowed
    ],
)
def test_validate_identifier_fails(invalid_identifier: str):
    with pytest.raises(ValueError):
        ExasolIdentifier.of(invalid_identifier)
