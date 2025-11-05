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

	@app.route('/benchmark/codeinj-00/BenchmarkTest00544', methods=['GET'])
	def BenchmarkTest00544_get():
		return BenchmarkTest00544_post()

	@app.route('/benchmark/codeinj-00/BenchmarkTest00544', methods=['POST'])
	def BenchmarkTest00544_post():
		RESPONSE = ""

		param = request.headers.get("BenchmarkTest00544")
		if not param:
		    param = ""

		import configparser
		
		bar = 'safe!'
		conf19542 = configparser.ConfigParser()
		conf19542.add_section('section19542')
		conf19542.set('section19542', 'keyA-19542', 'a_Value')
		conf19542.set('section19542', 'keyB-19542', param)
		bar = conf19542.get('section19542', 'keyA-19542')

		try:
			exec(bar)
		except:
			RESPONSE += (
				f'Error executing statement \'{escape_for_html(bar)}\''
			)

		return RESPONSE

