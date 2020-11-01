while True:
 # nghe
 import  sppech_recognition
 import pyttsx3
 from datetime import date
 robot_ear = speech_recognition.Recognizer()
 robot_mouth = pyttsx3.init()
 robot_brain = ''
 with  speech_recognition.Microphone() as mic:
      print('Robot: I am listening')
      audio = robot_ear.listen(mic)
 print('Robot: ...')
 try:
    you = robot_ear.recognize_google(audio)
 except:
   you = ''
 print('You: ' + you)

 # hieu
 if you == '':
     robot_brain = 'I can not hear you, try again'
 elif 'today'in you:
     today = date.today()
     robot_brain = today.strftime('%B &d, %Y')
 elif 'hello' in you:
     robot_brain = 'Hello '
 elif 'bye' in you:
    print(' Robot: ' + robot_brain)
    robot_mouth.say(robot_brain)
    robot_mouth.runAndWait()
    break
 else:
     robot_brain = 'I am fine thank you. And you ?'
 print('Robot: ' + robot_brain)

 # noi

 robot_mouth.say(robot_brain)
 robot_mouth.runAndWait()