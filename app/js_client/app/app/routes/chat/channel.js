import Route from '@ember/routing/route';
import { inject as service } from '@ember/service';

export default class ChatChannelRoute extends Route {
	@service store

	async model(params) {
		return {"messages": this.store.findAll('message'), "channel": params.channel};
	}
}
