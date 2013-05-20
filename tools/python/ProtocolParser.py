from ProtocolException import ProtocolFileError;

import json;

class ProtocolParser:
    def parse(self):
        pass;

class JSONProtocolParser:
    def parse(self, fileName):
        fileHandle = open(fileName);

        try:
            jsonData = json.load(fileHandle);
        except Exception as e:
            fileHandle.close();
            raise ProtocolFileError(fileName, e.message);

        fileHandle.close();
        return jsonData;
