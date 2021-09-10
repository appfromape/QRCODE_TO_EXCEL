from flask import Flask, request, render_template, send_file
from model import RegForm
from flask_bootstrap import Bootstrap
import openpyxl
import qrcode
from openpyxl.drawing.image import Image
import os

app = Flask(__name__)
app.config.from_mapping(SECRET_KEY=b'\xd6\x04\xbdj\xfe\xed$c\x1e@\xad\x0f\x13,@G')
Bootstrap(app)

@app.route('/', methods=['GET', 'POST'])
def registration():
    form = RegForm(request.form)
    if request.method == 'POST' and form.validate_on_submit():
        xfile = openpyxl.load_workbook('result.xlsx')
        sheet = xfile.get_sheet_by_name('result')
        sheet.title = form.store_name.data
        sheet['C1'] = form.store_name.data

        img_one = qrcode.make(form.equipment_code_one.data)
        img_one.save("img1.png")
        img = Image("img1.png")
        img.height = 140
        img.width = 140
        sheet['A3'] = form.equipment_number_one.data
        sheet['B3'] = form.equipment_code_one.data
        sheet['C3'] = form.equipment_number_one.data
        sheet['D3'] = form.equipment_money_one.data
        sheet.add_image(img, 'E3')
        
        img_two = qrcode.make(form.equipment_code_two.data)
        img_two.save("img2.png")
        img = Image("img2.png")
        img.height = 140
        img.width = 140
        sheet['A4'] = form.equipment_number_two.data
        sheet['B4'] = form.equipment_code_two.data
        sheet['C4'] = form.equipment_number_two.data
        sheet['D4'] = form.equipment_money_two.data
        sheet.add_image(img, 'E4')

        img_three = qrcode.make(form.equipment_code_three.data)
        img_three.save("img3.png")
        img = Image("img3.png")
        img.height = 140
        img.width = 140
        sheet['A5'] = form.equipment_number_three.data
        sheet['B5'] = form.equipment_code_three.data
        sheet['C5'] = form.equipment_number_three.data
        sheet['D5'] = form.equipment_money_three.data
        sheet.add_image(img, 'E5')

        img_four = qrcode.make(form.equipment_code_four.data)
        img_four.save("img4.png")
        img = Image("img4.png")
        img.height = 140
        img.width = 140
        sheet['A6'] = form.equipment_number_four.data
        sheet['B6'] = form.equipment_code_four.data
        sheet['C6'] = form.equipment_number_four.data
        sheet['D6'] = form.equipment_money_four.data
        sheet.add_image(img, 'E6')

        xfile.save(f'{form.store_name.data}.xlsx')

        return send_file(f'{form.store_name.data}.xlsx', as_attachment=True), os.remove(f'{form.store_name.data}.xlsx')
    return render_template('registration.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
