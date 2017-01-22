from flask_security.forms import RegisterForm,StringField,Required,EqualTo
icodevalue='qwe123456'
class ExtendedRegisterForm(RegisterForm):
    # invitationcode=StringField('invitationcode',[Required('invitatoncode not provided'),EqualTo(icodevalue)])
    invitationcode=StringField('invitationcode',[Required('invitatoncode not provided')])
    def validate(self):
        check_validate= super().validate()
        if not check_validate:
            return False
        if self.invitationcode.data != str(icodevalue):
            self.invitationcode.errors.append('邀请码不正确 请联系管理员拿邀请码')
            return False
        return True


