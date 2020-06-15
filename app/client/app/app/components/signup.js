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
    	if (!this.validateEmail()) {return null};
     	if (!this.validatePassword()) {return null};
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

	@action
	validateEmail() {
	  const re = /^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
	  if (!re.test(this.email)) {
	  	this.errorMessage = 'Invalid email';
	  	return false;
	  } else {
	  	return true;
	  }
	}

	validatePassword() {
		/*
		Rules
			1 Uppercase
			1 Number
			> 8 chars
			password2 input matches
		*/
		
		// Uppercase char
		let uppercaseCheck = false;
		let re = /[A-Z]/;
		if (re.test(this.password)) {
			uppercaseCheck = true;
		} 

		// Number
		let numberCheck = false;
		re = /\d/;
		if (re.test(this.password)) {
			numberCheck = true;
		} 

		// Length >= 8
		let lengthCheck = false;
		if (this.password.length >= 8) {
			lengthCheck = true;
		}

		// Retype password check
		let retypeCheck = false;
		if (this.password2 == this.password) {
			retypeCheck = true
		}

		const checkArray = [uppercaseCheck, numberCheck, lengthCheck, retypeCheck]
		console.log(checkArray)
		if (!checkArray.every((currentValue) => {return currentValue})) {
			this.errorMessage = 'Password failed validation'
			return false
		} else {
			return true
		}
	}	
}
