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

	@app.route('/benchmark/weakrand-01/BenchmarkTest00412', methods=['GET'])
	def BenchmarkTest00412_get():
		return BenchmarkTest00412_post()

	@app.route('/benchmark/weakrand-01/BenchmarkTest00412', methods=['POST'])
	def BenchmarkTest00412_post():
		RESPONSE = ""

		param = ""
		for name in request.form.keys():
			if "BenchmarkTest00412" in request.form.getlist(name):
				param = name
				break

		import configparser
		
		bar = 'safe!'
		conf30805 = configparser.ConfigParser()
		conf30805.add_section('section30805')
		conf30805.set('section30805', 'keyA-30805', 'a_Value')
		conf30805.set('section30805', 'keyB-30805', param)
		bar = conf30805.get('section30805', 'keyA-30805')

		import random
		from helpers.utils import mysession

		num = 'BenchmarkTest00412'[13:]
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

