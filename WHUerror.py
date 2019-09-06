class WHUError(Exception):
    pass

class UserInfoError(WHUError):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not args:
            self.args = ('用户名/密码错误',)

class VerifyCodeError(WHUError):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not args:
            self.args = ('验证码错误',)
    
class SessionError(WHUError):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not args:
            self.args = ('会话超时，请重新登录',)
    
class ServerError(WHUError):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not args:
            self.args = ('Internal Server Error',)
