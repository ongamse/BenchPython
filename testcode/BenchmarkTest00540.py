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

	@app.route('/benchmark/codeinj-00/BenchmarkTest00540', methods=['GET'])
	def BenchmarkTest00540_get():
		return BenchmarkTest00540_post()

	@app.route('/benchmark/codeinj-00/BenchmarkTest00540', methods=['POST'])
	def BenchmarkTest00540_post():
		RESPONSE = ""

		param = request.headers.get("BenchmarkTest00540")
		if not param:
		    param = ""

		import configparser
		
		bar = 'safe!'
		conf36502 = configparser.ConfigParser()
		conf36502.add_section('section36502')
		conf36502.set('section36502', 'keyA-36502', 'a_Value')
		conf36502.set('section36502', 'keyB-36502', param)
		bar = conf36502.get('section36502', 'keyA-36502')

		try:
			RESPONSE += (
				eval(bar)
			)
		except:
			RESPONSE += (
				f'Error evaluating expression \'{escape_for_html(bar)}\''
			)

		return RESPONSE

