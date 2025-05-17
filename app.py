# --- 必要なライブラリ ---
import os
from dotenv import load_dotenv
import streamlit as st
from langchain_openai import ChatOpenAI

# --- 環境変数読み込み ---
load_dotenv()

# --- LLMの初期化 ---
llm = ChatOpenAI(model_name="gpt-3.5-turbo")

# --- 条件分岐 ---
def get_llm_response(expert, user_input):
    if expert == "栄養士":
        system_message = "あなたは優秀な栄養士です。相手の健康を気遣い、分かりやすく丁寧にアドバイスしてください。"
    elif expert == "メンタルトレーナー":
        system_message = "あなたは一流のメンタルトレーナーです。相手の心に寄り添い、前向きな声がけをしてください。"
    else:
        system_message = "あなたは親切なアシスタントです。"

    # LangChainのメッセージテンプレート作成
    from langchain.schema import SystemMessage, HumanMessage

    messages = [
        SystemMessage(content=system_message),
        HumanMessage(content=user_input)
    ]

    return llm(messages)

# --- Streamlit UI ---
st.markdown("このアプリでは、選んだ専門家に相談ができます。内容を入力して送信してください。")

selected_item = st.radio(
    "以下の専門家からお選びください",
    ["栄養士", "メンタルトレーナー"]
)

user_input = st.text_input("相談内容を入力してください")

if st.button("送信"):
    response = get_llm_response(selected_item, user_input)
    st.write(response.content)