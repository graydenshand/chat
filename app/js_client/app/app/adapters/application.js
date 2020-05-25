import RESTAdapter from '@ember-data/adapter/rest';
import ENV from '../config/environment'; 


export default RESTAdapter.extend({
  // Application specific overrides go here
  host: ENV.api_url,
  buildURL: function() {
    const url = this._super(...arguments);
    return `${url}.json`;
  }
})