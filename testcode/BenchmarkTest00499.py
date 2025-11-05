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

	@app.route('/benchmark/weakrand-01/BenchmarkTest00499', methods=['GET'])
	def BenchmarkTest00499_get():
		return BenchmarkTest00499_post()

	@app.route('/benchmark/weakrand-01/BenchmarkTest00499', methods=['POST'])
	def BenchmarkTest00499_post():
		RESPONSE = ""

		param = request.headers.get("BenchmarkTest00499")
		if not param:
		    param = ""

		import configparser
		
		bar = 'safe!'
		conf92831 = configparser.ConfigParser()
		conf92831.add_section('section92831')
		conf92831.set('section92831', 'keyA-92831', 'a-Value')
		conf92831.set('section92831', 'keyB-92831', param)
		bar = conf92831.get('section92831', 'keyB-92831')

		import secrets
		from helpers.utils import mysession

		num = 'BenchmarkTest00499'[13:]
		user = f'SafeRobbie{num}'
		cookie = f'rememberMe{num}'
		value = str(secrets.randbelow(2**32))

		if cookie in mysession and request.cookies.get(cookie) == mysession[cookie]:
			RESPONSE += (
				f'Welcome back: {user}<br/>'
			)
		else:
			mysession[cookie] = value
			RESPONSE += (
				f'{user} has been remembered with cookie:'
				f'{cookie} whose value is: {mysession[cookie]}<br/>'
			)

		return RESPONSE

