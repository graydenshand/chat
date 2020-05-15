import Model, { attr } from '@ember-data/model';

export default class Message extends Model {
  @attr('string') id;
  @attr('string') text;
  @attr('date') sent_at;
  @attr('string') from;
}