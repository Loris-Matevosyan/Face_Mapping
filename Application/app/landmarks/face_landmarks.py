
class FaceLandmarks():

    def __init__(self):

        self.__forehead_landmarks = [10,21,54,67,68,69,103,104,108,109,151,297,299,298,
                                   332,333,337,338]

        self.__left_eyebrow_landmarks = [276,282,283,285,293,295,296,300,334,336,383]

        self.__right_eyebrow_landmarks = [46,52,53,55,63,65,70,105,107,139,156]

        self.__left_eye_landmarks = [249,252,253,254,255,256,257,258,259,260,263,286,339,341,
                                   359,362,373,374,380,381,382,384,385,386,387,388,390,
                                   413,414,441,442,443,444,445,446,463,464,466,467]

        self.__right_eye_landmarks = [7,22,23,24,25,26,27,28,29,30,33,56,110,112,113,
                                    130,133,144,145,153,154,155,157,158,159,160,161,
                                    163,173,189,190,221,222,223,224,225,226,243,246]

        self.__left_cheekbone_landmarks = [266,277,280,329,330,340,345,346,347,348,349,350,
                                         352,355,371,376,411,423,426,425,427,448,449,450,
                                         451]

        self.__right_cheekbone_landmarks = [31,111,36,50,100,101,116,117,118,119,120,123,142,147,187,
                                          205,207,228,229,230,231,232]

        self.__nose_landmarks = [1,2,4,5,6,8,3,19,20,44,45,48,49,51,59,60,64,75,79,94,97,98,99,
                               102,115,114,122,125,126,128,129,131,134,141,168,166,174,188,193,
                               195,196,197,198,209,217,218,219,220,236,237,238,239,240,241,242,
                               244,245,248,250,274,275,278,279,281,289,290,294,305,309,326,327,
                               328,331,343,344,351,354,358,360,363,370,392,399,412,417,419,420,
                               429,437,438,439,440,455,456,457,458,459,460,461,462,465]

        self.__lips_landmarks = [0,11,13,14,15,16,17,37,38,39,40,41,42,61,62,72,73,74,
                               76,77,78,80,81,82,84,85,86,87,88,89,90,91,95,96,146,
                               178,179,180,181,183,184,185,191,267,268,269,270,271,
                               272,291,292,302,303,304,306,307,308,310,311,312,314,
                               315,316,317,318,319,320,321,324,325,375,402,403,404,
                               405,407,408,409,415]

    def foreheadLandmarks(self):
        return self.__forehead_landmarks

    def leftEyeLandmarks(self):
        return self.__left_eye_landmarks

    def rightEyeLandmarks(self):
        return self.__right_eye_landmarks

    def leftCheekboneLandmarks(self):
        return self.__left_cheekbone_landmarks

    def rightCheekboneLandmarks(self):
        return self.__right_cheekbone_landmarks

    def leftEyebrowLandmarks(self):
        return self.__left_eyebrow_landmarks

    def rightEyebrowLandmarks(self):
        return self.__right_eyebrow_landmarks

    def noseLandmarks(self):
        return self.__nose_landmarks

    def lipsLandmarks(self):
        return self.__lips_landmarks