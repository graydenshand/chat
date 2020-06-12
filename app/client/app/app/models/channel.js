import Model, { attr, hasMany } from '@ember-data/model';

export default class ChannelModel extends Model {
  @attr('string') name;
  @attr('date') createdAt;

  @hasMany('messages') messages;
}