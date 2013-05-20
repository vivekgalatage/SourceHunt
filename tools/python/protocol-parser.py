from ProtocolBuilder import ProtocolBuilder;
from ProtocolException import ProtocolException;

def main():
    try:
        builder = ProtocolBuilder(ProtocolBuilder.JSON, "src/protocol/protocol.json", "src/protocol/protocol-schema.json");
        builder.load();
    except ProtocolException as e:
        print e.message;

if __name__ == "__main__":
    main();
