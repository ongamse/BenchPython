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

	@app.route('/benchmark/hash-00/BenchmarkTest00620', methods=['GET'])
	def BenchmarkTest00620_get():
		return BenchmarkTest00620_post()

	@app.route('/benchmark/hash-00/BenchmarkTest00620', methods=['POST'])
	def BenchmarkTest00620_post():
		RESPONSE = ""

		param = ""
		headers = request.headers.getlist("BenchmarkTest00620")
		
		if headers:
			param = headers[0]

		import configparser
		
		bar = 'safe!'
		conf68524 = configparser.ConfigParser()
		conf68524.add_section('section68524')
		conf68524.set('section68524', 'keyA-68524', 'a_Value')
		conf68524.set('section68524', 'keyB-68524', param)
		bar = conf68524.get('section68524', 'keyA-68524')

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

		hash = hashlib.md5()
		hash.update(input)

		result = hash.digest()
		f = open(f'{helpers.utils.TESTFILES_DIR}/passwordFile.txt', 'a')
		f.write(f'hash_value={base64.b64encode(result)}\n')
		RESPONSE += (
			f'Sensitive value \'{helpers.utils.escape_for_html(input.decode('utf-8'))}\' hashed and stored.'
		)
		f.close()

		return RESPONSE

