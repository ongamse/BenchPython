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

	@app.route('/benchmark/codeinj-00/BenchmarkTest00275', methods=['GET'])
	def BenchmarkTest00275_get():
		return BenchmarkTest00275_post()

	@app.route('/benchmark/codeinj-00/BenchmarkTest00275', methods=['POST'])
	def BenchmarkTest00275_post():
		RESPONSE = ""

		values = request.form.getlist("BenchmarkTest00275")
		param = ""
		if values:
			param = values[0]

		import configparser
		
		bar = 'safe!'
		conf4093 = configparser.ConfigParser()
		conf4093.add_section('section4093')
		conf4093.set('section4093', 'keyA-4093', 'a_Value')
		conf4093.set('section4093', 'keyB-4093', param)
		bar = conf4093.get('section4093', 'keyA-4093')

		try:
			exec(bar)
		except:
			RESPONSE += (
				f'Error executing statement \'{escape_for_html(bar)}\''
			)

		return RESPONSE

