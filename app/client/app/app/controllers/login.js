import Controller from '@ember/controller';
import { inject as service } from '@ember/service';
import { action } from '@ember/object';


export default class LoginController extends Controller {
	@service session

	@action
    async authenticate() {
	      const credentials = this.getProperties('email', 'password');
	      const authenticator = 'authenticator:application'; // or 'authenticator:jwt'
	      await this.session.authenticate(authenticator, credentials);
	      
	      if (this.session.isAuthenticated) {
	      	console.log('authenticated')
	      	console.log(this.session.data)
	      }
    }
}
