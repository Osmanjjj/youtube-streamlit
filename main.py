import streamlit as st
import time

st.title('Streamlit超入門')
st.write('プログレスバーの表示')
latest_iteration = st.empty()
bar = st.progress(0)
# カラムの作成
left_column, right_column = st.columns(2)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.01)

# その他のコードはそのままにしてください
button = left_column.button('右からみに文字を表示')
if button:
    right_column.write('ここは右コラム')

expander1 = st.expander('問い合わせ')
expander1.write('お問い合わせ1の回答')
expander2 = st.expander('問い合わせ')
expander2.write('お問い合わせ2の回答')
expander3 = st.expander('問い合わせ')
expander3.write('お問い合わせ3の回答')
# if button:
#     right_column.write('ここは右コラム')

# 画像の表示（コメントを外して使用）
# if st.checkbox('show image'):
#     img = Image.open('munchkin045.jpg')
#     st.image(img, caption='猫たん', use_column_width=True)

# サイドバーの入力
text = st.sidebar.text_input('あなたの趣味を教えてください')
condition = st.sidebar.slider('あなたの今の調子は？', 0, 100, 50)

'あなたの趣味:', text
'コンディション:', condition
