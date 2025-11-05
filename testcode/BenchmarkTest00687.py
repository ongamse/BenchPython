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

	@app.route('/benchmark/intoverflow-00/BenchmarkTest00687', methods=['GET'])
	def BenchmarkTest00687_get():
		return BenchmarkTest00687_post()

	@app.route('/benchmark/intoverflow-00/BenchmarkTest00687', methods=['POST'])
	def BenchmarkTest00687_post():
		RESPONSE = ""

		import helpers.utils
		param = ""
		
		for name in request.headers.keys():
			if name.lower() in helpers.utils.commonHeaderNames:
				continue
		
			if request.headers.get_all(name):
				param = name
				break

		import configparser
		
		bar = 'safe!'
		conf69622 = configparser.ConfigParser()
		conf69622.add_section('section69622')
		conf69622.set('section69622', 'keyA-69622', 'a_Value')
		conf69622.set('section69622', 'keyB-69622', param)
		bar = conf69622.get('section69622', 'keyA-69622')

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

