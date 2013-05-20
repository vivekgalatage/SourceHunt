from ProtocolException import ProtocolSchemaFileError;
import json;

class SchemaValidator:
    def validate(self, parsedObject, schemaFileName):
        pass;

class JSONSchemaValidator(SchemaValidator):
    def __loadSchema(self, schemaFileName):
        fileHandle = open(schemaFileName);

        try:
            schemaData = json.load(fileHandle);
        except Exception as e:
            fileHandle.close();
            raise ProtocolSchemaFileError(schemaFileName, e.message);

        for rule in schemaData:
            print rule;

        fileHandle.close();

    def validate(self, parsedObject, schemaFileName):
        assert(isinstance(parsedObject, dict));
        self.__loadSchema(schemaFileName);
        for obj in parsedObject["version"]:
            print obj, parsedObject["version"][obj], type(parsedObject["version"][obj]);
        return True;
