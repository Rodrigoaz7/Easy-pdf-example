# from io import BytesIO
# from django.http import HttpResponse
# from django.template.loader import get_template
# import xhtml2pdf.pisa as pisa
from easy_pdf.views import PDFTemplateView

# def pdf_generation(request):
# 	template = get_template('templates/index.html')
# 	html = template.render()
# 	response = BytesIO()
# 	pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), response)
# 	if not pdf.err:
# 		return HttpResponse(response.getvalue(), content_type='application/pdf')
# 	else:
# 		return HttpResponse("Error Rendering PDF", status=400)

class HelloPDFView(PDFTemplateView):
    template_name = 'templates/index.html'

    def get_context_data(self, *args, **kwargs):
    	return super(HelloPDFView, self).get_context_data(pagesize="A4 landscape",**kwargs)