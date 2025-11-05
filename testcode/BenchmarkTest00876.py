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

	@app.route('/benchmark/cmdi-00/BenchmarkTest00876', methods=['GET'])
	def BenchmarkTest00876_get():
		return BenchmarkTest00876_post()

	@app.route('/benchmark/cmdi-00/BenchmarkTest00876', methods=['POST'])
	def BenchmarkTest00876_post():
		RESPONSE = ""

		values = request.args.getlist("BenchmarkTest00876")
		param = ""
		if values:
			param = values[0]

		import configparser
		
		bar = 'safe!'
		conf8113 = configparser.ConfigParser()
		conf8113.add_section('section8113')
		conf8113.set('section8113', 'keyA-8113', 'a_Value')
		conf8113.set('section8113', 'keyB-8113', param)
		bar = conf8113.get('section8113', 'keyA-8113')

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

