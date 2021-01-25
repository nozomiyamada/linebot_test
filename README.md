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

# What is Front End / Back End ?

website ปัจจุบันหน้าตาเป็นแบบนี้

![front_end](https://user-images.githubusercontent.com/44984892/105697436-21cf3600-5f37-11eb-8898-148b062e4a89.png)

back end = web/application/database server อาจจะเป็นอันเดียวกันก็ได้ ยังไงต้องมีโปรแกรมเบื้อนหลัง ซึ่งเขียนโดยภาษาอะไรก็ได้

Python มี Framework ดังสองอย่าง ได้แก่ `Django` กับ `Flask` ถ้าทำโปรแกรมเล็กๆ Flask น่าจะง่ายกว่า

ทีนี้ ไม่ต้องทำ frontend เพราะไม่มี website แค่ทำ backend ที่จัดการข้อความก็พอ

# What is virtual environment?

Python นั้นมีอยู่ในเครื่องแล้ว แต่ติดตั้ง package มาเยอะแยะ ซึ่งส่วนใหญ่ไม่จำเป็น

เพราะฉะนั้น ควรสร้างสิ่งแวดล้อมใหม่ที่ไม่เกี่ยวกับ python ที่มีอยู่แล้ว จะได้ทดสอบโปรแกรมง่าย

clone เสร็จแล้ว สร้าง virtual environment ใน repository อย่างนี้ (`.` แปลว่า hidden file ซึ่งไม่ใส่ก็ได้ แต่ปกติใส่)

~~~
$ python3 -m venv .venv
~~~

แต่อันนี้สร้าง environment เฉยๆ ต้องเลือกใช้อันนี้

~~~
$ source .venv/bin/activate
(.venv) $
~~~

ใน environment นี้ ยังไม่มี package อะไรเลย ก็เลยต้อง install ใหม่จากไฟล์

~~~
(.venv) $ pip install -r requirements.txt
~~~

กรณี install เพิ่มเติม ต้องเขียนเป็นไฟล์ว่าใช้อะไร เพื่อติดตั้งใน server

~~~
(.venv) $ pip freeze > requirements.txt
~~~

# What is environment variable?

ตัวแปลที่เซฟไว้ใน OS ซึ่งสามาระอ้างอิงได้โดย `os.environ['<ชื่อตัวแปล>']`

ใช้เพื่อโหลด ไอดี รหัด เป็นต้น ซึ่งไม่ควรจะเขียนลงในโปรแกรม (แต่ที่นี่เป็น private repository คนอื่นก็มองไม่เห็น)

ถ้าใช้ library `dotenv` สามารถโหลดจากไฟล์ `.env` ได้
