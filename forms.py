from wtforms import Form
from wtforms.fields import (
    StringField, IntegerField, PasswordField, DateField, 
    RadioField, SelectField, BooleanField, TextAreaField,
    EmailField, SubmitField
)
# 使用するvalidatorをインポート
# 【リスト5.14】 で「ValidationError」を追加
from wtforms.validators import (
    DataRequired, EqualTo, Length, NumberRange, Email, ValidationError
)
# ==================================================
# Formクラス
# ==================================================
# ユーザー情報クラス
class UserInfoForm(Form):

    # メッセージ：複数行テキスト
    note = TextAreaField('備考: ')
    # ボタン
    submit = SubmitField('送信')

    # ▼▼▼ 【リスト5.14】 ▼▼▼ 
    # カスタムバリデータ
    # 英数字と記号が含まれているかチェックする
    def validate_password(self, password):
        if not (any(c.isalpha() for c in password.data) and \
            any(c.isdigit() for c in password.data) and \
            any(c in '!@#$%^&*()' for c in password.data)):
            raise ValidationError('パスワードには【英数字と記号：!@#$%^&*()】を含める必要があります')
    # ▲▲▲ 【リスト5.14】 ▲▲▲ 
