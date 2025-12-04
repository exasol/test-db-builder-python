import regex


class ExasolIdentifier:
    IDENTIFIER_PATTERN = r"^[\p{Lu}\p{Ll}]\p{Lt}\p{Lm}\p{Lo}\p{Nl}]*"
    r"[\p{Lu}\p{Ll}\p{Lt}\p{Lm}\p{Lo}\p{Nl}\p{Mn}\p{Mc}\p{Nd}\p{Pc}\p{Cf}\u00B7]*$"

    def __init__(self, identifier: str):
        self.identifier = identifier

    @staticmethod
    def of(identifier: str):
        if regex.match(ExasolIdentifier.IDENTIFIER_PATTERN, identifier, regex.UNICODE):
            return ExasolIdentifier(identifier)
        else:
            raise ValueError(
                f"Invalid Exasol identifier '{identifier}'. Identifiers must start with a Unicode letter or letter "
                f"number and can only contain letters, numbers, marks, connectors, formatting codes or the middle dot "
                f"character."
            )
