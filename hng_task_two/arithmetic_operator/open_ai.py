import openai

def operation_type(stext):
    openai.api_key = 'Enter your secrete key here' #secrete needed here

    response = openai.Completion.create(
      model="text-davinci-002",
      #engine = 'davinci-instruct-beta',
      prompt=stext,
      temperature=0.7,
      max_tokens=256,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0
    ) 
    
    content = response.choices[0].text
    return content
    
