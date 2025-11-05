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

	@app.route('/benchmark/intoverflow-00/BenchmarkTest00265', methods=['GET'])
	def BenchmarkTest00265_get():
		return BenchmarkTest00265_post()

	@app.route('/benchmark/intoverflow-00/BenchmarkTest00265', methods=['POST'])
	def BenchmarkTest00265_post():
		RESPONSE = ""

		values = request.form.getlist("BenchmarkTest00265")
		param = ""
		if values:
			param = values[0]

		import configparser
		
		bar = 'safe!'
		conf1676 = configparser.ConfigParser()
		conf1676.add_section('section1676')
		conf1676.set('section1676', 'keyA-1676', 'a-Value')
		conf1676.set('section1676', 'keyB-1676', param)
		bar = conf1676.get('section1676', 'keyB-1676')

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

