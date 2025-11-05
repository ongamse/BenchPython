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

	@app.route('/benchmark/codeinj-00/BenchmarkTest00174', methods=['GET'])
	def BenchmarkTest00174_get():
		return BenchmarkTest00174_post()

	@app.route('/benchmark/codeinj-00/BenchmarkTest00174', methods=['POST'])
	def BenchmarkTest00174_post():
		RESPONSE = ""

		param = request.form.get("BenchmarkTest00174")
		if not param:
			param = ""

		import configparser
		
		bar = 'safe!'
		conf56895 = configparser.ConfigParser()
		conf56895.add_section('section56895')
		conf56895.set('section56895', 'keyA-56895', 'a_Value')
		conf56895.set('section56895', 'keyB-56895', param)
		bar = conf56895.get('section56895', 'keyA-56895')

		if not bar.startswith('\'') or not bar.endswith('\'') or '\'' in bar[1:-1]:
			RESPONSE += (
				"Exec argument must be a plain string literal."
			)
			return RESPONSE

		try:
			exec(bar)
		except:
			RESPONSE += (
				f'Error executing statement \'{escape_for_html(bar)}\''
			)

		return RESPONSE

