import Controller from '@ember/controller';
import { inject as service } from '@ember/service';
import { action } from '@ember/object';
import ENV from '../config/environment'; 


export default class ChatController extends Controller {
	@service session
}
