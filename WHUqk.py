import re
import threading
from hashlib import md5
from tkinter.messagebox import showerror, showinfo
from urllib.parse import quote, unquote

import requests as rqs
from bs4 import BeautifulSoup

from WHUerror import *

main_url = 'http://bkjw.whu.edu.cn'

index_url = main_url+'/stu/stu_index.jsp'
login_url = main_url+'/servlet/Login'
verify_code_url = main_url+'/servlet/GenImg'
course_post_url = main_url+'/servlet/ProcessApply?applyType={type}&studentNum={stu_id}'

courses_dict = {
    'pub': [
        'pub',
        main_url+'/stu/choose_PubLsn_list.jsp?keyword={course_name}',
        main_url+'/stu/choose_Publsn_Apply.jsp',
    ],
    'pub_required': [
        'pub_required',
        main_url+'/stu/choose_PubRequiredLsn_list.jsp?keyword={course_id}',
        main_url+'/stu/choose_pubRequiredLesson_apply.jsp',
    ],
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Host': 'bkjw.whu.edu.cn',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
}

login_headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Content-Length': '64',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Host': 'bkjw.whu.edu.cn',
    'Origin': 'http://bkjw.whu.edu.cn',
    # 'Referer': 'http://bkjw.whu.edu.cn',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
}

course_post_headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Host': 'bkjw.whu.edu.cn',
    'Origin': 'http://bkjw.whu.edu.cn',
    # 'Referer': 'http://bkjw.whu.edu.cn/stu/choose_pubRequiredLesson_apply.jsp',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
}


class WHU:
    def __init__(self, stu_id, pwd):
        self.__is_login = False
        self.stu_id = str(stu_id)
        self.pwd = md5(str(pwd).encode('utf-8')).hexdigest()
        self.session = rqs.Session()
        self.session.headers = headers

    def __errorDetector(self, response):
        assert response.__class__ == rqs.models.Response
        try:
            if str(response.status_code).startswith('5'):
                raise ServerError
            elif str(response.status_code).startswith('4'):
                raise WHUError(str(response.status_code))
            else:
                soup = BeautifulSoup(
                    response.content.decode('gbk'), 'html5lib')
                error = soup.find('font', {'color': 'red'})
                if error:
                    error_text = error.getText()
                    if error_text == '用户名/密码错误':
                        raise UserInfoError
                    elif error_text == '验证码错误':
                        raise VerifyCodeError
                    elif error_text == '会话超时，请重新登录':
                        raise SessionError
        except WHUError:
            self.__is_login = False
            raise

    def is_login(self):
        return self.__is_login

    def loadVerifyCodeImg(self, filename='verify_code.jpg'):
        codeRes = self.session.get(verify_code_url)
        if str(codeRes.status_code).startswith('5'):
            raise ServerError

        with open(filename, 'wb') as img:
            img.write(codeRes.content)
        # print('验证码获取成功')
        return True

    def _login(self, code):
        login_data = {}

        if not self.stu_id or not self.pwd:
            raise UserInfoError

        login_data['id'] = self.stu_id
        login_data['pwd'] = self.pwd
        login_data['xdvfb'] = code

        if not self.__is_login:
            loginRes = self.session.post(
                url=login_url, data=login_data, headers=login_headers)

            self.__errorDetector(loginRes)

            login_html = loginRes.content.decode('gbk')
            tokens = re.findall(
                r'csrftoken=([0-9a-z]{8}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{12})', login_html)
            self.csrftoken = tokens[0]
            self.__is_login = True
            # print('登录成功')
            return True

    def _qureyCourses(self, course_type, id_to_name):
        assert course_type in courses_dict.keys()

        result = {}

        if course_type == 'pub':
            for item in id_to_name.items():
                qureyRes = self.session.get(
                    url=courses_dict[course_type][1].format(course_name=quote(item[1], encoding='gbk')))
                self.__errorDetector(qureyRes)

                soup = BeautifulSoup(
                    qureyRes.content.decode('gbk'), 'html5lib')
                all_list = soup.find_all('tr')

                left_num = -1
                for i in all_list:
                    try:
                        if i.input.attrs['id'].strip(' ') == item[0]:
                            left_num = i.find(
                                'font', {'color': '#FF0000'}).getText()
                            break
                    except AttributeError:
                        continue
                result[item[0]] = left_num

        elif course_type == 'pub_required':
            for item in id_to_name.items():
                qureyRes = self.session.get(
                    url=courses_dict[course_type][1].format(course_id=item[0]))
                self.__errorDetector(qureyRes)

                soup = BeautifulSoup(
                    qureyRes.content.decode('gbk'), 'html5lib')
                left_num = -1
                left_num = soup.find('font', {'color': '#FF0000'}).getText()
                result[item[0]] = left_num

        return result

    def _selectCourses(self, course_type, courses_id):
        assert course_type in courses_dict.keys()

        course_post_data = {}

        course_post_data['apply'] = set(courses_id)
        course_post_data['csrftoken'] = self.csrftoken

        selectRes = self.session.post(url=course_post_url.format(type=courses_dict[course_type][0], stu_id=self.stu_id),
                                      data=course_post_data, headers=course_post_headers)
        self.__errorDetector(selectRes)
        # print('提交成功')
        return True

    def setCourses(self, course_type, courses_id):
        assert course_type in courses_dict.keys()

        self.course_type = course_type
        self.courses_id = courses_id

    def setVerifyCode(self, code):
        self.verify_code = code

    def autoSelect(self):
        try:
            self._login(self.verify_code)
            self._selectCourses(self.course_type, self.courses_id)
            showinfo('Info', '提交成功')
        except WHUError as error:
            showerror('Error', error)

    def startThread(self, name=None):
        selectThread = threading.Thread(target=self.autoSelect, name=name)
        selectThread.start()
