from ProtocolParser import JSONProtocolParser;
from ProtocolSchemaValidator import JSONSchemaValidator;

class ProtocolBuilder:
    JSON = 0;
    XML = 1;
    protocolMapper = {
        JSON: {
            "parser": JSONProtocolParser(),
            "validator": JSONSchemaValidator()
        }
    }

    def __init__(self, protocolType, fileName, schemaFileName):
        self.protocolType = protocolType;
        self.fileName = fileName;
        self.schemaFileName = schemaFileName;

    def load(self):
        protocolHandler = self.protocolMapper[self.protocolType];

        parsedObject = protocolHandler["parser"].parse(self.fileName);
        try:
            assert(protocolHandler["validator"].validate(parsedObject, self.schemaFileName));
        except AssertionError as e:
            raise ProtocolValidationError(self.fileName, self.schemaFileName, e.message);

        return parsedObject;
