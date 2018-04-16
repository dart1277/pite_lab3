import socket

from game.common.messages import Messages
from game.server.controller import Controller
from game.server.logger import Logger


class OXServer:
    TCP_IP = '127.0.0.1'
    TCP_PORT = 5005
    BUFFER_SIZE = 1024
    controller = Controller()

    def _bind_and_listen(self):
        s = None
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.bind((self.TCP_IP, self.TCP_PORT))
            s.listen(8)
        except (socket.error, socket.herror, socket.gaierror, socket.timeout):
            s = None
        if s is None:
            Logger.log('Could not open socket')
            exit(1)
        return s

    def run(self):
        s = self._bind_and_listen()

        # server loop
        while True:
            conn = addr = None
            try:
                # accept next connection
                conn, addr = s.accept()

                # get data from the client
                data = conn.recv(self.BUFFER_SIZE)  # constant BUFFER_SIZE for GET requests prevents simple DoS attacks
                if not data:
                    Logger.log('Empty request from', addr)
                    continue

                # call the controller get method
                action, game_id, optional_params = Messages.parse_incoming_request(data)
                ret = self.controller.get(action, game_id, *optional_params)
                json_ret = Messages.prepare_response(ret)
                conn.sendall(str(json_ret).encode())
            except Exception as e:
                # log exception and client address
                Logger.log_request(e, addr)
            finally:
                conn.close()
                # print('Games active: ' + str(self.controller.games_active()))
        s.close()  # this line should remain here in the case of using os signals to close the server process


if __name__ == '__main__':
    OXServer().run()
