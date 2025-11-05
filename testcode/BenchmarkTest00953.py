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

	@app.route('/benchmark/intoverflow-00/BenchmarkTest00953', methods=['GET'])
	def BenchmarkTest00953_get():
		return BenchmarkTest00953_post()

	@app.route('/benchmark/intoverflow-00/BenchmarkTest00953', methods=['POST'])
	def BenchmarkTest00953_post():
		RESPONSE = ""

		import helpers.separate_request
		
		wrapped = helpers.separate_request.request_wrapper(request)
		param = wrapped.get_query_parameter("BenchmarkTest00953")
		if not param:
			param = ""

		import configparser
		
		bar = 'safe!'
		conf96796 = configparser.ConfigParser()
		conf96796.add_section('section96796')
		conf96796.set('section96796', 'keyA-96796', 'a_Value')
		conf96796.set('section96796', 'keyB-96796', param)
		bar = conf96796.get('section96796', 'keyA-96796')

		import re

		regex = re.compile(r'^(([a-z])+.)+')

		if regex.match(bar) is not None:
			RESPONSE += (
				'String matches!'
			)
		else:
			RESPONSE += (
				'String does not match.'
			)

		return RESPONSE

