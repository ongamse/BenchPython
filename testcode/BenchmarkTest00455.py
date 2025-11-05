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

	@app.route('/benchmark/codeinj-00/BenchmarkTest00455', methods=['GET'])
	def BenchmarkTest00455_get():
		return BenchmarkTest00455_post()

	@app.route('/benchmark/codeinj-00/BenchmarkTest00455', methods=['POST'])
	def BenchmarkTest00455_post():
		RESPONSE = ""

		param = ""
		for name in request.form.keys():
			if "BenchmarkTest00455" in request.form.getlist(name):
				param = name
				break

		import configparser
		
		bar = 'safe!'
		conf61311 = configparser.ConfigParser()
		conf61311.add_section('section61311')
		conf61311.set('section61311', 'keyA-61311', 'a_Value')
		conf61311.set('section61311', 'keyB-61311', param)
		bar = conf61311.get('section61311', 'keyA-61311')

		try:
			RESPONSE += (
				eval(bar)
			)
		except:
			RESPONSE += (
				f'Error evaluating expression \'{escape_for_html(bar)}\''
			)

		return RESPONSE

