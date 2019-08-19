from googletrans import Translator
translator = Translator()
translation = translator.translate('美容学校哪里好 广州纹绣培训学院，7天学习课程', dest='en')
translation_back = translator.translate(translation.text, dest='zh-CN')
print(translation.text)
print(translation_back.text)

translation = translator.translate('美容学校哪里好 广州纹绣培训学院，7天学习课程', dest='it')
translation_back = translator.translate(translation.text, dest='zh-CN')
print(translation.text)
print(translation_back.text)

translation = translator.translate('美容学校哪里好 广州纹绣培训学院，7天学习课程', dest='fr')
translation_back = translator.translate(translation.text, dest='zh-CN')
print(translation.text)
print(translation_back.text)

translation = translator.translate('美容学校哪里好 广州纹绣培训学院，7天学习课程', dest='bg')
translation_back = translator.translate(translation.text, dest='zh-CN')
print(translation.text)
print(translation_back.text)

translation = translator.translate('美容学校哪里好 广州纹绣培训学院，7天学习课程', dest='cs')
translation_back = translator.translate(translation.text, dest='zh-CN')
print(translation.text)
print(translation_back.text)

translation = translator.translate('美容学校哪里好 广州纹绣培训学院，7天学习课程', dest='fi')
translation_back = translator.translate(translation.text, dest='zh-CN')
print(translation.text)
print(translation_back.text)

translation = translator.translate('美容学校哪里好 广州纹绣培训学院，7天学习课程', dest='hu')
translation_back = translator.translate(translation.text, dest='zh-CN')
print(translation.text)
print(translation_back.text)