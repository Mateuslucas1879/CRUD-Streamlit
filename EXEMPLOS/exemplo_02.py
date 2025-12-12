import streamlit as st
from PIL import  Image,ImageDraw, ImageFont
import os

def aplicar_texto(img_file,texto,fonte_size,color):
    img = Image.open(img_file)
    draw = ImageDraw.Draw(img)
    if os.name == "nt":
        font_path = "arial.ttf"
    else:
        font_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

    font = ImageFont.truetype(font_path, fonte_size)

    iw, ih = img.size
    bbox = draw.textbbox((0, 0), texto, font=font)
    fw = bbox[2] - bbox[0]
    fh = bbox[3] - bbox[1]

    draw.text(
        ((iw - fw) / 2, (ih-fh)/2),
        texto,
        fill=color,
        font=font,
    )
    output_path = "image_bonita.jpg"
    img.save(output_path)
    return output_path

st.title("Marca d'água automática")
image = st.file_uploader('Envie sua imagem',type=['jpeg','jpg','png'])
texto = st.text_input("Texto da marca d'água")
color = st.selectbox('Cor',['black','red','blue','yellow'])
font_size = st.number_input("Tamanho da Fonte", min_value=20, max_value=200, value=60)


if image and texto:
    if st.button('Aplicar',type="primary"):
        output = aplicar_texto(image,texto,font_size,color)
        st.image(output,caption="Resultado")

        with open(output,"rb") as file:
            st.download_button(
                label='Baixar',
                file_name='imagem_editada.jpg',
                data=file,
                mime='image/jpg'

            )