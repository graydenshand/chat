import Route from '@ember/routing/route';
import { inject as service } from '@ember/service';

export default class ChatRoute extends Route {
	@service store;
	@service session;

	async model(params) {
		let users = await this.store.findAll('user').catch((errors) => {console.log(errors.errors)});
		let channels = await this.store.findAll('channel').catch((errors) => {console.log(errors.errors)});
		//let messages = await this.store.findAll('message').catch((errors) => {console.log(errors.errors)});
		return {"users": users, "channels": channels};
	}

}
