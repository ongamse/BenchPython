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

	@app.route('/benchmark/xxe-00/BenchmarkTest00483', methods=['GET'])
	def BenchmarkTest00483_get():
		return BenchmarkTest00483_post()

	@app.route('/benchmark/xxe-00/BenchmarkTest00483', methods=['POST'])
	def BenchmarkTest00483_post():
		RESPONSE = ""

		param = request.headers.get("BenchmarkTest00483")
		if not param:
		    param = ""

		map46512 = {}
		map46512['keyA-46512'] = 'a-Value'
		map46512['keyB-46512'] = param
		map46512['keyC'] = 'another-Value'
		bar = "safe!"
		bar = map46512['keyB-46512']
		bar = map46512['keyA-46512']

		import xml.dom.minidom
		import xml.sax.handler

		try:
			parser = xml.sax.make_parser()
			# all features are disabled by default

			doc = xml.dom.minidom.parseString(bar, parser)

			out = ''
			processing = [doc.documentElement]
			while processing:
				e = processing.pop(0)
				if e.nodeType == xml.dom.Node.TEXT_NODE:
					out += e.data
				else:
					processing[:0] = e.childNodes

			RESPONSE += (
				f'Your XML doc results are: <br>{escape_for_html(out)}'
			)
		except:
			RESPONSE += (
				f'There was an error reading your XML doc:<br>{escape_for_html(bar)}'
			)

		return RESPONSE

