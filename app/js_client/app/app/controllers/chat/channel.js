import Controller from '@ember/controller';
import { action } from '@ember/object';
import { inject as service } from '@ember/service';
import { getOwner } from '@ember/application';


export default class ChatChannelController extends Controller {
	//@service store

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
		window.alert('test')
	}

	@action 
	insertMessage() {
		console.log('insrting message')
		let channel = this.store.peekRecord('channel', 2);
		let user = this.store.peekRecord('user', 1)
		let message = this.store.createRecord('message', {
			message: 'Hi there buddy!',
			userId: user,
			channelId: channel,
		})
		message.save();
	}
}
