#assumptions
# bose_bass
# bose_build
# bose_price
import numpy as np

bose_dic = {}
sony_dic = {}
jbl_dic = {}
#or if subtraction is not req we can just multiply -1 to all the values in bad category put it in one arary and then take mean
def for_each_company():
    bose_dic = {}
    bose_dic['bass'] = calculate_score(bose_bass_array) - calculate_score(bose_bad_bass_arr) 
    bose_dic['build'] = calculate_score(bose_build_array) - calculate_score(bose_bad_build_array)
    bose_dic['price'] = calculate_score(bose_price_arr) - calculate_score(bose_bad_price_arr)
    #similarly for others


def calculate_score(arr):
    arr = np.array(arr)
    return np.mean(arr)


def recommender(aspect_attributes, target = None):
    '''here aspect attributes will be a list of aspects of combination of bass, build, and price'''
    bose_score = 0
    sony_score = 0
    jbl_score = 0
    if 'bass' in aspect_attributes:
        bose_score += bose_dic['bass']
        sony_score += sony_dic['bass']
        jbl_score += jbl_dic['bass']

    if 'build' in aspect_attributes:
        bose_score += bose_dic['build']
        sony_score += sony_dic['build']
        jbl_score += jbl_dic['build']

    if 'price' in aspect_attributes:
        bose_score += bose_dic['price']
        sony_score += sony_dic['price']
        jbl_score += jbl_dic['price']

    if bose_score > jbl_score:
        if bose_score > sony_score:
            print('bose')
        else:
            print('sony')
    else:
        if jbl_score > sony_score:
            print('jbl')
        else:
            print('sony')
