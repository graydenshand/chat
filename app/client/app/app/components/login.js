import Component from '@glimmer/component';
import { inject as service } from '@ember/service';
import { action } from '@ember/object';
import { tracked } from '@glimmer/tracking';

export default class LoginComponent extends Component {
	@service session
	@tracked email
	@tracked password
	@tracked loginMode = true // false for "signup" mode
	@tracked errorMessage

	@action
    async authenticate() {
		const credentials = {email: this.email, password: this.password};
		const authenticator = 'authenticator:application'; // or 'authenticator:jwt'
		this.session.authenticate(authenticator, credentials)
			.then( (response) => {
				if (this.session.isAuthenticated) {
					console.log('authenticated')
					console.log(this.session.data)
				}
			}).catch( (response) => {
					const error = response.errors[0]
					this.errorMessage = error;
				}
			);

		
    }

    @action
    toggleMode() {
    	this.loginMode = !this.loginMode
    }

}
