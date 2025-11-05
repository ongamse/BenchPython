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

	@app.route('/benchmark/hash-00/BenchmarkTest00515', methods=['GET'])
	def BenchmarkTest00515_get():
		return BenchmarkTest00515_post()

	@app.route('/benchmark/hash-00/BenchmarkTest00515', methods=['POST'])
	def BenchmarkTest00515_post():
		RESPONSE = ""

		param = request.headers.get("BenchmarkTest00515")
		if not param:
		    param = ""

		import configparser
		
		bar = 'safe!'
		conf95991 = configparser.ConfigParser()
		conf95991.add_section('section95991')
		conf95991.set('section95991', 'keyA-95991', 'a-Value')
		conf95991.set('section95991', 'keyB-95991', param)
		bar = conf95991.get('section95991', 'keyB-95991')

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

		hash = hashlib.new('sha1')
		hash.update(input)

		result = hash.digest()
		f = open(f'{helpers.utils.TESTFILES_DIR}/passwordFile.txt', 'a')
		f.write(f'hash_value={base64.b64encode(result)}\n')
		RESPONSE += (
			f'Sensitive value \'{helpers.utils.escape_for_html(input.decode('utf-8'))}\' hashed and stored.'
		)
		f.close()

		return RESPONSE

