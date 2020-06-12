import Component from '@glimmer/component';
import { inject as service } from '@ember/service';
import { action } from '@ember/object';
import { tracked } from '@glimmer/tracking';

export default class LoginComponent extends Component {
	@service session
	@tracked email
	@tracked password
	@tracked loginMode = true // false for "signup" mode

	@action
    async authenticate() {
		const credentials = {email: this.email, password: this.password};
		const authenticator = 'authenticator:application'; // or 'authenticator:jwt'
		await this.session.authenticate(authenticator, credentials);

		if (this.session.isAuthenticated) {
			console.log('authenticated')
			console.log(this.session.data)
		}
    }

    @action
    toggleMode() {
    	this.loginMode = !this.loginMode
    }

}
