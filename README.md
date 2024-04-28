# bsc_thesis

Coref from https://github.com/andreasvc/dutchcoref/

python3 ../dutchcoref/coref.py --fmt=booknlp parses/100/Nescio_Dichtertje > corefs/100/Nescio_Dichtertje.conll


Coval from https://github.com/andreasvc/coval/

python3 ../coval/scorer.py corefs/all/Nescio_Dichtertje_gold.conll corefs/all/Nescio_Dichtertje.conll

python3 ../coval/scorer.py corefs/100/Nescio_Dichtertje_gold.conll corefs/100/Nescio_Dichtertje.conll

