
#MBART FINE TUNE
#import os
#os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2' untuk mengatasi error di TF (tidak bisa) 

import gradio as gr
#import tensorflow as tf masih error 
import torch #ganti ke pt

import sentencepiece
from transformers import MBartTokenizer, MBartForConditionalGeneration

def run_model(input_text, 
              min_length,
              max_length,            
              length_penalty):

    #MBART Transformer 
    mbart_model =  MBartForConditionalGeneration.from_pretrained("facebook/mbart-large-50")#, from_pt=True) untuk TFMbart
    mbart_tokenizer = MBartTokenizer.from_pretrained("facebook/mbart-large-50")

    #encode input to vector
    input_text = str(input_text)
    input_text = ' '.join(input_text.split()) # hapus white space 
    input_tokenized = mbart_tokenizer.encode(input_text, return_tensors='pt')
        
    #generate input
    summary_ids = mbart_model.generate(input_tokenized,                                      
                                       length_penalty = length_penalty, #Atur ke nilai <1.0 untuk menghasilkan urutan yang lebih pendek, ke nilai > 1.0 untuk menghasilkan urutan yang lebih panjang)             
                                       min_length = min_length, #Panjang minimum urutan yang akan dihasilkan)             
                                       max_length = max_length, #Panjang maksimum urutan yang akan dihasilkan)"""                                       
                                       num_beams = 5,#pencarian 
                                       no_repeat_ngram_size = 2,#jika diatur ke int > 0, semua ngram dengan ukuran tersebut hanya dapat muncul sekali.
                                      early_stopping = True)

    #decode output to text
    output = mbart_tokenizer.batch_decode(summary_ids, skip_special_tokens=True, clean_up_tokenization_spaces=False) 
        
    return output[0]
                             
# end 

#example 
         # source Wikipedia
contoh = [["Dota 2 adalah sebuah permainan arena pertarungan daring multipemain, dan merupakan sekuel dari Defense of the Ancients mod pada Warcraft 3: Reign of Chaos dan Warcraft 3: The Frozen Throne. DotA 2 dikembangkan oleh Valve Corporation, terbit juli 2013 dota 2 dapat dimainkan secara gratis pada sistem operasi Microsoft Windows, OS X and Linux. Dota 2 dapat dimainkan secara eksklusif melalui distributor resmi valve, Steam.Dota 2 dimainkan oleh 2 tim yang beranggota 5 orang pemain, setiap tim memiliki markas yang berada dipojok peta, setiap markas memiliki satu bangunan bernama 'Ancient', Di mana tim harus berusaha menghancurkan 'Ancient' tim lawan agar dapat memenangkan pertandingan. Setiap pemain hanya dapat mengontrol satu karakter Hero yang berfokus pada menaikan level, mengumpulkan gold, membeli item dan melawan tim lawan untuk menang.Pengembangan Dota 2 dimulai sejak tahun 2009. Ketika pengembang mod DotA, Icefrog, dipekerjakan oleh Valve sebagai lead designer. Dota 2 dipuji oleh kritikus karena gameplay-nya, kualitas pembuatan dan kesetiaan pada gameplay pendahulu (DotA mod Warcraft 3). tetapi Dota 2 juga menuai kritik sebagai game yang susah dipelajari dan para pemain yang tidak ramah.Sampai pertengahan 2017 Dota 2 menjadi game yang memiliki aktivitas pemain paling banyak di Steam, dengan pucak 800,000 pemain online bersamaan setiap hari", 30, 100, 2], 
          ["Gangguan jiwa atau penyakit jiwa adalah pola psikologis atau perilaku yang pada umumnya terkait dengan stres atau kelainan jiwa yang tidak dianggap sebagai bagian dari perkembangan normal manusia.[1] Gangguan tersebut didefinisikan sebagai kombinasi afektif, perilaku, komponen kognitif atau persepsi yang berhubungan dengan fungsi tertentu pada daerah otak atau sistem saraf yang menjalankan fungsi sosial manusia. Penemuan dan pengetahuan tentang kondisi kesehatan jiwa telah berubah sepanjang perubahan waktu dan perubahan budaya, dan saat ini masih terdapat perbedaan tentang definisi, penilaan dan klasifikasi, meskipun kriteria pedoman standar telah digunakan secara luas. Lebih dari sepertiga orang di sebagian besar negara-negara melaporkan masalah pada satu waktu pada hidup mereka yang memenuhi kriteria salah satu atau beberapa tipe umum dari kelainan jiwa.", 30, 100, 1]]
          
#judul
title = "Text Sumarization id2id"

#deskripsi
description = "Demo for Text Sumarization id2id. Models are MBART(50 languages)"           

#footer            
article = "<p style='text-align: center'><a href='https://github.com/sultanbst123/Text_summarization-id2id' target='_blank'><u>Untuk penjelasan lihat di repo ku</u> 😁</a></p>"

#run gradio
gr.Interface(
    fn=run_model,
    #input text
    inputs=[
        gr.inputs.Textbox(
            lines=7,
            placeholder="Ketik disini...", 
            label="Text",
        ),
        #fine tune
        #min length
        gr.inputs.Slider(
           minimum=10,
           maximum=50,  
           step=5,
           default=20,
           label="Min Length(panjang minimal urutan)",
       ),
        #max length
        gr.inputs.Slider(
           minimum=100,
           maximum=2500,  
           step=100,
           default=300, 
           label="Max Length(panjang maksimum urutan)",
       ),
        #length_penalty
        gr.inputs.Slider(
           minimum=1,
           maximum=3,  
           step=1,
           default=1,
           label="Length Penalty",
       ),        
    ],
    #output text
    outputs=gr.outputs.Textbox(       
            label="Output text", 
    ),
    title=title,
    description=description,
    article=article,
    examples=contoh,
    theme = "dark-peach").launch(debug = True)