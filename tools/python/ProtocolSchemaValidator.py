# Copyright (c) 2013, Vivek Galatage
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# 1. Redistributions of source code must retain the above copyright notice, this
#    list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR
# ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#
# The views and conclusions contained in the software and documentation are those
# of the authors and should not be interpreted as representing official policies,
# either expressed or implied, of the FreeBSD Project.

from ProtocolException import ProtocolSchemaFileError;
from ProtocolException import ProtocolSchemaKeyError;

import json;

class SchemaValidator:
    def validate(self, parsedObject, schemaFileName):
        pass;

class JSONSchemaValidator(SchemaValidator):
    def __assertProperty(self, schemaObject, property):
        try:
            assert(schemaObject[property]);
        except KeyError as e:
            raise ProtocolSchemaKeyError(self.schemaFileName, e.message)

    def __validateObject(self, schemaObject):
        self.__assertProperty(schemaObject, "properties");
        if "description" in schemaObject:
            print schemaObject["description"];
        for property in schemaObject["properties"]:
            self.__validateSchema(schemaObject["properties"][property]);

    def __validateNumer(self, schemaObject):
        if "required" in schemaObject:
            print schemaObject;

    def __validateSchema(self, schemaData):
        if not hasattr(self, "schemaTypeHandler"):
            self.schemaTypeHandler = {
                "object": self.__validateObject,
                "number": self.__validateNumer
            };

        self.__assertProperty(schemaData, "type");
        self.schemaTypeHandler[schemaData["type"]](schemaData);

    def __loadSchema(self):
        try:
            fileHandle = open(self.schemaFileName);
            schemaData = json.load(fileHandle);
            fileHandle.close();
            self.__validateSchema(schemaData);
        except Exception as e:
            fileHandle.close();
            raise ProtocolSchemaFileError(self.schemaFileName, e.message);

    def validate(self, parsedObject, schemaFileName):
        assert(isinstance(parsedObject, dict));
        self.schemaFileName = schemaFileName;
        self.__loadSchema();
        for obj in parsedObject["version"]:
            print obj, parsedObject["version"][obj], type(parsedObject["version"][obj]);
        return True;
