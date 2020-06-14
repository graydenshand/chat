import Component from '@glimmer/component';
import { action } from '@ember/object';
import { tracked } from '@glimmer/tracking';
import { inject as service } from '@ember/service';

export default class SignupComponent extends Component {
	@service session
	@tracked email
	@tracked password
	@tracked errorMessage
	
	@action
    signUp() {
    	console.log('signup')
    }
}
