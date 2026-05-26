##### 기본 정보 불러오기 ####
# Streamlit 패키지 추가
import streamlit as st
# OpenAI 패키지 추가
import openai

##### 기능 구현 함수 #####
def askGpt(prompt, apikey):
    # OpenAI API 클라이언트를 초기화합니다.
    client = openai.OpenAI(api_key=apikey)
    # GPT 모델에 프롬프트를 보내어 응답을 요청합니다.
    response = client.responses.create(
        model="gpt-4.1-nano",   # 첨 앱은 Non-Reasoning 모델로 빠르고 저렴하게
        input=prompt
    )
    # 응답에서 요약된 텍스트를 추출하여 반환합니다.
    return response.output_text

##### 메인 함수 #####
def main():
    st.set_page_config(page_title="요약 프로그램")
    st.header("요약 프로그램")
    st.markdown('-----')

    with st.sidebar:
        openai_apikey = st.text_input(
            label='OPENAI API 키',
            placeholder='Enter Your API Key',
            value='',
            type='password'
        )

    text = st.text_area("요약 할 글을 입력하세요")
    if st.button("요약"):
        # 5차시 4대 원칙 적용한 프롬프트
        prompt = f'''
        # 역할
        너는 한국어 글을 핵심만 간결하게 요약하는 전문가야.
        
        # 규칙
        - 중복 내용은 생략, 다만 중복된 내용은 그만큼 비중을 더 두기
        - 사례·예시보다는 개념·주장 중심으로 요약
        - 3줄의 불릿 포인트 형식
        - 각 줄은 1문장 이내
        
        # 입력 글
        {text}
        '''
        
        if openai_apikey:
            # API 키가 유효한 경우 요약 작업 수행
            st.info(askGpt(prompt, openai_apikey))
        else:
            st.info("API 키를 입력하세요")



if __name__=="__main__":
    main()