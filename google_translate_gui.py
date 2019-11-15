from PyQt5.QtWidgets import QDialog,QApplication
from googletrans import Translator
from google_translate_ui import *

class Form(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.plainTextEdit_translate_text.textChanged.connect(self.translate_text)
        self.ui.comboBox_language_text.currentIndexChanged.connect(self.select_translate_text)
        self.ui.comboBox_list_language_translate.currentIndexChanged.connect(self.select_translate_text)
        self.translator = Translator()
        self.LANGUAGES = {
    'af': 'afrikaans',
        'sq': 'albanian',
        'am': 'amharic',
        'ar': 'arabic',
        'hy': 'armenian',
        'az': 'azerbaijani',
        'eu': 'basque',
        'be': 'belarusian',
        'bn': 'bengali',
        'bs': 'bosnian',
        'bg': 'bulgarian',
        'ca': 'catalan',
        'ceb': 'cebuano',
        'ny': 'chichewa',
        'zh-cn': 'chinese (simplified)',
        'zh-tw': 'chinese (traditional)',
        'co': 'corsican',
        'hr': 'croatian',
        'cs': 'czech',
        'da': 'danish',
        'nl': 'dutch',
        'en': 'english',
        'eo': 'esperanto',
        'et': 'estonian',
        'tl': 'filipino',
        'fi': 'finnish',
        'fr': 'french',
        'fy': 'frisian',
        'gl': 'galician',
        'ka': 'georgian',
        'de': 'german',
        'el': 'greek',
        'gu': 'gujarati',
        'ht': 'haitian creole',
        'ha': 'hausa',
        'haw': 'hawaiian',
        'iw': 'hebrew',
        'hi': 'hindi',
        'hmn': 'hmong',
        'hu': 'hungarian',
        'is': 'icelandic',
        'ig': 'igbo',
        'id': 'indonesian',
        'ga': 'irish',
        'it': 'italian',
        'ja': 'japanese',
        'jw': 'javanese',
        'kn': 'kannada',
        'kk': 'kazakh',
        'km': 'khmer',
        'ko': 'korean',
        'ku': 'kurdish (kurmanji)',
        'ky': 'kyrgyz',
        'lo': 'lao',
        'la': 'latin',
        'lv': 'latvian',
        'lt': 'lithuanian',
        'lb': 'luxembourgish',
        'mk': 'macedonian',
        'mg': 'malagasy',
        'ms': 'malay',
        'ml': 'malayalam',
        'mt': 'maltese',
        'mi': 'maori',
        'mr': 'marathi',
        'mn': 'mongolian',
        'my': 'myanmar (burmese)',
        'ne': 'nepali',
        'no': 'norwegian',
        'ps': 'pashto',
        'fa': 'persian',
        'pl': 'polish',
        'pt': 'portuguese',
        'pa': 'punjabi',
        'ro': 'romanian',
        'ru': 'russian',
        'sm': 'samoan',
        'gd': 'scots gaelic',
        'sr': 'serbian',
        'st': 'sesotho',
        'sn': 'shona',
        'sd': 'sindhi',
        'si': 'sinhala',
        'sk': 'slovak',
        'sl': 'slovenian',
        'so': 'somali',
        'es': 'spanish',
        'su': 'sundanese',
        'sw': 'swahili',
        'sv': 'swedish',
        'tg': 'tajik',
        'ta': 'tamil',
        'te': 'telugu',
        'th': 'thai',
        'tr': 'turkish',
        'uk': 'ukrainian',
        'ur': 'urdu',
        'uz': 'uzbek',
        'vi': 'vietnamese',
        'cy': 'welsh',
        'xh': 'xhosa',
        'yi': 'yiddish',
        'yo': 'yoruba',
        'zu': 'zulu',
        'fil': 'Filipino',
        'he': 'Hebrew'

    } 
        self.src = 'en'
        self.dest=''
        self.text =''
        
    def translate_text(self):
        try:
            # print(self.text)
            # print(self.src)
            # print(self.dest)
            text = str(self.translator.translate(self.text,self.src,self.dest).text)
            self.ui.plainTextEdit_text_translated.setPlainText(text)  
        except:
            pass
    
    def add_item_to_combobox(self):
        
        for item in list(self.LANGUAGES.values()):
            self.ui.comboBox_list_language_translate.addItem(str(item)[0].upper()+str(item)[1::])
            self.ui.comboBox_language_text.addItem(str(item)[0].upper()+str(item)[1::])
    
    def select_translate_text(self):
        self.text = self.ui.plainTextEdit_translate_text.toPlainText()
        if self.ui.comboBox_language_text.currentText() ==  "Auto":
            self.dest = self.translator.detect(self.text).lang
            
        else:
            self.dest =list(self.LANGUAGES)[ self.ui.comboBox_language_text.currentIndex()-2 ]
             
        if self.ui.comboBox_list_language_translate.currentIndex():
            self.src = list(self.LANGUAGES)[ self.ui.comboBox_list_language_translate.currentIndex() ]
            print(self.dest)
        Form.translate_text(self)
    

if __name__ in '__main__':
    
    app = QApplication([])
    form = Form()
    form.add_item_to_combobox()
    form.show()
    app.exec_()