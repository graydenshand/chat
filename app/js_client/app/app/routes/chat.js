import Route from '@ember/routing/route';
import { inject as service } from '@ember/service';

export default class ChatRoute extends Route {
	@service store

	async model(params) {
		let users = await this.store.findAll('user');
		let channels = await this.store.findAll('channel');
		let messages = await this.store.findAll('message');
		return {"users": users, "channels": channels, "messages": messages};
	}

}
