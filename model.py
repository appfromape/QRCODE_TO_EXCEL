from wtforms import SubmitField, BooleanField, StringField, PasswordField, validators
from flask_wtf import Form

class RegForm(Form):
    store_name = StringField('店名 (ex:華盛頓自助洗)')

    equipment_number_one = StringField('設備 1 (ex:洗1)')
    equipment_code_one = StringField('設備 1 代號')
    equipment_time_one = StringField('設備 1 使用時間(分鐘)')
    equipment_money_one = StringField('設備 1 洗衣價格(元)')

    equipment_number_two = StringField('設備 2 (ex:洗2)')
    equipment_code_two = StringField('設備 2 代號')
    equipment_time_two = StringField('設備 2 使用時間(分鐘)')
    equipment_money_two = StringField('設備 2 洗衣價格(元)')

    equipment_number_three = StringField('設備 3 (ex:烘3)')
    equipment_code_three = StringField('設備 3 代號')
    equipment_time_three = StringField('設備 3 使用時間(分鐘)')
    equipment_money_three = StringField('設備 3 洗衣價格(元)')

    equipment_number_four = StringField('設備 4 (ex:烘4)')
    equipment_code_four = StringField('設備 4 代號')
    equipment_time_four = StringField('設備 4 使用時間(分鐘)')
    equipment_money_four = StringField('設備 4 洗衣價格(元)')

    submit = SubmitField('輸出 EXCEL')