import regex


class ExasolIdentifier:
    """
    Represents an Exasol identifier.

    This class provides functionality to validate and create Exasol-compatible
    identifiers. Identifiers are validated against a specific pattern that defines
    valid Exasol identifier strings. The class ensures that only valid identifiers
    can be instantiated.

    The main purpose is to prevent SQL injection attacks by ensuring that
    user-provided identifiers are valid.

    See Also:
        https://docs.exasol.com/db/latest/sql_references/basiclanguageelements.htm#SQLidentifier
    """

    __IDENTIFIER_PATTERN = (
        r"^[\p{Lu}\p{Ll}\p{Lt}\p{Lm}\p{Lo}\p{Nl}]"
        r"[\p{Lu}\p{Ll}\p{Lt}\p{Lm}\p{Lo}\p{Nl}\p{Mn}\p{Mc}\p{Nd}\p{Pc}\p{Cf}\u00B7]*$"
    )

    def __init__(self, identifier: str):
        self.identifier = identifier

    def __str__(self):
        return self.identifier

    @staticmethod
    def of(identifier: str):
        """
        Creates an instance of ExasolIdentifier when the provided identifier is valid according to the Exasol SQL
        identifier specification.

        The method validates the identifier string against the Exasol identifier rules, ensuring it starts with a Unicode
        letter or letter number and only includes valid characters. Raises a ValueError for invalid identifiers.

        Args:
            identifier (str): The string representing the identifier to be validated and converted
                into an ExasolIdentifier instance.

        Returns:
            ExasolIdentifier: An ExasolIdentifier instance when the given identifier is valid.

        Raises:
            ValueError: If the provided identifier does not comply with the Exasol identifier pattern.
        """
        if (identifier is not None) and regex.match(
            ExasolIdentifier.__IDENTIFIER_PATTERN, identifier, regex.UNICODE
        ):
            return ExasolIdentifier(identifier)
        else:
            raise ValueError(
                f"Invalid Exasol identifier '{identifier}'. Identifiers must start with a Unicode letter or letter "
                "number and can only contain letters, numbers, marks, connectors, formatting codes or the middle dot "
                "character."
            )
