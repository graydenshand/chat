import Route from '@ember/routing/route';
import { inject as service } from '@ember/service';

export default class ChatRoute extends Route {
	@service store

	async model(params) {
		let users = this.store.findAll('user');
		let channels = this.store.findAll('channel');
		return {"users": users, "channels": channels};
	}

}
