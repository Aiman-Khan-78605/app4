from fpdf import FPDF
import pandas as pd

df=pd.read_csv('topics.csv')
pdf=FPDF(orientation="P",unit="mm",format='A4')
pdf.set_auto_page_break(auto=False,margin=0)

for index,row in df.iterrows():

    pdf.add_page()
    topic=row['Topic']
    pdf.set_font(family='Times',style='B',size=15)
    pdf.cell(w=0,h=15,txt=topic,align='L',ln=1)
    for y in range(20,270,10):
         pdf.line(10,y,200,y)

    pdf.ln(260)
    pdf.set_font(family='Times', style='I', size=8)
    pdf.set_text_color(180,180,180)
    pdf.cell(w=0, h=15, txt=topic, align='R', ln=1)




    for j in range(int(row['Pages']-1)):
        pdf.add_page()
        pdf.ln(272)
        pdf.set_font(family='Times', style='I', size=8)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=15, txt=topic, align='R', ln=1)
        for y in range(20, 270, 10):
            pdf.line(10, y, 200, y)

pdf.output('output_lined.pdf')