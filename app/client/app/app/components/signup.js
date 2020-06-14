import Component from '@glimmer/component';
import { action } from '@ember/object';
import { tracked } from '@glimmer/tracking';
import { inject as service } from '@ember/service';
import ENV from '../config/environment';

export default class SignupComponent extends Component {
	@service session
	@service store
	@service router
	@tracked name
	@tracked email
	@tracked password
	@tracked password2
	@tracked errorMessage
	
	@action
    signUp() {
    	this.createUser().then((data) => {
    		this.store.pushPayload(data)
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
    	}).catch((response)=> {
    		console.log(response)
    		const error = response.errors[0]
			this.errorMessage = error;
    	})
    	

    }

    createUser() {
    	const data = {
    		name: this.name,
    		email: this.email,
    		password: this.password
    	}
    	return new Ember.RSVP.Promise( async (resolve, reject) => {
		  // Default options are marked with *
		  var success = true;
		  fetch(`${ENV.api_url}/users.json`, {
		    method: 'POST', // *GET, POST, PUT, DELETE, etc.
		    mode: 'cors', // no-cors, *cors, same-origin
		    cache: 'no-cache', // *default, no-cache, reload, force-cache, only-if-cached
		    credentials: 'same-origin', // include, *same-origin, omit
		    headers: {
		      'Content-Type': 'application/json'
		      // 'Content-Type': 'application/x-www-form-urlencoded',
		    },
		    redirect: 'follow', // manual, *follow, error
		    referrerPolicy: 'no-referrer', // no-referrer, *no-referrer-when-downgrade, origin, origin-when-cross-origin, same-origin, strict-origin, strict-origin-when-cross-origin, unsafe-url
		    body: JSON.stringify(data) // body data type must match "Content-Type" header
		  }).then( (response) => { 
		  	if (response.status != 201) {
		  		success = false;
		  	} 
		  	return response.json()
		  }).then( (response) => {
		  	if (success) { 
		  		resolve(response)
		  	} else {
		  		reject(response)
		  	}
		  }).catch( (error) => {
		  	reject(error)
		  });
		})
	}	
}
