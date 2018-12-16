#emailモジュールのインポート
from email import message

#smtp通信のモジュールをインポート
import smtplib

#smptのホストを設定
smtp_host = 'smtp.gmail.com'

#smptのポート番号を指定
smtp_port = 465

#誰から送信するか設定
from_email = 'exsample@gmail.com'

#誰に送信するか設定
to_email = 'exsample@xxx.com'

#gmailのIDとパスワード
username = 'exsample@gmail.com'
passwd = 'exsample'

#送信の確認
send_msg = input("メールを送信します。本文を入力してください。")
print('送信メッセージ：{}'.format(send_msg))

accepto = int(input("送信する：０　送信しない：１ :"))

if accepto == 0:
    #送信メッセージオブジェクト生成
    msg = message.EmailMessage()
    #本文設定
    msg.set_content(send_msg)
    #件名設定
    msg['Subject'] = 'Test'
    #送信元設定
    msg['From'] = from_email
    #送信先設定
    msg['To'] = to_email

    #smpt通信オブジェクト生成
    server = smtplib.SMTP_SSL(smtp_host, smtp_port)
    #smptに事前に挨拶
    server.ehlo()
    #グーグルにログイン
    server.login(username, passwd)
    #メッセージの送信
    server.send_message(msg)
    #切断
    server.quit()

    print('送信完了')
else:
    print('送信中止')
