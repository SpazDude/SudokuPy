def getVals(i):
    if i == 0 : return [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 18, 27, 36, 45, 54, 63, 72, 10, 11, 19, 20]
    if i == 1 : return [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 10, 19, 28, 37, 46, 55, 64, 73, 9, 11, 18, 20]
    if i == 2 : return [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 11, 20, 29, 38, 47, 56, 65, 74, 9, 10, 18, 19]
    if i == 3 : return [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 12, 21, 30, 39, 48, 57, 66, 75, 13, 14, 22, 23]
    if i == 4 : return [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 13, 22, 31, 40, 49, 58, 67, 76, 12, 14, 21, 23]
    if i == 5 : return [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 14, 23, 32, 41, 50, 59, 68, 77, 12, 13, 21, 22]
    if i == 6 : return [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 15, 24, 33, 42, 51, 60, 69, 78, 16, 17, 25, 26]
    if i == 7 : return [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 16, 25, 34, 43, 52, 61, 70, 79, 15, 17, 24, 26]
    if i == 8 : return [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 17, 26, 35, 44, 53, 62, 71, 80, 15, 16, 24, 25]
    if i == 9 : return [ 9, 10, 11, 12, 13, 14, 15, 16, 17, 0, 18, 27, 36, 45, 54, 63, 72, 1, 2, 19, 20]
    if i == 10 : return [ 9, 10, 11, 12, 13, 14, 15, 16, 17, 1, 19, 28, 37, 46, 55, 64, 73, 0, 2, 18, 20]
    if i == 11 : return [ 9, 10, 11, 12, 13, 14, 15, 16, 17, 2, 20, 29, 38, 47, 56, 65, 74, 0, 1, 18, 19]
    if i == 12 : return [ 9, 10, 11, 12, 13, 14, 15, 16, 17, 3, 21, 30, 39, 48, 57, 66, 75, 4, 5, 22, 23]
    if i == 13 : return [ 9, 10, 11, 12, 13, 14, 15, 16, 17, 4, 22, 31, 40, 49, 58, 67, 76, 3, 5, 21, 23]
    if i == 14 : return [ 9, 10, 11, 12, 13, 14, 15, 16, 17, 5, 23, 32, 41, 50, 59, 68, 77, 3, 4, 21, 22]
    if i == 15 : return [ 9, 10, 11, 12, 13, 14, 15, 16, 17, 6, 24, 33, 42, 51, 60, 69, 78, 7, 8, 25, 26]
    if i == 16 : return [ 9, 10, 11, 12, 13, 14, 15, 16, 17, 7, 25, 34, 43, 52, 61, 70, 79, 6, 8, 24, 26]
    if i == 17 : return [ 9, 10, 11, 12, 13, 14, 15, 16, 17, 8, 26, 35, 44, 53, 62, 71, 80, 6, 7, 24, 25]
    if i == 18 : return [ 18, 19, 20, 21, 22, 23, 24, 25, 26, 0, 9, 27, 36, 45, 54, 63, 72, 1, 2, 10, 11]
    if i == 19 : return [ 18, 19, 20, 21, 22, 23, 24, 25, 26, 1, 10, 28, 37, 46, 55, 64, 73, 0, 2, 9, 11]
    if i == 20 : return [ 18, 19, 20, 21, 22, 23, 24, 25, 26, 2, 11, 29, 38, 47, 56, 65, 74, 0, 1, 9, 10]
    if i == 21 : return [ 18, 19, 20, 21, 22, 23, 24, 25, 26, 3, 12, 30, 39, 48, 57, 66, 75, 4, 5, 13, 14]
    if i == 22 : return [ 18, 19, 20, 21, 22, 23, 24, 25, 26, 4, 13, 31, 40, 49, 58, 67, 76, 3, 5, 12, 14]
    if i == 23 : return [ 18, 19, 20, 21, 22, 23, 24, 25, 26, 5, 14, 32, 41, 50, 59, 68, 77, 3, 4, 12, 13]
    if i == 24 : return [ 18, 19, 20, 21, 22, 23, 24, 25, 26, 6, 15, 33, 42, 51, 60, 69, 78, 7, 8, 16, 17]
    if i == 25 : return [ 18, 19, 20, 21, 22, 23, 24, 25, 26, 7, 16, 34, 43, 52, 61, 70, 79, 6, 8, 15, 17]
    if i == 26 : return [ 18, 19, 20, 21, 22, 23, 24, 25, 26, 8, 17, 35, 44, 53, 62, 71, 80, 6, 7, 15, 16]
    if i == 27 : return [ 27, 28, 29, 30, 31, 32, 33, 34, 35, 0, 9, 18, 36, 45, 54, 63, 72, 37, 38, 46, 47]
    if i == 28 : return [ 27, 28, 29, 30, 31, 32, 33, 34, 35, 1, 10, 19, 37, 46, 55, 64, 73, 36, 38, 45, 47]
    if i == 29 : return [ 27, 28, 29, 30, 31, 32, 33, 34, 35, 2, 11, 20, 38, 47, 56, 65, 74, 36, 37, 45, 46]
    if i == 30 : return [ 27, 28, 29, 30, 31, 32, 33, 34, 35, 3, 12, 21, 39, 48, 57, 66, 75, 40, 41, 49, 50]
    if i == 31 : return [ 27, 28, 29, 30, 31, 32, 33, 34, 35, 4, 13, 22, 40, 49, 58, 67, 76, 39, 41, 48, 50]
    if i == 32 : return [ 27, 28, 29, 30, 31, 32, 33, 34, 35, 5, 14, 23, 41, 50, 59, 68, 77, 39, 40, 48, 49]
    if i == 33 : return [ 27, 28, 29, 30, 31, 32, 33, 34, 35, 6, 15, 24, 42, 51, 60, 69, 78, 43, 44, 52, 53]
    if i == 34 : return [ 27, 28, 29, 30, 31, 32, 33, 34, 35, 7, 16, 25, 43, 52, 61, 70, 79, 42, 44, 51, 53]
    if i == 35 : return [ 27, 28, 29, 30, 31, 32, 33, 34, 35, 8, 17, 26, 44, 53, 62, 71, 80, 42, 43, 51, 52]
    if i == 36 : return [ 36, 37, 38, 39, 40, 41, 42, 43, 44, 0, 9, 18, 27, 45, 54, 63, 72, 28, 29, 46, 47]
    if i == 37 : return [ 36, 37, 38, 39, 40, 41, 42, 43, 44, 1, 10, 19, 28, 46, 55, 64, 73, 27, 29, 45, 47]
    if i == 38 : return [ 36, 37, 38, 39, 40, 41, 42, 43, 44, 2, 11, 20, 29, 47, 56, 65, 74, 27, 28, 45, 46]
    if i == 39 : return [ 36, 37, 38, 39, 40, 41, 42, 43, 44, 3, 12, 21, 30, 48, 57, 66, 75, 31, 32, 49, 50]
    if i == 40 : return [ 36, 37, 38, 39, 40, 41, 42, 43, 44, 4, 13, 22, 31, 49, 58, 67, 76, 30, 32, 48, 50]
    if i == 41 : return [ 36, 37, 38, 39, 40, 41, 42, 43, 44, 5, 14, 23, 32, 50, 59, 68, 77, 30, 31, 48, 49]
    if i == 42 : return [ 36, 37, 38, 39, 40, 41, 42, 43, 44, 6, 15, 24, 33, 51, 60, 69, 78, 34, 35, 52, 53]
    if i == 43 : return [ 36, 37, 38, 39, 40, 41, 42, 43, 44, 7, 16, 25, 34, 52, 61, 70, 79, 33, 35, 51, 53]
    if i == 44 : return [ 36, 37, 38, 39, 40, 41, 42, 43, 44, 8, 17, 26, 35, 53, 62, 71, 80, 33, 34, 51, 52]
    if i == 45 : return [ 45, 46, 47, 48, 49, 50, 51, 52, 53, 0, 9, 18, 27, 36, 54, 63, 72, 28, 29, 37, 38]
    if i == 46 : return [ 45, 46, 47, 48, 49, 50, 51, 52, 53, 1, 10, 19, 28, 37, 55, 64, 73, 27, 29, 36, 38]
    if i == 47 : return [ 45, 46, 47, 48, 49, 50, 51, 52, 53, 2, 11, 20, 29, 38, 56, 65, 74, 27, 28, 36, 37]
    if i == 48 : return [ 45, 46, 47, 48, 49, 50, 51, 52, 53, 3, 12, 21, 30, 39, 57, 66, 75, 31, 32, 40, 41]
    if i == 49 : return [ 45, 46, 47, 48, 49, 50, 51, 52, 53, 4, 13, 22, 31, 40, 58, 67, 76, 30, 32, 39, 41]
    if i == 50 : return [ 45, 46, 47, 48, 49, 50, 51, 52, 53, 5, 14, 23, 32, 41, 59, 68, 77, 30, 31, 39, 40]
    if i == 51 : return [ 45, 46, 47, 48, 49, 50, 51, 52, 53, 6, 15, 24, 33, 42, 60, 69, 78, 34, 35, 43, 44]
    if i == 52 : return [ 45, 46, 47, 48, 49, 50, 51, 52, 53, 7, 16, 25, 34, 43, 61, 70, 79, 33, 35, 42, 44]
    if i == 53 : return [ 45, 46, 47, 48, 49, 50, 51, 52, 53, 8, 17, 26, 35, 44, 62, 71, 80, 33, 34, 42, 43]
    if i == 54 : return [ 54, 55, 56, 57, 58, 59, 60, 61, 62, 0, 9, 18, 27, 36, 45, 63, 72, 64, 65, 73, 74]
    if i == 55 : return [ 54, 55, 56, 57, 58, 59, 60, 61, 62, 1, 10, 19, 28, 37, 46, 64, 73, 63, 65, 72, 74]
    if i == 56 : return [ 54, 55, 56, 57, 58, 59, 60, 61, 62, 2, 11, 20, 29, 38, 47, 65, 74, 63, 64, 72, 73]
    if i == 57 : return [ 54, 55, 56, 57, 58, 59, 60, 61, 62, 3, 12, 21, 30, 39, 48, 66, 75, 67, 68, 76, 77]
    if i == 58 : return [ 54, 55, 56, 57, 58, 59, 60, 61, 62, 4, 13, 22, 31, 40, 49, 67, 76, 66, 68, 75, 77]
    if i == 59 : return [ 54, 55, 56, 57, 58, 59, 60, 61, 62, 5, 14, 23, 32, 41, 50, 68, 77, 66, 67, 75, 76]
    if i == 60 : return [ 54, 55, 56, 57, 58, 59, 60, 61, 62, 6, 15, 24, 33, 42, 51, 69, 78, 70, 71, 79, 80]
    if i == 61 : return [ 54, 55, 56, 57, 58, 59, 60, 61, 62, 7, 16, 25, 34, 43, 52, 70, 79, 69, 71, 78, 80]
    if i == 62 : return [ 54, 55, 56, 57, 58, 59, 60, 61, 62, 8, 17, 26, 35, 44, 53, 71, 80, 69, 70, 78, 79]
    if i == 63 : return [ 63, 64, 65, 66, 67, 68, 69, 70, 71, 0, 9, 18, 27, 36, 45, 54, 72, 55, 56, 73, 74]
    if i == 64 : return [ 63, 64, 65, 66, 67, 68, 69, 70, 71, 1, 10, 19, 28, 37, 46, 55, 73, 54, 56, 72, 74]
    if i == 65 : return [ 63, 64, 65, 66, 67, 68, 69, 70, 71, 2, 11, 20, 29, 38, 47, 56, 74, 54, 55, 72, 73]
    if i == 66 : return [ 63, 64, 65, 66, 67, 68, 69, 70, 71, 3, 12, 21, 30, 39, 48, 57, 75, 58, 59, 76, 77]
    if i == 67 : return [ 63, 64, 65, 66, 67, 68, 69, 70, 71, 4, 13, 22, 31, 40, 49, 58, 76, 57, 59, 75, 77]
    if i == 68 : return [ 63, 64, 65, 66, 67, 68, 69, 70, 71, 5, 14, 23, 32, 41, 50, 59, 77, 57, 58, 75, 76]
    if i == 69 : return [ 63, 64, 65, 66, 67, 68, 69, 70, 71, 6, 15, 24, 33, 42, 51, 60, 78, 61, 62, 79, 80]
    if i == 70 : return [ 63, 64, 65, 66, 67, 68, 69, 70, 71, 7, 16, 25, 34, 43, 52, 61, 79, 60, 62, 78, 80]
    if i == 71 : return [ 63, 64, 65, 66, 67, 68, 69, 70, 71, 8, 17, 26, 35, 44, 53, 62, 80, 60, 61, 78, 79]
    if i == 72 : return [ 72, 73, 74, 75, 76, 77, 78, 79, 80, 0, 9, 18, 27, 36, 45, 54, 63, 55, 56, 64, 65]
    if i == 73 : return [ 72, 73, 74, 75, 76, 77, 78, 79, 80, 1, 10, 19, 28, 37, 46, 55, 64, 54, 56, 63, 65]
    if i == 74 : return [ 72, 73, 74, 75, 76, 77, 78, 79, 80, 2, 11, 20, 29, 38, 47, 56, 65, 54, 55, 63, 64]
    if i == 75 : return [ 72, 73, 74, 75, 76, 77, 78, 79, 80, 3, 12, 21, 30, 39, 48, 57, 66, 58, 59, 67, 68]
    if i == 76 : return [ 72, 73, 74, 75, 76, 77, 78, 79, 80, 4, 13, 22, 31, 40, 49, 58, 67, 57, 59, 66, 68]
    if i == 77 : return [ 72, 73, 74, 75, 76, 77, 78, 79, 80, 5, 14, 23, 32, 41, 50, 59, 68, 57, 58, 66, 67]
    if i == 78 : return [ 72, 73, 74, 75, 76, 77, 78, 79, 80, 6, 15, 24, 33, 42, 51, 60, 69, 61, 62, 70, 71]
    if i == 79 : return [ 72, 73, 74, 75, 76, 77, 78, 79, 80, 7, 16, 25, 34, 43, 52, 61, 70, 60, 62, 69, 71]
    if i == 80 : return [ 72, 73, 74, 75, 76, 77, 78, 79, 80, 8, 17, 26, 35, 44, 53, 62, 71, 60, 61, 69, 70]


for i in range(81):
    print(sorted(getVals(i))
