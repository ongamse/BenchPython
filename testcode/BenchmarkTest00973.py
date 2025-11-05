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

	@app.route('/benchmark/trustbound-00/BenchmarkTest00973', methods=['GET'])
	def BenchmarkTest00973_get():
		return BenchmarkTest00973_post()

	@app.route('/benchmark/trustbound-00/BenchmarkTest00973', methods=['POST'])
	def BenchmarkTest00973_post():
		RESPONSE = ""

		import helpers.separate_request
		
		wrapped = helpers.separate_request.request_wrapper(request)
		param = wrapped.get_query_parameter("BenchmarkTest00973")
		if not param:
			param = ""

		import configparser
		
		bar = 'safe!'
		conf73289 = configparser.ConfigParser()
		conf73289.add_section('section73289')
		conf73289.set('section73289', 'keyA-73289', 'a-Value')
		conf73289.set('section73289', 'keyB-73289', param)
		bar = conf73289.get('section73289', 'keyB-73289')

		import flask

		flask.session['userid'] = bar

		RESPONSE += (
			f'Item: \'userid\' with value \'{escape_for_html(bar)}'
			'\'saved in session.'
		)

		return RESPONSE

