import time

comparacoes = 0

def mergesort(lista, inicio=0, fim=None):
    global comparacoes

    if fim is None:
        fim = len(lista)
    if fim - inicio > 1:
        meio = (fim + inicio) // 2
        mergesort(lista, inicio, meio)
        mergesort(lista, meio, fim)
        comparacoes += merge(lista, inicio, meio, fim)


def merge(lista, inicio, meio, fim):
    global comparacoes

    left = lista[inicio:meio]
    right = lista[meio:fim]
    top_left, top_right = 0, 0
    comparacoes_merge = 0

    for k in range(inicio, fim):
        if top_left >= len(left):
            lista[k] = right[top_right]
            top_right += 1
        elif top_right >= len(right):
            lista[k] = left[top_left]
            top_left += 1
        else:
            comparacoes += 1 
            comparacoes_merge += 1
            if left[top_left] <= right[top_right]:
                lista[k] = left[top_left]
                top_left += 1
            else:
                lista[k] = right[top_right]
                top_right += 1

    return comparacoes_merge 


def execute_mergesort(dataset):
    global comparacoes
    comparacoes = 0

    start_time = time.perf_counter()
    mergesort(dataset)
    end_time = time.perf_counter()

    print(dataset)
    print(f"Tempo: {end_time - start_time:.10f} segundos")
    print(f"Comparações: {comparacoes}")
    print("Trocas: N/A")
    print("")

