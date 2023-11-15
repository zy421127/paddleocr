import streamlit as st
from paddleocr import PaddleOCR
# Paddleocr supports Chinese, English, French, German, Korean and Japanese.
# You can set the parameter `lang` as `ch`, `en`, `french`, `german`, `korean`, `japan`
# to switch the language model in order.
st.title('欢迎进入图像识别空间')
ocr = PaddleOCR(use_angle_cls=True)
params = st.experimental_get_query_params()
if len(params) == 0:
    st.toast('请在URL中输入参数，参数名为image!')
    st.stop()
print(params)
# img_path = 'C:/data/cc.png'
status = st.status("图像正在扫描识别中，请稍等...")
result = ocr.ocr(params.get('image')[0], cls=True)
for idx in range(len(result)):
    res = result[idx]
    for line in res:
        st.write(line[1][0])

status.update(label="恭喜你，图像识别完成！",state="complete")