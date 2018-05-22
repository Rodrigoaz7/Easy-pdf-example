from easy_pdf.views import PDFTemplateView
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa


class HelloPDFView(PDFTemplateView):
	template_name = 'templates/index.html'

	def render_to_pdf(self, template_src):
		template = get_template(template_src)
		html  = template.render()
		result = BytesIO()
		pdf = pisa.pisaDocument(BytesIO(html.encode("utf-8")), result)

		if not pdf.err:
			return HttpResponse(result.getvalue(), content_type='application/pdf')
		return None

	def get_context_data(self, *args, **kwargs):
		return super(HelloPDFView, self).get_context_data(
			pagesize="A4 landscape",
			nome_orgao="",
			uf="",
			num_convenio="",
			tipo="",
			num_processo="",
			cnpj="",
			num_parcela="",
			exercicio="",
			#Proximos serao instancias
			num_ordem="",
			cpf_or_nome="",
			licitacao="",
			tipo_documento="",
			num_documento="",
			data_documento="",
			num_pagamento="",
			data_pagamento="",
			nat_despesa_pagamento="",
			valor_pagamento="",
			total="",
			total_acumulado="",
			**kwargs
		)


		pdf = self.render_to_pdf('templates/index.html')
		if pdf:
			response = HttpResponse(pdf, content_type='application/pdf')
			filename = "Invoice_%s.pdf" %("12341231")
			content = "inline; filename='%s'" %(filename)
			download = request.GET.get("download")
			if download:
				content = "attachment; filename='%s'" %(filename)
			response['Content-Disposition'] = content
			return response
		return HttpResponse("Not found")