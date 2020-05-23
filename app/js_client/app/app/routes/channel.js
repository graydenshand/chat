import Route from '@ember/routing/route';

export default class ChannelRoute extends Route {

	model() {
		return {channel: "random"}
	}
}
