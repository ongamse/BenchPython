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

	@app.route('/benchmark/deserialization-00/BenchmarkTest00552', methods=['GET'])
	def BenchmarkTest00552_get():
		return BenchmarkTest00552_post()

	@app.route('/benchmark/deserialization-00/BenchmarkTest00552', methods=['POST'])
	def BenchmarkTest00552_post():
		RESPONSE = ""

		param = request.headers.get("BenchmarkTest00552")
		if not param:
		    param = ""

		import configparser
		
		bar = 'safe!'
		conf67597 = configparser.ConfigParser()
		conf67597.add_section('section67597')
		conf67597.set('section67597', 'keyA-67597', 'a-Value')
		conf67597.set('section67597', 'keyB-67597', param)
		bar = conf67597.get('section67597', 'keyB-67597')

		import pickle
		import base64
		import helpers.utils

		helpers.utils.sharedstr = "no pickles to be seen here"

		try:
			unpickled = pickle.loads(base64.urlsafe_b64decode(bar))
		except:
			RESPONSE += (
				'Unpickling failed!'
			)
			return RESPONSE

		RESPONSE += (
			f'shared string is {helpers.utils.sharedstr}'
		)

		return RESPONSE

