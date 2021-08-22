import cv2 as cv
import googletrans
import numpy as np
import os
from time import sleep, time
from windowcapture import WindowCapture
import pytesseract
from PIL import ImageFont, Image, ImageDraw
from googletrans import Translator
from translate import TranslateTool
import textwrap
import argparse
from appconfig import *

parser = argparse.ArgumentParser(description='Princess Connect Re:dive auto translate')
parser.add_argument('--translate', nargs="?" ,const=str, default="googleDict",
                    help='Select Translate endpoint, Available now : azure, ibm, googleModule, googleDict, default: googleDict')
parser.add_argument('--data', nargs="?" ,const=str, default="best",
                    help='Select language datapack, Available now : fast, medium, best')
                                        
args = vars(parser.parse_args())
# Change the working directory to the folder this script is in.
# Doing this because I'll be putting the files from each video in their own folder on GitHub
os.chdir(os.path.dirname(os.path.abspath(__file__)))


def translate(img):
    text = pytesseract.image_to_string(img, langdata).strip().replace(" ", "").replace("。", "。 ").replace("〆","")

    return text

if args['data'] == 'fast':
    print("Using fast detection")
    langdata = "jpn1"
elif args['data'] == 'medium':
    print("Using medium detection")
    langdata = "jpn2"
elif args['data'] == 'best':
    print("Using best detection")
    langdata = "jpn"
else:
    pass
# initialize the WindowCapture class
wincap = WindowCapture('PrincessConnectReDive')

loop_time = time()
text = "Initial.."
text1 = ""
sel_text = ""
sel_text_cmp = ""
sel_text1 = ""
sel_text_cmp1 = ""

