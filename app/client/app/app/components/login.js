import Component from '@glimmer/component';
import { inject as service } from '@ember/service';
import { action } from '@ember/object';
import { tracked } from '@glimmer/tracking';

export default class LoginComponent extends Component {
	@service session
	@service router
	@tracked email
	@tracked password
	@tracked errorMessage

	@action
    async authenticate() {
    	if (!this.validateEmail()) {
    		this.errorMessage = 'Invalid email'
    		return null
    	}
		const credentials = {email: this.email, password: this.password};
		const authenticator = 'authenticator:application'; // or 'authenticator:jwt'
		this.session.authenticate(authenticator, credentials)
		.then( (response) => {
			if (this.session.isAuthenticated) {
				this.router.transitionTo('chat');
			}
		}).catch( (response) => {
				const error = response.errors[0]
				this.errorMessage = error;
			}
		);	
    }

    validateEmail() {
	  const re = /^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
	  return re.test(this.email);
	}

}
