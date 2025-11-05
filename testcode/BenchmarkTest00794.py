'''
OWASP Benchmark for Python v0.1

This file is part of the Open Web Application Security Project (OWASP) Benchmark Project.
For details, please see https://owasp.org/www-project-benchmark.

The OWASP Benchmark is free software: you can redistribute it and/or modify it under the terms
of the GNU General Public License as published by the Free Software Foundation, version 3.

The OWASP Benchmark is distributed in the hope that it will be useful, but WITHOUT ANY
WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR
PURPOSE. See the GNU General Public License for more details.

  Author: Theo Cartsonis
  Created: 2025
'''

from flask import redirect, url_for, request, make_response, render_template
from helpers.utils import escape_for_html

def init(app):

	@app.route('/benchmark/deserialization-00/BenchmarkTest00794', methods=['GET'])
	def BenchmarkTest00794_get():
		return BenchmarkTest00794_post()

	@app.route('/benchmark/deserialization-00/BenchmarkTest00794', methods=['POST'])
	def BenchmarkTest00794_post():
		RESPONSE = ""

		param = request.args.get("BenchmarkTest00794")
		if not param:
			param = ""

		import configparser
		
		bar = 'safe!'
		conf88104 = configparser.ConfigParser()
		conf88104.add_section('section88104')
		conf88104.set('section88104', 'keyA-88104', 'a-Value')
		conf88104.set('section88104', 'keyB-88104', param)
		bar = conf88104.get('section88104', 'keyB-88104')

		import yaml

		try:
			yobj = yaml.load(bar, Loader=yaml.Loader)

			RESPONSE += (
				yobj['text']
			)
		except:
			RESPONSE += (
				"There was an error loading the configuration"
			)

		return RESPONSE