fontpath = 'C:\Windows\Fonts\ARIAL.TTF'
font = ImageFont.truetype(fontpath, 18)
while(True):

    # get an updated image of the game
    screenshot = wincap.get_screenshot()
    

    # kotak = cv.rectangle(screenshot, (0, 0), (808, 113), (255, 255, 255), -1)
    img_pil = Image.fromarray(screenshot)
    jendela = cv.imread("jendela.png", cv.IMREAD_UNCHANGED)
    # img_pil = Image.fromarray(screenshot)
    img = np.array(img_pil)

 
    position = (15, 10)
    textbox1 = cv.imread("template/coba.png", cv.IMREAD_UNCHANGED)
    textbox2 = cv.imread("template/text_box2.png", cv.IMREAD_UNCHANGED)
    textbox3 = cv.imread("template/text_box4.png", cv.IMREAD_UNCHANGED)
    textbox4 = cv.imread("template/text_box5.png", cv.IMREAD_UNCHANGED)
    textbox5 = cv.imread("template/text_box1.png", cv.IMREAD_UNCHANGED)
    love_box = cv.imread("template/love_box.png", cv.IMREAD_UNCHANGED)
    charabox = cv.imread("template/charatextbox.png", cv.IMREAD_UNCHANGED)
    selection_red = cv.imread("template/selection.png", cv.IMREAD_UNCHANGED)
    selection_blue = cv.imread("template/selectionblu.png", cv.IMREAD_UNCHANGED)


    

    img_edges = cv.Canny(screenshot,100,200,3,L2gradient=True)
    tmplt_edges_txt = cv.Canny(textbox1,100,200,3,L2gradient=True)
    tmplt_edges_txt2 = cv.Canny(textbox2,100,200,3,L2gradient=True)
    tmplt_edges_txt3 = cv.Canny(love_box,100,200,3,L2gradient=True)
    tmplt_edges_txt4 = cv.Canny(textbox3,100,200,3,L2gradient=True)
    tmplt_edges_txt5 = cv.Canny(textbox4,100,200,3,L2gradient=True)
    tmplt_edges_txt6 = cv.Canny(textbox5,100,200,3,L2gradient=True)
    tmplt_edges_chara = cv.Canny(charabox,100,200,3,L2gradient=True)




    tmplt_edges_red = cv.Canny(selection_red,100,200,3,L2gradient=True)
    tmplt_edges_blue = cv.Canny(selection_blue,100,200,3,L2gradient=True)


    result_txt = cv.matchTemplate(img_edges, tmplt_edges_txt, cv.TM_CCORR_NORMED)
    result_txt2 = cv.matchTemplate(img_edges, tmplt_edges_txt2, cv.TM_CCORR_NORMED)
    result_txt3 = cv.matchTemplate(img_edges, tmplt_edges_txt3, cv.TM_CCORR_NORMED)
    result_txt4 = cv.matchTemplate(img_edges, tmplt_edges_txt4, cv.TM_CCORR_NORMED)
    result_txt5 = cv.matchTemplate(img_edges, tmplt_edges_txt5, cv.TM_CCORR_NORMED)
    result_txt6 = cv.matchTemplate(img_edges, tmplt_edges_txt6, cv.TM_CCORR_NORMED)
    result_chara = cv.matchTemplate(img_edges, tmplt_edges_chara, cv.TM_CCORR_NORMED)




    result_red = cv.matchTemplate(img_edges, tmplt_edges_red, cv.TM_CCORR_NORMED)
    result_blue = cv.matchTemplate(img_edges, tmplt_edges_blue, cv.TM_CCORR_NORMED)


    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result_txt)
    min_val1, max_val1, min_loc1, max_loc1 = cv.minMaxLoc(result_txt2)
    _,max_val4,_,max_loc4=cv.minMaxLoc(result_txt3)
    _,max_val5,_,max_loc5=cv.minMaxLoc(result_txt4)
    _,max_val6,_,max_loc6=cv.minMaxLoc(result_txt5)
    _,max_val8,_,max_loc8=cv.minMaxLoc(result_txt6)
    _,max_val7,_,max_loc7=cv.minMaxLoc(result_chara)





    _,max_val2,_,max_loc2=cv.minMaxLoc(result_red)
    _,max_val3,_,max_loc3=cv.minMaxLoc(result_blue)


    # print(max_loc1, max_val1)
    
    height, width, channels = screenshot.shape
    # print(height, width)
    
    w = textbox1.shape[1]
    h = textbox1.shape[0]

    w1 = textbox2.shape[1]
    h1 = textbox2.shape[0]

    w2 = selection_red.shape[1]
    h2 = selection_red.shape[0]

    w3 = selection_blue.shape[1]
    h3 = selection_blue.shape[0]

    w4 = love_box.shape[1]
    h4 = love_box.shape[0]

    w5 = textbox3.shape[1]
    h5 = textbox3.shape[0]

    w6 = textbox4.shape[1]
    h6 = textbox4.shape[0]

    w7 = charabox.shape[1]
    h7 = charabox.shape[0]

    w8 = textbox5.shape[1]
    h8 = textbox5.shape[0]
    threshold = 0.26
    
    # print(max_val8)

    # print(cv.boundingRect(tes))
    # print(tes.shape)
    
    # if max
    
    if max_val >= threshold and max_val < 0.4:
        cv.rectangle(screenshot, max_loc, (max_loc[0] + w, max_loc[1] + h), (0, 198, 0), 2)
        crop = img[(max_loc[1] + 45):max_loc[1] + (h-25), max_loc[0]+20:max_loc[0] +(w -30)]
    elif max_val8 >= threshold and max_val8 < 0.6:
        cv.rectangle(screenshot, max_loc8, (max_loc8[0] + w8, max_loc8[1] + h8), (0, 198, 0), 2)
        crop = img[(max_loc8[1] + 15):max_loc8[1] + (h8-15), max_loc8[0]+15:max_loc8[0] +(w8 -20)]

    elif max_val1 >= threshold and max_val1 < 0.4:
        cv.rectangle(screenshot, max_loc1, (max_loc1[0] + w1, max_loc1[1] + h1), (0, 198, 0), 2)

        crop = img[(max_loc1[1] + 45):max_loc1[1] + (h1-25) , max_loc1[0]+20:max_loc1[0] +(w1 -30)]
    elif max_val4 >= threshold and max_val4 < 0.7:
        cv.rectangle(screenshot, max_loc4, (max_loc4[0] + w4, max_loc4[1] + h4), (0, 198, 0), 2)

        crop = img[(max_loc4[1] + 65):max_loc4[1] + (h4-50) , max_loc4[0]+55:max_loc4[0] +(w4 -55)]
        # cv.imshow("test", crop)
    elif max_val5 >= threshold and max_val5 < 0.4:
        cv.rectangle(screenshot, max_loc5, (max_loc5[0] + w5, max_loc5[1] + h5), (0, 198, 0), 2)

        crop = img[(max_loc5[1] + 42):max_loc5[1] + (h5-25) , max_loc5[0]+30:max_loc5[0] +(w5 -30)]
    
    elif max_val5 >= threshold and max_val5 < 0.4:
        cv.rectangle(screenshot, max_loc7, (max_loc7[0] + w7, max_loc7[1] + h7), (0, 198, 0), 2)

        crop = img[(max_loc7[1] + 42):max_loc7[1] + (h7-25) , max_loc7[0]+30:max_loc7[0] +(w7 -30)]
        # cv.imshow("test", crop)
    elif max_val7 >= 0.23 and max_val7 < 0.4:
        cv.rectangle(screenshot, max_loc7, (max_loc7[0] + w7, max_loc7[1] + h7), (0, 198, 0), 2)
        crop = img[(max_loc7[1] + 40):max_loc7[1] + (h7-10), max_loc7[0]+20:max_loc7[0] +(w7 -30)]
        crop = cv.copyMakeBorder(crop, 0, 0, 500, 0, cv.BORDER_CONSTANT, None, 500)


        # cv.imshow("test", crop)
    # print(max_val7)
    if max_val2 >= 0.6:
        cv.rectangle(screenshot, max_loc2, (max_loc2[0] + w2, max_loc2[1] + h2), (0, 198, 0), 2)

        sel_red = img[(max_loc2[1]):max_loc2[1] + h2 , max_loc2[0]:max_loc2[0] + w2]
        sel_red_black = cv.cvtColor(sel_red, cv.COLOR_BGR2GRAY)
        (thresh, blackAndWhiteImage) = cv.threshold(sel_red_black, 127, 255, cv.THRESH_BINARY)
 
        sel_text = translate(blackAndWhiteImage)
        # print(sel_text)
        # cv.imshow("test", blackAndWhiteImage)
        # print(max_val2)

    if max_val3 >= 0.6:
        cv.rectangle(screenshot, max_loc3, (max_loc3[0] + w3, max_loc3[1] + h3), (0, 198, 0), 2)

        sel_blue = img[(max_loc3[1]):max_loc3[1] + h3 , max_loc3[0]:max_loc3[0] + w3]
        sel_text1 = translate(sel_blue)
        # print(sel_text1)

        # print(max_val3)

    # print(d)
    # print(crop.shape)
    # cv.imshow("aa",tes)
    # print(text)
    try:
        text = translate(crop)
    except:
        pass
    if sel_text == "" or sel_text_cmp  == sel_text or sel_text == "Initial..":
        pass
    else:
        if args['translate'] == "disable":
            # print(namee)
            pass
        elif args['translate'] == "googleDict":
            try:
                sel_text_tl = TranslateTool.googleDict(sel_text)
                sel_text_tl1 = TranslateTool.googleDict(sel_text1)
                print(''.join([a for a in sel_text_tl]))
                print(''.join([a for a in sel_text_tl1]))

            except Exception as e:
                print(e)
                pass
        elif args['translate'] == "googleModule":
            text_tl = TranslateTool.googleModule(sel_text)
            sel_text_tl1 = TranslateTool.googleModule(sel_text1)


        elif args['translate'] == "azure":
            if AZURE_SUBKEY == "":
                print("Azure Translate need Key! Set at appconfig.py")
                exit()
            elif AZURE_ENDPOINT == "":
                print("Azure Translate need endpoint set! Change at appconfig.py")
                exit()
            elif AZURE_LOCATION == "":
                print("Azure Translate need location set! Change at appconfig.py")
                exit()
            else:
                sel_text_tl = TranslateTool.azure(sel_text)
                sel_text_tl1 = TranslateTool.azure(sel_text1)

        elif args['translate'] == "ibm":
            sel_text_tl = TranslateTool.ibm(sel_text)
            sel_text_tl1 = TranslateTool.ibm(sel_text1)

        else:
            print("Need translate argument!")
            exit()
        try:
            print(sel_text_tl)
            select_red = cv.rectangle(sel_red, (0, 0), (808, 113), (255, 255, 255), -1)
            select_redd = Image.fromarray(select_red)
            select_red_draw = ImageDraw.Draw(select_redd)
            select_red_offset = 10
            try:
                select_red_draw.text((15, 10), "Selection Red : " + ''.join([a for a in sel_text_tl]), font=font, fill=(0, 0, 0, 0))
                select_red_draw.text((15, 30), "Selection Blue : " + ''.join([a for a in sel_text_tl1]), font=font, fill=(0, 0, 0, 0))

            except:
                select_red_draw.text((15, 30), "Selection Blue : " + ''.join([a for a in sel_text_tl1]), font=font, fill=(0, 0, 0, 0))
        except:
            pass
        sel_text_cmp = sel_text
        sel_text_cmp1 = sel_text1

    

    
    if text == "" or text1 == text: 
        pass
    else:

        
        # print(args)
        

        if args['translate'] == "disable":
            # print(namee)
            pass
        elif args['translate'] == "googleDict":
            text_tl = TranslateTool.googleDict(text)

        elif args['translate'] == "googleModule":
            text_tl = TranslateTool.googleModule(text)

        elif args['translate'] == "azure":
            if AZURE_SUBKEY == "":
                print("Azure Translate need Key! Set at appconfig.py")
                exit()
            elif AZURE_ENDPOINT == "":
                print("Azure Translate need endpoint set! Change at appconfig.py")
                exit()
            elif AZURE_LOCATION == "":
                print("Azure Translate need location set! Change at appconfig.py")
                exit()
            else:
                text_tl = TranslateTool.azure(text)
        elif args['translate'] == "ibm":
            text_tl = TranslateTool.ibm(text)
        else:
            print("Need translate argument!")
            exit()

        
        # draw.text(position, coba, font=font, fill=(0, 0, 0, 0))
        try:
            d = cv.rectangle(crop, (0, 0), (808, 113), (255, 255, 255), -1)
            dd = Image.fromarray(d)

            

            draw = ImageDraw.Draw(dd)
            offset = 10
            for texted in text_tl:
                for line in textwrap.wrap( texted, width=80):

                    draw.text((15, offset), line, font=font, fill=(0, 0, 0, 0))
                    offset += font.getsize(line)[1]
        except Exception as e:
            # print(e)
            pass
        
        text1 = text
        
        try:
            print(text)
        except:
            pass
    


    try:
        
        if max_val >= threshold or max_val1 >= threshold or max_val4 >= threshold or max_val5 >= threshold or max_val6 >= threshold or max_val7 >= 0.23 or max_val8 >= threshold:
            output = np.array(dd)

            cv.imshow('Translated', output)
        # if max_val2 >= threshold:
        output_red = np.array(select_redd)
        cv.imshow('selection', output_red)
        # cv.imshow("aa",screenshot)
        # cv.imshow("a1a",crop)
    except Exception as e:
        # print(e)
        pass
    # print(cv.getWindowImageRect('Computer Vision'))

    # debug the loop rate
    # print('FPS {}'.format(1 / (time() - loop_time)))
    # loop_time = time()

    # press 'q' with the output window focused to exit.
    # waits 1 ms every loop to process key presses
    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break
    # sleep(2)
print('Done.')
