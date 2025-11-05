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

	@app.route('/benchmark/weakrand-02/BenchmarkTest00753', methods=['GET'])
	def BenchmarkTest00753_get():
		return BenchmarkTest00753_post()

	@app.route('/benchmark/weakrand-02/BenchmarkTest00753', methods=['POST'])
	def BenchmarkTest00753_post():
		RESPONSE = ""

		param = request.args.get("BenchmarkTest00753")
		if not param:
			param = ""

		import configparser
		
		bar = 'safe!'
		conf72616 = configparser.ConfigParser()
		conf72616.add_section('section72616')
		conf72616.set('section72616', 'keyA-72616', 'a-Value')
		conf72616.set('section72616', 'keyB-72616', param)
		bar = conf72616.get('section72616', 'keyB-72616')

		import random
		from helpers.utils import mysession

		num = 'BenchmarkTest00753'[13:]
		user = f'SafeIsaac{num}'
		cookie = f'rememberMe{num}'
		value = str(random.SystemRandom().randint(0, 2**32))

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

