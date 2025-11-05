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

	@app.route('/benchmark/cmdi-00/BenchmarkTest00555', methods=['GET'])
	def BenchmarkTest00555_get():
		return BenchmarkTest00555_post()

	@app.route('/benchmark/cmdi-00/BenchmarkTest00555', methods=['POST'])
	def BenchmarkTest00555_post():
		RESPONSE = ""

		param = request.headers.get("BenchmarkTest00555")
		if not param:
		    param = ""

		num = 106
		
		bar = "This should never happen" if (7*42) - num > 200 else param

		import os
		import subprocess
		import helpers.utils

		argList = []
		if "Windows" in os.name:
			argList.append("cmd.exe")
			argList.append("-c")
		else:
			argList.append("sh")
			argList.append("-c")
		argList.append(f"echo {bar}")

		proc = subprocess.run(argList, capture_output=True, encoding="utf-8")
		RESPONSE += (
			helpers.utils.commandOutput(proc)
		)

		return RESPONSE

