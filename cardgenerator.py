# coding: utf-8
from nider.core import Font
from nider.core import Outline
from nider.models import Header
from nider.models import Paragraph
from nider.models import Content
from nider.models import Linkback
from nider.models import Image
from PIL import ImageEnhance
from PIL import ImageFilter

def card_gen(image, name,  fact, linkback = 'learnfacts.fun | @learnafunfact'):
    ''' Genera una tarjeta ./facts_imgs/[query]-fact.jpg a partir de  la imagen ./images/[query].jpg y el
    fact que se le envia en forma de texto. Opcional puedes agregar tu linkback pero si le mandas
    nada usa 'learnafact.fun' 
    '''

    fact_img = './facts_imgs/' + name + '-fact.png'

    roboto_font_folder = './fonts/Roboto/'
    outline = Outline(2, '#121212')
    para = Paragraph( text=fact,
        font = Font(roboto_font_folder + 'Roboto-Medium.ttf', 55),
        text_width = 30,
        align='left',
        color='#ededed', 
        outline=outline,
        )

    linkback = Linkback(text= str(linkback),
        font = Font(roboto_font_folder + 'Roboto-Bold.ttf', 18),
        color = '#ededed',
        bottom_padding = 300,
        outline=outline
        )
    content = Content(para, linkback)
    img = Image(content,
        fullpath = fact_img,
        width=1080,
        height=720
        )
    img.draw_on_image(image,
    image_enhancements=((ImageEnhance.Contrast, 0.75),
    (ImageEnhance.Brightness, 0.75)),
    image_filters=((ImageFilter.BLUR),)
    )
    return ({ 'image':image, 'fact_img': fact_img})
