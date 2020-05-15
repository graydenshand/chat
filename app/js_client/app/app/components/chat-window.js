import Component from '@glimmer/component';
import { inject as service } from '@ember/service';
import { action } from '@ember/object';

export default class ChatWindow extends Component {
    constructor(...args) {
        super(...args);
        this.namespace = '';
    }

    @service socketIO

    @action test() {
        window.alert("test");
    }

    @action openSocket()  {
      const socket = this.socketIO.socketFor(`http://localhost:5000/${this.namespace}`);
      console.log(socket)
      socket.on('connect', this.onConnect, this);
      socket.on('message', this.onMessage, this);
    }

    @action closeSocket() {
      const socket = this.socketIO.socketFor(`http://localhost:5000/${this.namespace}`);
      socket.off('connect', this.onConnect);
      socket.off('message', this.onMessage);
    }

    onMessage(data) {
      // This is executed within the ember run loop
      console.log(`Message from server: ${data}`)
    }

    onConnect() {
      const socket = this.socketIO.socketFor(`http://localhost:5000/${this.namespace}`);
      socket.send('Hello World');
      socket.emit('message', 'Hello Server');
      console.log('Connected')
    }

    @action sendMessage() {
      const socket = this.socketIO.socketFor(`http://localhost:5000/${this.namespace}`);
      socket.send('Test');
    }
}