dataset1 = [87, 91, 2, 15, 60, 78, 99, 58, 23, 37]
dataset2 = [231, 103, 52, 233, 493, 85, 110, 68, 320, 235, 323, 457, 295, 445, 227, 396, 449, 276, 232, 450, 382, 284, 272, 341, 46, 376, 485, 245, 427, 150, 19, 200, 82, 310, 172, 74, 203, 352, 392, 53, 69, 173, 470, 11, 178, 47, 127, 431, 13, 249]
dataset3 = [117, 143, 505, 212, 717, 708, 169, 298, 897, 140, 731, 635, 20, 769, 351, 721, 119, 330, 935, 819, 148, 514, 801, 311, 74, 880, 592, 567, 430, 156, 726, 112, 892, 75, 281, 884, 504, 634, 252, 399, 141, 214, 774, 498, 397, 953, 648, 163, 519, 6, 253, 917, 966, 740, 17, 978, 685, 64, 750, 603, 739, 913, 370, 348, 965, 586, 912, 679, 270, 4, 537, 500, 825, 400, 867, 539, 1000, 28, 734, 157, 826, 201, 5, 932, 125, 969, 788, 818, 996, 308, 918, 245, 618, 814, 128, 854, 506, 251, 136, 562]
dataset4 = [804, 504, 287, 150, 524, 726, 336, 208, 121, 280,
428, 313, 119, 879, 206, 134, 298, 40, 704, 171,
605, 61, 508, 843, 788, 609, 702, 232, 333, 58,
400, 499, 929, 802, 593, 221, 891, 547, 562, 255,
10, 447, 844, 756, 429, 122, 469, 622, 936, 57,
274, 603, 95, 564, 682, 190, 574, 736, 164, 922,
120, 346, 772, 711, 662, 604, 628, 919, 694, 934,
462, 448, 996, 534, 611, 689, 652, 110, 851, 653,
157, 420, 290, 937, 824, 623, 439, 722, 512, 717,
687, 12, 656, 350, 537, 730, 354, 73, 494, 869,
866, 381, 146, 585, 946, 790, 918, 685, 285, 900,
894, 990, 278, 199, 238, 556, 467, 427, 859, 24,
338, 515, 670, 731, 104, 331, 921, 42, 85, 776,
826, 176, 544, 963, 198, 289, 812, 651, 795, 300,
132, 729, 324, 998, 332, 940, 838, 525, 759, 637,
282, 848, 11, 803, 595, 488, 217, 139, 643, 926,
527, 563, 930, 522, 692, 901, 830, 849, 959, 470,
853, 79, 351, 740, 700, 845, 363, 560, 474, 235,
127, 371, 431, 850, 69, 774, 707, 21, 316, 174,
65, 614, 633, 650, 516, 182, 323, 912, 678, 88,
732, 801, 98, 748, 478, 647, 753, 355, 28, 584,
330, 228, 951, 645, 71, 482, 31, 935, 422, 493,
402, 407, 950, 388, 491, 309, 749, 964, 796, 993,
74, 523, 893, 77, 376, 568, 185, 545, 90, 519,
920, 148, 972, 186, 941, 883, 7, 89, 557, 307,
249, 8, 138, 822, 94, 721, 464, 579, 468, 406,
733, 236, 567, 663, 648, 39, 266, 264, 541, 343,
735, 676, 888, 246, 938, 260, 273, 820, 194, 403,
397, 931, 606, 565, 189, 624, 112, 117, 315, 542,
761, 209, 356, 954, 108, 870, 421, 156, 168, 294,
877, 367, 348, 340, 416, 911, 783, 597, 498, 956,
520, 172, 301, 510, 128, 245, 616, 337, 724, 655,
187, 486, 805, 137, 163, 277, 251, 151, 809, 555,
864, 703, 654, 142, 979, 779, 59, 705, 49, 135,
674, 976, 807, 533, 281, 973, 454, 487, 220, 968,
671, 819, 239, 440, 443, 344, 54, 791, 642, 161,
197, 966, 561, 799, 396, 618, 45, 399, 369, 839,
384, 409, 26, 578, 4, 554, 718, 785, 109, 389,
612, 615, 72, 184, 483, 310, 335, 329, 806, 312,
836, 992, 29, 582, 591, 326, 781, 295, 38, 143,
764, 658, 237, 141, 292, 60, 875, 101, 123, 107,
860, 821, 827, 147, 34, 314, 816, 927, 317, 868,
811, 885, 507, 982, 479, 27, 449, 334, 903, 1,
320, 339, 353, 621, 70, 18, 5, 723, 37, 553,
828, 155, 207, 372, 96, 425, 896, 598, 23, 160,
159, 258, 725, 492, 414, 375, 882, 706, 63, 571,
17, 210, 928, 744, 272, 386, 408, 965, 140, 500,
14, 720, 259, 684, 213, 125, 322, 30, 581, 773,
130, 601, 620, 223, 641, 825, 6, 276, 444, 433,
867, 506, 275, 842, 710, 481, 728, 91, 768, 361,
627, 345, 898, 496, 341, 417, 924, 957, 419, 252,
480, 349, 502, 170, 535, 666, 786, 586, 325, 115,
673, 949, 540, 379, 863, 149, 319, 412, 93, 766,
126, 131, 668, 975, 437, 263, 712, 902, 514, 193,
78, 52, 22, 573, 41, 978, 20, 580, 881, 683,
861, 672, 215, 436, 495, 974, 455, 977, 708, 485,
989, 987, 907, 179, 818, 669, 909, 680, 572, 87,
383, 750, 450, 382, 916, 716, 180, 257, 153, 583,
758, 913, 415, 833, 607, 288, 413, 962, 358, 800,
960, 392, 599, 847, 677, 899, 418, 438, 832, 789,
229, 878, 219, 829, 608, 570, 948, 763, 538, 719,
787, 874, 366, 279, 857, 442, 401, 374, 430, 162,
798, 183, 518, 727, 166, 243, 472, 528, 840, 391,
457, 588, 823, 696, 886, 969, 490, 67, 395, 632,
546, 576, 398, 347, 646, 767, 559, 517, 629, 638,
895, 476, 327, 265, 817, 214, 635, 780, 102, 43,
178, 378, 952, 944, 66, 473, 831, 884, 299, 46,
953, 167, 321, 357, 737, 814, 81, 854, 747, 105,
897, 551, 318, 531, 196, 630, 852, 222, 530, 856,
97, 775, 794, 513, 734, 306, 958, 212, 771, 855,
75, 2, 631, 271, 352, 876, 411, 111, 739, 997,
475, 701, 695, 751, 370, 195, 887, 917, 760, 667,
241, 435, 113, 872, 587, 505, 231, 777, 661, 754,
985, 387, 463, 284, 988, 293, 50, 521, 906, 477,
765, 203, 484, 304, 532, 233, 793, 446, 889, 715,
360, 552, 458, 910, 970, 955, 664, 434, 769, 660,
84, 423, 596, 915, 873, 36, 106, 594, 152, 44,
679, 55, 200, 64, 262, 270, 362, 460, 205, 770,
13, 862, 933, 224, 188, 124, 634, 169, 649, 441,
33, 51, 62, 390, 762, 625, 745, 908, 158, 550,
136, 923, 385, 269, 204, 342, 713, 9, 456, 904,
995, 56, 686, 503, 558, 129, 784, 191, 983, 693,
305, 858, 424, 994, 529, 741, 939, 841, 709, 364,
432, 114, 15, 35, 526, 47, 613, 466, 665, 3,
394, 404, 201, 410, 234, 778, 932, 575, 86, 489,
247, 961, 890, 986, 261, 813, 871, 659, 53, 452,
592, 914, 253, 835, 268, 453, 405, 25, 32, 82,
640, 782, 865, 626, 297, 600, 577, 19, 99, 699,
590, 947, 373, 808, 302, 688, 984, 461, 445, 254,
697, 752, 539, 16, 291, 308, 815, 942, 68, 644,
359, 548, 133, 610, 589, 738, 543, 165, 118, 501,
92, 154, 1000, 116, 691, 173, 834, 690, 230, 509,
83, 714, 810, 636, 892, 880, 103, 211, 617, 471,
743, 945, 536, 242, 80, 365, 746, 256, 100, 227,
971, 283, 240, 905, 602, 639, 681, 76, 250, 459,
267, 675, 175, 426, 144, 999, 742, 311, 451, 218,
837, 216, 757, 393, 797, 846, 296, 980, 967, 286,
566, 511, 619, 328, 244, 755, 657, 202, 226, 569,
981, 380, 181, 145, 177, 225, 368, 465, 925, 303,
792, 549, 991, 497, 248, 698, 48, 943, 192, 377,
]

print("Dataset1")
print("Dataset2")
execute_mergesort(dataset2)
print("Dataset3")
execute_mergesort(dataset3)
print("Dataset4")
execute_mergesort(dataset4)
