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

	@app.route('/benchmark/xxe-00/BenchmarkTest00402', methods=['GET'])
	def BenchmarkTest00402_get():
		return BenchmarkTest00402_post()

	@app.route('/benchmark/xxe-00/BenchmarkTest00402', methods=['POST'])
	def BenchmarkTest00402_post():
		RESPONSE = ""

		param = ""
		for name in request.form.keys():
			if "BenchmarkTest00402" in request.form.getlist(name):
				param = name
				break

		map26982 = {}
		map26982['keyA-26982'] = 'a-Value'
		map26982['keyB-26982'] = param
		map26982['keyC'] = 'another-Value'
		bar = map26982['keyB-26982']

		import xml.dom.minidom
		import xml.sax.handler

		try:
			parser = xml.sax.make_parser()
			# all features are disabled by default
			parser.setFeature(xml.sax.handler.feature_external_ges, True)

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

