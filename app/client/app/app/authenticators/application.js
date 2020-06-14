// app/authenticators/custom.js
import Base from 'ember-simple-auth/authenticators/base';
import ENV from '../config/environment';

export default class CustomAuthenticator extends Base {


  authenticate(options) {
  	return new Ember.RSVP.Promise( async (resolve, reject) => {
	  // Default options are marked with *
	  var success = true;
	  fetch(`${ENV.api_url}/auth.json`, {
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
	    body: JSON.stringify(options) // body data type must match "Content-Type" header
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

  restore(options) {
  	return new Ember.RSVP.Promise( async (resolve, reject) => {
  		var success = true;
  		fetch(`${ENV.api_url}/auth.json`, {
			method: 'PUT', // *GET, POST, PUT, DELETE, etc.
			mode: 'cors', // no-cors, *cors, same-origin
			cache: 'no-cache', // *default, no-cache, reload, force-cache, only-if-cached
			credentials: 'same-origin', // include, *same-origin, omit
			headers: {
			  'Content-Type': 'application/json'
			  // 'Content-Type': 'application/x-www-form-urlencoded',
			},
			redirect: 'follow', // manual, *follow, error
			referrerPolicy: 'no-referrer', // no-referrer, *no-referrer-when-downgrade, origin, origin-when-cross-origin, same-origin, strict-origin, strict-origin-when-cross-origin, unsafe-url
			body: JSON.stringify(options) // body data type must match "Content-Type" header
		}).then( (response) => { 
		  	if (response.status != 200) {
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