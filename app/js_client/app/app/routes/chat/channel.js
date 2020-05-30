import Route from '@ember/routing/route';
import { inject as service } from '@ember/service';
import RSVP from "rsvp";



export default class ChatChannelRoute extends Route {
	@service store

	async model(params) {
		var channel = this.store.peekRecord("channel", params.channel);

		return channel;
	}
}
