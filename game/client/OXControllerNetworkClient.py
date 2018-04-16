import socket
from game.common.messages import Messages
from game.server.OXServer import OXServer


class OXControllerNetworkClient:
    TCP_IP = '127.0.0.1'
    TCP_PORT = OXServer.TCP_PORT
    BUFFER_SIZE = OXServer.BUFFER_SIZE

    def get(self, query_str):
        request_not_completed = True
        return_val = s = None

        # handle client request
        while request_not_completed:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((self.TCP_IP, self.TCP_PORT))
                s.send(query_str.encode())
                data = s.recv(self.BUFFER_SIZE).decode(encoding='UTF-8')
                return_val = Messages.process_response(data)
                request_not_completed = False
            except (socket.error, socket.herror, socket.gaierror, socket.timeout):
                print('Error: Cannot connect to the server!')
                try_again = input('Do you want to try again? Please press enter to confirm or type N to exit.\n')
                if len(try_again) > 0:
                    exit(1)
                print('Please wait...')
            finally:
                s.close()
        return return_val
