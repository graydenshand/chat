import Route from '@ember/routing/route';
import { inject as service } from '@ember/service';
import RSVP from "rsvp";



export default class ChatChannelRoute extends Route {
	@service store
	channelId = null

	async model(params) {
		var channel = this.store.peekRecord("channel", params.channel);

		// copy messages to mutable list
		var messages = null;
		await this.store.query("message", {"channelId":params.channel}).then((message_list) => {
			messages = message_list.toArray();
		});
		
		this.channelId = params.channel
		return {'channel': channel, 'messages': messages};
	}

	setupController(controller, model) {
	    // Call _super for default behavior
	    this._super(controller, model);
	    // Implement your custom setup after
	    controller.set('channelId', this.get('channelId'));
	    controller.set('model', model)
	  }
}
