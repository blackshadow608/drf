import os

import pdfkit
from django.http import HttpResponse


def pdf_converter(data, content_type):
    """
    PDF converter. Converts input data to PDF file
    :param data: data object
    :param content_type: type of data object(file, string, url, etc.)
    :return: PDF file object
    """
    wkhtmltopdf_bin = os.environ.get('WKHTMLTOPDF_PATH')
    config = pdfkit.configuration(wkhtmltopdf=wkhtmltopdf_bin)
    options = {'load-error-handling': 'ignore'}
    pdf = pdfkit.PDFKit(data,
                        content_type,
                        configuration=config,
                        options=options).to_pdf()

    return pdf


def prepare_file_response(file):
    """
    Preparing file response with headers
    :param file: file object
    :return: HTTPResponse
    """
    response = HttpResponse(file)
    response['Content-Type'] = 'application/pdf'
    response['Content-disposition'] = 'attachment;filename='
    response['Content-disposition'] += 'out.pdf'
    return response
