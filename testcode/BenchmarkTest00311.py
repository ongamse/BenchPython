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

	@app.route('/benchmark/xxe-00/BenchmarkTest00311', methods=['GET'])
	def BenchmarkTest00311_get():
		return BenchmarkTest00311_post()

	@app.route('/benchmark/xxe-00/BenchmarkTest00311', methods=['POST'])
	def BenchmarkTest00311_post():
		RESPONSE = ""

		import helpers.separate_request
		
		wrapped = helpers.separate_request.request_wrapper(request)
		param = wrapped.get_form_parameter("BenchmarkTest00311")
		if not param:
			param = ""

		import configparser
		
		bar = 'safe!'
		conf45571 = configparser.ConfigParser()
		conf45571.add_section('section45571')
		conf45571.set('section45571', 'keyA-45571', 'a-Value')
		conf45571.set('section45571', 'keyB-45571', param)
		bar = conf45571.get('section45571', 'keyB-45571')

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

