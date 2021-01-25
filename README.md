# linebot_test

- ลงทะเบียน line developer ก่อน https://developers.line.biz/en/

- Products > Messaging API > Start Now

# What is Webhook?

Linebot มันไม่ใช่โปรแกรมใน Line แต่ถ้ารับเมสเสจแล้ว ส่ง request ไปโปรแกรมที่อื่นที่กำหนดไว้และได้ response 

ซึ่งเรียกว่า webhook (API ชนิดหนึ่ง)

![webhook](https://user-images.githubusercontent.com/44984892/105693161-fe55bc80-5f31-11eb-8037-d9ab7904d058.png)

https://developers.line.biz/en/docs/messaging-api/overview/

request และ response ที่แลกกันคือ **POST request** ซึ่งหน้าตาเป็น json แบบนี้

- Line -> Program

~~~
{
	"destination": "1654034294",
	"events": [
		{
			"replyToken": "0f3779fba3b349968c5d07db31eab56f",
			"type": "message",
			"mode": "active",
			"timestamp": 1462629479859,
			"source": {
				"type": "user",
				"userId": "Ua5a81fcab991a3f24e44ae4bfc89a"
			},
			"message": {
				"id": "325708",
				"type": "text",
				"text": "Hello, world"
			}
		}
	]
}
~~~

- Program -> Line

~~~
curl -v -X POST https://api.line.me/v2/bot/message/reply \
-H 'Content-Type: application/json' \
-H 'Authorization: Bearer {channel access token}' \
-d '{
    "replyToken":"nHuyWiB7yP5Zw52FIkcQobQuGDXCTA",
    "messages":[
        {
            "type":"text",
            "text":"Hello, user"
        },
        {
            "type":"text",
            "text":"May I help you?"
        }
    ]
}'
~~~

แต่มี SDK (software development kit) สำหรับ Python ด้วย จึงไม่ต้องเขียนเอง (import library แล้วรับ/ส่งได้ง่าย)
