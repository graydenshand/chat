import Route from '@ember/routing/route';
import { inject as service } from '@ember/service';

export default class ChatRoute extends Route {
	@service store

	async model() {
		return {"users": this.store.findAll('user')};
	}
}
