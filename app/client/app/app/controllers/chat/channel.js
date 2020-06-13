import Controller from '@ember/controller';
import { action } from '@ember/object';
import { inject as service } from '@ember/service';
import { getOwner } from '@ember/application';
import { tracked } from '@glimmer/tracking';


export default class ChatChannelController extends Controller {
	@service store
	@tracked messageText = '';

	@action
	refresh() {
		console.log("refresh")
	}

	@action
	refreshModel() {
		getOwner(this).lookup('route:chat.channel').refresh();
	}

	@action 
	test() {
		window.alert(this.messageText)
	}

	@action
	scrollMessageContainer() {
		var messageContainer = document.querySelector(".message-container");
		messageContainer.scrollTop = messageContainer.scrollHeight
	}

	@action 
	insertMessage() {
		console.log('Inserting message')
		let channel = this.store.peekRecord('channel', this.get('channelId'));
		let user = this.store.peekRecord('user', 1)
		let message = this.store.createRecord('message', {
			message: this.messageText,
			userId: user,
			channelId: channel,
		})
		message.save();
		this.messageText = ''
		this.scrollMessageContainer()
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
}
