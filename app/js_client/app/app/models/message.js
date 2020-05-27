import Model, { attr, belongsTo } from '@ember-data/model';

export default class MessageModel extends Model {
  @attr('string') message;
  @attr('date') createdAt;
  @attr('number') userId;
  @attr('number') channelId;

  @belongsTo('user') user;
  @belongsTo('channel') channel;
}