from socketIO_client import SocketIO, BaseNamespace

class ChatNamespace(BaseNamespace):

    def on_my_response(self, *args):
        print('my_response', args)


socketIO = SocketIO('localhost', 5000)
chat_namespace = socketIO.define(ChatNamespace, '/test')

chat_namespace.emit('my_room_event',
         {'data': 'Hello', 'receive_count': 111, 'room': 'abc'})
socketIO.wait(seconds=100)
