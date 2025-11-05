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

	@app.route('/benchmark/cmdi-00/BenchmarkTest00368', methods=['GET'])
	def BenchmarkTest00368_get():
		return BenchmarkTest00368_post()

	@app.route('/benchmark/cmdi-00/BenchmarkTest00368', methods=['POST'])
	def BenchmarkTest00368_post():
		RESPONSE = ""

		import helpers.separate_request
		
		wrapped = helpers.separate_request.request_wrapper(request)
		param = wrapped.get_form_parameter("BenchmarkTest00368")
		if not param:
			param = ""

		import configparser
		
		bar = 'safe!'
		conf66599 = configparser.ConfigParser()
		conf66599.add_section('section66599')
		conf66599.set('section66599', 'keyA-66599', 'a-Value')
		conf66599.set('section66599', 'keyB-66599', param)
		bar = conf66599.get('section66599', 'keyB-66599')

		import platform
		import subprocess
		import helpers.utils

		argStr = ""
		if platform.system() == "Windows":
			argStr = "cmd.exe /c "
		else:
			argStr = "sh -c "
		argStr += f"echo {bar}"

		try:
			proc = subprocess.run(argStr, shell=True, capture_output=True, encoding="utf-8")

			RESPONSE += (
				helpers.utils.commandOutput(proc)
			)
		except IOError:
			RESPONSE += (
				"Problem executing cmdi - subprocess.run(list) Test Case"
			)

		return RESPONSE

