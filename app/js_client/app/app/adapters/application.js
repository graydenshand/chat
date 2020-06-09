import RESTAdapter from '@ember-data/adapter/rest';
import ENV from '../config/environment'; 
import { computed } from '@ember/object';
import { inject as service } from '@ember/service';


export default RESTAdapter.extend({
	host: ENV.api_url,

	session: service('session'),

	buildURL: function() {
	const url = this._super(...arguments);
		return `${url}.json`;
  	},

  	headers: computed('session.data.authenticated.token', function() {
  		let token = this.get('session.data.authenticated.token')
	    return {
	      'Authorization': `Bearer ${token}`,
	    };
	}),
})