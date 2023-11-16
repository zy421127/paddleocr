import streamlit as st
from paddleocr import PaddleOCR
# from PIL import Image
# Paddleocr supports Chinese, English, French, German, Korean and Japanese.
# You can set the parameter `lang` as `ch`, `en`, `french`, `german`, `korean`, `japan`
# to switch the language model in order.
st.title('欢迎进入我的图像空间')
file_uploader = st.file_uploader(label="请您上传一张图片",type=['png', 'jpg', 'jpeg'],help="请您上传一张图片")
if file_uploader is not None:
    print(file_uploader.name)
    st.image(file_uploader, caption="正在识别的图片", use_column_width=True)
    ocr = PaddleOCR(use_angle_cls=True)

    # img_path = 'C:/data/cc.png'
    status = st.status("图像正在扫描识别中，请稍等...")
    result = ocr.ocr(file_uploader.getvalue(), cls=True)
    for idx in range(len(result)):
        res = result[idx]
        for line in res:
            st.write(line[1][0])

    status.update(label="恭喜你，图像识别完成！",state="complete")