# Text_summarization(FT) with mT5 & Mbart

Demo Text summarization:
- Demo [mT5](https://huggingface.co/spaces/Sultannn/Text_summarization_with-MT5) dan serta [45 bahasa/languages](https://huggingface.co/csebuetnlp/mT5_multilingual_XLSum#benchmarks) 
- Demo [MBart](https://huggingface.co/spaces/Sultannn/Text_summarization_with-MBART) dan serta [50 bahasa/languages](https://huggingface.co/facebook/mbart-large-50#languages-covered)  


## mBart-50
mBART-50 adalah model Sequence-to-Sequence multibahasa. yang diperkenalkan untuk menunjukkan bahwa model terjemahan multibahasa dapat dibuat melalui fine-tuning multibahasa. Alih-alih fine-tuning pada satu arah, model pra-latihan ini fine-tuning di banyak arah secara bersamaan. mBART-50 dibuat menggunakan model mBART asli dan diperluas untuk menambahkan 25 bahasa tambahan untuk mendukung model terjemahan mesin multibahasa dari 50 bahasa.

## mT5
“Text-to-Text Transfer Transformer”” (T5) baru-baru ini memanfaatkan format dan skala teks-ke-teks terpadu untuk mencapai hasil mutakhir pada berbagai tugas NLP berbahasa Inggris. Google memperkenalkan mT5, varian multibahasa dari T5 yang telah dilatih sebelumnya pada kumpulan data berbasis Common Crawl baru yang mencakup 101 bahasa. Kami merinci desain dan pelatihan modifikasi mT5 dan mendemonstrasikan kinerja mutakhirnya di banyak tolok ukur multibahasa. Kami juga menjelaskan teknik sederhana untuk mencegah "penerjemahan yang tidak disengaja" dalam pengaturan zero-shot, di mana model generatif memilih untuk (sebagian) menerjemahkan prediksinya ke dalam bahasa yang salah.
Note untuk mT5: mT5 dilatih tanpa pengawasan jadi fine tuning untuk mendapatkan hasil yang di harapkan(saya pakai check point mT5 yang sudah di fine tuning) 


## Paper:
- [mT5: A massively multilingual pre-trained text-to-text transformer](https://arxiv.org/abs/2010.11934) paper by Linting Xue, Noah Constant, Adam Roberts, Mihir Kale, Rami Al-Rfou, Aditya Siddhant, Aditya Barua, Colin Raffel.
- [MBart-50: Multilingual Translation with Extensible Multilingual Pretraining and Finetuning](https://arxiv.org/abs/2008.00401) paper by Yuqing Tang, Chau Tran, Xian Li, Peng-Jen Chen, Naman Goyal. 


## Referensi:
 
- [google-research/multilingual-t5(official)](https://github.com/google-research/multilingual-t5)
- [MBart and MBart-50 documentation](https://huggingface.co/docs/transformers/model_doc/mbart)
- [mT5 documentation](https://huggingface.co/docs/transformers/model_doc/mt5)

## Important: 
- jika ada bacaan error clear lalu submit ulang 
- <b>Laporkan jika ada kesalahan</b>
