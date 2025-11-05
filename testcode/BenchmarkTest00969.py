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

	@app.route('/benchmark/redirect-00/BenchmarkTest00969', methods=['GET'])
	def BenchmarkTest00969_get():
		return BenchmarkTest00969_post()

	@app.route('/benchmark/redirect-00/BenchmarkTest00969', methods=['POST'])
	def BenchmarkTest00969_post():
		RESPONSE = ""

		import helpers.separate_request
		
		wrapped = helpers.separate_request.request_wrapper(request)
		param = wrapped.get_query_parameter("BenchmarkTest00969")
		if not param:
			param = ""

		import configparser
		
		bar = 'safe!'
		conf16616 = configparser.ConfigParser()
		conf16616.add_section('section16616')
		conf16616.set('section16616', 'keyA-16616', 'a-Value')
		conf16616.set('section16616', 'keyB-16616', param)
		bar = conf16616.get('section16616', 'keyB-16616')

		import flask

		return flask.redirect(bar)

		return RESPONSE

