import pytest

from exasol.tdbp.dialects.exasol.exasol_identifier import ExasolIdentifier
from exasol.tdbp.schema import Schema
from exasol.tdbp.table import Table


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
        "name·name",  # With the middle dot (U+00B7)
        "name︳name",  # With connector punctuation (Pc)
        "nañme",  # With non-spacing mark (Mn)
        "naྲme",  # With a spacing mark (Mc)
        "name٢",  # With decimal number (Nd)
        "naמּe",  # With format control (Cf)
    ],
)
def test_validate_identifier(valid_identifier: str):
    ExasolIdentifier.of(valid_identifier)


@pytest.mark.parametrize(
    "invalid_identifier",
    [
        "foo bar",
        "foo.bar",  # A dot can connect identifiers; But is not allowed in an identifier
        "'foo",
        "'foo'",
        '"foo"',
        'foo"',
        "123name",
        "·name",
        "@name",
        "",
        None,
    ],
)
def test_validate_identifier_fails(invalid_identifier: str):
    with pytest.raises(ValueError):
        ExasolIdentifier.of(invalid_identifier)


def test_to_string():
    identifier = ExasolIdentifier.of("the_identifier")
    assert str(identifier) == "the_identifier"
