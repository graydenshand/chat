import RESTAdapter from '@ember-data/adapter/rest';

export default RESTAdapter.extend({
  // Application specific overrides go here
  host: 'http://127.0.0.1:5000',
  buildURL: function() {
    const url = this._super(...arguments);
    return `${url}.json`;
  }
})