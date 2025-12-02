from dbbuilder.dialect import Dialect


class Exasol(Dialect):
    def __init__(self):
        Dialect.__init__(self, "Exasol")