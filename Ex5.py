import json

json_text = '''{
  "messages": [
    {
      "message": "This is the first message",
      "timestamp": "2021-06-04 16:40:53"
    },
    {
      "message": "And this is a second message",
      "timestamp": "2021-06-04 16:41:01"
    }
  ]
}'''
obj = json.loads(json_text)

main_key = "messages"

sub_key_1 = '''{
      "message": "This is the first message",
      "timestamp": "2021-06-04 16:40:53"
    }'''

sub_key_2 = '''{
      "message": "And this is a second message",
      "timestamp": "2021-06-04 16:41:01"
    }'''

obj_message_1 = '{message": "This is the first message}'

obj_message_2 = '{message: "And this is a second message"}'

sub_time_1 = '{timestamp": "2021-06-04 16:40:53}'

sub_time_2 = '{timestamp": "2021-06-04 16:41:01}'

print(obj_message_2)

