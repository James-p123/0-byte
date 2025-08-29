# -*- coding: utf-8 -*-
# Author: @O-byte

import requests
import json
import lxml 
import httpx
 
 
 
url_home = "https://exam.mshengedu.com/examPC/"


MathJax = {
  tex: {
    inlineMath: [['$', '$'], ['\\(', '\\)'],['\`', '\`']]
  }
};
</script>
<script id="MathJax-script" async
  src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-chtml.js">
</script>

 
for i in range(217853,217867):
    f = open('question'+str(i)+'.html','w')
    f.write('<!DOCTYPE html><html><meta charset="utf-8"><body>')
    counter = 1
    url = url_home + str(i) + '/'
    response = requests.get(url,headers=headers)
    #print(response)
    data = json.loads(response.text)
    problems = data.get('data').get('question')
    for problem in problems:
        html = problem.get('content').get('Body')
        soup = BeautifulSoup(html)
        f.write('<p>'+str(counter)+'.' + soup.p.contents[0]+'</p>')
        counter+=1
        choiceKey = 'A'
        for choice in problem.get('content').get('Options'):
            soup = BeautifulSoup(choice['value'])
            f.write('<p>'+choiceKey + '.' + soup.p.contents[0]+'</p>')
            choiceKey = chr(ord(choiceKey)+1)
    f.write('</body></html>')
    f.close()

