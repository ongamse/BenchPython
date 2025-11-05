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

	@app.route('/benchmark/securecookie-00/BenchmarkTest00865', methods=['GET'])
	def BenchmarkTest00865_get():
		return BenchmarkTest00865_post()

	@app.route('/benchmark/securecookie-00/BenchmarkTest00865', methods=['POST'])
	def BenchmarkTest00865_post():
		RESPONSE = ""

		values = request.args.getlist("BenchmarkTest00865")
		param = ""
		if values:
			param = values[0]

		import configparser
		
		bar = 'safe!'
		conf5880 = configparser.ConfigParser()
		conf5880.add_section('section5880')
		conf5880.set('section5880', 'keyA-5880', 'a_Value')
		conf5880.set('section5880', 'keyB-5880', param)
		bar = conf5880.get('section5880', 'keyA-5880')

		from flask import make_response
		import io
		import helpers.utils

		input = ''
		if isinstance(bar, str):
			input = bar.encode('utf-8')
		elif isinstance(bar, io.IOBase):
			input = bar.read(1000)

		cookie = 'SomeCookie'
		value = input.decode('utf-8')

		RESPONSE += (
			f'Created cookie: \'{cookie}\' with value \'{helpers.utils.escape_for_html(value)}\' and secure flag set to false.'
		)

		RESPONSE = make_response(RESPONSE)
		RESPONSE.set_cookie(cookie, value,
			path=request.path,
			secure=True,
			httponly=True)

		return RESPONSE

