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

	@app.route('/benchmark/intoverflow-00/BenchmarkTest00629', methods=['GET'])
	def BenchmarkTest00629_get():
		return BenchmarkTest00629_post()

	@app.route('/benchmark/intoverflow-00/BenchmarkTest00629', methods=['POST'])
	def BenchmarkTest00629_post():
		RESPONSE = ""

		param = ""
		headers = request.headers.getlist("BenchmarkTest00629")
		
		if headers:
			param = headers[0]

		import configparser
		
		bar = 'safe!'
		conf33984 = configparser.ConfigParser()
		conf33984.add_section('section33984')
		conf33984.set('section33984', 'keyA-33984', 'a_Value')
		conf33984.set('section33984', 'keyB-33984', param)
		bar = conf33984.get('section33984', 'keyA-33984')

		import re

		regex = r'(a+)+$'

		if re.match(regex, bar) is not None:
			RESPONSE += (
				'String matches!'
			)
		else:
			RESPONSE += (
				'String does not match.'
			)

		return RESPONSE

