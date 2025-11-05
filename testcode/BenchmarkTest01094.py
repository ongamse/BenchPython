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

	@app.route('/benchmark/deserialization-00/BenchmarkTest01094', methods=['GET'])
	def BenchmarkTest01094_get():
		return BenchmarkTest01094_post()

	@app.route('/benchmark/deserialization-00/BenchmarkTest01094', methods=['POST'])
	def BenchmarkTest01094_post():
		RESPONSE = ""

		import urllib.parse
		
		query_string = request.query_string.decode('utf-8')
		paramLoc = query_string.find("BenchmarkTest01094" + '=')
		if paramLoc == -1:
			return f"request.query_string did not contain expected parameter \'{"BenchmarkTest01094"}\'."
		param = query_string[paramLoc + len("BenchmarkTest01094") + 1:]
		ampLoc = param.find('&')
		if ampLoc != -1:
			param = param[:ampLoc]
		
		param = urllib.parse.unquote_plus(param)

		import configparser
		
		bar = 'safe!'
		conf36072 = configparser.ConfigParser()
		conf36072.add_section('section36072')
		conf36072.set('section36072', 'keyA-36072', 'a_Value')
		conf36072.set('section36072', 'keyB-36072', param)
		bar = conf36072.get('section36072', 'keyA-36072')

		import yaml

		try:
			yobj = yaml.safe_load(bar)

			RESPONSE += (
				yobj['text']
			)
		except:
			RESPONSE += (
				"There was an error loading the configuration"
			)

		return RESPONSE

