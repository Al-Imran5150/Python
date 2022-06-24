qna = {
    'Is anyone available here?':  'Yes, available.',
    'How much time do you provide service?': '24 hours, 7 days.',
    'Do you have any weekly holiday?' : 'No.',
    'What kind of service can you provide us?': 'Offline and online service also.',
    'Do you have any regional limitations?' : 'No.',
    'What is the payment method of online delivery?' : 'Cash on delivery.',
    'Can you show some sample of product?' : 'Yes, Ofcourse.'
}

data=open('demo.txt','r')
data=data.read().split(':')

print(data[1])
while True:
    
    ques = input()
    print(qna[ques])