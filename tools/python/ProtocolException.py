class ProtocolException(Exception):
    def message(self):
        return "Generic Protocol Error";

class ProtocolFileError(ProtocolException):
    def __init__(self, fileName, error):
        self.message = "Protocol File Error: \n\t" + fileName + " -> " + error;

class ProtocolValidationError(ProtocolException):
    def __init__(self, fileName, schemaFileName, error):
        self.message = "Protocol Validation Error: \n\t" + "fileName: " + fileName + "\n\t" + "schemaFileName: " + schemaFileName + "\n\t" + error;

class ProtocolSchemaFileError(ProtocolException):
    def __init__(self, schemaFileName, error):
        self.message = "Protocol-Schema File Error: \n\t" + schemaFileName + " -> " + error;
