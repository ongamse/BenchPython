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

	@app.route('/benchmark/redirect-00/BenchmarkTest01246', methods=['GET'])
	def BenchmarkTest01246_get():
		return BenchmarkTest01246_post()

	@app.route('/benchmark/redirect-00/BenchmarkTest01246', methods=['POST'])
	def BenchmarkTest01246_post():
		RESPONSE = ""

		import helpers.separate_request
		scr = helpers.separate_request.request_wrapper(request)
		param = scr.get_safe_value("BenchmarkTest01246")

		import configparser
		
		bar = 'safe!'
		conf96176 = configparser.ConfigParser()
		conf96176.add_section('section96176')
		conf96176.set('section96176', 'keyA-96176', 'a-Value')
		conf96176.set('section96176', 'keyB-96176', param)
		bar = conf96176.get('section96176', 'keyB-96176')

		import flask
		import urllib.parse

		try:
			url = urllib.parse.urlparse(bar)
			if url.netloc not in ['google.com'] or url.scheme != 'https':
				RESPONSE += (
					'Invalid URL.'
				)
				return RESPONSE
		except:
			RESPONSE += (
				'Error parsing URL.'
			)
			return RESPONSE

		return flask.redirect(bar)

		return RESPONSE

