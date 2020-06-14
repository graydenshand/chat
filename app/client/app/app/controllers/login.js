import Controller from '@ember/controller';
import { inject as service } from '@ember/service';
import { action } from '@ember/object';
import { tracked } from '@glimmer/tracking';

export default class LoginController extends Controller {
	@service session
	@tracked loginMode = true // false for "signup" mode

	@action
    toggleMode() {
    	this.loginMode = !this.loginMode
    }
}
