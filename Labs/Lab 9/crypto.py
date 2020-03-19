from abc import ABC

from des import DesKey
import argparse
import abc
import enum


class CryptoMode(enum.Enum):
    """
    Lists the various modes that the Crypto application can run in.
    """
    # Encryption mode
    EN = "en"
    # Decryption Mode
    DE = "de"


class Request:
    """
    The request object represents a request to either encrypt or decrypt
    certain data. The request object comes with certain accompanying
    configuration options as well as a field that holds the result. The
    attributes are:
        - encryption_state: 'en' for encrypt, 'de' for decrypt
        - data_input: This is the string data that needs to be encrypted or
        decrypted. This is None if the data is coming in from a file.
        - input_file: The text file that contains the string to be encrypted or
        decrypted. This is None if the data is not coming from a file and is
        provided directly.
        - output: This is the method of output that is requested. At this
        moment the program supports printing to the console or writing to
        another text file.
        - key: The Key value to use for encryption or decryption.
        - result: Placeholder value to hold the result of the encryption or
        decryption. This does not usually come in with the request.

    """

    def __init__(self):
        self.encryption_state = None
        self.data_input = None
        self.input_file = None
        self.output = None
        self.key = None
        self.result = None

    def __str__(self):
        return f"Request: State: {self.encryption_state}, Data: {self.data_input}" \
               f", Input file: {self.input_file}, Output: {self.output}, " \
               f"Key: {self.key}, Result: {self.result}"


def setup_request_commandline() -> Request:
    """
    Implements the argparse module to accept arguments via the command
    line. This function specifies what these arguments are and parses it
    into an object of type Request. If something goes wrong with
    provided arguments then the function prints an error message and
    exits the application.
    :return: The object of type Request with all the arguments provided
    in it.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("key", help="The key to use when encrypting or "
                                    "decrypting. This needs to be of "
                                    "length 8, 16 or 24")
    parser.add_argument("-s", "--string", help="The string that needs to be "
                                               "encrypted or decrypted")
    parser.add_argument("-f", "--file", help="The text file that needs to be"
                                             "encrypted or decrypted")
    parser.add_argument("-o", "--output", default="print",
                        help="The output of the program. This is 'print' by "
                             "default, but can be set to a file name as well.")
    parser.add_argument("-m", "--mode", default="en",
                        help="The mode to run the program in. If 'en' (default)"
                             " then the program will encrypt, 'de' will cause "
                             "the program to decrypt")
    try:
        args = parser.parse_args()
        request = Request()
        request.encryption_state = CryptoMode(args.mode)
        request.data_input = args.string
        request.input_file = args.file
        request.output = args.output
        request.key = args.key
        print(request)
        return request
    except Exception as e:
        print(f"Error! Could not read arguments.\n{e}")
        quit()


class BaseCryptoHandler(abc.ABC):

    def __init__(self, next_handler=None):
        self.next_handler = next_handler

    @abc.abstractmethod
    def handle_request(self, req):
        pass

    def set_handler(self, handler):
        self.next_handler = handler


class ErrorHandler:
    @staticmethod
    def handle_error(error):
        print(error)


class EncryptHandler(BaseCryptoHandler):

    def handle_request(self, req: Request):
        if req.encryption_state == CryptoMode.EN:
            self.set_handler(KeyHandler)
            return self.next_handler.handle_request(KeyHandler, req)
        else:
            return ErrorHandler.handle_error("Not in EN mode.")


class KeyHandler(BaseCryptoHandler):

    def handle_request(self, req: Request):
        if req.key is not None:
            req.key = DesKey(bytes(req.key, encoding='utf-8'))
            self.set_handler(self, InputHandler)
            return self.next_handler.handle_request(InputHandler, req)
        else:
            return ErrorHandler.handle_error("No key provided.")


class InputHandler(BaseCryptoHandler):

    def handle_request(self, req: Request):
        if (req.input_file is not None) or (req.data_input is not None):
            self.set_handler(self, OutputHandler)
            return self.next_handler.handle_request(self, req)
        else:
            return ErrorHandler.handle_error("No data/file input to encrypt")


class OutputHandler(BaseCryptoHandler):

    def handle_request(self, req: Request):
        if req.input_file is not None:
            f = open(req.input_file, "r")
            data = (f.read())
            f.close()
            if req.output == "print":
                req.result = (req.key.encrypt(bytes(data, encoding='utf-8'), padding=True))
                return req
            else:
                file = open(req.output, "wb")
                req.result = (req.key.encrypt(bytes(data, encoding='utf-8'), padding=True))
                file.write(req.result)
                file.close()
        else:
            if req.output == "print":
                req.result = (req.key.encrypt(bytes(req.data_input, encoding='utf-8'), padding=True))
                return req
            else:
                file = open(req.output, "wb")
                req.result = (req.key.encrypt(bytes(req.data_input, encoding='utf-8'), padding=True))
                file.write(req.result)
                file.close()


class DecryptHandler(BaseCryptoHandler):

    def handle_request(self, req: Request):
        if req.encryption_state == CryptoMode.DE:
            self.set_handler(KeyHandlerDe)
            return self.next_handler.handle_request(KeyHandlerDe, req)
        else:
            return ErrorHandler.handle_error("Not in DE mode.")


class KeyHandlerDe(BaseCryptoHandler):

    def handle_request(self, req: Request):
        if req.key is not None:
            req.key = DesKey(bytes(req.key, encoding='utf-8'))
            self.set_handler(self, InputHandlerDe)
            return self.next_handler.handle_request(InputHandlerDe, req)
        else:
            return ErrorHandler.handle_error("No key provided.")


class InputHandlerDe(BaseCryptoHandler):

    def handle_request(self, req: Request):
        if (req.input_file is not None) or (req.data_input is not None):
            self.set_handler(self, OutputHandlerDe)
            return self.next_handler.handle_request(self, req)
        else:
            return ErrorHandler.handle_error("No data/file input to decrypt")


class OutputHandlerDe(BaseCryptoHandler):

    def handle_request(self, req: Request):
        if req.input_file is not None:
            f = open(req.input_file, "r")
            data = (f.read())
            f.close()
            if req.output == "print":
                req.result = (req.key.decrypt(str.encode(data), padding=True))
                return req
            else:
                file = open(req.output, "wb")
                req.result = (req.key.decrypt(data, padding=True))
                file.write(req.result)
                file.close()
        else:
            if req.output == "print":
                req.result = (req.key.decrypt(str.encode(req.data_input), padding=True))
                return req
            else:
                file = open(req.output, "wb")
                req.result = (req.key.decrypt(req.data_input, padding=True))
                file.write(req.result)
                file.close()


class Crypto:

    def __init__(self):
        self.encryption_start_handler = EncryptHandler()
        self.decryption_start_handler = DecryptHandler()

    def execute_request(self, req: Request):
        if req.encryption_state == CryptoMode.EN:
            result = self.encryption_start_handler.handle_request(req)
            print(result)
        else:
            print("de")
            result = self.decryption_start_handler.handle_request(req)
            print(result)


def main(request: Request):
    crypto = Crypto()
    crypto.execute_request(request)
    # key1 = DesKey(b"some key")
    # key2 = DesKey(b"diff key")
    # test = (key1.encrypt(b"helloworld", padding=True))
    # print(test)
    # print(key2.decrypt(test, padding=True))


if __name__ == '__main__':
    request = setup_request_commandline()
    main(request)
