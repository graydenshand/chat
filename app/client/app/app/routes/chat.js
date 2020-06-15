import Route from '@ember/routing/route';
import { inject as service } from '@ember/service';

export default class ChatRoute extends Route {
	@service store;
	@service session;

	beforeModel(transition) {
		if (!this.session.isAuthenticated) {
			this.transitionTo('login');
		}
	}

	async model(params) {
		let users = await this.store.findAll('user').catch((errors) => {console.log(errors.errors)});
		let channels = await this.store.findAll('channel').catch((errors) => {console.log(errors.errors)});
		let currentUser = this.store.peekRecord('user', this.session.data.authenticated.id);
		//let messages = await this.store.findAll('message').catch((errors) => {console.log(errors.errors)});
		return {"users": users, "channels": channels, "currentUser":currentUser};
	}

}
