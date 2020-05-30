import RESTSerializer from '@ember-data/serializer/rest';

export default class ApplicationSerializer extends RESTSerializer {
	serializeIntoHash(data, type, snapshot, options) {
		/*
		Remove outer level of nesting for JSON body 
		on POST and PUT requests

		e.g
		FROM 
		{
			"message": {
				field: value,
				field: value
			}
		}

		TO
		{
			field: value,
			field: value
		}

		*/
		super.serializeIntoHash(...arguments);
		let key = Object.keys(data)[0]
		let subKeys = Object.keys(data[key])
		let values = Object.values(data[key])
		let i = 0;
		for (i=0; i < subKeys.length; i++) {
			if (values[i] != null) {
				data[subKeys[i]] = values[i];
			}
		}
		if (!subKeys.includes(key)){
			delete data[key]
		}
	}
}