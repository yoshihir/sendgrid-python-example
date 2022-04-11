# sendgrid-python-example

本コードは[SendGrid公式pythonライブラリ](https://github.com/sendgrid/sendgrid-python)の利用サンプルです。

## 使い方

```bash
cd sendgrid-python-example
cp .env.example .env
# .envファイルを編集してください

export PIPENV_VENV_IN_PROJECT=1

pipenv install
pipenv shell
python simple/simple.py
```

## .envファイルの編集
.envファイルは以下のような内容になっています。

```bash
API_KEY=api_key
TOS=you@youremail.com,friend1@friendemail.com,friend2@friendemail.com
FROM=you@youremail.com
```
API_KEY:SendGridの[API Key](https://sendgrid.kke.co.jp/docs/User_Manual_JP/Settings/api_keys.html)を指定してください。  
TOS:宛先をカンマ区切りで指定してください。  
FROM:送信元アドレスを指定してください。  

## sendgridの制限
[API概要](https://sendgrid.kke.co.jp/docs/API_Reference/Web_API_v3/Mail/index.html)
