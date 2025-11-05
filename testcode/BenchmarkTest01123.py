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

	@app.route('/benchmark/weakrand-03/BenchmarkTest01123', methods=['GET'])
	def BenchmarkTest01123_get():
		return BenchmarkTest01123_post()

	@app.route('/benchmark/weakrand-03/BenchmarkTest01123', methods=['POST'])
	def BenchmarkTest01123_post():
		RESPONSE = ""

		parts = request.path.split("/")
		param = parts[1]
		if not param:
			param = ""

		import configparser
		
		bar = 'safe!'
		conf63527 = configparser.ConfigParser()
		conf63527.add_section('section63527')
		conf63527.set('section63527', 'keyA-63527', 'a-Value')
		conf63527.set('section63527', 'keyB-63527', param)
		bar = conf63527.get('section63527', 'keyB-63527')

		import random
		from helpers.utils import mysession

		num = 'BenchmarkTest01123'[13:]
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

