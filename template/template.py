from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import *
import os
from dotenv import load_dotenv

if __name__ == '__main__':
    load_dotenv()

    # .envから環境変数を読み込む
    sendgrid_api_key = os.environ.get('API_KEY')
    from_address = os.environ.get('FROM')
    to_list = os.environ.get('TOS').split(',')
    template_id = os.environ.get('TEMPLATE_ID')

    # メッセージの構築
    message = Mail(
        to_emails=to_list,  # 1000件まで
        from_email=From(from_address, '送信者名'),
    )
    # templateを指定
    message.template_id = template_id
    message.dynamic_template_data = {
        'emailAddress': 'test@example.com'
    }

    # メール送信を行い、レスポンスを表示
    sendgrid_client = SendGridAPIClient(sendgrid_api_key)
    response = sendgrid_client.send(message=message)
    print(response.status_code)
    print(response.body)
    print(response.headers)
