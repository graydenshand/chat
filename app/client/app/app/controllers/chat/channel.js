import Controller from '@ember/controller';
import { action } from '@ember/object';
import { inject as service } from '@ember/service';
import { getOwner } from '@ember/application';
import { tracked } from '@glimmer/tracking';


export default class ChatChannelController extends Controller {
	@service store;
	@service session;
	@tracked messageText;

	@action
	scrollMessageContainer() {
		var messageContainer = document.querySelector(".message-container");
		messageContainer.scrollTop = messageContainer.scrollHeight
	}

	@action 
	insertMessage() {
		console.log('Inserting message')
		let messageModel = this.get('model.messages');
		let channel = this.store.peekRecord('channel', this.get('channelId'));
		let user = this.store.peekRecord('user', this.session.data.authenticated.id)
		let message = this.store.createRecord('message', {
			message: this.messageText,
			userId: user,
			channelId: channel,
		})
		message.save().then((data)=>{
			messageModel.pushObject(message);
			this.messageText = ''
			// need to wait for new message to render
			window.setTimeout(this.scrollMessageContainer,10);
		});
	}


	@action
	resizeMessageInput() {
		const messageInput = document.querySelector("#chat-input");
		messageInput.style.height = 'auto';
	  	messageInput.style.height = (messageInput.scrollHeight) + 'px';
	}

	@action
	setUpMessageInput() {
		var messageInput = document.querySelector('#chat-input');
		messageInput.setAttribute('style', 'height:' + (messageInput.scrollHeight) + 'px;overflow-y:hidden;');
	}

	@action
	updateMessageText() {
		var messageInput = document.querySelector('#chat-input');
		this.messageText = messageInput.value;
	}
}
