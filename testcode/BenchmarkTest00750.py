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

	@app.route('/benchmark/weakrand-02/BenchmarkTest00750', methods=['GET'])
	def BenchmarkTest00750_get():
		return BenchmarkTest00750_post()

	@app.route('/benchmark/weakrand-02/BenchmarkTest00750', methods=['POST'])
	def BenchmarkTest00750_post():
		RESPONSE = ""

		param = request.args.get("BenchmarkTest00750")
		if not param:
			param = ""

		import configparser
		
		bar = 'safe!'
		conf8238 = configparser.ConfigParser()
		conf8238.add_section('section8238')
		conf8238.set('section8238', 'keyA-8238', 'a-Value')
		conf8238.set('section8238', 'keyB-8238', param)
		bar = conf8238.get('section8238', 'keyB-8238')

		import random
		from helpers.utils import mysession

		num = 'BenchmarkTest00750'[13:]
		user = f'SafeNancy{num}'
		cookie = f'rememberMe{num}'
		value = str(random.SystemRandom().normalvariate())[2:]

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

