// app/authenticators/custom.js
import Base from 'ember-simple-auth/authenticators/base';
import ENV from '../config/environment';

export default class CustomAuthenticator extends Base {


  authenticate(options) {
    return this.postData(`${ENV.api_url}/auth.json`, options)
  }

  restore(options) {
  	return this.putData(`${ENV.api_url}/auth.json`, options)
  }


  async postData(url = '', data = {}) {
	  // Default options are marked with *
	  const response = await fetch(url, {
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
	  });
	  return response.json(); // parses JSON response into native JavaScript objects
	}


  async putData(url = '', data = {}) {
	  // Default options are marked with *
	const response = await fetch(url, {
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
		body: JSON.stringify(data) // body data type must match "Content-Type" header
	});
	  return response.json(); // parses JSON response into native JavaScript objects
	}
}