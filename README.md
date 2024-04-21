## make_trans.py


## 설치
- python 3.11.9 로만 테스트 해보았음.
- ffmpeg 가  설치되어 있어야 함.
- openapi key 를 받아서 .env 에 OPENAI_API_KEY 로 설정해야 함.
```
pip install uv
uv pip install -r requirements.txt
./make_trans.py
```

## 사용법
- src 에 wav 파일을 추가한다.
- make_trans.py 를 실행한다.
- txt 파일의 녹취 내용을 확인한다.
- txt 를 합쳐서 ChatGPT 등의 LLM 에 첨부로 사용하고 다음의 프롬프트를 사용한다.
```
너는 개발자를 멘토링하는 멘토야. 
첨부된 파일은 멘토링을 한 녹취내역이야. 
첨부된 파일을 가지고 멘토링 보고서를 작성해야해.
첨부된 파일을 처음부터 끝까지 읽어보고 분활해서 이해한후에 보고서에 들어갈 내용을 요약해.
보고서를 읽는 사람은 개발에 대해서 잘 모르는 사람임을 기억하고 작성해야해.
최소 100자 이상으로 작성해야해.
출력내용은 멘토링 보고서에 들어갈 내용만 적어줘서 내가 바로 제출용으로 복사가 가능하도록 codeblock 으로 만들어줘.
```
