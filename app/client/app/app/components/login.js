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
		this.session.authenticate(authenticator, credentials)
		.then(
			(data) => {
				//console.log(data)
				if (this.session.isAuthenticated) {
					console.log('authenticated')
					console.log(this.session.data)
				}
			}
		).catch(
			(error) => {
				console.log(error)
			}
		);

		
    }

    @action
    toggleMode() {
    	this.loginMode = !this.loginMode
    }

}
