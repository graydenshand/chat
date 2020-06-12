import Route from '@ember/routing/route';
import { inject as service } from '@ember/service';
import RSVP from "rsvp";



export default class ChatChannelRoute extends Route {
	@service store

	async model(params) {
		var channel = this.store.peekRecord("channel", params.channel);
		this.set('channelId', params.channel) 

		return channel;
	}

	setupController(controller, model) {
	    // Call _super for default behavior
	    this._super(controller, model);
	    // Implement your custom setup after
	    controller.set('channelId', this.get('channelId'));
	  }
}
