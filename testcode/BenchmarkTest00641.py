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

	@app.route('/benchmark/codeinj-00/BenchmarkTest00641', methods=['GET'])
	def BenchmarkTest00641_get():
		return BenchmarkTest00641_post()

	@app.route('/benchmark/codeinj-00/BenchmarkTest00641', methods=['POST'])
	def BenchmarkTest00641_post():
		RESPONSE = ""

		param = ""
		headers = request.headers.getlist("BenchmarkTest00641")
		
		if headers:
			param = headers[0]

		import configparser
		
		bar = 'safe!'
		conf83525 = configparser.ConfigParser()
		conf83525.add_section('section83525')
		conf83525.set('section83525', 'keyA-83525', 'a-Value')
		conf83525.set('section83525', 'keyB-83525', param)
		bar = conf83525.get('section83525', 'keyB-83525')

		if not bar.startswith('\'') or not bar.endswith('\'') or '\'' in bar[1:-1]:
			RESPONSE += (
				"Eval argument must be a plain string literal."
			)
			return RESPONSE		

		try:
			RESPONSE += (
				eval(bar)
			)
		except:
			RESPONSE += (
				f'Error evaluating expression \'{escape_for_html(bar)}\''
			)

		return RESPONSE

