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

	@app.route('/benchmark/intoverflow-00/BenchmarkTest00956', methods=['GET'])
	def BenchmarkTest00956_get():
		return BenchmarkTest00956_post()

	@app.route('/benchmark/intoverflow-00/BenchmarkTest00956', methods=['POST'])
	def BenchmarkTest00956_post():
		RESPONSE = ""

		import helpers.separate_request
		
		wrapped = helpers.separate_request.request_wrapper(request)
		param = wrapped.get_query_parameter("BenchmarkTest00956")
		if not param:
			param = ""

		import configparser
		
		bar = 'safe!'
		conf98918 = configparser.ConfigParser()
		conf98918.add_section('section98918')
		conf98918.set('section98918', 'keyA-98918', 'a_Value')
		conf98918.set('section98918', 'keyB-98918', param)
		bar = conf98918.get('section98918', 'keyA-98918')

		import re

		regex = re.compile(r'a*bcde[e-z]+')

		if regex.match(bar) is not None:
			RESPONSE += (
				'String matches!'
			)
		else:
			RESPONSE += (
				'String does not match.'
			)

		return RESPONSE

