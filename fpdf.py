from reportlab.lib.pagesizes import letter
import os
import datetime


def pdf():
    try:
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'form.pdf')
        os.remove(path)
    except FileNotFoundError:
        pass
    now = datetime.datetime.now()
    from reportlab.pdfgen import canvas
    canvas = canvas.Canvas("form.pdf", pagesize=letter)
    canvas.setLineWidth(.3)
    canvas.setFont('Helvetica', 12)
    canvas.drawString(450, 50, 'CREATED BY SOLARIS')
    canvas.drawString(500, 750, "{day}/{month}/{year}".format(day=now.day, month=now.month, year=now.year))
    canvas.line(480, 747, 580, 747)
    canvas.setFont('Helvetica', 18)
    canvas.drawString(225, 725, 'Performance metric')
    canvas.setFont('Helvetica', 12)
    canvas.drawString(50, 670, 'Information:')
    canvas.setFont('Helvetica', 11)
    canvas.drawString(70, 630, '- This data is based on Solaris algorithm')
    canvas.drawString(70, 600, '- Frequency - 1 FPS')
    canvas.drawInlineImage('dio.png', 80, 250, height=270, width=480)
    canvas.save()
    return None
