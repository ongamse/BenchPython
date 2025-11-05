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

	@app.route('/benchmark/hash-01/BenchmarkTest01060', methods=['GET'])
	def BenchmarkTest01060_get():
		return BenchmarkTest01060_post()

	@app.route('/benchmark/hash-01/BenchmarkTest01060', methods=['POST'])
	def BenchmarkTest01060_post():
		RESPONSE = ""

		import urllib.parse
		
		query_string = request.query_string.decode('utf-8')
		paramLoc = query_string.find("BenchmarkTest01060" + '=')
		if paramLoc == -1:
			return f"request.query_string did not contain expected parameter \'{"BenchmarkTest01060"}\'."
		param = query_string[paramLoc + len("BenchmarkTest01060") + 1:]
		ampLoc = param.find('&')
		if ampLoc != -1:
			param = param[:ampLoc]
		
		param = urllib.parse.unquote_plus(param)

		map28601 = {}
		map28601['keyA-28601'] = 'a-Value'
		map28601['keyB-28601'] = param
		map28601['keyC'] = 'another-Value'
		bar = map28601['keyB-28601']

		import hashlib, base64
		import io, helpers.utils

		input = ''
		if isinstance(bar, str):
			input = bar.encode('utf-8')
		elif isinstance(bar, io.IOBase):
			input = bar.read(1000)

		if len(input) == 0:
			RESPONSE += (
				'Cannot generate hash: Input was empty.'
			)
			return RESPONSE

		hash = hashlib.sha512()
		hash.update(input)

		result = hash.digest()
		f = open(f'{helpers.utils.TESTFILES_DIR}/passwordFile.txt', 'a')
		f.write(f'hash_value={base64.b64encode(result)}\n')
		RESPONSE += (
			f'Sensitive value \'{helpers.utils.escape_for_html(input.decode('utf-8'))}\' hashed and stored.'
		)
		f.close()

		return RESPONSE

