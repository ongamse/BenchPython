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

	@app.route('/benchmark/weakrand-01/BenchmarkTest00415', methods=['GET'])
	def BenchmarkTest00415_get():
		return BenchmarkTest00415_post()

	@app.route('/benchmark/weakrand-01/BenchmarkTest00415', methods=['POST'])
	def BenchmarkTest00415_post():
		RESPONSE = ""

		param = ""
		for name in request.form.keys():
			if "BenchmarkTest00415" in request.form.getlist(name):
				param = name
				break

		import configparser
		
		bar = 'safe!'
		conf88136 = configparser.ConfigParser()
		conf88136.add_section('section88136')
		conf88136.set('section88136', 'keyA-88136', 'a-Value')
		conf88136.set('section88136', 'keyB-88136', param)
		bar = conf88136.get('section88136', 'keyB-88136')

		import base64
		import secrets
		from helpers.utils import mysession

		num = 'BenchmarkTest00415'[13:]
		user = f'SafeToby{num}'
		cookie = f'rememberMe{num}'
		value = base64.b64encode(secrets.token_bytes(32))

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

