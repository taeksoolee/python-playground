# -*- coding:utf-8 -*-
 
import smtplib
from email.mime.text import MIMEText

# 세션 생성
s = smtplib.SMTP('smtp.gmail.com', 587)

# 세션 생성
s = smtplib.SMTP('smtp.gmail.com', 587)
# TLS 보안 시작
s.starttls()
# 로그인 인증
s.login('lts170238@gmail.com', 'nrkpgpkzcstiqpfw')

# 보낼 메시지 설정
msg = MIMEText('내용 : 본문내용 테스트입니다.')
msg['Subject'] = '제목 : 메일 보내기 테스트입니다.'


# 메일 보내기
s.sendmail("lts170238@gmail.com", "9119k@naver.com", msg.as_string())

# 세션 종료
s.quit()


