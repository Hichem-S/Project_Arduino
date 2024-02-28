#install package pip install docx2pdf
import library
from docx2pdf import convert 
convert (r"C:\Users\hiche\Desktop\loi interne.docx",r"C:\Users\hiche\Desktop\loi interne.pdf")
#install package pip installpydub
import library 
from pydub import AudioSegment
src = r"C:\Users\hiche\Desktop\GOOBA.mp3"
dst = r"C:\Users\hiche\Desktop\GOOBA.wav"
sound = AudioSegment_from_mp3(src)
sound.export(dst, format="wav") 


from pydub import AudioSegment

# Load the MP3 file
#mp3_file = AudioSegment.from_mp3(r"C:\Users\hiche\Desktop\GOOBA.mp3")

# Convert the loaded MP3 to WAV format and specify the output path
#output_path = r"C:\Users\hiche\Desktop\output.wav"
#mp3_file.export(output_path, format="wav")
##################### convert image to pdf 
#import os 
#from PIL import Image

#sortie = r"C:\Users\hiche\Desktop\PDF"
#source = r"C:\Users\hiche\Desktop\Image"
#for file in os.listdir(source):
 #   if file.split('.')[-1] in ('png','jpg','jpeg'):
  #      img=Image.open(os.path.join(source,file))
   #     img_converted = img.convert('RGB')
    #    img_converted.save(os.path.join(sortie, '{0}.pdf'.format(file.split('.')[-2])))
###################convert pdf to docx
from pdf2docx import Converter
pdf = r"C:\Users\hiche\Desktop\Mycode\loi_interne.pdf"
docx =r"C:\Users\hiche\Desktop\Mycode\loi-interne.docx"
cv = Converter(pdf)
cv.convert(docx)
################## remove background
#from rembg import remove
from PIL import Image
#input_path="hichem.jpg"
#outpath_path="img.png"
#input=Image.open(input_path)
#output=remove(input)
#output.save(outpath_path)
