import Model, { attr } from '@ember-data/model';

export default class MessageModel extends Model {
  @attr('string') message;
  @attr('date') created_at;
  @attr('number') userId;
}