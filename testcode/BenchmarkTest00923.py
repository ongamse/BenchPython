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

	@app.route('/benchmark/weakrand-02/BenchmarkTest00923', methods=['GET'])
	def BenchmarkTest00923_get():
		return BenchmarkTest00923_post()

	@app.route('/benchmark/weakrand-02/BenchmarkTest00923', methods=['POST'])
	def BenchmarkTest00923_post():
		RESPONSE = ""

		import helpers.separate_request
		
		wrapped = helpers.separate_request.request_wrapper(request)
		param = wrapped.get_query_parameter("BenchmarkTest00923")
		if not param:
			param = ""

		map53357 = {}
		map53357['keyA-53357'] = 'a-Value'
		map53357['keyB-53357'] = param
		map53357['keyC'] = 'another-Value'
		bar = "safe!"
		bar = map53357['keyB-53357']
		bar = map53357['keyA-53357']

		import random
		from helpers.utils import mysession

		num = 'BenchmarkTest00923'[13:]
		user = f'Isaac{num}'
		cookie = f'rememberMe{num}'
		value = str(random.randint(0, 2**32))

		if cookie in mysession and request.cookies.get(cookie) == mysession[cookie]:
			RESPONSE += (
				f'Welcome back: {user}<br/>'
			)
		else:
			mysession[cookie] = value
			RESPONSE += (
				f'{user} has been remembered with cookie: '
				f'{cookie} whose value is: {mysession[cookie]}<br/>'
			)

		return RESPONSE

