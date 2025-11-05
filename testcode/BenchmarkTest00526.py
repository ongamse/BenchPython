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

	@app.route('/benchmark/intoverflow-00/BenchmarkTest00526', methods=['GET'])
	def BenchmarkTest00526_get():
		return BenchmarkTest00526_post()

	@app.route('/benchmark/intoverflow-00/BenchmarkTest00526', methods=['POST'])
	def BenchmarkTest00526_post():
		RESPONSE = ""

		param = request.headers.get("BenchmarkTest00526")
		if not param:
		    param = ""

		import configparser
		
		bar = 'safe!'
		conf95384 = configparser.ConfigParser()
		conf95384.add_section('section95384')
		conf95384.set('section95384', 'keyA-95384', 'a-Value')
		conf95384.set('section95384', 'keyB-95384', param)
		bar = conf95384.get('section95384', 'keyB-95384')

		import re

		regex = re.compile(r'^(([a-z])+.)+')

		if regex.match(bar) is not None:
			RESPONSE += (
				'String matches!'
			)
		else:
			RESPONSE += (
				'String does not match.'
			)

		return RESPONSE

