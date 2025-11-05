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

	@app.route('/benchmark/intoverflow-00/BenchmarkTest00529', methods=['GET'])
	def BenchmarkTest00529_get():
		return BenchmarkTest00529_post()

	@app.route('/benchmark/intoverflow-00/BenchmarkTest00529', methods=['POST'])
	def BenchmarkTest00529_post():
		RESPONSE = ""

		param = request.headers.get("BenchmarkTest00529")
		if not param:
		    param = ""

		import configparser
		
		bar = 'safe!'
		conf5707 = configparser.ConfigParser()
		conf5707.add_section('section5707')
		conf5707.set('section5707', 'keyA-5707', 'a_Value')
		conf5707.set('section5707', 'keyB-5707', param)
		bar = conf5707.get('section5707', 'keyA-5707')

		import re

		regex = re.compile(r'a*bcde[e-z]+')

		if regex.match(bar) is not None:
			RESPONSE += (
				'String matches!'
			)
		else:
			RESPONSE += (
				'String does not match.'
			)

		return RESPONSE

