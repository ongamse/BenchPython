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

	@app.route('/benchmark/intoverflow-00/BenchmarkTest01236', methods=['GET'])
	def BenchmarkTest01236_get():
		return BenchmarkTest01236_post()

	@app.route('/benchmark/intoverflow-00/BenchmarkTest01236', methods=['POST'])
	def BenchmarkTest01236_post():
		RESPONSE = ""

		import helpers.separate_request
		scr = helpers.separate_request.request_wrapper(request)
		param = scr.get_safe_value("BenchmarkTest01236")

		import configparser
		
		bar = 'safe!'
		conf58555 = configparser.ConfigParser()
		conf58555.add_section('section58555')
		conf58555.set('section58555', 'keyA-58555', 'a-Value')
		conf58555.set('section58555', 'keyB-58555', param)
		bar = conf58555.get('section58555', 'keyB-58555')

		import re

		regex = r'(abc)*(bcd)+'

		if re.match(regex, bar) is not None:
			RESPONSE += (
				'String matches!'
			)
		else:
			RESPONSE += (
				'String does not match.'
			)

		return RESPONSE

