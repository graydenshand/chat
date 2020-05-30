import Component from '@glimmer/component';
import { inject as service } from '@ember/service';
import { action } from '@ember/object';


export default class ChatInputComponent extends Component {
	@service store

	@action insertMessage() {
		console.log('insrting message')
		let message = this.store.createRecord('message', {
			message: 'Hi there buddy!',
			userId: 1,
			channelId: 2,
		})
		message.save();
	}

	@action test() {
		window.alert('test')
	}
}
