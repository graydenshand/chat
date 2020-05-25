#!/bin/env python
from app import create_app, socketio
from app.config import DevelopmentConfig, ProductionConfig
import os

if os.environ.get("ENVIRONMENT") == "DEV":
	app = create_app(debug=True, config="app.config.DevelopmentConfig")
else:
	app = create_app(config="app.config.ProductionConfig")

if __name__ =='__main__':
	socketio.run(app, host='0.0.0.0', port=os.environ.get('PORT'))