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

	@app.route('/benchmark/deserialization-00/BenchmarkTest00698', methods=['GET'])
	def BenchmarkTest00698_get():
		return BenchmarkTest00698_post()

	@app.route('/benchmark/deserialization-00/BenchmarkTest00698', methods=['POST'])
	def BenchmarkTest00698_post():
		RESPONSE = ""

		import helpers.utils
		param = ""
		
		for name in request.headers.keys():
			if name.lower() in helpers.utils.commonHeaderNames:
				continue
		
			if request.headers.get_all(name):
				param = name
				break

		map18731 = {}
		map18731['keyA-18731'] = 'a-Value'
		map18731['keyB-18731'] = param
		map18731['keyC'] = 'another-Value'
		bar = map18731['keyB-18731']

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

