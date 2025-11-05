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

	@app.route('/benchmark/weakrand-02/BenchmarkTest01019', methods=['GET'])
	def BenchmarkTest01019_get():
		return BenchmarkTest01019_post()

	@app.route('/benchmark/weakrand-02/BenchmarkTest01019', methods=['POST'])
	def BenchmarkTest01019_post():
		RESPONSE = ""

		import urllib.parse
		
		query_string = request.query_string.decode('utf-8')
		paramLoc = query_string.find("BenchmarkTest01019" + '=')
		if paramLoc == -1:
			return f"request.query_string did not contain expected parameter \'{"BenchmarkTest01019"}\'."
		param = query_string[paramLoc + len("BenchmarkTest01019") + 1:]
		ampLoc = param.find('&')
		if ampLoc != -1:
			param = param[:ampLoc]
		
		param = urllib.parse.unquote_plus(param)

		import configparser
		
		bar = 'safe!'
		conf49778 = configparser.ConfigParser()
		conf49778.add_section('section49778')
		conf49778.set('section49778', 'keyA-49778', 'a_Value')
		conf49778.set('section49778', 'keyB-49778', param)
		bar = conf49778.get('section49778', 'keyA-49778')

		import random
		from helpers.utils import mysession

		num = 'BenchmarkTest01019'[13:]
		user = f'Nancy{num}'
		cookie = f'rememberMe{num}'
		value = str(random.normalvariate())[2:]

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

