from experta import *
# # from Core.rule import CLOTHES ,age,SkinColor,Season,Occasion,Person_type,Gender,search

class age(Fact):
    pass
# لون الجلد
class SkinColor(Fact):
    pass
# جنس
class Gender(Fact):
    pass

# نمط الشخص
class Person_type(Fact):
    pass
# مناسبة
class Occasion(Fact):
    pass
# لون
class Color(Fact):
    pass
# بنطال
class Trousers(Fact):
    pass
#  بنطال عريض
class wide_pants(Fact):
    pass


# كنزة
class T_Shirt(Fact):
    pass
# قميص
class Shirt(Fact):
    pass
#
class MidSkirt(Fact):
    pass

class shortSkirt(Fact):
    pass
# حذاء
class Shoes(Fact):
    pass
# طقم رسمي
class formal_suit(Fact):
    pass

# صندل
class Sandal(Fact):
    pass
# كندرة
class Kandra(Fact):
    pass
# معطف
class Coat(Fact):
    pass
# طاقية
class Hat(Fact):
    pass

# كرافة
class carafe(Fact):
    pass
# جاكيت
class Jacket(Fact):
    pass
# فصل
class Season(Fact):
    pass


# فستان طويل
class Long_robe(Fact):
    pass


# فستان متوسط الطول
class MidiDress(Fact):
    pass


# فستان قصير
class Midriff(Fact):
    pass


# عباءة التخرج
class graduation_gown(Fact):
    pass


# تنورة
class Skirt(Fact):
    pass


# حزام
class waistband(Fact):
    pass


# نص كم

class T_Shirt(Fact):
    pass


# بنطال بجامة
class pajama(Fact):
    pass


# شرط
class short(Fact):
    pass


# كنزة مع طاقية
class Hoodie(Fact):
    pass


# طقم رسمي
class formal_suit(Fact):
    pass


# طقم رسمي للمراة
class formal_suit_skirt(Fact):
    pass


class piece_name(Fact):
    pass


class piece_color(Fact):
    pass


class piece_type(Fact):
    pass


class Myclothes():

    # بنطال
    trousers = 0
    colortrousers = ""
    typetrousers = ""
    #  كنزة
    T_Shirt = 0
    colorT_Shirt = ""
    typeT_Shirt = ""
    #  قميص
    shirt = 0
    colorShirt = ""
    typeShirt = ""
    #  تنورة
    skirt = 0
    colorSkirt = ""
    typeSkirt = ""
    #  حذاء
    shoes = 0
    colorShoes = ""
    typeShoes = ""
    #  معطف
    coat = 0
    colorCoats = ""
    typeCoat = ""
    # طاقية
    Hat = 0
    colorHat = ""
    typeHat = ""
    #  كرافة
    carafe = 0
    colorcarafe = ""
    typecarafe = ""
    #  جاكيت
    Jacket = 0
    colorJacket = ""
    typeJacket = ""
    #
    dress = 0
    colorDress = ""
    typeDress = ""
    #  حزام
    waistband = 0
    colorwaistband = ""
    typewaistband = ""

    #  طقم
    formal_suit = 0
    colorformal_suit = ""
    typeformal_suit = ""
    # عباية تخرج
    graduation_gown = 0
    colorgraduation_gown = ""
    typegraduation_gown = ""

    #
    def __init__(self,

                 trousers,
                 colortrousers,
                 typetrousers,

                 T_Shirt,
                 colorT_Shirt,
                 typeT_Shirt,

                 shirt,
                 colorShirt,
                 typeShirt,

                 skirt,
                 colorSkirt,
                 typeSkirt,

                 shoes,
                 colorShoes,
                 typeShoes,

                 coat,
                 colorCoats,
                 typeCoat,

                 Hat,
                 colorHat,
                 typeHat,

                 carafe,
                 colorcarafe,
                 typecarafe,

                 Jacket,
                 colorJacket,
                 typeJacket,

                 dress,
                 colorDress,
                 typeDress,

                 waistband,
                 colorwaistband,
                 typewaistband,

                 formal_suit,
                 colorformal_suit,
                 typeformal_suit,

                 graduation_gown,
                 colorgraduation_gown,
                 typegraduation_gown,

                 ):
        self.trousers = trousers
        self.colortrousers = colortrousers
        self.typetrousers = typetrousers

        self.T_Shirt = T_Shirt
        self.colorT_Shirt = colorT_Shirt
        self.typeT_Shirt = typeT_Shirt

        self.shirt = shirt
        self.colorShirt = colorShirt
        self.typeShirt = typeShirt

        self.skirt = skirt
        self.colorSkirt = colorSkirt
        self.typeSkirt = typeSkirt

        self.shoes = shoes
        self.colorShoes = colorShoes
        self.typeShoes = typeShoes

        self.coat = coat
        self.colorCoats = colorCoats
        self.typeCoat = typeCoat

        self.Hat = Hat
        self.colorHat = colorHat
        self.typeHat = typeHat

        self.carafe = carafe
        self.colorcarafe = colorcarafe
        self.typecarafe = typecarafe

        self.Jacket = Jacket
        self.colorJacket = colorJacket
        self.typeJacket = typeJacket

        self.dress = dress
        self.colorDress = colorDress
        self.typeDress = typeDress

        self.waistband = waistband
        self.colorwaistband = colorwaistband
        self.typewaistband = typewaistband

        self.formal_suit = formal_suit
        self.colorformal_suit = colorformal_suit
        self.typeformal_suit = typeformal_suit

        self.graduation_gown = graduation_gown
        self.colorgraduation_gown = colorgraduation_gown
        self.typegraduation_gown = typegraduation_gown

class CLOTHES(KnowledgeEngine):
    # """ trousers,T_shirt,shirt,skirt,shoes,coat,Hat,carafe,Jacket,dress,waistband,formal_suit, graduation_gown"""
    result = []
    myclothes=Myclothes(0,"","",0,"","",0,"","",0,"","",0,"","",0,"","",0,"","",0,"","",0,"","",0,"","",0,"","",0,"","",0,"","")
    @DefFacts()
    def _init_(self):
        self.result = []
        yield age(16)


    # ///////////////////////////////////////////////////////////////////المرحلة الاولى
    # مقابلة التخرج
    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='white'),Occasion('work'), Gender('male'), Person_type('officer'), Season("summer")), salience=1)
    def clothes(self):
        self.myclothes = Myclothes(1, "darkblue", "Trousers", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "brown",
                                   "shose", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 11, "brown",
                                   "waistband", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='white'),
              Occasion('work'), Gender('male'), Person_type('officer'), Season("summer")), salience=1)
    def clothes0(self):
        self.myclothes = Myclothes(1, "beige", "Trousers", 0, "", "", 3, "cyan", "Shirt", 0, "", "", 5, "brown",
                                   "shose", 6, "white", "Coat", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 11, "brown",
                                   "waistband", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='white'),
              Occasion('work'), Gender('male'), Person_type('officer'), Season("winter")), salience=1)
    def clothes00(self):
        self.myclothes = Myclothes(1, "beige", "Trousers", 2, "black", "T_Shirt", 3, "cyan", "Shirt", 0, "", "", 5, "brown",
                                   "shose", 6, "white", "Coat", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 11, "brown",
                                   "waistband", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)
    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('work'), Gender('male'), Person_type('officer'), Season("summer")), salience=1)
    def clothes1(self):
        self.myclothes = Myclothes(1, "black", "Trousers", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "black",
                                   "shose", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 11, "black",
                                   "waistband", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='dark'),
              Occasion('work'), Gender('male'), Person_type('officer'), Season("summer")), salience=1)
    def clothes2(self):
        self.myclothes = Myclothes(1, "gray", "Trousers", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "black",
                                   "shose", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 11, "black",
                                   "waistband", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='white'),
              Occasion('work'), Gender('female'), Person_type('officer'), Season("summer")), salience=1)
    def clothes3(self):
        self.myclothes = Myclothes(1, "darkblue", "wide_pants", 0, "", "", 3, "white", "Shirt", 0, "", "", 5,
                                   "beige ", "Kandra", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 11,
                                   "beige", "waistband", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('work'), Gender('female'), Person_type('officer'), Season("summer")), salience=1)
    def clothes4(self):
        self.myclothes = Myclothes(1, "black", "wide_pants", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "vinous",
                                   "Kandra", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 11, "vinous",
                                   "waistband", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)
    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('work'), Gender('female'), Person_type('officer'), Season("summer")), salience=1)
    def clothes41111(self):
        self.myclothes = Myclothes(1, "darkblue", "wide_pants", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "beige",
                                   "Kandra", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 11, "beige",
                                   "waistband", 0, "", "", 0, "", "")

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('work'), Gender('female'), Person_type('officer'), Season("summer")), salience=1)
    def clothes41151(self):
        self.myclothes = Myclothes(1, "darkblue", "wide_pants", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "beige",
                                   "Kandra", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 11, "beige",
                                   "waistband", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)
    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='dark'),
              Occasion('work'), Gender('female'), Person_type('officer'), Season("summer")), salience=1)
    def clothes5(self):
        self.myclothes = Myclothes(1, "gray", "wide_pants", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "black",
                                   "Kandra", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 11, "black", "waistband", 0,
                                   "", "", 0, "", "")
        self.result.append(self.myclothes)
    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='dark'),
              Occasion('work'), Gender('female'), Person_type('officer'), Season("winter")), salience=1)
    def clothes5333(self):
        self.myclothes = Myclothes(1, "gray", "wide_pants", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "black",
                                   "Kandra", 6, "black", "Coat", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 11, "black", "waistband", 0,
                                   "", "", 0, "", "")
        self.result.append(self.myclothes)
    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='white'),
              Occasion('work'), Gender('female'), Person_type('officer'), Season("summer")), salience=1)
    def clothes20(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 4, "darkblue", "shortSkirt", 5,
                                   "darkblue", "Kandra", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "",
                                   "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('work'), Gender('female'), Person_type('officer'), Season("winter")), salience=1)
    def clothes6(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 4, "black", "shortSkirt", 5, "black",
                                   "Kandra", 0, "", "", 0, "", "", 0, "", "", 9, "black", "Jacket", 0, "", "", 0, "",
                                   "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('work'), Gender('female'), Person_type('officer'), Season("winter")), salience=1)
    def clothes6m(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 4, "black", "shortSkirt", 5, "black",
                                   "Kandra", 0, "", "", 0, "", "", 0, "", "", 9, "black", "Jacket", 0, "", "", 0, "",
                                   "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='dark'),
              Occasion('work'), Gender('female'), Person_type('officer'), Season("summer")), salience=1)
    def clothes7(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 4, "gray", "shortSkirt", 5, "black",
                                   "Kandra", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "",
                                   "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='dark'),
              Occasion('work'), Gender('female'), Person_type('officer'), Season("winter")), salience=1)
    def clothes7v(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 4, "gray", "shortSkirt", 5, "black",
                                   "Kandra", 0, "", "", 0, "", "", 0, "", "", 9, "black", "Jacket", 0, "", "", 0, "",
                                   "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='white'),
              Occasion('work'), Gender('male'), Person_type('business'), Season("summer")), salience=1)
    def clothes8(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "brown", "Kandra", 0, "",
                                   "", 0, "", "", 8, "darkblue", "carafe", 0, "", "", 0, "", "", 11, "brown", "waistband", 12,
                                   "darkblue", "formal_suit", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='white'),
              Occasion('work'), Gender('male'), Person_type('business'), Season("summer")), salience=1)
    def clothes9999998(self):
        self.myclothes = Myclothes(1, "black" , "Trousers", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "brown", "Kandra", 0, "",
                                   "", 0, "", "", 8, "darkblue", "carafe", 0, "", "", 0, "", "", 11, "brown", "waistband", 0,
                                   "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('work'), Gender('male'), Person_type('business'), Season("summer")), salience=1)
    def clothes9977998(self):
        self.myclothes = Myclothes(1, "gray" , "Trousers", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "brown", "Kandra", 0, "",
                                   "", 0, "", "", 8, "darkblue", "carafe", 0, "", "", 0, "", "", 11, "brown", "waistband", 0,
                                   "", "", 0, "", "")
        self.result.append(self.myclothes)
    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('work'), Gender('male'), Person_type('business'), Season("summer")), salience=1)
    def clothes9(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "black", "Kandra", 0, "",
                                   "", 0, "", "", 8, "vinous", "carafe", 0, "", "", 0, "", "", 0, "", "", 12, "black",
                                   "formal_suit", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='dark'),
              Occasion('work'), Gender('male'), Person_type('business'), Season("summer")), salience=1)
    def clothes10(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "black", "Kandra", 0, "",
                                   "", 0, "", "", 8, "black", "carafe", 0, "", "", 0, "", "", 0, "", "", 12, "gray",
                                   "formal_suit", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='white'),
              Occasion('work'), Gender('female'), Person_type('business'), Season("summer")), salience=1)
    def clothes11(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "darkblue", "Kandra", 0,
                                   "", "", 0, "", "", 8, "darkblue", "carafe", 0, "", "", 0, "", "", 0, "", "", 12,
                                   "darkblue", "formal_suit_skirt")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('work'), Gender('female'), Person_type('business'), Season("summer")), salience=1)
    def clothes12(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "black", "Kandra", 0, "",
                                   "", 0, "", "", 8, "vinous", "carafe", 0, "", "", 0, "", "", 0, "", "", 12, "black",
                                   "formal_suit_skirt", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='dark'),
              Occasion('work'), Gender('female'), Person_type('business'), Season("summer")), salience=1)
    def clothes13(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "black", "Kandra", 0, "",
                                   "", 0, "", "", 8, "black", "carafe", 0, "", "", 0, "", "", 0, "", "", 12, "gray",
                                   "formal_suit_skirt", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)



    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='white'),
              Occasion('work'), Gender('male'), Person_type('engineer'), Season("summer")), salience=1)
    def clothes14(self):
        self.myclothes = Myclothes(1, "darkblue", "jeans", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "white",
                                   "shose", 0, "", "", 7, "yellow", "Hat", 0, "", "", 9, "orange", "Jacket", 0, "", "",
                                   0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('work'), Gender('male'), Person_type('engineer'), Season("summer")), salience=1)
    def clothes15(self):
        self.myclothes = Myclothes(1, "darkblue", "jeans", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "white",
                                   "shose", 0, "", "", 7, "yellow", "Hat", 0, "", "", 9, "orange", "Jacket", 0, "", "",
                                   0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='dark'),
              Occasion('work'), Gender('male'), Person_type('engineer'), Season("summer")), salience=1)
    def clothes16(self):
        self.myclothes = Myclothes(1, "darkblue", "jeans", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "white",
                                   "shose", 0, "", "", 7, "yellow", "Hat", 0, "", "", 9, "orange", "Jacket", 0, "", "",
                                   0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='white'),
              Occasion('work'), Gender('female'), Person_type('engineer'), Season("summer")), salience=1)
    def clothes17(self):
        self.myclothes = Myclothes(1, "darkblue", "jeans", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "white",
                                   "shose", 0, "", "", 7, "yellow", "Hat", 0, "", "", 9, "orange", "Jacket", 0, "", "",
                                   0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('work'), Gender('female'), Person_type('engineer'), Season("summer")), salience=1)
    def clothes18(self):
        self.myclothes = Myclothes(1, "darkblue", "jeans", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "white",
                                   "shose", 0, "", "", 7, "yellow", "Hat", 0, "", "", 9, "orange", "Jacket", 0, "", "",
                                   0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='dark'),
              Occasion('work'), Gender('female'), Person_type('engineer'), Season("summer")), salience=1)
    def clothes19(self):
        self.myclothes = Myclothes(1, "darkblue", "jeans", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "white",
                                   "shose", 0, "", "", 7, "yellow", "Hat", 0, "", "", 9, "orange", "Jacket", 0, "", "",
                                   0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('work'), Gender('male'), Person_type('officer'), Season("winter")), salience=1)
    def clothes21(self):
        self.myclothes = Myclothes(1, "black", "Trousers", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "brown",
                                   "shose", 6, "black", "Coat", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 11, "brown",
                                   "waistband", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='dark'),
              Occasion('work'), Gender('male'), Person_type('officer'), Season("winter")), salience=1)
    def clothes22(self):
        self.myclothes = Myclothes(1, "gray", "Trousers", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "black",
                                   "shose", 6, "gray", "Coat", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 11, "black",
                                   "waistband", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='white'),
              Occasion('work'), Gender('female'), Person_type('officer'), Season("winter")), salience=1)
    def clothes23(self):
        self.myclothes = Myclothes(1, "darkblue", "wide_pants", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "beige",
                                   "Kandra", 6, "darkblue", "Coat", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 11,
                                   "beige", "waistband", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='white'),
              Occasion('work'), Gender('male'), Person_type('officer'), Season("winter")), salience=1)
    def clothes24(self):
        self.myclothes = Myclothes(1, "darkblue", "Trousers", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "beige",
                                   "Kandra", 6, "darkblue", "Coat", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 11,
                                   "beige", "waistband", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('work'), Gender('female'), Person_type('officer'), Season("winter")), salience=1)
    def clothes25(self):
        self.myclothes = Myclothes(1, "black", "Trousers", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "black",
                                   "Kandra", 6, "black", "Coat", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 11,
                                   "black", "waistband", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='dark'),
              Occasion('work'), Gender('female'), Person_type('officer'), Season("winter")), salience=1)
    def clothes26(self):
        self.myclothes = Myclothes(1, "gray", "Trousers", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "black",
                                   "Kandra", 6, "black", "Coat", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 11,
                                   "black", "waistband", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='white'),
              Occasion('work'), Gender('female'), Person_type('officer'), Season("winter")), salience=1)
    def clothes27(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 4, "darkblue", "shortSkirt", 5, "beige",
                                   "Kandra", 6, "beige", "Coat", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 11,
                                   "beige", "waistband", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('work'), Gender('female'), Person_type('officer'), Season("winter")), salience=1)
    def clothes28(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 4, "black", "shortSkirt", 5, "black",
                                   "Kandra", 6, "vinous", "Coat", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 11,
                                   "black", "waistband", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='dark'),
              Occasion('work'), Gender('female'), Person_type('officer'), Season("winter")), salience=1)
    def clothes29(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 4, "gray", "shortSkirt", 5, "black",
                                   "Kandra", 6, "gray", "Coat", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 11,
                                   "black", "waistband", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='white'),
              Occasion('work'), Gender('male'), Person_type('business'), Season("winter")), salience=1)
    def clothes30(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "brown", "Kandra", 6,
                                   "brown", "Coat", 0, "", "", 8, "darkblue", "carafe", 0, "", "", 0, "", "", 0, "", "",
                                   12, "darkblue", "formal_suit")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('work'), Gender('male'), Person_type('business'), Season("winter")), salience=1)
    def clothes31(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "black", "Kandra", 6,
                                   "black", "Coat", 0, "", "", 8, "vinous", "carafe", 0, "", "", 0, "", "", 0, "", "",
                                   12, "black", "formal_suit", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='dark'),
              Occasion('work'), Gender('male'), Person_type('business'), Season("winter")), salience=1)
    def clothes32(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "black", "Kandra", 6,
                                   "black", "Coat", 0, "", "", 8, "black", "carafe", 0, "", "", 0, "", "", 0, "", "",
                                   12, "gray", "formal_suit_skirt", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='white'),
              Occasion('work'), Gender('female'), Person_type('business'), Season("winter")), salience=1)
    def clothes33(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "beige", "Kandra", 6,
                                   "beige", "Coat", 0, "", "", 8, "beige", "carafe", 0, "", "", 0, "", "", 0, "", "",
                                   12, "darkblue", "formal_suit_skirt", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('work'), Gender('female'), Person_type('business'), Season("winter")), salience=1)
    def clothes34(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "vinous", "Kandra", 6,
                                   "black", "Coat", 0, "", "", 8, "vinous", "carafe", 0, "", "", 0, "", "", 0, "", "",
                                   12, "black", "formal_suit_skirt", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='dark'),
              Occasion('work'), Gender('female'), Person_type('business'), Season("winter")), salience=1)
    def clothes35(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "black", "Kandra", 6,
                                   "black", "Coat", 0, "", "", 8, "black", "carafe", 0, "", "", 0, "", "", 0, "", "",
                                   12, "gray", "formal_suit_skirt", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='white'),
              Occasion('work'), Gender('male'), Person_type('engineer'), Season("winter")), salience=1)
    def clothes36(self):
        self.myclothes = Myclothes(1, "darkblue", "jeans", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "white",
                                   "shose", 6, "darkblue", "Coat", 7, "yellow", "Hat", 0, "", "", 9, "orange",
                                   "Jacket", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('work'), Gender('male'), Person_type('engineer'), Season("winter")), salience=1)
    def clothes37(self):
        self.myclothes = Myclothes(1, "cyan", "jeans", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "white", "shose",
                                   6, "black", "Coat", 7, "yellow", "Hat", 0, "", "", 9, "orange", "Jacket", 0, "", "",
                                   0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='dark'),
              Occasion('work'), Gender('male'), Person_type('engineer'), Season("winter")), salience=1)
    def clothes38(self):
        self.myclothes = Myclothes(1, "darkblue", "jeans", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "white",
                                   "shose", 6, "black", "Coat", 7, "yellow", "Hat", 0, "", "", 9, "orange", "Jacket",
                                   0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='white'),
              Occasion('work'), Gender('female'), Person_type('engineer'), Season("winter")), salience=1)
    def clothes39(self):
        self.myclothes = Myclothes(1, "darkblue", "jeans", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "white",
                                   "shose", 6, "darkblue", "Coat", 7, "yellow", "Hat", 0, "", "", 9, "orange",
                                   "Jacket", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('work'), Gender('female'), Person_type('engineer'), Season("winter")), salience=1)
    def clothes40(self):
        self.myclothes = Myclothes(1, "darkblue", "jeans", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "white",
                                   "shose", 6, "black", "Coat", 7, "yellow", "Hat", 0, "", "", 9, "orange", "Jacket",
                                   0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='dark'),
              Occasion('work'), Gender('female'), Person_type('Engineer'), Season("winter")), salience=1)
    def clothes41(self):
        self.myclothes = Myclothes(1, "darkblue", "jeans", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "white",
                                   "shose", 6, "black", "Coat", 7, "yellow", "Hat", 0, "", "", 9, "orange", "Jacket",
                                   0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    ##مناسبة التخرج

    @Rule(AND(age(value=P(lambda value: value >= 21) & P(lambda value: value <= 35)), SkinColor(color='dark'),
              Occasion('gradution'), Gender('female'), Person_type('student'), Season("summer")), salience=1)
    def clothes42(self):
        self.myclothes = Myclothes(0, "", " ", 0, "", "", 3, "white", "Shirt", 4, "black", "MidSkirt", 5, "black",
                                   "Kandra", 6, "black", "Coat", 7, "black", "Hat", 0, "", "", 0, "", "", 0, "", "", 0,
                                   "", "", 0, "", "", 13, "black", "graduation_gown")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 21) & P(lambda value: value <= 35)), SkinColor(color='dark'),
              Occasion('gradution'), Gender('female'), Person_type('student'), Season("summer")), salience=1)
    def clothes43(self):
        self.myclothes = Myclothes(0, "", " ", 0, "", "", 3, "white", "Shirt", 4, "vinous", "MidSkirt", 5, "black",
                                   "Kandra", 6, "black", "Coat", 7, "black", "Hat", 0, "", "", 0, "", "", 0, "", "", 0,
                                   "", "", 0, "", "", 13, "black", "graduation_gown")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 21) & P(lambda value: value <= 35)), SkinColor(color='dark'),
              Occasion('gradution'), Gender('female'), Person_type('student'), Season("summer")), salience=1)
    def clothes44(self):
        self.myclothes = Myclothes(0, "", " ", 0, "", "", 3, "white", "Shirt", 4, "black", "MidSkirt", 5, "vinous",
                                   "Kandra", 6, "black", "Coat", 7, "black", "Hat", 0, "", "", 0, "", "", 0, "", "", 0,
                                   "", "", 0, "", "", 13, "black", "graduation_gown")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 21) & P(lambda value: value <= 35)), SkinColor(color='dark'),
              Occasion('gradution'), Gender('female'), Person_type('student'), Season("summer")), salience=1)
    def clothes45(self):
        self.myclothes = Myclothes(0, "", " ", 0, "", "", 3, "white", "Shirt", 4, "gray", "MidSkirt", 5, "black",
                                   "Kandra", 6, "black", "Coat", 7, "black", "Hat", 0, "", "", 0, "", "", 0, "", "", 0,
                                   "", "", 0, "", "", 13, "black", "graduation_gown")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 21) & P(lambda value: value <= 35)), SkinColor(color='dark'),
              Occasion('gradution'), Gender('female'), Person_type('student'), Season("summer")), salience=1)
    def clothes46(self):
        self.myclothes = Myclothes(0, "", " ", 0, "", "", 3, "white", "Shirt", 4, " vinous", "MidSkirt", 5, "black",
                                   "Kandra", 6, "black", "Coat", 7, "black", "Hat", 0, "", "", 0, "", "", 0, "", "", 0,
                                   "", "", 0, "", "", 13, "black", "graduation_gown")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 21) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('gradution'), Gender('female'), Person_type('student'), Season("summer")), salience=1)
    def clothes47(self):
        self.myclothes = Myclothes(0, "", " ", 0, "", "", 3, "white", "Shirt", 4, "gray", "MidSkirt", 5, "black",
                                   "Kandra", 6, "black", "Coat", 7, "black", "Hat", 0, "", "", 0, "", "", 0, "", "", 0,
                                   "", "", 0, "", "", 13, "black", "graduation_gown")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 21) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('gradution'), Gender('female'), Person_type('student'), Season("summer")), salience=1)
    def clothes48(self):
        self.myclothes = Myclothes(0, "", " ", 0, "", "", 3, "white", "Shirt", 4, "black", "MidSkirt", 5, "vinous",
                                   "Kandra", 6, "black", "Coat", 7, "black", "Hat", 0, "", "", 0, "", "", 0, "", "", 0,
                                   "", "", 0, "", "", 13, "black", "graduation_gown")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 21) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('gradution'), Gender('female'), Person_type('student'), Season("summer")), salience=1)
    def clothes49(self):
        self.myclothes = Myclothes(0, "", " ", 0, "", "", 3, "white", "Shirt", 4, " black", "MidSkirt", 5, "black",
                                   "Kandra", 6, "black", "Coat", 7, "black", "Hat", 0, "", "", 0, "", "", 0, "", "", 0,
                                   "", "", 0, "", "", 13, "black", "graduation_gown")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 21) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('gradution'), Gender('female'), Person_type('student'), Season("summer")), salience=1)
    def clothes50(self):
        self.myclothes = Myclothes(0, "", " ", 0, "", "", 3, "cyan", "Shirt", 4, "black", "MidSkirt", 5, "black",
                                   "Kandra", 6, "black", "Coat", 7, "black", "Hat", 0, "", "", 0, "", "", 0, "", "", 0,
                                   "", "", 0, "", "", 13, "black", "graduation_gown")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 21) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('gradution'), Gender('female'), Person_type('student'), Season("summer")), salience=1)
    def clothes51(self):
        self.myclothes = Myclothes(0, "", " ", 0, "", "", 3, "white", "Shirt", 4, "vinous", "MidSkirt", 5, "black",
                                   "Kandra", 6, "black", "Coat", 7, "black", "Hat", 0, "", "", 0, "", "", 0, "", "", 0,
                                   "", "", 0, "", "", 13, "black", "graduation_gown")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 21) & P(lambda value: value <= 35)), SkinColor(color='hanatawi'),
              Occasion('gradution'), Gender('female'), Person_type('student'), Season("summer")), salience=1)
    def clothes52(self):
        self.myclothes = Myclothes(0, "", " ", 0, "", "", 3, "white", "Shirt", 4, " black", "MidSkirt", 5, "black",
                                   "Kandra", 6, "black", "Coat", 7, "black", "Hat", 0, "", "", 0, "", "", 0, "", "", 0,
                                   "", "", 0, "", "", 13, "black", "graduation_gown")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 21) & P(lambda value: value <= 35)), SkinColor(color='hanatawi'),
              Occasion('gradution'), Gender('female'), Person_type('student'), Season("summer")), salience=1)
    def clothes53(self):
        self.myclothes = Myclothes(1, "black", "wide_pants", 0, "", "", 3, "white", "Shirt", 0, " ", "", 5, "black",
                                   "Kandra", 0, "", "", 7, "black", "Hat", 0, "", "", 0, "", "", 0, "", "", 0, "", "",
                                   0, "", "", 13, "black", "graduation_gown")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 21) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('gradution'), Gender('female'), Person_type('student'), Season("summer")), salience=1)
    def clothes54(self):
        self.myclothes = Myclothes(0, "", " ", 0, "", "", 3, "pink ", "Shirt", 4, " black", "MidSkirt", 5, "black",
                                   "Kandra", 0, "", "", 7, "black", "Hat", 0, "", "", 0, "", "", 0, "", "", 0, "", "",
                                   0, "", "", 13, "black", "graduation_gown")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 21) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('gradution'), Gender('female'), Person_type('student'), Season("summer")), salience=1)
    def clothes55(self):
        self.myclothes = Myclothes(1, "black", "wide_pants", 0, "", "", 3, "pink", "Shirt", 0, " ", "", 5, "black",
                                   "Kandra", 0, "", "", 7, "black", "Hat", 0, "", "", 0, "", "", 0, "", "", 0, "", "",
                                   0, "", "", 13, "black", "graduation_gown")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 21) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('gradution'), Gender('female'), Person_type('student'), Season("summer")), salience=1)
    def clothes56(self):
        self.myclothes = Myclothes(0, "", " ", 0, "", "", 3, "white ", "Shirt", 4, "vinous", "MidSkirt", 5, "black",
                                   "Kandra", 0, "", "", 7, "black", "Hat", 0, "", "", 0, "", "", 0, "", "", 0, "", "",
                                   0, "", "", 13, "black", "graduation_gown")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 21) & P(lambda value: value <= 35)), SkinColor(color='hanatawi'),
              Occasion('gradution'), Gender('female'), Person_type('student'), Season("summer")), salience=1)
    def clothes57(self):
        self.myclothes = Myclothes(0, "", " ", 0, "", "", 3, "white", "Shirt", 4, "black", "MidSkirt", 5, "black",
                                   "Kandra", 0, "", "", 7, "black", "Hat", 0, "", "", 0, "", "", 0, "", "", 0, "", "",
                                   0, "", "", 13, "black", "graduation_gown")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 21) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('gradution'), Gender('female'), Person_type('student'), Season("summer")), salience=1)
    def clothes58(self):
        self.myclothes = Myclothes(0, "", " ", 0, "", "", 3, "pink", "Shirt", 4, "black", "MidSkirt", 5, "black",
                                   "Kandra", 0, "", "", 7, "black", "Hat", 0, "", "", 0, "", "", 0, "", "", 0, "", "",
                                   0, "", "", 13, "black", "graduation_gown")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 21) & P(lambda value: value <= 35)), SkinColor(color='dark'),
              Occasion('gradution'), Gender('female'), Person_type('student'), Season("summer")), salience=1)
    def clothes59(self):
        self.myclothes = Myclothes(0, "", " ", 0, "", "", 3, "white", "Shirt", 4, "vinous", "MidSkirt", 5, "black",
                                   "Kandra", 0, "", "", 7, "black", "Hat", 0, "", "", 0, "", "", 0, "", "", 0, "", "",
                                   0, "", "", 13, "black", "graduation_gown")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 21) & P(lambda value: value <= 35)), SkinColor(color='dark'),
              Occasion('gradution'), Gender('female'), Person_type('student'), Season("summer")), salience=1)
    def clothes60(self):
        self.myclothes = Myclothes(1, "white", "wide_pants", 0, "", "", 3, "white", "Shirt", 0, " ", "", 5, "black",
                                   "Kandra", 0, "", "", 7, "black", "Hat", 0, "", "", 0, "", "", 0, "", "", 0, "", "",
                                   0, "", "", 13, "black", "graduation_gown")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 21) & P(lambda value: value <= 35)), SkinColor(color='hanatawi'),
              Occasion('gradution'), Gender('female'), Person_type('student'), Season("summer")), salience=1)
    def clothes600(self):
        self.myclothes = Myclothes(1, "white", "wide_pants", 0, "", "", 3, "white", "Shirt", 0, " ", "", 5, "white",
                                   "Kandra", 6, "pink", "Coat", 7, "black", "Hat", 0, "", "", 0, "", "", 0, "", "", 0,
                                   "", "", 0, "", "", 13, "black", "graduation_gown")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 21) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('gradution'), Gender('female'), Person_type('student'), Season("summer")), salience=1)
    def clothes601(self):
        self.myclothes = Myclothes(0, " ", " ", 0, "", "", 3, "white", "Shirt", 4, "beige", "MidSkirt", 5, "beige",
                                   "Kandra", 0, "", "", 7, "black", "Hat", 0, "", "", 9, "oil", "Jacket", 0, "", "", 0,
                                   "", "", 0, "", "", 13, "black", "graduation_gown")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 21) & P(lambda value: value <= 35)), SkinColor(color='hanatawi'),
              Occasion('gradution'), Gender('female'), Person_type('student'), Season("summer")), salience=1)
    def clothes602(self):
        self.myclothes = Myclothes(0, " ", " ", 0, "", "", 3, "white", "Shirt", 4, "black", "MidSkirt", 5, "black",
                                   "Kandra", 6, "vinous", "Coat", 7, "black", "Hat", 0, "", "", 0, "", "", 0, "", "", 0,
                                   "", "", 0, "", "", 13, "black", "graduation_gown")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 21) & P(lambda value: value <= 35)), SkinColor(color='hanatawi'),
              Occasion('gradution'), Gender('female'), Person_type('student'), Season("summer")), salience=1)
    def clothes64402(self):
        self.myclothes = Myclothes(0, " ", " ", 0, "", "", 3, "white", "Shirt", 4, "darkblue", "MidSkirt", 5, "gray",
                                   "Kandra", 6, "cyan", "Coat", 7, "black", "Hat", 0, "", "", 0, "", "", 0, "", "", 0,
                                   "", "", 0, "", "", 13, "black", "graduation_gown")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 21) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('gradution'), Gender('male'), Person_type('student'), Season("summer")), salience=1)
    def clothes61(self):
        self.myclothes = Myclothes(1, "gray", "Trousers", 0, "", "", 3, "white", "Shirt", 0, " ", "", 5, "darkblue",
                                   "Kandra", 0, "", "", 7, "black", "Hat", 8, "darkblue", "carafe", 0, "", "", 0, "",
                                   "", 0, "", "", 0, "", "", 13, "black", "graduation_gown")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 21) & P(lambda value: value <= 35)), SkinColor(color='hanatawi'),
              Occasion('gradution'), Gender('male'), Person_type('student'), Season("summer")), salience=1)
    def clothes62(self):
        self.myclothes = Myclothes(1, "black", "Trousers", 0, "", "", 3, "white", "Shirt", 0, " ", "", 5, "black",
                                   "Kandra", 0, "", "", 7, "black", "Hat", 8, "vinous", "carafe", 0, "", "", 0, "", "",
                                   0, "", "", 0, "", "", 13, "black", "graduation_gown")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 21) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('gradution'), Gender('male'), Person_type('student'), Season("summer")), salience=2)
    def clothes63(self):
        self.myclothes = Myclothes(1, "darkblue", "Trousers", 0, "", "", 3, "cyan", "Shirt", 0, " ", "", 5, "brown",
                                   "Kandra", 0, "", "", 7, "black", "Hat", 8, "darkblue", "carafe", 0, "", "", 0, "",
                                   "", 0, "", "", 0, "", "", 13, "black", "graduation_gown")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 21) & P(lambda value: value <= 35)), SkinColor(color='hanatawi'),
              Occasion('gradution'), Gender('male'), Person_type('student'), Season("summer")), salience=2)
    def clothes64(self):
        self.myclothes = Myclothes(1, "gray", "Trousers", 0, "", "", 3, "white", "Shirt", 0, " ", "", 5, "black",
                                   "Kandra", 0, "", "", 7, "black", "Hat", 8, "darkblue", "carafe", 0, "", "", 0, "",
                                   "", 0, "", "", 0, "", "", 13, "black", "graduation_gown")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 21) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('gradution'), Gender('male'), Person_type('student'), Season("summer")), salience=2)
    def clothes65(self):
        self.myclothes = Myclothes(1, "darkblue", "Trousers", 0, "", "", 3, "beige", "Shirt", 0, " ", "", 5,
                                   "darkblue", "Kandra", 0, "", "", 7, "black", "Hat", 8, "beige", "carafe", 0, "", "",
                                   0, "", "", 0, "", "", 0, "", "", 13, "black", "graduation_gown")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 21) & P(lambda value: value <= 35)), SkinColor(color='dark'),
              Occasion('gradution'), Gender('male'), Person_type('student'), Season("summer")), salience=2)
    def clothes66(self):
        self.myclothes = Myclothes(1, "gray", "Trousers", 0, "", "", 3, "white", "Shirt", 0, " ", "", 5, "grown",
                                   "Kandra", 0, "", "", 7, "black", "Hat", 8, "black", "carafe", 0, "", "", 0, "", "",
                                   0, "", "", 0, "", "", 13, "black", "graduation_gown")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 21) & P(lambda value: value <= 35)), SkinColor(color='dark'),
              Occasion('gradution'), Gender('male'), Person_type('student'), Season("summer")), salience=2)
    def clothes67(self):
        self.myclothes = Myclothes(1, "vinous", "Trousers", 0, "", "", 3, "white", "Shirt", 0, " ", "", 5, "black",
                                   "Kandra", 0, "", "", 7, "black", "Hat", 8, "vinous", "carafe", 0, "", "", 0, "", "",
                                   0, "", "", 0, "", "", 13, "black", "graduation_gown")
        self.result.append(self.myclothes)

    #  مناسبة زفاف
    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='dark'),
              Occasion('wadding'), Gender('male'), Person_type('brother'), Season("summer")), salience=1)
    def clothes68(self):
        self.myclothes = Myclothes(1, "black", "Trousers", 0, "", "", 3, "white", "Shirt", 0, " ", "", 5, "gray",
                                   "shose", 0, "", "", 0, "", "", 8, "gray", "carafe", 0, "", "", 0, "", "", 11,
                                   "black", "waistband", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='dark'),
              Occasion('wadding'), Gender('male'), Person_type('brother'), Season("summer")), salience=1)
    def clothes69(self):
        self.myclothes = Myclothes(1, "gray", "Trousers", 0, "", "", 3, "white", "Shirt", 0, " ", "", 5, "brown",
                                   "shose", 0, "", "", 0, "", "", 8, "grown", "carafe", 0, "", "", 0, "", "", 11,
                                   "black", "waistband", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('male'), Person_type('brother'), Season("summer")), salience=1)
    def clothes70(self):
        self.myclothes = Myclothes(1, "darkblue", "Trousers", 0, "", "", 3, "white", "Shirt", 0, " ", "", 5, "black",
                                   "shose", 0, "", "", 0, "", "", 8, "vinous", "carafe", 0, "", "", 0, "", "", 11,
                                   "black", "waistband", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='hanatawi'),
              Occasion('wadding'), Gender('male'), Person_type('brother'), Season("summer")), salience=1)
    def clothes71(self):
        self.myclothes = Myclothes(1, "black", "Trousers", 0, "", "", 3, "white", "Shirt", 0, " ", "", 5, "black",
                                   "shose", 0, "", "", 0, "", "", 8, "black", "carafe", 0, "", "", 0, "", "", 11,
                                   "black", "waistband", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='hanatawi'),
              Occasion('wadding'), Gender('male'), Person_type('friend'), Season("summer")), salience=1)
    def clothes72(self):
        self.myclothes = Myclothes(1, "white", "Trousers", 0, "", "", 3, "white", "Shirt", 0, " ", "", 5, "brown",
                                   "shose", 6, "darkblue", "Coat", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 11,
                                   "brown", "waistband", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='hanatawi'),
              Occasion('wadding'), Gender('male'), Person_type('friend'), Season("summer")), salience=1)
    def clothes73(self):
        self.myclothes = Myclothes(1, "black", "Trousers", 0, "", "", 3, "pink", "Shirt", 0, " ", "", 5, "black",
                                   "shose", 0, "", "", 0, "", "", 8, "black", "carafe", 0, "", "", 0, "", "", 11,
                                   "black", "waistband", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='dark'),
              Occasion('wadding'), Gender('male'), Person_type('friend'), Season("summer")), salience=1)
    def clothes74(self):
        self.myclothes = Myclothes(1, "gray", "Trousers ", 0, "", "", 3, "white", "Shirt", 0, " ", "", 5, "brown",
                                   "shose", 0, "", "", 0, "", "", 8, "darkblue", "carafe", 0, "", "", 0, "", "", 11,
                                   "brown", "waistband", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('male'), Person_type('friend'), Season("summer")), salience=1)
    def clothes75(self):
        self.myclothes = Myclothes(1, "darkblue", "Trousers", 0, "", "", 3, "cyan", "Shirt", 0, " ", "", 5, "brown",
                                   "shose", 0, "", "", 0, "", "", 8, "grown", "carafe", 0, "", "", 0, "", "", 11,
                                   "brown", "waistband", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('male'), Person_type('friend'), Season("summer")), salience=1)
    def clothes76(self):
        self.myclothes = Myclothes(1, "black", "Trousers", 0, "", "", 3, "gray", "Shirt", 0, " ", "", 5, "black",
                                   "shose", 0, "", "", 0, "", "", 8, "black", "carafe", 0, "", "", 0, "", "", 11,
                                   "black", "waistband", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='dark'),
              Occasion('wadding'), Gender('male'), Person_type('relatives'), Season("summer")), salience=1)
    def clothes77(self):
        self.myclothes = Myclothes(1, "gray", "Trousers", 0, "", "", 3, "white", "Shirt", 0, " ", "", 5, "brown",
                                   "shose", 0, "", "", 0, "", "", 8, "black", "carafe", 0, "", "", 0, "", "", 0, "", "",
                                   0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='dark'),
              Occasion('wadding'), Gender('male'), Person_type('relatives'), Season("summer")), salience=1)
    def clothes78(self):
        self.myclothes = Myclothes(1, "darkblue", "jeans", 0, "", "", 3, "gray", "Shirt", 0, " ", "", 5, "brown",
                                   "shose", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 11, "black",
                                   "waistband", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='hanatawi'),
              Occasion('wadding'), Gender('male'), Person_type('relatives'), Season("summer")), salience=1)
    def clothes79(self):
        self.myclothes = Myclothes(1, "black", "Trousers", 0, "", "", 3, "vinous", "Shirt", 0, " ", "", 5, "black",
                                   "shose", 0, "", "", 0, "", "", 8, "black", "carafe", 0, "", "", 0, "", "", 11,
                                   "black", "waistband", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='hanatawi'),
              Occasion('wadding'), Gender('male'), Person_type('relatives'), Season("summer")), salience=1)
    def clothes80(self):
        self.myclothes = Myclothes(1, "black", "jeans", 2, "brown", "T_Shirt", 0, "", "", 0, " ", "", 5, "black",
                                   "shose", 0, "", "", 0, "", "", 8, "black", "carafe", 0, "", "", 0, "", "", 11,
                                   "black", "waistband", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='dark'),
              Occasion('wadding'), Gender('male'), Person_type('relatives'), Season("summer")), salience=1)
    def clothes81(self):
        self.myclothes = Myclothes(1, "brown", "Trousers", 2, "beige", "T_Shirt", 0, "", "", 0, " ", "", 5, "brown",
                                   "shose", 0, "", "", 0, "", "", 8, "brown", "carafe", 0, "", "", 0, "", "", 11,
                                   "brown", "waistband", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('male'), Person_type('relatives'), Season("summer")), salience=1)
    def clothes82(self):
        self.myclothes = Myclothes(1, " darkblue", "jeans", 0, "", "", 3, "cyan", "Shirt", 0, " ", "", 5, "black",
                                   "shose", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 11, "black",
                                   "waistband", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('male'), Person_type('relatives'), Season("summer")), salience=1)
    def clothes83(self):
        self.myclothes = Myclothes(1, "black", "Trousers", 0, "", "", 3, "oil", "Shirt", 0, " ", "", 5, "black",
                                   "shose", 0, "", "", 0, "", "", 8, "black", "carafe", 0, "", "", 0, "", "", 11,
                                   "black", "waistband", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('male'), Person_type('relatives'), Season("summer")), salience=1)
    def clothes84(self):
        self.myclothes = Myclothes(1, "darkblue", "Trousers", 2, "beige", "T_Shirt", 0, "", "", 0, " ", "", 5,
                                   "brown", "shose", 0, "", "", 0, "", "", 8, "black", "carafe", 0, "", "", 0, "", "",
                                   11, "black", "waistband", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('female'), Person_type('relatives'), Season("summer")), salience=1)
    def clothes85(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, " ", "", 0, "", "", 5, "black", "Kandra ", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "", 10, "black", "Mididress", 0, "", "", 0, "", "", 0, "",
                                   "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('female'), Person_type('relatives'), Season("summer")), salience=1)
    def clothes86(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 0, "", "", 5, "black", "Kandra", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "", 10, " vinous", "Mididress", 0, "", "", 0, "", "", 0,
                                   "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('female'), Person_type('relatives'), Season("summer")), salience=1)
    def clothes87(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 0, "", "", 5, "black", "Kandra", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "", 10, "pink", "Long_robe", 0, "", "", 0, "", "", 0, "",
                                   "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('female'), Person_type('relatives'), Season("summer")), salience=1)
    def clothes88(self):
        self.myclothes = Myclothes(1, "cyan", "jeans", 2, "pink", "T_Shirt", 0, "", "", 0, " ", "", 5, "white",
                                   "Kandra", 0, "", "", 0, "", "", 0, " ", "", 0, "", "", 0, "", "", 11, "black",
                                   "waistband", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('female'), Person_type('relatives'), Season("summer")), salience=1)
    def clothes89(self):
        self.myclothes = Myclothes(1, "black", "jeans", 2, "yellow", "T_Shirt", 0, "", "", 0, " ", "", 5, "black",
                                   "Kandra", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 11, "black",
                                   "waistband", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='dark'),
              Occasion('wadding'), Gender('female'), Person_type('relatives'), Season("summer")), salience=1)
    def clothes90(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 0, "", "", 5, "silver", "Kandra", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "", 10, "blue", "Mididress", 0, "", "", 0, "", "", 0, "",
                                   "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='dark'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer")), salience=1)
    def clothes91(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 0, " ", "", 5, "black", "Kandra", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "", 10, "gray", "Midriff", 0, "", "", 0, "", "", 0, "",
                                   "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='dark'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer")), salience=1)
    def clothes800(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 0, " ", "", 5, "white", "Kandra", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "", 10, "pink", "Midriff", 0, "", "", 0, "", "", 0, "",
                                   "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='dark'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer")), salience=1)
    def clothes92(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 0, "", "", 5, "silver", "Kandra", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "", 10, "pink", "Mididress", 0, "", "", 0, "", "", 0, "",
                                   "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='dark'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer")), salience=1)
    def clothes93(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, " ", "", 0, " ", "", 5, "gold", "Kandra", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "", 10, "red", "Mididress", 0, "", "", 0, "", "", 0, "",
                                   "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='dark'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer")), salience=1)
    def clothes94(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, " ", "", 0, " ", "", 5, "black", "Kandra", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "", 10, "gold", "Long_robe", 0, "", "", 0, "", "", 0, "",
                                   "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='dark'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer")), salience=1)
    def clothes95(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 0, "", "", 5, "black", "Kandra", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "", 10, "silver", "Long_robe", 0, "", "", 0, "", "", 0, "",
                                   "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='dark'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer")), salience=1)
    def clothes96(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, " ", "", 0, "", "", 5, "vinous", "Kandra", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "", 10, " black", "Long_robe", 0, "", "", 0, "", "", 0, "",
                                   "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='dark'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer")), salience=1)
    def clothes97(self):
        self.myclothes = Myclothes(1, "black", "Trousers", 0, "", "", 3, "white", "Shirt", 0, " ", "", 5, "black",
                                   "Kandra", 5, "vinous", "Coat", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 11,
                                   "black", "waistband", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='dark'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer")), salience=1)
    def clothes98(self):
        self.myclothes = Myclothes(1, "cyan", "jeans", 2, "yellow", "T_Shirt", 0, "", "", 0, "", "", 5, "black",
                                   "Kandra", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "",
                                   "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='dark'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer")), salience=1)
    def clothes99(self):
        self.myclothes = Myclothes(1, "black", "wide_pants", 2, "pink", "T_Shirt", 0, "", "", 0, "", "", 5, "black",
                                   "Kandra", 0, "", "", 0, "", "", 0, " ", "", 0, "", "", 0, "", "", 0, "", "", 0, "",
                                   "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='dark'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer")), salience=1)
    def clothes100(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "red", "Shirt", 4, "white", "shortSkirt", 5, "white",
                                   "Kandra", 6, "black", "Coat", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "",
                                   "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='dark'),
              Occasion('wadding'), Gender('female'), Person_type('relatives'), Season("summer")), salience=1)
    def clothes101(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, " ", "", 0, " ", "", 5, "black", "Kandra", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "", 10, "beige", "Mididress", 0, "", "", 0, "", "", 0, "",
                                   "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='dark'),
              Occasion('wadding'), Gender('female'), Person_type('relatives'), Season("summer")), salience=1)
    def clothes102(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, " ", "", 0, "", "", 5, "black", "Kandra", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "", 10, "gray", "Long_robe", 0, "", "", 0, "", "", 0, "",
                                   "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='dark'),
              Occasion('wadding'), Gender('female'), Person_type('relatives'), Season("summer")), salience=1)
    def clothes103(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, " ", "", 0, "", "", 5, "vinous", "Kandra ", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "", 10, "black", "Long_robe", 0, "", "", 0, "", "", 0, "",
                                   "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='dark'),
              Occasion('wadding'), Gender('female'), Person_type('relatives'), Season("summer")), salience=1)
    def clothes104(self):
        self.myclothes = Myclothes(1, "cyan", "jeans", 2, "black", "T_Shirt", 0, "", "", 0, " ", "", 5, "white",
                                   "shose", 0, "", "", 0, "", "", 0, " ", "", 0, "", "", 0, "", "", 0, "", "", 0, "",
                                   "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='dark'),
              Occasion('wadding'), Gender('female'), Person_type('relatives'), Season("summer")), salience=1)
    def clothes105(self):
        self.myclothes = Myclothes(1, "darkblue", "jeans", 2, "yellow", "T_Shirt", 0, "", "", 0, "", "", 5, "white",
                                   "shose", 0, "", "", 0, "", "", 0, " ", "", 0, "", "", 0, "", "", 0, "", "", 0, "",
                                   "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='dark'),
              Occasion('wadding'), Gender('female'), Person_type('relatives'), Season("summer")), salience=1)
    def clothes106(self):
        self.myclothes = Myclothes(1, "cyan", "jeans", 2, "pink", "T_Shirt", 0, "", "", 0, "", "", 5, "white",
                                   "shose", 0, "", "", 0, "", "", 0, " ", "", 0, "", "", 0, "", "", 0, "", "", 0, "",
                                   "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='dark'),
              Occasion('wadding'), Gender('female'), Person_type('relatives'), Season("summer")), salience=1)
    def clothes107(self):
        self.myclothes = Myclothes(0, "", "", 2, "red", "T_Shirt", 0, "", "", 4, "white", "MidSkirt", 5, "white",
                                   "shose", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, " ", "", 0, "", "", 0, "",
                                   "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='hanatawi'),
              Occasion('wadding'), Gender('female'), Person_type('relatives'), Season("summer")), salience=1)
    def clothes108(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 0, " ", "", 5, "gold", "Kandra", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "", 10, "red", "Mididress", 0, "", "", 0, "", "", 0, "",
                                   "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='hanatawi'),
              Occasion('wadding'), Gender('female'), Person_type('relatives'), Season("summer")), salience=1)
    def clothes109(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 0, "", "", 5, "black", "Kandra ", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "", 10, "pink", "Mididress", 0, "", "", 0, "", "", 0, "",
                                   "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='hanatawi'),
              Occasion('wadding'), Gender('female'), Person_type('relatives'), Season("summer")), salience=1)
    def clothes110(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 0, "", "", 5, "black", "Kandra", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "", 10, "glod", "Long_robe", 0, "", "", 0, "", "", 0, "",
                                   "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='hanatawi'),
              Occasion('wadding'), Gender('female'), Person_type('relatives'), Season("summer")), salience=1)
    def clothes111(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 0, "", "", 5, "black", "Kandra", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "", 10, "pink", "Long_robe", 0, "", "", 0, "", "", 0, "",
                                   "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='hanatawi'),
              Occasion('wadding'), Gender('female'), Person_type('relatives'), Season("summer")), salience=1)
    def clothes112(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 0, "", "", 5, "vinous", "Kandra", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "", 10, "black", "Long_robe", 0, "", "", 0, "", "", 0, "",
                                   "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='hanatawi'),
              Occasion('wadding'), Gender('female'), Person_type('relatives'), Season("summer")), salience=1)
    def clothes113(self):
        self.myclothes = Myclothes(1, "white", "jeans", 2, "pink", "T_Shirt", 0, "", "", 0, " ", "", 5, "white",
                                   "shose", 0, "", "", 0, "", "", 0, " ", "", 0, "", "", 0, "", "", 0, "", "", 0, "",
                                   "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='hanatawi'),
              Occasion('wadding'), Gender('female'), Person_type('relatives'), Season("summer")), salience=1)
    def clothes114(self):
        self.myclothes = Myclothes(1, "cyan", "jeans", 2, "yellow", "T_Shirt", 0, "", "", 0, " ", "", 5, "white",
                                   "shose", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "",
                                   "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='hanatawi'),
              Occasion('wadding'), Gender('female'), Person_type('relatives'), Season("summer")), salience=1)
    def clothes115(self):
        self.myclothes = Myclothes(1, "black", "jeans", 2, "vinous", "T_Shirt", 0, "", "", 0, " ", "", 5, "white",
                                   "shose", 0, "", "", 0, "", "", 0, " ", "", 0, "", "", 0, "", "", 0, "", "", 0, "",
                                   "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='hanatawi'),
              Occasion('wadding'), Gender('female'), Person_type('relatives'), Season("summer")), salience=1)
    def clothes116(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 4, "black", "MidSkirt", 5, "black",
                                   "Kandra", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "",
                                   "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='hanatawi'),
              Occasion('wadding'), Gender('female'), Person_type('brother'), Season("summer")), salience=1)
    def clothes117(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 0, "", "", 5, "gold", "Kandra", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "", 10, "gold", "Midriff", 0, "", "", 0, "", "", 0, "",
                                   "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='hanatawi'),
              Occasion('wadding'), Gender('female'), Person_type('brother'), Season("summer")), salience=1)
    def clothes118(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 0, "", "", 5, "black", "Kandra", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "", 10, "silver", "Midriff", 0, "", "", 0, "", "", 0, "",
                                   "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer")), salience=1)
    def clothes119(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 0, "", "", 5, "white", "Sandal", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "", 10, "pink", "Midriff", 0, "", "", 0, "", "", 0, "",
                                   "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer")), salience=1)
    def clothes120(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 0, "", "", 5, "black", "Kandra ", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "", 10, "pink", "Midriff", 0, "", "", 0, "", "", 0, "",
                                   "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer")), salience=1)
    def clothes121(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 0, "", "", 5, "pink", "Kandra", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "", 10, "darkblue", "Midriff", 0, "", "", 0, "", "", 0,
                                   "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer")), salience=1)
    def clothes122(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 0, "", "", 5, "black", "Kandra", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "", 10, "red", "Midriff", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer")), salience=1)
    def clothes123(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, " ", "", 0, " ", "", 5, "silver", "Kandra", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "", 10, "pink", "Long_robe", 0, "", "", 0, "", "", 0, "",
                                   "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer")), salience=1)
    def clothes124(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 0, "", "", 5, "black", "Kandra", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "", 10, "beige", "Long_robe", 0, "", "", 0, "", "", 0, "",
                                   "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer")), salience=1)
    def clothes125(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 0, "", "", 5, "silver", "Kandra", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "", 10, "black", "Long_robe", 0, "", "", 0, "", "", 0, "",
                                   "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer")), salience=1)
    def clothes126(self):
        self.myclothes = Myclothes(1, "cyan", "jeans", 2, "green", "T_Shirt", 0, "", "", 0, "", "", 5, "white",
                                   "shose", 0, "", "", 0, "", "", 0, " ", "", 0, "", "", 0, "", "", 0, "", "", 0, "",
                                   "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer")), salience=1)
    def clothes127(self):
        self.myclothes = Myclothes(1, "cyan", "jeans", 2, "vinous", "T_Shirt", 0, "", "", 0, "", "", 5, "white",
                                   "shose", 0, "", "", 0, "", "", 0, " ", "", 0, "", "", 0, "", "", 0, "", "", 0, "",
                                   "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer")), salience=1)
    def clothes128(self):
        self.myclothes = Myclothes(1, "black", "wide_pants", 0, "", "", 3, "white", "Shirt", 0, " ", "", 5, "black",
                                   "Kandra", 0, "", "", 0, "", "", 0, " ", "", 0, "", "", 0, "", "", 0, "", "", 0, "",
                                   "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer")), salience=1)
    def clothes129(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "cyan", "Shirt", 4, "darkblue", "MidSkirt", 5, "silver",
                                   "Kandra", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, " ", "", 0, "", "", 0, "",
                                   "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer")), salience=1)
    def clothes130(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "pink", "Shirt", 4, "white", "MidSkirt", 5, "pink",
                                   "Kandra", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "",
                                   "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='hanatawi'),
              Occasion('wadding'), Gender('female'), Person_type('brother'), Season("summer")), salience=1)
    def clothes131(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 0, "", "", 5, "black", "Kandra", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "", 10, "gold", "Mididress", 0, "", "", 0, "", "", 0, "",
                                   "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='hanatawi'),
              Occasion('wadding'), Gender('female'), Person_type('brother'), Season("summer")), salience=1)
    def clothes132(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, " ", "", 0, "", "", 5, "gold", "Kandra", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "", 10, "vinous", "Mididress", 0, "", "", 0, "", "", 0,
                                   "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='hanatawi'),
              Occasion('wadding'), Gender('female'), Person_type('brother'), Season("summer")), salience=1)
    def clothes133(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, " ", "", 0, "", "", 5, "black", "Kandra", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "", 10, "pink", "Long_robe", 0, "", "", 0, "", "", 0, "",
                                   "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='hanatawi'),
              Occasion('wadding'), Gender('female'), Person_type('brother'), Season("summer")), salience=1)
    def clothes134(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 0, "", "", 5, "silver", "Kandra", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "", 10, "silver", "Long_robe", 0, "", "", 0, "", "", 0,
                                   "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='hanatawi'),
              Occasion('wadding'), Gender('female'), Person_type('brother'), Season("summer")), salience=1)
    def clothes135(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 0, "", "", 5, "vinous", "Kandra", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "", 10, "black", "Long_robe", 0, "", "", 0, "", "", 0, "",
                                   "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='hanatawi'),
              Occasion('wadding'), Gender('female'), Person_type('brother'), Season("summer")), salience=1)
    def clothes136(self):
        self.myclothes = Myclothes(1, "white", "Trousers", 2, "vinous", "T_Shirt", 0, "", "", 0, " ", "", 5, "white",
                                   "shose", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "",
                                   "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='hanatawi'),
              Occasion('wadding'), Gender('female'), Person_type('brother'), Season("summer")), salience=1)
    def clothes137(self):
        self.myclothes = Myclothes(1, "black", "wide_pants", 0, "", "", 3, "white", "Shirt", 0, " ", "", 5, "black",
                                   "Kandra", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "",
                                   "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='hanatawi'),
              Occasion('wadding'), Gender('female'), Person_type('brother'), Season("summer")), salience=1)
    def clothes138(self):
        self.myclothes = Myclothes(0, "", "", 2, "white", "T_Shirt", 0, "", "", 4, "cyan", "MidSkirt", 5, "white",
                                   "shose", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "",
                                   "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('female'), Person_type('brother'), Season("summer")), salience=1)
    def clothes139(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 0, "", "", 5, "black", "Kandra", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "", 10, "gold", "Midriff", 0, "", "", 0, "", "", 0, "",
                                   "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('female'), Person_type('brother'), Season("summer")), salience=1)
    def clothes140(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 0, "", "", 5, "black", "Kandra", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "", 10, "silver", "Midriff", 0, "", "", 0, "", "", 0, "",
                                   "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('female'), Person_type('brother'), Season("summer")), salience=1)
    def clothes141(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 0, "", "", 5, "white", "Kandra", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "", 10, "pink", "Mididress", 0, "", "", 0, "", "", 0, "",
                                   "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('female'), Person_type('brother'), Season("summer")), salience=1)
    def clothes142(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 0, "", "", 5, "black", "Kandra", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "", 10, "vinous", "Mididress", 0, "", "", 0, "", "", 0,
                                   "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('female'), Person_type('brother'), Season("summer")), salience=1)
    def clothes143(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 0, "", "", 5, "black", "Kandra", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "", 10, "beige", "Long_robe", 0, "", "", 0, "", "", 0, "",
                                   "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('female'), Person_type('brother'), Season("summer")), salience=1)
    def clothes144(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 0, "", "", 5, "silver", "Kandra", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "", 10, "silver", "Long_robe", 0, "", "", 0, "", "", 0,
                                   "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('female'), Person_type('brother'), Season("summer")), salience=1)
    def clothes145(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 0, "", "", 5, "silver", "Kandra", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "", 10, "black", "Long_robe", 0, "", "", 0, "", "", 0, "",
                                   "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('female'), Person_type('brother'), Season("summer")), salience=1)
    def clothes146(self):
        self.myclothes = Myclothes(1, "white", "Trousers", 0, "", "", 3, "pink", "Shirt", 0, "", "", 5, "pink",
                                   "shose", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "",
                                   "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('female'), Person_type('brother'), Season("summer")), salience=1)
    def clothes147(self):
        self.myclothes = Myclothes(1, "black", "wide_pants", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "black",
                                   "Kandra", 0, "", "", 0, "", "", 0, " ", "", 0, "", "", 0, "", "", 0, "", "", 0, "",
                                   "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('female'), Person_type('brother'), Season("summer")), salience=1)
    def clothes148(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "cyan", "Shirt", 4, "gray", "shortSkirt", 5, "gray",
                                   "Kandra", 6, "white", "Coat", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "",
                                   "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='dark'),
              Occasion('wadding'), Gender('female'), Person_type('brother'), Season("summer")), salience=1)
    def clothes149(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 0, "", "", 5, "black", "Kandra", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "", 10, "gold", "Midriff", 0, "", "", 0, "", "", 0, "",
                                   "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='dark'),
              Occasion('wadding'), Gender('female'), Person_type('brother'), Season("summer")), salience=1)
    def clothes150(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 0, "", "", 5, "black", "Kandra", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "", 10, "silver", "Midriff", 0, "", "", 0, "", "", 0, "",
                                   "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='dark'),
              Occasion('wadding'), Gender('female'), Person_type('brother'), Season("summer")), salience=1)
    def clothes151(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 0, "", "", 5, "silver", "Kandra", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "", 10, "pink", "Mididress", 0, "", "", 0, "", "", 0, "",
                                   "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='dark'),
              Occasion('wadding'), Gender('female'), Person_type('brother'), Season("summer")), salience=1)
    def clothes152(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 0, "", "", 5, "gray", "Kandra", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "", 10, "blue", "Mididress", 0, "", "", 0, "", "", 0, "",
                                   "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='dark'),
              Occasion('wadding'), Gender('female'), Person_type('brother'), Season("summer")), salience=1)
    def clothes153(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 0, "", "", 5, "silver", "Kandra", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "", 10, "vinous", "Long_robe", 0, "", "", 0, "", "", 0,
                                   "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='dark'),
              Occasion('wadding'), Gender('female'), Person_type('brother'), Season("summer")), salience=1)
    def clothes154(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 0, "", "", 5, "silver", "Kandra", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "", 10, "gray", "Long_robe", 0, "", "", 0, "", "", 0, "",
                                   "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='dark'),
              Occasion('wadding'), Gender('female'), Person_type('brother'), Season("summer")), salience=1)
    def clothes155(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 0, "", "", 5, "silver", "Kandra", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "", 10, "black", "Long_robe", 0, "", "", 0, "", "", 0, "",
                                   "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='dark'),
              Occasion('wadding'), Gender('female'), Person_type('brother'), Season("summer")), salience=1)
    def clothes156(self):
        self.myclothes = Myclothes(1, " blue", "Trousers", 0, "", "", 3, "pink", "Shirt", 0, " ", "", 5, "pink",
                                   "Kandra", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "",
                                   "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='dark'),
              Occasion('wadding'), Gender('female'), Person_type('brother'), Season("summer")), salience=1)
    def clothes157(self):
        self.myclothes = Myclothes(1, "black", "wide_pants", 0, "", "", 3, "white", "Shirt", 0, " ", "", 5, "black",
                                   "Kandra", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "",
                                   "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='dark'),
              Occasion('wadding'), Gender('female'), Person_type('brother'), Season("summer")), salience=1)
    def clothes158(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 4, "black", "shortSkirt", 5, "black",
                                   "Kandra", 6, "black", "Coat", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "",
                                   "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='hanatawi'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer")), salience=1)
    def clothes159(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 0, "", "", 5, "pink", "Kandra", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "", 10, "white", "Midriff", 0, "", "", 0, "", "", 0, "",
                                   "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='hanatawi'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer")), salience=1)
    def clothes160(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 0, "", "", 5, "black", "Kandra", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "", 10, "pink", "Midriff", 0, "", "", 0, "", "", 0, "",
                                   "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='hanatawi'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer")), salience=1)
    def clothes161(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 0, "", "", 5, "white", "Sandal", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "", 10, "cyan", "Mididress", 0, "", "", 0, "", "", 0, "",
                                   "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='hanatawi'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer")), salience=1)
    def clothes162(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 0, "", "", 5, "white", "Sandal", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "", 10, "blue", "Mididress", 0, "", "", 0, "", "", 0, "",
                                   "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='hanatawi'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer")), salience=1)
    def clothes163(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 0, "", "", 5, "silver", "Kandra", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "", 10, "pink", "Long_robe", 0, "", "", 0, "", "", 0, "",
                                   "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='hanatawi'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer")), salience=1)
    def clothes164(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 0, "", "", 5, "black", "Kandra", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "", 10, "vinous", "Long_robe", 0, "", "", 0, "", "", 0,
                                   "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='hanatawi'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer")), salience=1)
    def clothes165(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 0, "", "", 5, "black", "Kandra", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "", 10, "black", "Long_robe", 0, "", "", 0, "", "", 0, "",
                                   "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='hanatawi'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer")), salience=1)
    def clothes166(self):
        self.myclothes = Myclothes(1, "cyan", "Trousers", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "cyan",
                                   "Kandra", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "",
                                   "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='hanatawi'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer")), salience=1)
    def clothes167(self):
        self.myclothes = Myclothes(1, "cyan", "jeans", 2, "vinous", "T_Shirt", 0, "", "", 0, "", "", 5, "white",
                                   "shose", 0, "", "", 0, "", "", 0, " ", "", 0, "", "", 0, "", "", 0, "", "", 0, "",
                                   "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='hanatawi'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer")), salience=1)
    def clothes168(self):
        self.myclothes = Myclothes(1, "black", "wide_pants", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "black",
                                   "Sandal", 0, "", "", 0, "", "", 0, " ", "", 0, "", "", 0, "", "", 0, "", "", 0, "",
                                   "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='hanatawi'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer")), salience=1)
    def clothes170(self):
        self.myclothes = Myclothes(0, "", "", 2, "yellow", "T_Shirt", 0, "", "", 4, "darkblue", "jeans", 5, "white",
                                   "shose", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "",
                                   "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer")), salience=1)
    def clothes171(self):
        self.myclothes = Myclothes(0, "", "", 2, "pink", "T_Shirt", 0, "", "", 4, "white", "jeans", 5, "white",
                                   "shose", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "",
                                   "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer")), salience=1)
    def clothes172(self):
        self.myclothes = Myclothes(0, "", "", 2, "pink", "T_Shirt", 0, "", "", 4, "cyan", "jeans", 5, "white",
                                   "shose", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "",
                                   "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer")), salience=1)
    def clothes173(self):
        self.myclothes = Myclothes(0, "", "", 2, "pink", "T_Shirt", 0, "", "", 4, "white", "jeans", 5, "white",
                                   "shose", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "",
                                   "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='hanatawi'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer")), salience=1)
    def clothes174(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 4, "pink", "MidSkirt", 5, "white",
                                   "Sandal", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, " ", "", 0, "", "", 0, "",
                                   "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer")), salience=1)
    def clothes175(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "red", "Shirt", 4, "blue", "MidSkirt", 5, "silver",
                                   "Kandra", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "",
                                   "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='hanatawi'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer")), salience=1)
    def clothes176(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "beige", "Shirt", 4, "vinous", "MidSkirt", 5, "black",
                                   "Kandra", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, " ", "", 0, "", "", 0, "",
                                   "", 0, "", "")
        self.result.append(self.myclothes)

    # مناسبة رياضة

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('Sport'), Gender('female'), Person_type('person'), Season("summer")), salience=1)
    def clothes178(self):
        self.myclothes = Myclothes(1, "pink", "pajama", 2, "pink", "Hoodie", 0, "", "", 0, "", "", 5, "white",
                                   "shose", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "",
                                   "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('Sport'), Gender('female'), Person_type('person'), Season("summer")), salience=1)
    def clothes179(self):
        self.myclothes = Myclothes(1, "orange", "pajama", 2, "orange", "Hoodie", 0, "", "", 0, "", "", 5, "white",
                                   "shose", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "",
                                   "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('Sport'), Gender('female'), Person_type('person'), Season("summer")), salience=1)
    def clothes180(self):
        self.myclothes = Myclothes(1, "yellow", "pajama", 2, "yellow", "Hoodie", 0, "", "", 0, " ", "", 5, "white",
                                   "shose", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "",
                                   "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='dark'),
              Occasion('Sport'), Gender('female'), Person_type('person'), Season("summer")), salience=1)
    def clothes181(self):
        self.myclothes = Myclothes(1, "blue", "pajama", 2, "blue", "Hoodie", 0, "", "", 0, " ", "", 5, "white",
                                   "shose", 0, "", "", 0, "", "", 0, " ", "", 0, "", "", 0, "", "", 0, "", "", 0, "",
                                   "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('Sport'), Gender('female'), Person_type('person'), Season("summer")), salience=1)
    def clothes182(self):
        self.myclothes = Myclothes(1, "red", "pajama", 2, "red", "Hoodie", 0, "", "", 0, "", "", 5, "white",
                                   "shose", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "",
                                   "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='dark'),
              Occasion('Sport'), Gender('female'), Person_type('person'), Season("summer")), salience=1)
    def clothes183(self):
        self.myclothes = Myclothes(1, "gray", "pajama", 2, "gray", "Hoodie", 0, "", "", 0, "", "", 5, "white",
                                   "shose", 0, "", "", 0, "", "", 0, " ", "", 0, "", "", 0, "", "", 0, "", "", 0, "",
                                   "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('Sport'), Gender('female'), Person_type('person'), Season("summer")), salience=1)
    def clothes184(self):
        self.myclothes = Myclothes(1, "black", "pajama", 2, "green", "Hoodie", 0, "", "", 0, "", "", 5, "white",
                                   "shose", 0, "", "", 0, "", "", 0, " ", "", 0, "", "", 0, "", "", 0, "", "", 0, "",
                                   "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='white'),
              Occasion('Sport'), Gender('female'), Person_type('person'), Season("summer")), salience=1)
    def clothes185(self):
        self.myclothes = Myclothes(1, "black", "pajama", 2, "red", "Hoodie", 0, "", "", 0, "", "", 5, "white",
                                   "shose", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "",
                                   "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='white'),
              Occasion('Sport'), Gender('female'), Person_type('person'), Season("summer")), salience=1)
    def clothes186(self):
        self.myclothes = Myclothes(1, "vinous", "pajama", 2, "vinous", "Hoodie", 0, "", "", 0, "", "", 5, "white",
                                   "shose", 0, "", "", 0, "", "", 0, " ", "", 0, "", "", 0, "", "", 0, "", "", 0, "",
                                   "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='dark'),
              Occasion('Sport'), Gender('female'), Person_type('person'), Season("summer")), salience=1)
    def clothes187(self):
        self.myclothes = Myclothes(1, "black", "pajama", 2, "vinous", "Hoodie", 0, "", "", 0, "", "", 5, "white",
                                   "shose", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "",
                                   "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='white'),
              Occasion('Sport'), Gender('female'), Person_type('person'), Season("summer")), salience=1)
    def clothes189(self):
        self.myclothes = Myclothes(1, "white", "pajama", 2, "white", "Hoodie", 0, "", "", 0, "", "", 5, "white",
                                   "shose", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "",
                                   "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('Sport'), Gender('female'), Person_type('person'), Season("summer")), salience=1)
    def clothes190(self):
        self.myclothes = Myclothes(1, "gray", "pajama", 2, "yellow", "Hoodie", 0, "", "", 0, "", "", 5, "white",
                                   "shose", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "",
                                   "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='dark'),
              Occasion('Sport'), Gender('female'), Person_type('person'), Season("summer")), salience=1)
    def clothes191(self):
        self.myclothes = Myclothes(1, "yellow", "pajama", 2, "green", "Hoodie", 0, "", "", 0, "", "", 5, "white",
                                   "shose", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "",
                                   "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('Sport'), Gender('female'), Person_type('person'), Season("summer")), salience=1)
    def clothes192(self):
        self.myclothes = Myclothes(1, "darkblue", "pajama", 2, "pink", "Hoodie", 0, "", "", 0, "", "", 5, "white",
                                   "shose", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "",
                                   "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('Sport'), Gender('female'), Person_type('person'), Season("summer")), salience=1)
    def clothes801(self):
        self.myclothes = Myclothes(1, "white", "pajama", 2, "green", "Hoodie", 0, "", "", 0, "", "", 5, "white",
                                   "shose", 0, "", "", 0, "", "", 0, " ", "", 0, "", "", 0, "", "", 0, "", "", 0, "",
                                   "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('Sport'), Gender('female'), Person_type('person'), Season("summer")), salience=1)
    def clothes193(self):
        self.myclothes = Myclothes(1, "darkblue", "pajama", 2, "white", "Hoodie", 0, "", "", 0, "", "", 5, "white",
                                   "shose", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "",
                                   "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('Sport'), Gender('female'), Person_type('person'), Season("summer")), salience=1)
    def clothes194(self):
        self.myclothes = Myclothes(1, "white", "beige", 2, "beige", "Hoodie", 0, "", "", 0, "", "", 5, "white",
                                   "shose", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "",
                                   "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('Sport'), Gender('female'), Person_type('person'), Season("summer")), salience=1)
    def clothes195(self):
        self.myclothes = Myclothes(1, "cyan", "pajama", 2, "cyan", "Hoodie", 0, "", "", 0, "", "", 5, "white",
                                   "shose", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "",
                                   "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('Sport'), Gender('male'), Person_type('person'), Season("summer")), salience=1)
    def clothes196(self):
        self.myclothes = Myclothes(1, "black", "pajama", 2, "black", "Hoodie", 0, "", "", 0, "", "", 5, "white",
                                   "shose", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "",
                                   "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('Sport'), Gender('male'), Person_type('person'), Season("summer")), salience=1)
    def clothes197(self):
        self.myclothes = Myclothes(1, "darlblue", "pajama", 2, "darlblue", "Hoodie", 0, "", "", 0, "", "", 5,
                                   "white", "shose", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "",
                                   0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('Sport'), Gender('male'), Person_type('person'), Season("summer")), salience=1)
    def clothes198(self):
        self.myclothes = Myclothes(1, "blue", "pajama", 2, "blue", "Hoodie", 0, "", "", 0, "", "", 5, "white",
                                   "shose", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "",
                                   "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('Sport'), Gender('male'), Person_type('person'), Season("summer")), salience=1)
    def clothes199(self):
        self.myclothes = Myclothes(1, "gray", "pajama", 2, "gray", "Hoodie", 0, "", "", 0, " ", "", 5, "white",
                                   "shose", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "",
                                   "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('Sport'), Gender('male'), Person_type('person'), Season("summer")), salience=1)
    def clothes200(self):
        self.myclothes = Myclothes(1, "vinous", "pajama", 2, "vinous", "Hoodie", 0, "", "", 0, "", "", 5, "white",
                                   "shose", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "",
                                   "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('Sport'), Gender('male'), Person_type('person'), Season("summer")), salience=1)
    def clothes201(self):
        self.myclothes = Myclothes(1, "black", "pajama", 2, "white", "Hoodie", 0, "", "", 0, "", "", 5, "white",
                                   "shose", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "",
                                   "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('Sport'), Gender('male'), Person_type('person'), Season("summer")), salience=1)
    def clothes202(self):
        self.myclothes = Myclothes(1, "oil", "pajama", 2, "oil", "Hoodie", 0, "", "", 0, "", "", 5, "white",
                                   "shose", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "",
                                   "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('Sport'), Gender('male'), Person_type('person'), Season("summer")), salience=1)
    def clothes203(self):
        self.myclothes = Myclothes(1, "yellow", "pajama", 2, " yellow", "Hoodie", 0, "", "", 0, "", "", 5, "white",
                                   "shose", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "",
                                   "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='white'),
              Occasion('Sport'), Gender('male'), Person_type('person'), Season("summer")), salience=1)
    def clothes204(self):
        self.myclothes = Myclothes(1, "black", "short", 2, "yellow", "Hoodie", 0, "", "", 0, "", "", 5, "white",
                                   "shose", 0, "", "", 0, "", "", 0, " ", "", 0, "", "", 0, "", "", 0, "", "", 0, "",
                                   "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='dark'),
              Occasion('Sport'), Gender('male'), Person_type('person'), Season("summer")), salience=1)
    def clothes205(self):
        self.myclothes = Myclothes(1, "oil", "short", 2, "oil", "Hoodie", 0, "", "", 0, "", "", 5, "white", "shose",
                                   0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "",
                                   "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='white'),
              Occasion('Sport'), Gender('male'), Person_type('person'), Season("summer")), salience=1)
    def clothes206(self):
        self.myclothes = Myclothes(1, "red", "short", 2, "yellow", "Hoodie", 0, "", "", 0, " ", "", 5, "white",
                                   "shose", 0, "", "", 0, "", "", 0, " ", "", 0, "", "", 0, "", "", 0, "", "", 0, "",
                                   "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='white'),
              Occasion('Sport'), Gender('male'), Person_type('person'), Season("summer")), salience=1)
    def clothes207(self):
        self.myclothes = Myclothes(1, "white", "short", 2, "red", "Hoodie", 0, "", "", 0, "", "", 5, "white",
                                   "shose", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "",
                                   "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='dark'),
              Occasion('Sport'), Gender('male'), Person_type('person'), Season("summer")), salience=1)
    def clothes208(self):
        self.myclothes = Myclothes(1, "green", "short", 2, "yellow", "Hoodie", 0, "", "", 0, "", "", 5, "white",
                                   "shose", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "",
                                   "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='dark'),
              Occasion('Sport'), Gender('male'), Person_type('person'), Season("summer")), salience=1)
    def clothes209(self):
        self.myclothes = Myclothes(1, "black", "short", 2, "green", "Hoodie", 0, "", "", 0, " ", "", 5, "white",
                                   "shose", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "",
                                   "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('Sport'), Gender('male'), Person_type('person'), Season("summer")), salience=1)
    def clothes210(self):
        self.myclothes = Myclothes(1, "orange", "short", 2, "black", "Hoodie", 0, "", "", 0, "", "", 5, "white",
                                   "shose", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "",
                                   "", 0, "", "")
        self.result.append(self.myclothes)

    #    التنزه مع الاصدقاء

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='white'),
              Occasion('Hinking_with_friends'), Gender('female'), Person_type('person'), Season("summer")), salience=1)
    def clothes211(self):
        self.myclothes = Myclothes(1, "white", "Trousers", 2, "pink", "Hoodie", 0, "", "", 0, "", "", 5, "white",
                                   "shose", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "",
                                   "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='white'),
              Occasion('Hinking_with_friends'), Gender('female'), Person_type('person'), Season("summer")), salience=1)
    def clothes212(self):
        self.myclothes = Myclothes(1, "black", "pajama", 2, "black", "Hoodie", 0, "", "", 0, "", "", 5, "white",
                                   "shose", 0, "", "", 0, "", "", 0, " ", "", 0, "", "", 0, "", "", 0, "", "", 0, "",
                                   "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='white'),
              Occasion('Hinking_with_friends'), Gender('female'), Person_type('person'), Season("summer")), salience=1)
    def clothes213(self):
        self.myclothes = Myclothes(1, "black", "pajama", 2, "black", "Hoodie", 0, "", "", 0, " ", "", 5, "white",
                                   "shose", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "",
                                   "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('Hinking_with_friends'), Gender('female'), Person_type('person'), Season("summer")), salience=1)
    def clothes214(self):
        self.myclothes = Myclothes(1, "yellow", "pajama", 2, "yellow", "Hoodie", 0, "", "", 0, " ", "", 5, "white",
                                   "shose", 0, "", "", 0, "", "", 0, " ", "", 0, "", "", 0, "", "", 0, "", "", 0, "",
                                   "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='dark'),
              Occasion('Hinking_with_friends'), Gender('female'), Person_type('person'), Season("summer")), salience=1)
    def clothes215(self):
        self.myclothes = Myclothes(1, "blue", "pajama", 2, "blue", "Hoodie", 0, "", "", 0, "", "", 5, "white",
                                   "shose", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "",
                                   "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('Hinking_with_friends'), Gender('female'), Person_type('person'), Season("summer")), salience=1)
    def clothes216(self):
        self.myclothes = Myclothes(1, "gray", "Trousers", 0, "", "", 3, "cyan", "Shirt", 0, "", "", 5, "white",
                                   "shose", 0, "", "", 0, "", "", 0, " ", "", 0, "", "", 0, "", "", 0, "", "", 0, "",
                                   "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='white'),
              Occasion('Hinking_with_friends'), Gender('female'), Person_type('person'), Season("summer")), salience=1)
    def clothes217(self):
        self.myclothes = Myclothes(1, "gray", "Trousers", 0, "", "", 3, "cyan", "Shirt", 0, "", "", 5, "white",
                                   "shose", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "",
                                   "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('Hinking_with_friends'), Gender('female'), Person_type('person'), Season("summer")), salience=1)
    def clothes218(self):
        self.myclothes = Myclothes(1, "gray", "Trousers", 0, "", "", 3, "pink", "Shirt", 0, "", "", 5, "white",
                                   "shose", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "",
                                   "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='dark'),
              Occasion('Hinking_with_friends'), Gender('female'), Person_type('person'), Season("summer")), salience=1)
    def clothes219(self):
        self.myclothes = Myclothes(1, "gray", "Trousers", 0, "", "", 3, "vinous", "Shirt", 0, "", "", 5, "dark",
                                   "shose", 0, "", "", 0, "", "", 0, " ", "", 0, "", "", 0, "", "", 0, "", "", 0, "",
                                   "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='white'),
              Occasion('Hinking_with_friends'), Gender('female'), Person_type('person'), Season("summer")), salience=1)
    def clothes220(self):
        self.myclothes = Myclothes(1, "gray", "jeans", 2, "red", "T_Shirt", 0, "", "", 0, "", "", 5, "white",
                                   "shose", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "",
                                   "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('Hinking_with_friends'), Gender('female'), Person_type('person'), Season("summer")), salience=1)
    def clothes221(self):
        self.myclothes = Myclothes(1, "gray", "jeans", 2, "pink", "T_Shirt", 0, "", "", 0, "", "", 5, "white",
                                   "shose", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "",
                                   "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='dark'),
              Occasion('Hinking_with_friends'), Gender('female'), Person_type('person'), Season("summer")), salience=1)
    def clothes802(self):
        self.myclothes = Myclothes(1, "gray", "jeans", 2, "pink", "T_Shirt", 0, "", "", 0, "", "", 5, "pink",
                                   "shose", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "",
                                   "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='white'),
              Occasion('Hinking_with_friends'), Gender('female'), Person_type('person'), Season("summer")), salience=1)
    def clothes223(self):
        self.myclothes = Myclothes(1, "white", "Trousers", 2, "pink", "T_Shirt", 0, "", "", 0, " ", "", 5, "white",
                                   "shose", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "",
                                   "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('Hinking_with_friends'), Gender('female'), Person_type('person'), Season("summer")), salience=1)
    def clothes224(self):
        self.myclothes = Myclothes(1, "white", "Trousers", 2, "yellow", "T_Shirt", 0, "", "", 0, "", "", 5, "white",
                                   "shose", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "",
                                   "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='dark'),
              Occasion('Hinking_with_friends'), Gender('female'), Person_type('person'), Season("summer")), salience=1)
    def clothes225(self):
        self.myclothes = Myclothes(1, "white", "jeans", 2, "green", "T_Shirt", 0, "", "", 0, "", "", 5, "black",
                                   "shose", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "",
                                   "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='white'),
              Occasion('Hinking_with_friends'), Gender('female'), Person_type('person'), Season("summer")), salience=1)
    def clothes226(self):
        self.myclothes = Myclothes(1, "cyan", "jeans", 2, "vinous", "T_Shirt", 0, "", "", 0, "", "", 5, "white",
                                   "shose", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "",
                                   "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('Hinking_with_friends'), Gender('female'), Person_type('person'), Season("summer")), salience=1)
    def clothes227(self):
        self.myclothes = Myclothes(1, "black", "jeans", 2, "cyan", "T_Shirt", 0, "", "", 0, "", "", 5, "white",
                                   "shose", 0, "", "", 0, "", "", 0, " ", "", 0, "", "", 0, "", "", 0, "", "", 0, "",
                                   "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='dark'),
              Occasion('Hinking_with_friends'), Gender('female'), Person_type('person'), Season("summer")), salience=1)
    def clothes228(self):
        self.myclothes = Myclothes(1, "darkblue", "jeans", 2, "pink", "T_Shirt", 0, "", "", 0, "", "", 5, "white",
                                   "shose", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "",
                                   "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='white'),
              Occasion('Hinking_with_friends'), Gender('female'), Person_type('person'), Season("summer")), salience=1)
    def clothes229(self):
        self.myclothes = Myclothes(1, "black", "Trousers", 2, "orange", "T_Shirt", 0, "", "", 0, "", "", 5, "white",
                                   "shose", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "",
                                   "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('Hinking_with_friends'), Gender('female'), Person_type('person'), Season("summer")), salience=1)
    def clothes230(self):
        self.myclothes = Myclothes(1, "black", "Trousers", 2, "beige", "T_Shirt", 0, "", "", 0, "", "", 5, "white",
                                   "shose", 0, "", "", 0, "", "", 0, " ", "", 0, "", "", 0, "", "", 0, "", "", 0, "",
                                   "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='dark'),
              Occasion('Hinking_with_friends'), Gender('female'), Person_type('person'), Season("summer")), salience=1)
    def clothes240(self):
        self.myclothes = Myclothes(1, "black", "Trousers", 2, "brown", "T_Shirt", 0, "", "", 0, "", "", 5, "white",
                                   "shose", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "",
                                   "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='white'),
              Occasion('Hinking_with_friends'), Gender('female'), Person_type('person'), Season("summer")), salience=1)
    def clothes241(self):
        self.myclothes = Myclothes(1, "black", "jeans", 2, "orange", "T_Shirt", 0, "", "", 0, "", "", 5, "white",
                                   "shose", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "",
                                   "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('Hinking_with_friends'), Gender('female'), Person_type('person'), Season("summer")), salience=1)
    def clothes242(self):
        self.myclothes = Myclothes(1, "black", "jeans", 2, "beige", "T_Shirt", 0, "", "", 0, "", "", 5, "white",
                                   "shose", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "",
                                   "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='dark'),
              Occasion('Hinking_with_friends'), Gender('female'), Person_type('person'), Season("summer")), salience=1)
    def clothes245(self):
        self.myclothes = Myclothes(1, "black", "jeans", 2, "brown", "T_Shirt", 0, "", "", 0, "", "", 5, "white",
                                   "shose", 0, "", "", 0, "", "", 0, " ", "", 0, "", "", 0, "", "", 0, "", "", 0, "",
                                   "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='white'),
              Occasion('Hinking_with_friends'), Gender('female'), Person_type('person'), Season("summer")), salience=1)
    def clothes246(self):
        self.myclothes = Myclothes(1, "darkblue", "jeans", 2, "brown", "T_Shirt", 0, "", "", 0, "", "", 5, "white",
                                   "shose", 0, "", "", 0, "", "", 0, " ", "", 0, "", "", 0, "", "", 0, "", "", 0, "",
                                   "", 0, "", "")
        self.result.append(self.myclothes)

    #    //////////////pajama

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='white'),
              Occasion('Hinking_with_friends'), Gender('male'), Person_type('person'), Season("summer")), salience=1)
    def clothes247(self):
        self.myclothes = Myclothes(1, "white", "Trousers", 2, "pink", "Hoodie", 0, "", "", 0, "", "", 5, "white",
                                   "shose", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "",
                                   "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='dark'),
              Occasion('Hinking_with_friends'), Gender('male'), Person_type('person'), Season("summer")), salience=1)
    def clothes248(self):
        self.myclothes = Myclothes(1, "black", "pajama", 2, "black", "Hoodie", 0, "", "", 0, "", "", 5, "white",
                                   "shose", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "",
                                   "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='white'),
              Occasion('Hinking_with_friends'), Gender('male'), Person_type('person'), Season("summer")), salience=1)
    def clothes249(self):
        self.myclothes = Myclothes(1, "black", "pajama", 2, "black", "Hoodie", 0, "", "", 0, "", "", 5, "white",
                                   "shose", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "",
                                   "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('Hinking_with_friends'), Gender('male'), Person_type('person'), Season("summer")), salience=1)
    def clothes250(self):
        self.myclothes = Myclothes(1, "yellow", "pajama", 2, "yellow", "Hoodie", 0, "", "", 0, "", "", 5, "white",
                                   "shose", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "",
                                   "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='dark'),
              Occasion('Hinking_with_friends'), Gender('male'), Person_type('person'), Season("summer")), salience=1)
    def clothes251(self):
        self.myclothes = Myclothes(1, "blue", "pajama", 2, "blue", "Hoodie", 0, "", "", 0, "", "", 5, "white",
                                   "shose", 0, "", "", 0, "", "", 0, " ", "", 0, "", "", 0, "", "", 0, "", "", 0, "",
                                   "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('Hinking_with_friends'), Gender('male'), Person_type('person'), Season("summer")), salience=1)
    def clothes252(self):
        self.myclothes = Myclothes(1, "gray", "Trousers", 0, "", "", 3, "vinous", "Shirt", 0, "", "", 5, "white",
                                   "shose", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "",
                                   "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='white'),
              Occasion('Hinking_with_friends'), Gender('male'), Person_type('person'), Season("summer")), salience=1)
    def clothes253(self):
        self.myclothes = Myclothes(1, "darkblue", "Trousers", 0, "", "", 3, "cyan", "Shirt", 0, "", "", 5, "white",
                                   "shose", 0, "", "", 0, "", "", 0, " ", "", 0, "", "", 0, "", "", 0, "", "", 0, "",
                                   "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('Hinking_with_friends'), Gender('male'), Person_type('person'), Season("summer")), salience=1)
    def clothes254(self):
        self.myclothes = Myclothes(1, "gray", "Trousers", 0, "", "", 3, "darkblue", "Shirt", 0, "", "", 5, "white",
                                   "shose", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "",
                                   "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='dark'),
              Occasion('Hinking_with_friends'), Gender('male'), Person_type('person'), Season("summer")), salience=1)
    def clothes255(self):
        self.myclothes = Myclothes(1, "gray", "Trousers", 0, "", "", 3, "vinous", "Shirt", 0, "", "", 5, "dark",
                                   "shose", 0, "", "", 0, "", "", 0, " ", "", 0, "", "", 0, "", "", 0, "", "", 0, "",
                                   "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='white'),
              Occasion('Hinking_with_friends'), Gender('male'), Person_type('person'), Season("summer")), salience=1)
    def clothes256(self):
        self.myclothes = Myclothes(1, "gray", "jeans", 2, "oil", "T_Shirt", 0, "", "", 0, "", "", 5, "white",
                                   "shose", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "",
                                   "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('Hinking_with_friends'), Gender('male'), Person_type('person'), Season("summer")), salience=1)
    def clothes257(self):
        self.myclothes = Myclothes(1, "gray", "jeans", 2, "black", "T_Shirt", 0, "", "", 0, "", "", 5, "white",
                                   "shose", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "",
                                   "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='dark'),
              Occasion('Hinking_with_friends'), Gender('male'), Person_type('person'), Season("summer")), salience=1)
    def clothes258(self):
        self.myclothes = Myclothes(1, "gray", "jeans", 2, "pink", "T_Shirt", 0, "", "", 0, "", "", 5, "pink",
                                   "shose", 0, "", "", 0, "", "", 0, " ", "", 0, "", "", 0, "", "", 0, "", "", 0, "",
                                   "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='white'),
              Occasion('Hinking_with_friends'), Gender('male'), Person_type('person'), Season("summer")), salience=1)
    def clothes259(self):
        self.myclothes = Myclothes(1, "white", "Trousers", 2, "white", "T_Shirt", 0, "", "", 0, "", "", 5, "white",
                                   "shose", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "",
                                   "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('Hinking_with_friends'), Gender('male'), Person_type('person'), Season("summer")), salience=1)
    def clothes260(self):
        self.myclothes = Myclothes(1, "white", "Trousers", 2, "yellow", "T_Shirt", 0, "", "", 0, "", "", 5, "white",
                                   "shose", 0, "", "", 0, "", "", 0, " ", "", 0, "", "", 0, "", "", 0, "", "", 0, "",
                                   "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='dark'),
              Occasion('Hinking_with_friends'), Gender('male'), Person_type('person'), Season("summer")), salience=1)
    def clothes261(self):
        self.myclothes = Myclothes(1, "white", "jeans", 2, "green", "T_Shirt", 0, "", "", 0, "", "", 5, "black",
                                   "shose", 0, "", "", 0, "", "", 0, " ", "", 0, "", "", 0, "", "", 0, "", "", 0, "",
                                   "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='white'),
              Occasion('Hinking_with_friends'), Gender('male'), Person_type('person'), Season("summer")), salience=1)
    def clothes262(self):
        self.myclothes = Myclothes(1, "cyan", "jeans", 2, "vinous", "T_Shirt", 0, "", "", 0, "", "", 5, "white",
                                   "shose", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "",
                                   "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('Hinking_with_friends'), Gender('male'), Person_type('person'), Season("summer")), salience=1)
    def clothes263(self):
        self.myclothes = Myclothes(1, "black", "jeans", 2, "gray", "T_Shirt", 0, "", "", 0, "", "", 5, "white",
                                   "shose", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "",
                                   "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='dark'),
              Occasion('Hinking_with_friends'), Gender('male'), Person_type('person'), Season("summer")), salience=1)
    def clothes264(self):
        self.myclothes = Myclothes(1, "darkblue", "jeans", 2, "black", "T_Shirt", 0, "", "", 0, "", "", 5, "white",
                                   "shose", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "",
                                   "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='white'),
              Occasion('Hinking_with_friends'), Gender('male'), Person_type('person'), Season("summer")), salience=1)
    def clothes265(self):
        self.myclothes = Myclothes(1, "black", "Trousers", 2, "orange", "T_Shirt", 0, "", "", 0, " ", "", 5, "white",
                                   "shose", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "",
                                   "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('Hinking_with_friends'), Gender('male'), Person_type('person'), Season("summer")), salience=1)
    def clothes266(self):
        self.myclothes = Myclothes(1, "black", "Trousers", 2, "beige", "T_Shirt", 0, "", "", 0, "", "", 5, "white",
                                   "shose", 0, "", "", 0, "", "", 0, " ", "", 0, "", "", 0, "", "", 0, "", "", 0, "",
                                   "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='dark'),
              Occasion('Hinking_with_friends'), Gender('male'), Person_type('person'), Season("summer")), salience=1)
    def clothes267(self):
        self.myclothes = Myclothes(1, "black", "Trousers", 2, "brown", "T_Shirt", 0, "", "", 0, "", "", 5, "white",
                                   "shose", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "",
                                   "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='white'),
              Occasion('Hinking_with_friends'), Gender('male'), Person_type('person'), Season("summer")), salience=1)
    def clothes268(self):
        self.myclothes = Myclothes(1, "black", "jeans", 2, "orange", "T_Shirt", 0, "", "", 0, "", "", 5, "white",
                                   "shose", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "",
                                   "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('Hinking_with_friends'), Gender('male'), Person_type('person'), Season("summer")), salience=1)
    def clothes269(self):
        self.myclothes = Myclothes(1, "black", "jeans", 2, "beige", "T_Shirt", 0, "", "", 0, "", "", 5, "white",
                                   "shose", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "",
                                   "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='dark'),
              Occasion('Hinking_with_friends'), Gender('male'), Person_type('person'), Season("summer")), salience=1)
    def clothes270(self):
        self.myclothes = Myclothes(1, "black", "jeans", 2, "brown", "T_Shirt", 0, "", "", 0, "", "", 5, "white",
                                   "shose", 0, "", "", 0, "", "", 0, " ", "", 0, "", "", 0, "", "", 0, "", "", 0, "",
                                   "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='white'),
              Occasion('Hinking_with_friends'), Gender('male'), Person_type('person'), Season("summer")), salience=1)
    def clothes271(self):
        self.myclothes = Myclothes(1, "black", "jeans", 2, "cyan", "T_Shirt", 0, "", "", 0, "", "", 5, "white",
                                   "shose", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "",
                                   "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='white'),
              Occasion('Hinking_with_friends'), Gender('male'), Person_type('person'), Season("summer")), salience=1)
    def clothes272(self):
        self.myclothes = Myclothes(1, "beige", "short", 2, "cyan", "T_Shirt", 0, "", "", 0, "", "", 5, "white",
                                   "shose", 0, "", "", 0, "", "", 0, " ", "", 0, "", "", 0, "", "", 0, "", "", 0, "",
                                   "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='dark'),
              Occasion('Hinking_with_friends'), Gender('male'), Person_type('person'), Season("summer")), salience=1)
    def clothes273(self):
        self.myclothes = Myclothes(1, "beige", "short", 2, "brown", "T_Shirt", 0, "", "", 0, "", "", 5, "white",
                                   "shose", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "",
                                   "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('Hinking_with_friends'), Gender('male'), Person_type('person'), Season("summer")), salience=1)
    def clothes274(self):
        self.myclothes = Myclothes(1, "black", "short", 2, "white", "T_Shirt", 0, "", "", 0, "", "", 5, "white",
                                   "shose", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "",
                                   "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='dark'),
              Occasion('Hinking_with_friends'), Gender('male'), Person_type('person'), Season("summer")), salience=1)
    def clothes275(self):
        self.myclothes = Myclothes(1, "vinous", "short", 2, "gray", "T_Shirt", 0, "", "", 0, "", "", 5, "white",
                                   "shose", 0, "", "", 0, "", "", 0, " ", "", 0, "", "", 0, "", "", 0, "", "", 0, "",
                                   "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='white'),
              Occasion('Hinking_with_friends'), Gender('male'), Person_type('person'), Season("summer")), salience=1)
    def clothes276(self):
        self.myclothes = Myclothes(1, "black", "short", 2, "cyan", "T_Shirt", 0, "", "", 0, "", "", 5, "white",
                                   "shose", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "",
                                   "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='white'),
              Occasion('Hinking_with_friends'), Gender('male'), Person_type('person'), Season("summer")), salience=1)
    def clothes277(self):
        self.myclothes = Myclothes(1, "gray", "short", 2, "yellow", "T_Shirt", 0, "", "", 0, "", "", 5, "white",
                                   "shose", 0, "", "", 0, "", "", 0, " ", "", 0, "", "", 0, "", "", 0, "", "", 0, "",
                                   "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='dark'),
              Occasion('Hinking_with_friends'), Gender('male'), Person_type('person'), Season("summer")), salience=1)
    def clothes278(self):
        self.myclothes = Myclothes(1, "black", "short", 2, "vinous", "T_Shirt", 0, "", "", 0, "", "", 5, "white",
                                   "shose", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "",
                                   "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('Hinking_with_friends'), Gender('male'), Person_type('person'), Season("summer")), salience=1)
    def clothes279(self):
        self.myclothes = Myclothes(1, "white", "short", 2, "pink", "T_Shirt", 0, "", "", 0, "", "", 5, "white",
                                   "shose", 0, "", "", 0, "", "", 0, " ", "", 0, "", "", 0, "", "", 0, "", "", 0, "",
                                   "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('Hinking_with_friends'), Gender('male'), Person_type('person'), Season("summer")), salience=1)
    def clothes280(self):
        self.myclothes = Myclothes(1, "white", "short", 2, "pink", "T_Shirt", 0, "", "", 0, "", "", 5, "white",
                                   "shose", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "",
                                   "", 0, "", "")
        self.result.append(self.myclothes)

class CLOTHESSecond(KnowledgeEngine):
    result = []
    myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0,
                          "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")

    @DefFacts()
    def _init_(self):
        self.result = []
        yield age(16)

    @Rule(AND(age(value=P(lambda value: value >= 21) & P(lambda value: value <= 35)), SkinColor(color='dark'),
              Occasion('gradution'), Gender('female'), Person_type('student'), Season("summer"), piece_name("Skirt"),
              piece_type("MidSkirt"), piece_color("black")), salience=1)
    def clothes790(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "black", "Kandra", 6,
                                   "black", "Coat", 7, "black", "Hat", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0,
                                   "", "", 13, "black", "graduation_gown")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 21) & P(lambda value: value <= 35)), SkinColor(color='hanatawi'),
              Occasion('gradution'), Gender('female'), Person_type('student'), Season("summer"), piece_name("Skirt"),
              piece_type("MidSkirt"), piece_color("black")), salience=1)
    def clothes791(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "black", "Kandra", 6,
                                   "black", "Coat", 7, "black", "Hat", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0,
                                   "", "", 13, "black", "graduation_gown")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 21) & P(lambda value: value <= 35)), SkinColor(color='hanatawi'),
              Occasion('gradution'), Gender('female'), Person_type('student'), Season("summer"), piece_name("Skirt"),
              piece_type("MidSkirt"), piece_color("black")), salience=1)
    def clothes792(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "black", "Kandra", 6,
                                   "vinous", "Coat", 7, "black", "Hat", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0,
                                   "", "", 13, "black", "graduation_gown")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 21) & P(lambda value: value <= 35)), SkinColor(color='hanatawi'),
              Occasion('gradution'), Gender('female'), Person_type('student'), Season("summer"), piece_name("Skirt"),
              piece_type("MidSkirt"), piece_color("black")), salience=1)
    def clothes806(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "gray", "Kandra", 6,
                                   "cyan", "Coat", 7, "black", "Hat", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "",
                                   "", 13, "black", "graduation_gown")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 21) & P(lambda value: value <= 35)), SkinColor(color='dark'),
              Occasion('gradution'), Gender('female'), Person_type('student'), Season("summer"), piece_name("Skirt"),
              piece_type("MidSkirt"), piece_color("black")), salience=1)
    def clothes807(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "black", "Kandra", 6,
                                   "black", "Coat", 7, "black", "Hat", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0,
                                   "", "", 13, "black", "graduation_gown")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 21) & P(lambda value: value <= 35)), SkinColor(color='hanatawi'),
              Occasion('gradution'), Gender('female'), Person_type('student'), Season("summer"), piece_name("Skirt"),
              piece_type("MidSkirt"), piece_color("black")), salience=1)
    def clothes809(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "black", "Kandra", 6,
                                   "black", "Coat", 7, "black", "Hat", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0,
                                   "", "", 13, "black", "graduation_gown")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 21) & P(lambda value: value <= 35)), SkinColor(color='hanatawi'),
              Occasion('gradution'), Gender('female'), Person_type('student'), Season("summer"), piece_name("Skirt"),
              piece_type("MidSkirt"), piece_color("black")), salience=1)
    def clothes810(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "black", "Kandra", 6,
                                   "vinous", "Coat", 7, "black", "Hat", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0,
                                   "", "", 13, "black", "graduation_gown")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 21) & P(lambda value: value <= 35)), SkinColor(color='hanatawi'),
              Occasion('gradution'), Gender('female'), Person_type('student'), Season("summer"), piece_name("Skirt"),
              piece_type("MidSkirt"), piece_color("black")), salience=1)
    def clothes811(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "white", "Kandra", 6,
                                   "cyan", "Coat", 7, "black", "Hat", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "",
                                   "", 13, "black", "graduation_gown")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 21) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('gradution'), Gender('female'), Person_type('student'), Season("summer"), piece_name("Skirt"),
              piece_type("MidSkirt"), piece_color("black")), salience=1)
    def clothes812(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "black", "Kandra", 6,
                                   "vinous", "Coat", 7, "black", "Hat", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0,
                                   "", "", 13, "black", "graduation_gown")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 21) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('gradution'), Gender('female'), Person_type('student'), Season("summer"), piece_name("Skirt"),
              piece_type("MidSkirt"), piece_color("white")), salience=1)
    def clothes813(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "cyan", "Kandra", 6,
                                   "cyan", "Coat", 7, "black", "Hat", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "",
                                   "", 13, "black", "graduation_gown")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 21) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('gradution'), Gender('female'), Person_type('student'), Season("summer"), piece_name("Skirt"),
              piece_type("MidSkirt"), piece_color("white")), salience=1)
    def clothes814(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "pink", "Shirt", 0, "", "", 5, "cyan", "Kandra", 6, "cyan",
                                   "Coat", 7, "black", "Hat", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 13,
                                   "black", "graduation_gown")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 21) & P(lambda value: value <= 35)), SkinColor(color='dark'),
              Occasion('gradution'), Gender('female'), Person_type('student'), Season("summer"), piece_name("Skirt"),
              piece_type("MidSkirt"), piece_color("black")), salience=1)
    def clothes815(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "black", "Kandra", 6,
                                   "black", "Coat", 7, "black", "Hat", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0,
                                   "", "", 13, "black", "graduation_gown")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 21) & P(lambda value: value <= 35)), SkinColor(color='hanatawi'),
              Occasion('gradution'), Gender('female'), Person_type('student'), Season("summer"), piece_name("Skirt"),
              piece_type("MidSkirt"), piece_color("black")), salience=1)
    def clothes816(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "black", "Kandra", 6,
                                   "black", "Coat", 7, "black", "Hat", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0,
                                   "", "", 13, "black", "graduation_gown")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 21) & P(lambda value: value <= 35)), SkinColor(color='hanatawi'),
              Occasion('gradution'), Gender('female'), Person_type('student'), Season("summer"), piece_name("Trousers"),
              piece_type("wide_pants"), piece_color("white")), salience=1)
    def clothes820(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "white", "Kandra", 6,
                                   "pink", "Coat", 7, "black", "Hat", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "",
                                   "", 13, "black", "graduation_gown")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 21) & P(lambda value: value <= 35)), SkinColor(color='hanatawi'),
              Occasion('gradution'), Gender('female'), Person_type('student'), Season("summer"), piece_name("Trousers"),
              piece_type("wide_pants"), piece_color("black")), salience=1)
    def clothes821(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "white", "Kandra", 6,
                                   "cyan", "Coat", 7, "black", "Hat", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "",
                                   "", 13, "black", "graduation_gown")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 21) & P(lambda value: value <= 35)), SkinColor(color='dark'),
              Occasion('gradution'), Gender('female'), Person_type('student'), Season("summer"), piece_name("Trousers"),
              piece_type("wide_pants"), piece_color("black")), salience=1)
    def clothes822(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "vinous", "Shirt", 0, "", "", 5, "black", "Kandra", 6,
                                   "black", "Coat", 7, "black", "Hat", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0,
                                   "", "", 13, "black", "graduation_gown")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 21) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('gradution'), Gender('female'), Person_type('student'), Season("summer"), piece_name("Trousers"),
              piece_type("wide_pants"), piece_color("white")), salience=1)
    def clothes823(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "pink", "Kandra", 6,
                                   "pink", "Coat", 7, "black", "Hat", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "",
                                   "", 13, "black", "graduation_gown")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 21) & P(lambda value: value <= 35)), SkinColor(color='dark'),
              Occasion('gradution'), Gender('female'), Person_type('student'), Season("summer"), piece_name("Trousers"),
              piece_type("wide_pants"), piece_color("black")), salience=1)
    def clothes824(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "white", "Kandra", 6,
                                   "pink", "Coat", 7, "black", "Hat", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "",
                                   "", 13, "black", "graduation_gown")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 21) & P(lambda value: value <= 35)), SkinColor(color='hanatawi'),
              Occasion('gradution'), Gender('female'), Person_type('student'), Season("summer"), piece_name("Shirt"),
              piece_type("Shirt"), piece_color("white")), salience=1)
    def clothes825(self):
        self.myclothes = Myclothes(1, "white", "Trousers", 0, "", "", 3, "", "", 0, "", "", 5, "white", "Kandra", 6,
                                   "pink", "Coat", 7, "black", "Hat", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "",
                                   "", 13, "black", "graduation_gown")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 21) & P(lambda value: value <= 35)), SkinColor(color='hanatawi'),
              Occasion('gradution'), Gender('female'), Person_type('student'), Season("summer"), piece_name("Shirt"),
              piece_type("Shirt"), piece_color("white")), salience=1)
    def clothes826(self):
        self.myclothes = Myclothes(1, "black", "Trousers", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "white",
                                   "Kandra", 6, "cyan", "Coat", 7, "black", "Hat", 0, "", "", 0, "", "", 0, "", "", 0,
                                   "", "", 0, "", "", 13, "black", "graduation_gown")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 21) & P(lambda value: value <= 35)), SkinColor(color='dark'),
              Occasion('gradution'), Gender('female'), Person_type('student'), Season("summer"), piece_name("Shirt"),
              piece_type("Shirt"), piece_color("white")), salience=1)
    def clothes827(self):
        self.myclothes = Myclothes(1, "black", "Trousers", 0, "", "", 3, "vinous", "Shirt", 0, "", "", 5, "black",
                                   "Kandra", 6, "black", "Coat", 7, "black", "Hat", 0, "", "", 0, "", "", 0, "", "", 0,
                                   "", "", 0, "", "", 13, "black", "graduation_gown")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 21) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('gradution'), Gender('female'), Person_type('student'), Season("summer"), piece_name("Shirt"),
              piece_type("Shirt"), piece_color("white")), salience=1)
    def clothes828(self):
        self.myclothes = Myclothes(1, "white", "Trousers", 0, "", "", 0, "", "", 0, "", "", 5, "pink", "Kandra", 6,
                                   "pink", "Coat", 7, "black", "Hat", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "",
                                   "", 13, "black", "graduation_gown")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 21) & P(lambda value: value <= 35)), SkinColor(color='dark'),
              Occasion('gradution'), Gender('female'), Person_type('student'), Season("summer"), piece_name("Shirt"),
              piece_type("Shirt"), piece_color("white")), salience=1)
    def clothes829(self):
        self.myclothes = Myclothes(1, "black", " Trousers", 0, "", "", 0, "", "", 0, "", "", 5, "white", "Kandra", 6,
                                   "pink", "Coat", 7, "black", "Hat", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "",
                                   "", 13, "black", "graduation_gown")
        self.result.append(self.myclothes)

    #   ///////////

    @Rule(AND(age(value=P(lambda value: value >= 21) & P(lambda value: value <= 35)), SkinColor(color='hanatawi'),
              Occasion('gradution'), Gender('male'), Person_type('student'), Season("summer"), piece_name("Trousers"),
              piece_type("Trousers"), piece_color("black")), salience=2)
    def clothes830(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, " ", "", 5, "black", "Kandra", 0, "",
                                   "", 7, "black", "Hat", 8, "darkblue", "carafe", 0, "", "", 0, "", "", 0, "", "", 0,
                                   "", "", 13, "black", "graduation_gown")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 21) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('gradution'), Gender('male'), Person_type('student'), Season("summer"), piece_name("Trousers"),
              piece_type("Trousers"), piece_color("gray")), salience=2)
    def clothes831(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, " ", "", 5, "black", "Kandra", 0, "",
                                   "", 7, "black", "Hat", 8, "black", "carafe", 0, "", "", 0, "", "", 0, "", "", 0, "",
                                   "", 13, "black", "graduation_gown")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 21) & P(lambda value: value <= 35)), SkinColor(color='dark'),
              Occasion('gradution'), Gender('male'), Person_type('student'), Season("summer"), piece_name("Shirt"),
              piece_type("Trousers"), piece_color("darkblue")), salience=2)
    def clothes832(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, " ", "", 5, "brown", "Kandra", 0, "",
                                   "", 7, "black", "Hat", 8, "brown", "carafe", 0, "", "", 0, "", "", 0, "", "", 0, "",
                                   "", 13, "black", "graduation_gown")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 21) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('gradution'), Gender('male'), Person_type('student'), Season("summer"), piece_name("Shirt"),
              piece_type("Shirt"), piece_color("white")), salience=1)
    def clothes833(self):
        self.myclothes = Myclothes(1, "gray", "Trousers", 0, "", "", 0, "", "", 0, "", "", 5, "darkblue", "Kandra", 0,
                                   "", "", 7, "black", "Hat", 8, "darkblue", "carafe", 0, "", "", 0, "", "", 0, "", "",
                                   0, "", "", 13, "black", "graduation_gown")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 21) & P(lambda value: value <= 35)), SkinColor(color='hanatawi'),
              Occasion('gradution'), Gender('male'), Person_type('student'), Season("summer"), piece_name("Shirt"),
              piece_type("Shirt"), piece_color("white")), salience=1)
    def clothes834(self):
        self.myclothes = Myclothes(1, "black", "Trousers", 0, "", "", 0, "", "", 0, "", "", 5, "black", "Kandra", 0,
                                   "", "", 7, "black", "Hat", 8, "vinous", "carafe", 0, "", "", 0, "", "", 0, "", "", 0,
                                   "", "", 13, "black", "graduation_gown")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 21) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('gradution'), Gender('male'), Person_type('student'), Season("summer"), piece_name("Shirt"),
              piece_type("Shirt"), piece_color("cyan")), salience=1)
    def clothes835(self):
        self.myclothes = Myclothes(1, "darkblue", "Trousers", 0, "", "", 0, "", "", 0, " ", "", 5, "brown", "Kandra",
                                   0, "", "", 7, "black", "Hat", 8, "brown", "carafe", 0, "", "", 0, "", "", 0, "", "",
                                   0, "", "", 13, "black", "graduation_gown")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 21) & P(lambda value: value <= 35)), SkinColor(color='hanatawi'),
              Occasion('gradution'), Gender('male'), Person_type('student'), Season("summer"), piece_name("Trousers"),
              piece_type("Trousers"), piece_color("gray")), salience=1)
    def clothes836(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "black", "Kandra", 0, "",
                                   "", 7, "black", "Hat", 8, "darkblue", "carafe", 0, "", "", 0, "", "", 0, "", "", 0,
                                   "", "", 13, "black", "graduation_gown")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 21) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('gradution'), Gender('male'), Person_type('student'), Season("summer"), piece_name("Trousers"),
              piece_type("Trousers"), piece_color("darkblue")), salience=1)
    def clothes837(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "beige", "Shirt", 0, "", "", 5, "darkblue", "Kandra", 0,
                                   "", "", 7, "black", "Hat", 8, "beige", "carafe", 0, "", "", 0, "", "", 0, "", "", 0,
                                   "", "", 13, "black", "graduation_gown")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 21) & P(lambda value: value <= 35)), SkinColor(color='dark'),
              Occasion('gradution'), Gender('male'), Person_type('student'), Season("summer"), piece_name("Trousers"),
              piece_type("Trousers"), piece_color("black")), salience=1)
    def clothes838(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "grown", "Kandra", 0, "",
                                   "", 7, "black", "Hat", 8, "black", "carafe", 0, "", "", 0, "", "", 0, "", "", 0, "",
                                   "", 13, "black", "graduation_gown")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 21) & P(lambda value: value <= 35)), SkinColor(color='dark'),
              Occasion('gradution'), Gender('male'), Person_type('student'), Season("summer"), piece_name("Shirt"),
              piece_type("Shirt"), piece_color("white")), salience=1)
    def clothes839(self):
        self.myclothes = Myclothes(1, "vinous", "Trousers", 0, "", "", 0, "", "", 0, "", "", 5, "black", "Kandra", 0,
                                   "", "", 7, "black", "Hat", 8, "vinous", "carafe", 0, "", "", 0, "", "", 0, "", "", 0,
                                   "", "", 13, "black", "graduation_gown")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='dark'),
              Occasion('wadding'), Gender('male'), Person_type('brother'), Season("summer"), piece_name("Shirt"),
              piece_type("Shirt"), piece_color("white")), salience=1)
    def clothes840(self):
        self.myclothes = Myclothes(1, "black", "Trousers", 0, "", "", 0, "", "", 0, " ", "", 5, "gray", "shose", 0, "",
                                   "", 0, "", "", 8, "gray", "carafe", 0, "", "", 0, "", "", 11, "black", "waistband",
                                   0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='dark'),
              Occasion('wadding'), Gender('male'), Person_type('brother'), Season("summer"), piece_name("Shirt"),
              piece_type("Shirt"), piece_color("white")), salience=1)
    def clothes841(self):
        self.myclothes = Myclothes(1, "gray", "Trousers", 0, "", "", 0, "", "", 0, "", "", 5, "brown", "shose", 0,
                                   "", "", 0, "", "", 8, "grown", "carafe", 0, "", "", 0, "", "", 11, "black",
                                   "waistband", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('male'), Person_type('brother'), Season("summer"), piece_name("Shirt"),
              piece_type("Shirt"), piece_color("white")), salience=1)
    def clothes842(self):
        self.myclothes = Myclothes(1, "darkblue", "Trousers", 0, "", "", 0, "", "", 0, "", "", 5, "black", "shose", 0,
                                   "", "", 0, "", "", 8, "vinous", "carafe", 0, "", "", 0, "", "", 11, "black",
                                   "waistband", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='hanatawi'),
              Occasion('wadding'), Gender('male'), Person_type('brother'), Season("summer"), piece_name("Shirt"),
              piece_type("Shirt"), piece_color("white")), salience=1)
    def clothes843(self):
        self.myclothes = Myclothes(1, "black", "Trousers", 0, "", "", 0, "", "", 0, "", "", 5, "black", "shose", 0,
                                   "", "", 0, "", "", 8, "black", "carafe", 0, "", "", 0, "", "", 11, "black",
                                   "waistband", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='hanatawi'),
              Occasion('wadding'), Gender('male'), Person_type('friend'), Season("summer"), piece_name("Shirt"),
              piece_type("Shirt"), piece_color("white")), salience=1)
    def clothes844(self):
        self.myclothes = Myclothes(1, "white", "jeans", 0, "", "", 0, "", "", 0, "", "", 5, "brown", "shose", 6,
                                   "darkblue", "Coat", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 11, "brown",
                                   "waistband", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='hanatawi'),
              Occasion('wadding'), Gender('male'), Person_type('friend'), Season("summer"), piece_name("Shirt"),
              piece_type("Shirt"), piece_color("pink")), salience=1)
    def clothes845(self):
        self.myclothes = Myclothes(1, "black", "Trousers", 0, "", "", 0, "", "", 0, "", "", 5, "black", "shose", 0,
                                   "", "", 0, "", "", 8, "black", "carafe", 0, "", "", 0, "", "", 11, "black",
                                   "waistband", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='dark'),
              Occasion('wadding'), Gender('male'), Person_type('friend'), Season("summer"), piece_name("Shirt"),
              piece_type("Shirt"), piece_color("white")), salience=1)
    def clothes846(self):
        self.myclothes = Myclothes(1, "gray", "Trousers", 0, "", "", 0, "", "", 0, "", "", 5, "brown", "shose", 0, "",
                                   "", 0, "", "", 8, "darkblue", "carafe", 0, "", "", 0, "", "", 11, "brown",
                                   "waistband", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('male'), Person_type('friend'), Season("summer"), piece_name("Shirt"),
              piece_type("Shirt"), piece_color("cyan")), salience=1)
    def clothes847(self):
        self.myclothes = Myclothes(1, "darkblue", "Trousers", 0, "", "", 0, "", "", 0, "", "", 5, "brown", "shose",
                                   0, "", "", 0, "", "", 8, "grown", "carafe", 0, "", "", 0, "", "", 11, "brown",
                                   "waistband", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('male'), Person_type('friend'), Season("summer"), piece_name("Shirt"),
              piece_type("Shirt"), piece_color("gray")), salience=1)
    def clothes848(self):
        self.myclothes = Myclothes(1, "black", "Trousers", 0, "", "", 0, "", "", 0, " ", "", 5, "black", "shose", 0,
                                   "", "", 0, "", "", 8, "black", "carafe", 0, "", "", 0, "", "", 11, "black",
                                   "waistband", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='dark'),
              Occasion('wadding'), Gender('male'), Person_type('relatives'), Season("summer"), piece_name("Shirt"),
              piece_type("Shirt"), piece_color("white")), salience=1)
    def clothes849(self):
        self.myclothes = Myclothes(1, "gray", "Trousers", 0, "", "", 0, "", "", 0, "", "", 5, "brown", "shose", 0, "",
                                   "", 0, "", "", 8, "black", "carafe", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0,
                                   "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='dark'),
              Occasion('wadding'), Gender('male'), Person_type('relatives'), Season("summer"), piece_name("Shirt"),
              piece_type("Shirt"), piece_color("gray")), salience=1)
    def clothes850(self):
        self.myclothes = Myclothes(1, "darkblue", "jeans", 0, "", "", 0, "", "", 0, "", "", 5, "brown", "shose", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 11, "black", "waistband", 0, "",
                                   "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='hanatawi'),
              Occasion('wadding'), Gender('male'), Person_type('relatives'), Season("summer"), piece_name("Shirt"),
              piece_type("Shirt"), piece_color("vinous")), salience=1)
    def clothes851(self):
        self.myclothes = Myclothes(1, "black", "Trousers", 0, "", "", 0, "", "", 0, "", "", 5, "black", "shose", 0,
                                   "", "", 0, "", "", 8, "black", "carafe", 0, "", "", 0, "", "", 11, "black",
                                   "waistband", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    #     /////////////////////////////////////////////////////مناسبة زفاف
    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='dark'),
              Occasion('wadding'), Gender('male'), Person_type('brother'), Season("summer"), piece_name("Trousers"),
              piece_type("Trousers"), piece_color("black")), salience=1)
    def clothes852(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, " ", "", 5, "gray", "shose", 0, "",
                                   "", 0, "", "", 8, "gray", "carafe", 0, "", "", 0, "", "", 11, "black", "waistband",
                                   0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='dark'),
              Occasion('wadding'), Gender('male'), Person_type('brother'), Season("summer"), piece_name("Trousers"),
              piece_type("Trousers"), piece_color("gray")), salience=1)
    def clothes853(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, " ", "", 5, "brown", "shose", 0, "",
                                   "", 0, "", "", 8, "grown", "carafe", 0, "", "", 0, "", "", 11, "black", "waistband",
                                   0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('male'), Person_type('brother'), Season("summer"), piece_name("Trousers"),
              piece_type("Trousers"), piece_color("darkblue")), salience=1)
    def clothes854(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "black", "shose", 0, "",
                                   "", 0, "", "", 8, "vinous", "carafe", 0, "", "", 0, "", "", 11, "black", "waistband",
                                   0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='hanatawi'),
              Occasion('wadding'), Gender('male'), Person_type('brother'), Season("summer"), piece_name("Trousers"),
              piece_type("jeans"), piece_color("black")), salience=1)
    def clothes855(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, " ", "", 5, "black", "shose", 0, "",
                                   "", 0, "", "", 8, "black", "carafe", 0, "", "", 0, "", "", 11, "black", "waistband",
                                   0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='hanatawi'),
              Occasion('wadding'), Gender('male'), Person_type('friend'), Season("summer"), piece_name("Trousers"),
              piece_type("jeans"), piece_color("white")), salience=1)
    def clothes856(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, " ", "", 5, "brown", "shose", 6,
                                   "darkblue", "Coat", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 11, "brown",
                                   "waistband", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='hanatawi'),
              Occasion('wadding'), Gender('male'), Person_type('friend'), Season("summer"), piece_name("Trousers"),
              piece_type("Trousers"), piece_color("white")), salience=1)
    def clothes857(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "pink", "Shirt", 0, "", "", 5, "black", "shose", 0, "",
                                   "", 0, "", "", 8, "black", "carafe", 0, "", "", 0, "", "", 11, "black", "waistband",
                                   0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='dark'),
              Occasion('wadding'), Gender('male'), Person_type('friend'), Season("summer"), piece_name("Trousers"),
              piece_type("Trousers"), piece_color("gray")), salience=1)
    def clothes858(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "brown", "shose", 0, "",
                                   "", 0, "", "", 8, "darkblue", "carafe", 0, "", "", 0, "", "", 11, "brown",
                                   "waistband", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('male'), Person_type('friend'), Season("summer"), piece_name("Trousers"),
              piece_type("Trousers"), piece_color("darkblue")), salience=1)
    def clothes859(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "cyan", "Shirt", 0, " ", "", 5, "brown", "shose", 0, "",
                                   "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 11, "brown", "waistband", 0, "", "",
                                   0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('male'), Person_type('friend'), Season("summer"), piece_name("Trousers"),
              piece_type("Trousers"), piece_color("black")), salience=1)
    def clothes859999(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "cyan", "Shirt", 0, " ", "", 5, "brown", "shose", 0, "",
                                   "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 11, "brown", "waistband", 0, "", "",
                                   0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('male'), Person_type('friend'), Season("summer"), piece_name("Trousers"),
              piece_type("jeans"), piece_color("black")), salience=1)
    def clothes860(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "gray", "Shirt", 0, "", "", 5, "black", "shose", 0, "",
                                   "", 0, "", "", 8, "black", "carafe", 0, "", "", 0, "", "", 11, "black", "waistband",
                                   0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='dark'),
              Occasion('wadding'), Gender('male'), Person_type('relatives'), Season("summer"), piece_name("Trousers"),
              piece_type("jeans"), piece_color("gray")), salience=1)
    def clothes861(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "brown", "shose", 0, "",
                                   "", 0, "", "", 8, "black", "carafe", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0,
                                   "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='dark'),
              Occasion('wadding'), Gender('male'), Person_type('relatives'), Season("summer"), piece_name("jeans"),
              piece_type("Trousers"), piece_color("darkblue")), salience=1)
    def clothes862(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "gray", "Shirt", 0, "", "", 5, "brown", "shose", 0, "",
                                   "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 11, "black", "waistband", 0, "", "",
                                   0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='hanatawi'),
              Occasion('wadding'), Gender('male'), Person_type('relatives'), Season("summer"), piece_name("Trousers"),
              piece_type("Trousers"), piece_color("black")), salience=1)
    def clothes863(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "vinous", "Shirt", 0, "", "", 5, "black ", "shose", 0,
                                   "", "", 0, "", "", 8, "black", "carafe", 0, "", "", 0, "", "", 11, "black",
                                   "waistband", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('work'), Gender('female'), Person_type('officer'), Season("winter"), piece_name("Skirt"),
              piece_type("shortSkirt"), piece_color("black")), salience=1)
    def clothes864(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "black", "Kandra", 6,
                                   "vinous", "Coat", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 11, "black",
                                   "waistband", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='dark'),
              Occasion('work'), Gender('female'), Person_type('officer'), Season("winter"), piece_name("Skirt"),
              piece_type("shortSkirt"), piece_color("gray")), salience=1)
    def clothes865(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "black", "Kandra", 6,
                                   "gray", "Coat", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 11, "black", "waistband",
                                   0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='white'),
              Occasion('work'), Gender('female'), Person_type('officer'), Season("winter"), piece_name("Trousers"),
              piece_type("Trousers"), piece_color("black")), salience=1)
    def clothes866(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "black", "Kandra", 6,
                                   "beige", "Coat", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 11, "black",
                                   "waistband", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='white'),
              Occasion('work'), Gender('male'), Person_type('engineer'), Season("summer"), piece_name("Shirt"),
              piece_type("Shirt"), piece_color("white")), salience=1)
    def clothes867(self):
        self.myclothes = Myclothes(1, "darkblue", "jeans", 0, "", "", 0, "", "", 0, "", "", 5, "white", "shose", 0, "",
                                   "", 7, "yellow", "Hat", 0, "", "", 9, "orange", "Jacket", 0, "", "", 0, "", "", 0,
                                   "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('work'), Gender('male'), Person_type('engineer'), Season("summer"), piece_name("Shirt"),
              piece_type("Shirt"), piece_color("white")), salience=1)
    def clothes868(self):
        self.myclothes = Myclothes(1, "darkblue", "jeans", 0, "", "", 0, "", "", 0, "", "", 5, "white", "shose", 0, "",
                                   "", 7, "yellow", "Hat", 0, "", "", 9, "orange", "Jacket", 0, "", "", 0, "", "", 0,
                                   "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='dark'),
              Occasion('work'), Gender('male'), Person_type('engineer'), Season("summer"), piece_name("Shirt"),
              piece_type("Shirt"), piece_color("white")), salience=1)
    def clothes869(self):
        self.myclothes = Myclothes(1, "darkblue", "jeans", 0, "", "", 0, "", "", 0, "", "", 5, "white", "shose", 0, "",
                                   "", 7, "yellow", "Hat", 0, "", "", 9, "orange", "Jacket", 0, "", "", 0, "", "", 0,
                                   "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='white'),
              Occasion('work'), Gender('male'), Person_type('engineer'), Season("winter"), piece_name("Shirt"),
              piece_type("Shirt"), piece_color("white")), salience=1)
    def clothes870(self):
        self.myclothes = Myclothes(1, "gray", "jeans", 0, "", "", 0, "", "", 0, "", "", 5, "white", "shose", 0,
                                   "black", "Coat", 7, "yellow", "Hat", 0, "", "", 9, "orange", "Jacket", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('work'), Gender('male'), Person_type('engineer'), Season("winter"), piece_name("Shirt"),
              piece_type("Shirt"), piece_color("white")), salience=1)
    def clothes871(self):
        self.myclothes = Myclothes(1, "gray", "jeans", 0, "", "", 0, "", "", 0, "", "", 5, "white", "shose", 0,
                                   "black", "Coat", 7, "yellow", "Hat", 0, "", "", 9, "orange", "Jacket", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='dark'),
              Occasion('work'), Gender('male'), Person_type('engineer'), Season("winter"), piece_name("Shirt"),
              piece_type("Shirt"), piece_color("white")), salience=1)
    def clothes872(self):
        self.myclothes = Myclothes(1, "gray", "jeans", 0, "", "", 0, "", "", 0, "", "", 5, "white", "shose", 6, "gray",
                                   "Coat", 7, "yellow", "Hat", 0, "", "", 9, "orange", "Jacket", 0, "", "", 0, "", "",
                                   0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='white'),
              Occasion('work'), Gender('male'), Person_type('engineer'), Season("winter"), piece_name("Shirt"),
              piece_type("Shirt"), piece_color("white")), salience=1)
    def clothes873(self):
        self.myclothes = Myclothes(1, "darkblue", "jeans", 0, "", "", 0, "", "", 0, "", "", 5, "white", "shose", 6,
                                   "darkblue", "Coat", 7, "yellow", "Hat", 0, "", "", 9, "orange", "Jacket", 0, "", "",
                                   0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='white'),
              Occasion('work'), Gender('male'), Person_type('engineer'), Season("summer"), piece_name("Shirt"),
              piece_type("Shirt"), piece_color("white")), salience=1)
    def clothes874(self):
        self.myclothes = Myclothes(1, "darkblue", "jeans", 0, "", "", 0, "", "", 0, "", "", 5, "white", "shose", 6,
                                   "darkblue", "Coat", 7, "yellow", "Hat", 0, "", "", 9, "orange", "Jacket", 0, "", "",
                                   0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('work'), Gender('male'), Person_type('engineer'), Season("winter"), piece_name("Shirt"),
              piece_type("Shirt"), piece_color("white")), salience=2)
    def clothes875(self):
        self.myclothes = Myclothes(1, "darkblue", "jeans", 0, "", "", 0, "", "", 0, "", "", 5, "white", "shose", 6,
                                   "dark", "Coat", 7, "yellow", "Hat", 0, "", "", 9, "orange", "Jacket", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='dark'),
              Occasion('work'), Gender('male'), Person_type('engineer'), Season("winter"), piece_name("Shirt"),
              piece_type("Shirt"), piece_color("white")), salience=1)
    def clothes876(self):
        self.myclothes = Myclothes(1, "darkblue", "jeans", 0, "", "", 0, "", "", 0, "", "", 5, "white", "shose", 6,
                                   "gray", "Coat", 7, "yellow", "Hat", 0, "", "", 9, "orange", "Jacket", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='white'),
              Occasion('work'), Gender('male'), Person_type('engineer'), Season("winter"), piece_name("Trousers"),
              piece_type("jeans"), piece_color("gray")), salience=1)
    def clothes877(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "white", "shose", 6,
                                   "darkblue", "Coat", 7, "yellow", "Hat", 0, "", "", 9, "orange", "Jacket", 0, "", "",
                                   0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('work'), Gender('male'), Person_type('engineer'), Season("winter"), piece_name("Trousers"),
              piece_type("jeans"), piece_color("gray")), salience=1)
    def clothes878(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "white", "shose", 6,
                                   "dark", "Coat", 7, "yellow", "Hat", 0, "", "", 9, "orange", "Jacket", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='dark'),
              Occasion('work'), Gender('male'), Person_type('engineer'), Season("winter"), piece_name("Trousers"),
              piece_type("jeans"), piece_color("gray")), salience=1)
    def clothes879(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "white", "shose", 6,
                                   "gray", "Coat", 7, "yellow", "Hat", 0, "", "", 9, "orange", "Jacket", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='white'),
              Occasion('work'), Gender('male'), Person_type('engineer'), Season("winter"), piece_name("Trousers"),
              piece_type("jeans"), piece_color("darkblue")), salience=1)
    def clothes880(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "white", "shose", 6,
                                   "darkblue", "Coat", 7, "yellow", "Hat", 0, "", "", 9, "orange", "Jacket", 0, "", "",
                                   0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('work'), Gender('male'), Person_type('engineer'), Season("winter"), piece_name("Trousers"),
              piece_type("jeans"), piece_color("darkblue")), salience=1)
    def clothes881(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "white", "shose", 6,
                                   "dark", "Coat", 7, "yellow", "Hat", 0, "", "", 9, "orange", "Jacket", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='dark'),
              Occasion('work'), Gender('male'), Person_type('engineer'), Season("winter"), piece_name("Trousers"),
              piece_type("jeans"), piece_color("darkblue")), salience=1)
    def clothes882(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "white", "shose", 6,
                                   "gray", "Coat", 7, "yellow", "Hat", 0, "", "", 9, "orange", "Jacket", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='white'),
              Occasion('work'), Gender('male'), Person_type('engineer'), Season("summer"), piece_name("Trousers"),
              piece_type("jeans"), piece_color("gray")), salience=1)
    def clothes883(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "white", "shose", 0, "",
                                   "", 7, "yellow", "Hat", 0, "", "", 9, "orange", "Jacket", 0, "", "", 0, "", "", 0,
                                   "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('work'), Gender('male'), Person_type('engineer'), Season("summer"), piece_name("Trousers"),
              piece_type("jeans"), piece_color("gray")), salience=1)
    def clothes884(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "white", "shose", 0, "",
                                   "", 7, "yellow", "Hat", 0, "", "", 9, "orange", "Jacket", 0, "", "", 0, "", "", 0,
                                   "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='dark'),
              Occasion('work'), Gender('male'), Person_type('engineer'), Season("summer"), piece_name("Trousers"),
              piece_type("jeans"), piece_color("gray")), salience=1)
    def clothes885(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "white", "shose", 0, "",
                                   "", 7, "yellow", "Hat", 0, "", "", 9, "orange", "Jacket", 0, "", "", 0, "", "", 0,
                                   "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='white'),
              Occasion('work'), Gender('male'), Person_type('engineer'), Season("summer"), piece_name("Trousers"),
              piece_type("jeans"), piece_color("darkblue")), salience=1)
    def clothes886(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "white", "shose", 0, "",
                                   "", 7, "yellow", "Hat", 0, "", "", 9, "orange", "Jacket", 0, "", "", 0, "", "", 0,
                                   "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('work'), Gender('male'), Person_type('engineer'), Season("summer"), piece_name("Trousers"),
              piece_type("jeans"), piece_color("darkblue")), salience=1)
    def clothes887(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "white", "shose", 0, "",
                                   "", 7, "yellow", "Hat", 0, "", "", 9, "orange", "Jacket", 0, "", "", 0, "", "", 0,
                                   "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='dark'),
              Occasion('work'), Gender('male'), Person_type('engineer'), Season("summer"), piece_name("Trousers"),
              piece_type("jeans"), piece_color("darkblue")), salience=1)
    def clothes888(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "white", "shose", 0, "",
                                   "", 7, "yellow", "Hat", 0, "", "", 9, "orange", "Jacket", 0, "", "", 0, "", "", 0,
                                   "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='white'),
              Occasion('work'), Gender('female'), Person_type('engineer'), Season("summer"), piece_name("Shirt"),
              piece_type("Shirt"), piece_color("white")), salience=1)
    def clothes889(self):
        self.myclothes = Myclothes(1, "darkblue", "jeans", 0, "", "", 0, "", "", 0, "", "", 5, "white", "shose", 0, "",
                                   "", 7, "yellow", "Hat", 0, "", "", 9, "orange", "Jacket", 0, "", "", 0, "", "", 0,
                                   "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('work'), Gender('female'), Person_type('engineer'), Season("summer"), piece_name("Shirt"),
              piece_type("Shirt"), piece_color("white")), salience=1)
    def clothes890(self):
        self.myclothes = Myclothes(1, "darkblue", "jeans", 0, "", "", 0, "", "", 0, "", "", 5, "white", "shose", 0, "",
                                   "", 7, "yellow", "Hat", 0, "", "", 9, "orange", "Jacket", 0, "", "", 0, "", "", 0,
                                   "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='dark'),
              Occasion('work'), Gender('female'), Person_type('engineer'), Season("summer"), piece_name("Shirt"),
              piece_type("Shirt"), piece_color("white")), salience=1)
    def clothes891(self):
        self.myclothes = Myclothes(1, "darkblue", "jeans", 0, "", "", 0, "", "", 0, "", "", 5, "white", "shose", 0, "",
                                   "", 7, "yellow", "Hat", 0, "", "", 9, "orange", "Jacket", 0, "", "", 0, "", "", 0,
                                   "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='white'),
              Occasion('work'), Gender('female'), Person_type('engineer'), Season("winter"), piece_name("Shirt"),
              piece_type("Shirt"), piece_color("white")), salience=1)
    def clothes892(self):
        self.myclothes = Myclothes(1, "gray", "jeans", 0, "", "", 0, "", "", 0, "", "", 5, "white", "shose", 0,
                                   "black", "Coat", 7, "yellow", "Hat", 0, "", "", 9, "orange", "Jacket", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('work'), Gender('female'), Person_type('engineer'), Season("winter"), piece_name("Shirt"),
              piece_type("Shirt"), piece_color("white")), salience=1)
    def clothes893(self):
        self.myclothes = Myclothes(1, "gray", "jeans", 0, "", "", 0, "", "", 0, "", "", 5, "white", "shose", 0,
                                   "black", "Coat", 7, "yellow", "Hat", 0, "", "", 9, "orange", "Jacket", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='dark'),
              Occasion('work'), Gender('female'), Person_type('engineer'), Season("winter"), piece_name("Shirt"),
              piece_type("Shirt"), piece_color("white")), salience=1)
    def clothes894(self):
        self.myclothes = Myclothes(1, "gray", "jeans", 0, "", "", 0, "", "", 0, "", "", 5, "white", "shose", 6, "gray",
                                   "Coat", 7, "yellow", "Hat", 0, "", "", 9, "orange", "Jacket", 0, "", "", 0, "", "",
                                   0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='white'),
              Occasion('work'), Gender('female'), Person_type('engineer'), Season("winter"), piece_name("Shirt"),
              piece_type("Shirt"), piece_color("white")), salience=1)
    def clothes895(self):
        self.myclothes = Myclothes(1, "darkblue", "jeans", 0, "", "", 0, "", "", 0, "", "", 5, "white", "shose", 6,
                                   "darkblue", "Coat", 7, "yellow", "Hat", 0, "", "", 9, "orange", "Jacket", 0, "", "",
                                   0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('work'), Gender('female'), Person_type('engineer'), Season("winter"), piece_name("Shirt"),
              piece_type("Shirt"), piece_color("white")), salience=1)
    def clothes896(self):
        self.myclothes = Myclothes(1, "darkblue", "jeans", 0, "", "", 0, "", "", 0, "", "", 5, "white", "shose", 6,
                                   "dark", "Coat", 7, "yellow", "Hat", 0, "", "", 9, "orange", "Jacket", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='dark'),
              Occasion('work'), Gender('female'), Person_type('engineer'), Season("winter"), piece_name("Shirt"),
              piece_type("Shirt"), piece_color("white")), salience=1)
    def clothes897(self):
        self.myclothes = Myclothes(1, "darkblue", "jeans", 0, "", "", 0, "", "", 0, "", "", 5, "white", "shose", 6,
                                   "gray", "Coat", 7, "yellow", "Hat", 0, "", "", 9, "orange", "Jacket", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='white'),
              Occasion('work'), Gender('female'), Person_type('engineer'), Season("winter"), piece_name("Trousers"),
              piece_type("Trousers"), piece_color("gray")), salience=1)
    def clothes898(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "white", "shose", 6,
                                   "darkblue", "Coat", 7, "yellow", "Hat", 0, "", "", 9, "orange", "Jacket", 0, "", "",
                                   0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('work'), Gender('female'), Person_type('engineer'), Season("winter"), piece_name("Trousers"),
              piece_type("Trousers"), piece_color("gray")), salience=1)
    def clothes899(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "white", "shose", 6,
                                   "dark", "Coat", 7, "yellow", "Hat", 0, "", "", 9, "orange", "Jacket", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='dark'),
              Occasion('work'), Gender('female'), Person_type('engineer'), Season("winter"), piece_name("Trousers"),
              piece_type("Trousers"), piece_color("gray")), salience=1)
    def clothes900(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "white", "shose", 6,
                                   "gray", "Coat", 7, "yellow", "Hat", 0, "", "", 9, "orange", "Jacket", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='white'),
              Occasion('work'), Gender('female'), Person_type('engineer'), Season("winter"), piece_name("Trousers"),
              piece_type("Trousers"), piece_color("darkblue")), salience=1)
    def clothes901(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "white", "shose", 6,
                                   "darkblue", "Coat", 7, "yellow", "Hat", 0, "", "", 9, "orange", "Jacket", 0, "", "",
                                   0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('work'), Gender('female'), Person_type('engineer'), Season("winter"), piece_name("Trousers"),
              piece_type("Trousers"), piece_color("darkblue")), salience=1)
    def clothes902(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "white", "shose", 6,
                                   "dark", "Coat", 7, "yellow", "Hat", 0, "", "", 9, "orange", "Jacket", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='dark'),
              Occasion('work'), Gender('female'), Person_type('engineer'), Season("winter"), piece_name("Trousers"),
              piece_type("Trousers"), piece_color("darkblue")), salience=1)
    def clothes903(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "white", "shose", 6,
                                   "gray", "Coat", 7, "yellow", "Hat", 0, "", "", 9, "orange", "Jacket", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='white'),
              Occasion('work'), Gender('female'), Person_type('engineer'), Season("summer"), piece_name("Trousers"),
              piece_type("Trousers"), piece_color("gray")), salience=1)
    def clothes904(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "white", "shose", 0, "",
                                   "", 7, "yellow", "Hat", 0, "", "", 9, "orange", "Jacket", 0, "", "", 0, "", "", 0,
                                   "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('work'), Gender('female'), Person_type('engineer'), Season("summer"), piece_name("Trousers"),
              piece_type("Trousers"), piece_color("gray")), salience=1)
    def clothes905(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "white", "shose", 0, "",
                                   "", 7, "yellow", "Hat", 0, "", "", 9, "orange", "Jacket", 0, "", "", 0, "", "", 0,
                                   "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='dark'),
              Occasion('work'), Gender('female'), Person_type('engineer'), Season("summer"), piece_name("Trousers"),
              piece_type("Trousers"), piece_color("gray")), salience=1)
    def clothes906(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "white", "shose", 0, "",
                                   "", 7, "yellow", "Hat", 0, "", "", 9, "orange", "Jacket", 0, "", "", 0, "", "", 0,
                                   "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='white'),
              Occasion('work'), Gender('female'), Person_type('engineer'), Season("summer"), piece_name("Trousers"),
              piece_type("Trousers"), piece_color("darkblue")), salience=1)
    def clothes907(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "white", "shose", 0, "",
                                   "", 7, "yellow", "Hat", 0, "", "", 9, "orange", "Jacket", 0, "", "", 0, "", "", 0,
                                   "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('work'), Gender('female'), Person_type('engineer'), Season("summer"), piece_name("Trousers"),
              piece_type("Trousers"), piece_color("darkblue")), salience=1)
    def clothes908(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "white", "shose", 0, "",
                                   "", 7, "yellow", "Hat", 0, "", "", 9, "orange", "Jacket", 0, "", "", 0, "", "", 0,
                                   "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='dark'),
              Occasion('work'), Gender('female'), Person_type('ineer'), Season("summer"), piece_name("Trousers"),
              piece_type("Trousers"), piece_color("darkblue")), salience=1)
    def clothes910(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "white", "shose", 0, "",
                                   "", 7, "yellow", "Hat", 0, "", "", 9, "orange", "Jacket", 0, "", "", 0, "", "", 0,
                                   "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('work'), Gender('male'), Person_type('officer'), Season("winter"), piece_name("Trousers"),
              piece_type("Trousers"), piece_color("black")), salience=1)
    def clothes911(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "brown", "shose", 6,
                                   "black", "Coat", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 11, "brown",
                                   "waistband", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='dark'),
              Occasion('work'), Gender('male'), Person_type('officer'), Season("winter"), piece_name("Trousers"),
              piece_type("Trousers"), piece_color("gray")), salience=1)
    def clothes912(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "brown", "shose", 6,
                                   "black", "Coat", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 11, "brown",
                                   "waistband", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='white'),
              Occasion('work'), Gender('female'), Person_type('officer'), Season("winter"), piece_name("Trousers"),
              piece_type("Trousers"), piece_color("darkblue")), salience=1)
    def clothes913(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "beige", "Kandra", 6,
                                   "darkblue", "Coat", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 11, "beige",
                                   "waistband", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='dark'),
              Occasion('work'), Gender('female'), Person_type('business'), Season("winter"), piece_name("skirt"),
              piece_type("shortSkirt"), piece_color("gray")), salience=1)
    def clothes914(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "black", "Kandra", 6,
                                   "gray", "Coat", 0, "", "", 8, "blue", "carafe", 9, "black", "Jacket", 0, "", "", 0,
                                   "", "", 0, " ", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='white'),
              Occasion('work'), Gender('male'), Person_type('business'), Season("winter"), piece_name("skirt"),
              piece_type("shortSkirt"), piece_color("darkblue")), salience=1)
    def clothes915(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "brown", "Kandra", 6,
                                   "darkblue", "Coat", 0, "", "", 8, "brown", "darkblue", 9, "black", "Jacket", 0, "",
                                   "", 0, "", "", 0, " ", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('work'), Gender('female'), Person_type('business'), Season("winter"), piece_name("skirt"),
              piece_type("shortSkirt"), piece_color("gray")), salience=1)
    def clothes916(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "black", "Kandra", 6,
                                   "dark", "Coat", 0, "", "", 8, "black", "carafe", 9, "black", "Jacket", 0, "", "", 0,
                                   "", "", 0, " ", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='dark'),
              Occasion('work'), Gender('female'), Person_type('business'), Season("winter"), piece_name("Trousers"),
              piece_type("Trousers"), piece_color("gray")), salience=1)
    def clothes917(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "black", "Kandra", 6,
                                   "gray", "Coat", 0, "", "", 8, "blue", "carafe", 9, "black", "Jacket", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='white'),
              Occasion('work'), Gender('male'), Person_type('business'), Season("winter"), piece_name("Trousers"),
              piece_type("Trousers"), piece_color("darkblue")), salience=1)
    def clothes918(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "brown", "Kandra", 6,
                                   "darkblue", "Coat", 0, "", "", 8, "brown", "darkblue", 9, "black", "Jacket", 0, "",
                                   "", 0, "", "", 0, " ", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('work'), Gender('female'), Person_type('business'), Season("winter"), piece_name("Trousers"),
              piece_type("Trousers"), piece_color("gray")), salience=1)
    def clothes919(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "black", "Kandra", 6,
                                   "dark", "Coat", 0, "", "", 8, "black", "carafe", 9, "black", "Jacket", 0, "", "", 0,
                                   "", "", 0, " ", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='white'),
              Occasion('work'), Gender('male'), Person_type('business '), Season("winter"), piece_name("Trousers"),
              piece_type("Trousers"), piece_color("black")), salience=1)
    def clothes920(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "black", "Kandra", 6,
                                   "gray", "Coat", 0, "", "", 8, "vinous", "carafe", 9, "black", "Jacket", 0, "", "", 0,
                                   "", "", 0, " ", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='dark'),
              Occasion('work'), Gender('female'), Person_type('business'), Season("summer"), piece_name("Trousers"),
              piece_type("Trousers"), piece_color("gray")), salience=1)
    def clothes921(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "black", "Kandra", 6,
                                   "gray", "Coat", 0, "", "", 8, "blue", "carafe", 0, "", "", 0, "", "", 0, "", "", 0,
                                   " ", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='white'),
              Occasion('work'), Gender('male'), Person_type('business'), Season("summer"), piece_name("Trousers"),
              piece_type("Trousers"), piece_color("darkblue")), salience=1)
    def clothes922(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "brown", "Kandra", 6,
                                   "darkblue", "Coat", 0, "", "", 8, "brown", "darkblue", 0, "", "", 0, "", "", 0, "",
                                   "", 0, " ", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('work'), Gender('female'), Person_type('business'), Season("summer"), piece_name("Trousers"),
              piece_type("Trousers"), piece_color("gray")), salience=1)
    def clothes923(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "black", "Kandra", 6,
                                   "dark", "Coat", 0, "", "", 8, "black", "carafe", 0, "", "", 0, "", "", 0, "", "", 0,
                                   "", "", 0, "", )
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='white'),
              Occasion('work'), Gender('male'), Person_type('business'), Season("summer"), piece_name("Trousers"),
              piece_type("Trousers"), piece_color("black")), salience=1)
    def clothes924(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "black", "Kandra", 6,
                                   "gray", "Coat", 0, "", "", 8, "vinous", "carafe", 0, "", "", 0, "", "", 0, "", "", 0,
                                   " ", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('work'), Gender('female'), Person_type('business'), Season("summer"), piece_name("Shirt"),
              piece_type("Shirt"), piece_color("white")), salience=1)
    def clothes925(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 4, "darkblue", "skirt", 5, "beige", "Kandra", 6,
                                   "beige", "Coat", 0, "", "", 8, "beige", "carafe", 0, "", "", 0, "", "", 0, "", "", 0,
                                   "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('work'), Gender('female'), Person_type('business'), Season("summer"), piece_name("Shirt"),
              piece_type("Shirt"), piece_color("white")), salience=1)
    def clothes926(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 4, "black", "skirt", 5, "black", "Kandra", 6,
                                   "black", "Coat", 0, "", "", 8, "vinous", "carafe", 0, "", "", 0, "", "", 0, "", "",
                                   0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='dark'),
              Occasion('work'), Gender('female'), Person_type('business'), Season("summer"), piece_name("Shirt"),
              piece_type("Shirt"), piece_color("white")), salience=1)
    def clothes927(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 4, "gray", "skirt", 5, "black", "Kandra", 6, "gray",
                                   "Coat", 0, "", "", 8, "black", "carafe", 0, "", "", 0, "", "", 0, "", "", 0, " ", "",
                                   0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='white'),
              Occasion('work'), Gender('female'), Person_type('business'), Season("winter"), piece_name("Shirt"),
              piece_type("Shirt"), piece_color("white")), salience=1)
    def clothes928(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 4, "darkblue", "skirt", 5, "darkblue", "Kandra", 6,
                                   "darkblue", "Coat", 0, "", "", 8, "darkblue", "carafe", 9, "darkblue", "Jacket", 0,
                                   "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('work'), Gender('female'), Person_type('business'), Season("winter"), piece_name("Shirt"),
              piece_type("Shirt"), piece_color("white")), salience=1)
    def clothes929(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 4, "black", "skirt", 5, "black", "Kandra", 6,
                                   "black", "Coat", 0, "", "", 8, "vinous", "carafe", 9, "black", "Jacket", 0, "", "",
                                   0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='dark'),
              Occasion('work'), Gender('female'), Person_type('business'), Season("winter"), piece_name("Shirt"),
              piece_type("Shirt"), piece_color("white")), salience=1)
    def clothes930(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 4, "gray", "skirt", 5, "black", "Kandra", 6, "gray",
                                   "Coat", 0, "", "", 8, "black", "carafe", 9, "black", "Jacket", 0, "", "", 0, "", "",
                                   0, " ", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='white'),
              Occasion('work'), Gender('male'), Person_type('business'), Season("summer"), piece_name("Trousers"),
              piece_type("Trousers"), piece_color("darkblue")), salience=1)
    def clothes931(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "brown", "Kandra", 6,
                                   "darkblue", "Coat", 0, "", "", 8, "darkblue", "carafe", 0, "", "", 0, "", "", 0, "",
                                   "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('work'), Gender('male'), Person_type('business'), Season("summer"), piece_name("Trousers"),
              piece_type("Trousers"), piece_color("black")), salience=1)
    def clothes932(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "black", "Kandra", 6,
                                   "black", "Coat", 0, "", "", 8, "vinous", "carafe", 0, "", "", 0, "", "", 0, "", "",
                                   0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='dark'),
              Occasion('work'), Gender('male'), Person_type('business'), Season("summer"), piece_name("Trousers"),
              piece_type("Trousers"), piece_color("gray")), salience=1)
    def clothes933(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "black", "Kandra", 6,
                                   "gray", "Coat", 0, "", "", 8, "black", "carafe", 0, "", "", 0, "", "", 0, "", "", 0,
                                   "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='white'),
              Occasion('work'), Gender('male'), Person_type('business'), Season("summer"), piece_name("Shirt"),
              piece_type("Shirt"), piece_color("white")), salience=1)
    def clothes934(self):
        self.myclothes = Myclothes(1, "darkblue", "Trousers", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "brown",
                                   "Kandra", 6, "darkblue", "Coat", 0, "", "", 8, "darkblue", "carafe", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('work'), Gender('male'), Person_type('business'), Season("summer"), piece_name("Shirt"),
              piece_type("Shirt"), piece_color("white")), salience=1)
    def clothes935(self):
        self.myclothes = Myclothes(1, "black", "Trousers", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "black",
                                   "Kandra", 6, "black", "Coat", 0, "", "", 8, "vinous", "carafe", 0, "", "", 0, "", "",
                                   0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='dark'),
              Occasion('work'), Gender('male'), Person_type('business'), Season("summer"), piece_name("Shirt"),
              piece_type("Shirt"), piece_color("white")), salience=1)
    def clothes936(self):
        self.myclothes = Myclothes(1, "gray", "Trousers", 0, "", "", 0, "", "", 0, "", "", 5, "black", "Kandra", 6,
                                   "gray", "Coat", 0, "", "", 8, "black", "carafe", 0, "", "", 0, "", "", 0, "", "", 0,
                                   "", "", 0, "", "")
        self.result.append(self.myclothes)

    #         //////////

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='white'),
              Occasion('work'), Gender('female'), Person_type('business'), Season("summer"), piece_name("Shirt"),
              piece_type("Shirt"), piece_color("white")), salience=1)
    def clothes937(self):
        self.myclothes = Myclothes(1, "darkblue", "Trousers", 0, "", "", 0, "", "", 0, "", "", 5, "darkblue", "Kandra",
                                   6, "darkblue", "Coat", 0, "", "", 8, "darkblue", "carafe", 0, "", "", 0, "", "", 0,
                                   "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('work'), Gender('female'), Person_type('business'), Season("summer"), piece_name("Shirt"),
              piece_type("Shirt"), piece_color("white")), salience=1)
    def clothes938(self):
        self.myclothes = Myclothes(1, "black", "Trousers", 0, "", "", 0, "", "", 0, "", "", 5, "black", "Kandra", 6,
                                   "black", "Coat", 0, "", "", 8, "vinous", "carafe", 0, "", "", 0, "", "", 0, "", "",
                                   0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='dark'),
              Occasion('work'), Gender('female'), Person_type('business'), Season("summer"), piece_name("Shirt"),
              piece_type("Shirt"), piece_color("white")), salience=1)
    def clothes939(self):
        self.myclothes = Myclothes(1, "gray", "Trousers", 0, "", "", 0, "", "", 0, "", "", 5, "black", "Kandra", 6,
                                   "gray", "Coat", 0, "", "", 8, "black", "carafe", 0, "", "", 0, "", "", 0, "", "", 0,
                                   " ", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='white'),
              Occasion('work'), Gender('female'), Person_type('business'), Season("summer"), piece_name("Trousers"),
              piece_type("Trousers"), piece_color("darkblue")), salience=1)
    def clothes940(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 0, "", "", 5, "darkblue", "Kandra", 6, "darkblue",
                                   "Coat", 0, "", "", 8, "darkblue", "carafe", 0, "", "", 0, "", "", 0, "", "", 0, "",
                                   "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('work'), Gender('female'), Person_type('business'), Season("summer"), piece_name("Trousers"),
              piece_type("Trousers"), piece_color("black")), salience=1)
    def clothes941(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 0, "", "", 5, "black", "Kandra", 6, "black", "Coat",
                                   0, "", "", 8, "vinous", "carafe", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "",
                                   "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='dark'),
              Occasion('work'), Gender('female'), Person_type('business'), Season("summer"), piece_name("Trousers"),
              piece_type("Trousers"), piece_color("gray")), salience=1)
    def clothes942(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 0, "", "", 5, "black", "Kandra", 6, "gray", "Coat",
                                   0, "", "", 8, "black", "carafe", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "",
                                   "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='white'),
              Occasion('work'), Gender('female'), Person_type('business'), Season("winter"), piece_name("Jacket"),
              piece_type("Jacket"), piece_color("darkblue")), salience=1)
    def clothes943(self):
        self.myclothes = Myclothes(1, "darkblue", "Trousers", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "darkblue",
                                   "Kandra", 6, "darkblue", "Coat", 0, "", "", 8, "darkblue", "carafe", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('work'), Gender('female'), Person_type('business'), Season("winter"), piece_name("Jacket"),
              piece_type("Jacket"), piece_color("black")), salience=1)
    def clothes944(self):
        self.myclothes = Myclothes(1, "black", "Trousers", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "black",
                                   "Kandra", 6, "black", "Coat", 0, "", "", 8, "vinous", "carafe", 0, "", "", 0, "", "",
                                   0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='dark'),
              Occasion('work'), Gender('female'), Person_type('business'), Season("winter"), piece_name("Jacket"),
              piece_type("Jacket"), piece_color("black")), salience=1)
    def clothes945(self):
        self.myclothes = Myclothes(1, "gray", "Trousers", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "black",
                                   "Kandra", 6, "gray", "Coat", 0, "", "", 8, "black", "carafe", 0, "", "", 0, "", "",
                                   0, "", "", 0, " ", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='white'),
              Occasion('work'), Gender('female'), Person_type('business'), Season("winter"), piece_name("Trousers"),
              piece_type("Trousers"), piece_color("darkblue")), salience=1)
    def clothes946(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "darkblue", "Kandra", 6,
                                   "darkblue", "Coat", 0, "", "", 8, "darkblue", "carafe", 9, "darkblue", "Jacket", 0,
                                   "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('work'), Gender('female'), Person_type('business'), Season("winter"), piece_name("Trousers"),
              piece_type("Trousers"), piece_color("black")), salience=1)
    def clothes947(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "black", "Kandra", 6,
                                   "black", "Coat", 0, "", "", 8, "vinous", "carafe", 9, "black", "Jacket", 0, "", "",
                                   0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='dark'),
              Occasion('work'), Gender('female'), Person_type('business'), Season("winter"), piece_name("Trousers"),
              piece_type("Trousers"), piece_color("gray")), salience=1)
    def clothes948(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "black", "Kandra", 6,
                                   "gray", "Coat", 0, "", "", 8, "black", "carafe", 9, "black", "Jacket", 0, "", "", 0,
                                   "", "", 0, " ", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='white'),
              Occasion('work'), Gender('male'), Person_type('officer'), Season("summer"), piece_name("Trousers"),
              piece_type("Trousers"), piece_color("darkblue")), salience=1)
    def clothes949(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "brown", "shose", 0, "", "",
                                   0, "", "", 0, "", "", 0, "", "", 0, "", "", 11, "brown", "waistband", 0, "", "", 0,
                                   "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='white'),
              Occasion('work'), Gender('male'), Person_type('officer'), Season("summer"), piece_name("Shirt"),
              piece_type("Shirt"), piece_color("white")), salience=1)
    def clothes950(self):
        self.myclothes = Myclothes(1, "darkblue", "Trousers", 0, "", "", 0, "", "", 0, "", "", 5, "brown", "shose", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 11, "brown", "waistband", 0, "",
                                   "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='dark'),
              Occasion('work'), Gender('male'), Person_type('officer'), Season("summer"), piece_name("Shirt"),
              piece_type("Shirt"), piece_color("white")), salience=1)
    def clothes951(self):
        self.myclothes = Myclothes(1, "gray", "Trousers", 0, "", "", 0, "", "", 0, "", "", 5, "brown", "shose", 0, "",
                                   "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 11, "brown", "waistband", 0, "", "",
                                   0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('work'), Gender('male'), Person_type('officer'), Season("summer"), piece_name("Shirt"),
              piece_type("Shirt"), piece_color("white")), salience=1)
    def clothes952(self):
        self.myclothes = Myclothes(1, "black", "Trousers", 0, "", "", 0, "", "", 0, "", "", 5, "brown", "shose", 0, "",
                                   "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 11, "black", "waistband", 0, "", "",
                                   0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('work'), Gender('male'), Person_type('officer'), Season("summer"), piece_name("Trousers"),
              piece_type("Trousers"), piece_color("black")), salience=1)
    def clothes953(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "brown", "shose", 0, "", "",
                                   0, "", "", 0, "", "", 0, "", "", 0, "", "", 11, "black", "waistband", 0, "", "", 0,
                                   "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='dark'),
              Occasion('work'), Gender('male'), Person_type('officer'), Season("summer"), piece_name("Trousers"),
              piece_type("Trousers"), piece_color("gray")), salience=1)
    def clothes954(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "brown", "shose", 0, "", "",
                                   0, "", "", 0, "", "", 0, "", "", 0, "", "", 11, "brown", "waistband", 0, "", "", 0,
                                   "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='white'),
              Occasion('work'), Gender('male'), Person_type('officer'), Season("summer"), piece_name("Trousers"),
              piece_type("Trousers"), piece_color("black")), salience=1)
    def clothes955(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "brown", "shose", 0, "", "",
                                   0, "", "", 0, "", "", 0, "", "", 0, "", "", 11, "brown", "waistband", 0, "", "", 0,
                                   "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('work'), Gender('male'), Person_type('officer'), Season("summer"), piece_name("Trousers"),
              piece_type("Trousers"), piece_color("gray")), salience=1)
    def clothes956(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "brown", "shose", 0, "", "",
                                   0, "", "", 0, "", "", 0, "", "", 0, "", "", 11, "black", "waistband", 0, "", "", 0,
                                   "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='dark'),
              Occasion('work'), Gender('male'), Person_type('officer'), Season("summer"), piece_name("Trousers"),
              piece_type("Trousers"), piece_color("darkblue")), salience=1)
    def clothes957(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "brown", "shose", 0, "", "",
                                   0, "", "", 0, "", "", 0, "", "", 0, "", "", 11, "brown", "waistband", 0, "", "", 0,
                                   "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='white'),
              Occasion('work'), Gender('male'), Person_type('officer'), Season("summer"), piece_name("Trousers"),
              piece_type("Trousers"), piece_color("gray")), salience=1)
    def clothes958(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "brown", "shose", 0, "", "",
                                   0, "", "", 0, "", "", 0, "", "", 0, "", "", 11, "brown", "waistband", 0, "", "", 0,
                                   "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('work'), Gender('male'), Person_type('officer'), Season("summer"), piece_name("Trousers"),
              piece_type("Trousers"), piece_color("darkblue")), salience=1)
    def clothes959(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "brown", "shose", 0, "", "",
                                   0, "", "", 0, "", "", 0, "", "", 0, "", "", 11, "black", "waistband", 0, "", "", 0,
                                   "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='dark'),
              Occasion('work'), Gender('male'), Person_type('officer'), Season("summer"), piece_name("Trousers"),
              piece_type("Trousers"), piece_color("black")), salience=1)
    def clothes960(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "brown", "shose", 0, "", "",
                                   0, "", "", 0, "", "", 0, "", "", 0, "", "", 11, "brown", "waistband", 0, "", "", 0,
                                   "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='white'),
              Occasion('work'), Gender('female'), Person_type('officer'), Season("summer"), piece_name("Trousers"),
              piece_type("Trousers"), piece_color("darkblue")), salience=1)
    def clothes961(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "beige ", "Kandra", 0, "",
                                   "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 11, "beige", "waistband", 0, "", "",
                                   0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='white'),
              Occasion('work'), Gender('female'), Person_type('officer'), Season("summer"), piece_name("Shirt"),
              piece_type("Shirt"), piece_color("white")), salience=1)
    def clothes962(self):
        self.myclothes = Myclothes(1, "darkblue", "Trousers", 0, "", "", 0, "", "", 0, "", "", 5, "beige ", "Kandra", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 11, "beige", "waistband", 0, "",
                                   "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='dark'),
              Occasion('work'), Gender('female'), Person_type('officer'), Season("summer"), piece_name("Shirt"),
              piece_type("Shirt"), piece_color("white")), salience=1)
    def clothes963(self):
        self.myclothes = Myclothes(1, "gray", "Trousers", 0, "", "", 0, "", "", 0, "", "", 5, "beige", "Kandra", 0, "",
                                   "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 11, "beige", "waistband", 0, "", "",
                                   0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('work'), Gender('female'), Person_type('officer'), Season("summer"), piece_name("Shirt"),
              piece_type("Shirt"), piece_color("white")), salience=1)
    def clothes964(self):
        self.myclothes = Myclothes(1, "black", "Trousers", 0, "", "", 0, "", "", 0, "", "", 5, "beige", "Kandra", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 11, "beige", "waistband", 0, "",
                                   "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('work'), Gender('female'), Person_type('officer'), Season("summer"), piece_name("Trousers"),
              piece_type("Trousers"), piece_color("black")), salience=1)
    def clothes965(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "vinous", "Kandra", 0, "",
                                   "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 11, "vinous", "waistband", 0, "", "",
                                   0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='dark'),
              Occasion('work'), Gender('female'), Person_type('officer'), Season("summer"), piece_name("Trousers"),
              piece_type("Trousers"), piece_color("gray")), salience=1)
    def clothes969(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "black", "Kandra", 0, "",
                                   "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 11, "black", "waistband",
                                   0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='white'),
              Occasion('work'), Gender('female'), Person_type('officer'), Season("summer"), piece_name("Trousers"),
              piece_type("Trousers"), piece_color("black")), salience=1)
    def clothes970(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "beige ", "Kandra", 0, "",
                                   "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 11, "beige", "waistband", 0, "", "",
                                   0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('work'), Gender('female'), Person_type('officer'), Season("summer"), piece_name("Trousers"),
              piece_type("Trousers"), piece_color("gray")), salience=1)
    def clothes971(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "vinous", "Kandra", 0, "",
                                   "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 11, "vinous", "waistband", 0, "", "",
                                   0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='dark'),
              Occasion('work'), Gender('female'), Person_type('officer'), Season("summer"), piece_name("Trousers"),
              piece_type("Trousers"), piece_color("black")), salience=1)
    def clothes972(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "black", "Kandra", 0, "",
                                   "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 11, "black", "waistband",
                                   0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='white'),
              Occasion('work'), Gender('female'), Person_type('officer'), Season("summer"), piece_name("Trousers"),
              piece_type("Trousers"), piece_color("darkblue")), salience=1)
    def clothes972(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "darkblue", "Kandra", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "",
                                   0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('work'), Gender('female'), Person_type('officer'), Season("winter"), piece_name("Skirt"),
              piece_type("shortSkirt"), piece_color("black")), salience=1)
    def clothes972(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "black", "Kandra", 0, "",
                                   "", 0, "", "", 0, "", "", 9, "black", "Jacket", 0, "", "", 0, "", "", 0, "", "", 0,
                                   "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('work'), Gender('female'), Person_type('officer'), Season("winter"), piece_name("Shirt"),
              piece_type("Shirt"), piece_color("white")), salience=1)
    def clothes973(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 4, "black", "Skirt", 5, "black", "Kandra", 0, "",
                                   "", 0, "", "", 0, "", "", 9, "black", "Jacket", 0, "", "", 0, "", "", 0, "", "", 0,
                                   "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('work'), Gender('female'), Person_type('officer'), Season("winter"), piece_name("Shirt"),
              piece_type("Shirt"), piece_color("white")), salience=1)
    def clothes974(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 4, "black", "Skirt", 5, "black", "Kandra", 0, "",
                                   "", 0, "", "", 0, "", "", 9, "black", "Jacket", 0, "", "", 0, "", "", 0, "", "", 0,
                                   "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('work'), Gender('female'), Person_type('officer'), Season("winter"), piece_name("Jacket"),
              piece_type("Jacket"), piece_color("black")), salience=1)
    def clothes975(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 4, "black", "Skirt", 5, "black",
                                   "Kandra", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "",
                                   "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='dark'),
              Occasion('work'), Gender('female'), Person_type('officer'), Season("winter"), piece_name("Jacket"),
              piece_type("Jacket"), piece_color("black")), salience=1)
    def clothes976(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 4, "black", "Skirt", 5, "black",
                                   "Kandra", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "",
                                   "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='white'),
              Occasion('work'), Gender('female'), Person_type('officer'), Season("winter"), piece_name("Jacket"),
              piece_type("Jacket"), piece_color("darkblue")), salience=1)
    def clothes977(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 4, "gray", "Skirt", 5, "gray", "Kandra",
                                   0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "",
                                   "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='white'),
              Occasion('work'), Gender('female'), Person_type('officer'), Season("winter"), piece_name("Jacket"),
              piece_type("Jacket"), piece_color("gray")), salience=1)
    def clothes978(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 4, "black", "Skirt", 5, "black",
                                   "Kandra", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "",
                                   "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='dark'),
              Occasion('work'), Gender('female'), Person_type('officer'), Season("summer"), piece_name("Skirt"),
              piece_type("shortSkirt"), piece_color("darkblue")), salience=1)
    def clothes979(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "black", "Kandra", 0, "",
                                   "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='dark'),
              Occasion('work'), Gender('female'), Person_type('officer'), Season("winter"), piece_name("Skirt"),
              piece_type("shortSkirt"), piece_color("darkblue")), salience=1)
    def clothes980(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "black", "Kandra", 0, "",
                                   "", 0, "", "", 0, "", "", 9, "black", "Jacket", 0, "", "", 0, "", "", 0, "", "", 0,
                                   "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('work'), Gender('female'), Person_type('officer'), Season("winter"), piece_name("Skirt"),
              piece_type("shortSkirt"), piece_color("black")), salience=1)
    def clothes981(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "black", "Kandra", 0, "",
                                   "", 0, "", "", 0, "", "", 9, "black", "Jacket", 0, "", "", 0, "", "", 0, "", "", 0,
                                   "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='dark'),
              Occasion('work'), Gender('female'), Person_type('officer'), Season("summer"), piece_name("Skirt"),
              piece_type("shortSkirt"), piece_color("gray")), salience=1)
    def clothes982(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "black", "Kandra", 0, "",
                                   "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='dark'),
              Occasion('work'), Gender('female'), Person_type('officer'), Season("winter"), piece_name("Skirt"),
              piece_type("shortSkirt"), piece_color("gray")), salience=1)
    def clothes982(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "black", "Kandra", 0, "",
                                   "", 0, "", "", 0, "", "", 9, "black", "Jacket", 0, "", "", 0, "", "", 0, "", "", 0,
                                   "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('work'), Gender('female'), Person_type('officer'), Season("winter"), piece_name("Skirt"),
              piece_type("shortSkirt"), piece_color("darkblue")), salience=1)
    def clothes983(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "black", "Kandra", 0, "",
                                   "", 0, "", "", 0, "", "", 9, "black", "Jacket", 0, "", "", 0, "", "", 0, "", "", 0,
                                   "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='dark'),
              Occasion('work'), Gender('female'), Person_type('officer'), Season("summer"), piece_name("Skirt"),
              piece_type("shortSkirt"), piece_color("black")), salience=1)
    def clothes984(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "black", "Kandra", 0, "",
                                   "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='dark'),
              Occasion('work'), Gender('female'), Person_type('officer'), Season("winter"), piece_name("Skirt"),
              piece_type("shortSkirt"), piece_color("black")), salience=1)
    def clothes985(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "black", "Kandra", 0, "",
                                   "", 0, "", "", 0, "", "", 9, "black", "Jacket", 0, "", "", 0, "", "", 0, "", "", 0,
                                   "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='hanatawi'),
              Occasion('wadding'), Gender('male'), Person_type('relatives'), Season("summer"), piece_name("T_Shirt"),
              piece_type("T_Shirt"), piece_color("brown")), salience=1)
    def clothes985(self):
        self.myclothes = Myclothes(1, "black ", "jeans", 0, "", "", 0, "", "", 0, " ", "", 5, "black", "shose", 0, "",
                                   "", 0, "", "", 8, "black ", "carafe", 0, "", "", 0, "", "", 11, "black", "waistband",
                                   0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='dark'),
              Occasion('wadding'), Gender('male'), Person_type('relatives'), Season("summer"), piece_name("T_Shirt"),
              piece_type("T_Shirt"), piece_color("beige")), salience=1)
    def clothes986(self):
        self.myclothes = Myclothes(1, "darkblue", "Trousers", 0, "", "", 0, "", "", 0, " ", "", 5, "brown", "shose", 0,
                                   "", "", 0, "", "", 8, "darkblue ", "carafe", 0, "", "", 0, "", "", 11, "brown",
                                   "waistband", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('male'), Person_type('relatives'), Season("summer"), piece_name("Shirt"),
              piece_type("Shirt"), piece_color("cyan")), salience=1)
    def clothes987(self):
        self.myclothes = Myclothes(1, " darkblue", "jeans", 0, "", "", 0, "", "", 0, " ", "", 5, "black", "shose", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 11, "black", "waistband", 0, "",
                                   "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('male'), Person_type('relatives'), Season("summer"), piece_name("Shirt"),
              piece_type("Shirt"), piece_color("oil")), salience=1)
    def clothes988(self):
        self.myclothes = Myclothes(1, "black", "Trousers", 0, "", "", 0, "", "", 0, " ", "", 5, "black", "shose", 0,
                                   "", "", 0, "", "", 8, "black", "carafe", 0, "", "", 0, "", "", 11, "black",
                                   "waistband", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('male'), Person_type('relatives'), Season("summer"), piece_name("T_Shirt"),
              piece_type("T_Shirt"), piece_color("beige")), salience=1)
    def clothes989(self):
        self.myclothes = Myclothes(1, "darkblue", "Trousers", 0, " ", "", 0, "", "", 0, " ", "", 5, "brown", "shose",
                                   0, "", "", 0, "", "", 8, "black ", "carafe", 0, "", "", 0, "", "", 11, "black",
                                   "waistband", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='hanatawi'),
              Occasion('wadding'), Gender('male'), Person_type('relatives'), Season("summer"), piece_name("Trousers"),
              piece_type("jeans"), piece_color("black")), salience=1)
    def clothes990(self):
        self.myclothes = Myclothes(0, "", "", 2, "brown", "T_Shirt", 0, "", "", 0, "", "", 5, "black", "shose", 0,
                                   "", "", 0, "", "", 8, "black", "carafe", 0, "", "", 0, "", "", 11, "black",
                                   "waistband", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='dark'),
              Occasion('wadding'), Gender('male'), Person_type('relatives'), Season("summer"), piece_name("Trousers"),
              piece_type("jeans"), piece_color("brown")), salience=1)
    def clothes991(self):
        self.myclothes = Myclothes(0, "", "", 2, "beige", "T_Shirt", 0, "", "", 0, " ", "", 5, "brown", "shose", 0,
                                   "", "", 0, "", "", 8, "brown ", "carafe", 0, "", "", 0, "", "", 11, "brown ",
                                   "waistband", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('male'), Person_type('relatives'), Season("summer"), piece_name("Trousers"),
              piece_type("jeans"), piece_color("darkblue")), salience=1)
    def clothes992(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "cyan", "Shirt", 0, " ", "", 5, "black ", "shose", 0, "",
                                   "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 11, "black", "waistband", 0, "", "",
                                   0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('male'), Person_type('relatives'), Season("summer"), piece_name("Trousers"),
              piece_type("jeans"), piece_color("black")), salience=1)
    def clothes993(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "oil", "Shirt", 0, "", "", 5, "black", "shose", 0, "",
                                   "", 0, "", "", 8, "black", "carafe", 0, "", "", 0, "", "", 11, "black", "waistband",
                                   0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('male'), Person_type('relatives'), Season("summer"), piece_name("Trousers"),
              piece_type("jeans"), piece_color("darkblue")), salience=1)
    def clothes994(self):
        self.myclothes = Myclothes(1, "", "", 2, "beige", "T_Shirt", 0, "", "", 0, "", "", 5, "brown", "shose", 0,
                                   "", "", 0, "", "", 8, "black", "carafe", 0, "", "", 0, "", "", 11, "black",
                                   "waistband", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('female'), Person_type('relatives'), Season("summer"), piece_name("dress"),
              piece_type("Midriff"), piece_color("black")), salience=1)
    def clothes995(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 0, "", "", 5, "black", "Kandra", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('female'), Person_type('relatives'), Season("summer"), piece_name("dress"),
              piece_type("Midriff"), piece_color("vinous")), salience=1)
    def clothes996(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 0, "", "", 5, "black", "Kandra", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "", 0, " ", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('female'), Person_type('relatives'), Season("summer"), piece_name("dress"),
              piece_type("MidiDress"), piece_color("pink")), salience=1)
    def clothes997(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 0, "", "", 5, "black", "Kandra", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('female'), Person_type('relatives'), Season("summer"), piece_name("T_Shirt"),
              piece_type("T_Shirt"), piece_color("pink")), salience=1)
    def clothes998(self):
        self.myclothes = Myclothes(1, "cyan", "jeans", 0, "", "", 0, "", "", 0, "", "", 5, "white", "Kandra ", 0, "",
                                   "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 11, "black", "waistband", 0, "", "",
                                   0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('female'), Person_type('relatives'), Season("summer"), piece_name("T_Shirt"),
              piece_type("T_Shirt"), piece_color("yellow")), salience=1)
    def clothes999(self):
        self.myclothes = Myclothes(1, "black", "jeans", 0, "", "", 0, "", "", 0, " ", "", 5, "black", "Kandra", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 11, "black", "waistband", 0, "",
                                   "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='dark'),
              Occasion('wadding'), Gender('female'), Person_type('relatives'), Season("summer"), piece_name("dress"),
              piece_type("jeans"), piece_color("blue")), salience=1)
    def clothes1000(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 0, "", "", 5, "silver", "Kandra", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('female'), Person_type('relatives'), Season("summer"), piece_name("Trousers"),
              piece_type("Trousers"), piece_color("cyan")), salience=1)
    def clothes1001(self):
        self.myclothes = Myclothes(0, "", "", 2, " pink", "T_Shirt", 0, "", "", 0, " ", "", 5, "white", "Kandra", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 11, "black", "waistband", 0, "",
                                   "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('female'), Person_type('relatives'), Season("summer"), piece_name("Trousers"),
              piece_type("Trousers"), piece_color("black")), salience=1)
    def clothes1001(self):
        self.myclothes = Myclothes(0, "", "", 2, "yellow", "T_Shirt", 0, "", "", 0, "", "", 5, "black", "Kandra", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 11, "black", "waistband", 0, "",
                                   "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='dark'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer"), piece_name("dress"),
              piece_type("Midriff"), piece_color("gray")), salience=1)
    def clothes1002(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 0, "", "", 5, "black", "Kandra", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='hanatawi'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer"), piece_name("dress"),
              piece_type("MidiDress"), piece_color("pink")), salience=1)
    def clothes1003(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, " ", "", 0, "", "", 5, "white", "Kandra ", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", " ", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer"), piece_name("dress"),
              piece_type("MidiDress"), piece_color("cyan")), salience=1)
    def clothes1004(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 0, " ", "", 5, "silver", "Kandra", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer"), piece_name("dress"),
              piece_type("MidiDress"), piece_color("red")), salience=1)
    def clothes1005(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, " ", "", 0, " ", "", 5, "gold", "Kandra ", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='dark'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer"), piece_name("dress"),
              piece_type("Midriff"), piece_color("gold")), salience=1)
    def clothes1006(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, " ", "", 0, " ", "", 5, "black", "Kandra ", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='hanatawi'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer"), piece_name("dress"),
              piece_type("Long_robe"), piece_color("silver")), salience=1)
    def clothes1007(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, " ", "", 0, " ", "", 5, "black", "Kandra", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='dark'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer"), piece_name("dress"),
              piece_type("MidiDress"), piece_color("black")), salience=1)
    def clothes1008(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 0, "", "", 5, "vinous", "Kandra", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "", 0, " ", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer"), piece_name("dress"),
              piece_type("Long_robe"), piece_color("black")), salience=1)
    def clothes1009(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 0, "", "", 5, "vinous", "Kandra", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer"), piece_name("dress"),
              piece_type("Midriff"), piece_color("pink")), salience=1)
    def clothes1010(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 0, "", "", 5, "black", "Kandra", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer"), piece_name("dress"),
              piece_type("Long_robe"), piece_color("cyan")), salience=1)
    def clothes1011(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 0, "", "", 5, "gold", "Kandra", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "", 0, " ", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer"), piece_name("dress"),
              piece_type("Midriff"), piece_color("blue")), salience=1)
    def clothes1012(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 0, "", "", 5, "black", "Kandra", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='hanatawi'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer"), piece_name("dress"),
              piece_type("Long_robe"), piece_color("pink")), salience=1)
    def clothes1013(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 0, "", "", 5, "black", "Kandra", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='hanatawi'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer"), piece_name("dress"),
              piece_type("MidiDress"), piece_color("black")), salience=1)
    def clothes1014(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 0, " ", "", 5, "black", "Kandra", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='dark'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer"), piece_name("Shirt"),
              piece_type("Shirt"), piece_color("white")), salience=1)
    def clothes1015(self):
        self.myclothes = Myclothes(1, "black", "Trousers", 0, "", "", 0, "", "", 0, "", "", 5, "black", "Kandra", 6,
                                   "vinous", "Coat", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 11, "black",
                                   "waistband", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='dark'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer"), piece_name("Trousers"),
              piece_type("Trousers"), piece_color("black")), salience=1)
    def clothes1016(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "black", "Kandra", 6,
                                   "vinous", "Coat", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 11, "black",
                                   "waistband", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='dark'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer"), piece_name("T_Shirt"),
              piece_type("T_Shirt"), piece_color("yellow")), salience=1)
    def clothes1017(self):
        self.myclothes = Myclothes(1, "cyan", "Trousers", 0, "", "", 0, "", "", 0, " ", "", 5, "black", "Kandra", 0,
                                   "", "", 0, "", "", 0, " ", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='dark'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer"), piece_name("Trousers"),
              piece_type("jeans"), piece_color("cyan")), salience=1)
    def clothes1018(self):
        self.myclothes = Myclothes(0, "", "", 2, "yellow", "T_Shirt", 0, "", "", 0, "", "", 5, "black", "Kandra", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='dark'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer"), piece_name("T_Shirt"),
              piece_type("T_Shirt"), piece_color("pink")), salience=1)
    def clothes1019(self):
        self.myclothes = Myclothes(1, "black", "Trousers", 0, "", "", 0, "", "", 0, "", "", 5, "black", "Kandra", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer"), piece_name("T_Shirt"),
              piece_type("T_Shirt"), piece_color("yellow")), salience=1)
    def clothes1020(self):
        self.myclothes = Myclothes(1, "cyan", "Trousers", 0, "", "", 0, "", "", 0, "", "", 5, "black", "Kandra", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer"), piece_name("Trousers"),
              piece_type("jeans"), piece_color("cyan")), salience=1)
    def clothes1021(self):
        self.myclothes = Myclothes(0, "", "", 2, "yellow", "T_Shirt", 0, "", "", 0, "", "", 5, "black", "Kandra", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer"), piece_name("T_Shirt"),
              piece_type("T_Shirt"), piece_color("red")), salience=1)
    def clothes1022(self):
        self.myclothes = Myclothes(1, "black", "Trousers", 0, "", "", 0, "", "", 0, "", "", 5, "black", "Kandra", 0,
          "", "", 0, "", "", 0, " ", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='dark'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer"), piece_name("Trousers"),
              piece_type("jeans"), piece_color("black")), salience=1)
    def clothes1023(self):
        self.myclothes = Myclothes(0, "", "", 2, "pink", "T_Shirt", 0, "", "", 0, "", "", 5, "black", "Kandra", 0, "",
                                   "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='dark'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer"), piece_name("Shirt"),
              piece_type("Shirt"), piece_color("red")), salience=1)
    def clothes1024(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 4, "white", "shortSkirt", 5, "white", "Kandra",
                                   6, "black", "Coat", 0, "", "", 0, "", "", 0, "", "", 0, " ", "", 0, "", "", 0, "",
                                   "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='dark'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer"), piece_name("Skirt"),
              piece_type("MidSkirt"), piece_color("white")), salience=1)
    def clothes1025(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "pink", "Shirt", 0, " ", "", 5, "white", "Kandra", 6,
                                   "black", "Coat", 0, "", "", 0, "", "", 0, "", "", 0, " ", "", 0, "", "", 0, "", "",
                                   0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer"), piece_name("Skirt"),
              piece_type("MidSkirt"), piece_color("white")), salience=1)
    def clothes1026(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "red", "Shirt", 0, "", "", 5, "white", "Kandra", 6,
                                   "black", "Coat", 0, "", "", 0, "", "", 0, "", "", 0, " ", "", 0, "", "", 0, "", "",
                                   0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='hanatawi'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer"), piece_name("Skirt"),
              piece_type("MidSkirt"), piece_color("white")), salience=1)
    def clothes1027(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "pink", "Shirt", 0, "", "", 5, "white", "Kandra", 6,
                                   "black", "Coat", 0, "", "", 0, "", "", 0, "", "", 0, " ", "", 0, "", "", 0, "", "",
                                   0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='dark'),
              Occasion('wadding'), Gender('female'), Person_type('relatives'), Season("summer"), piece_name("dress"),
              piece_type("Midriff"), piece_color("beige")), salience=1)
    def clothes1028(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 0, "", "", 5, "black", "Kandra", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "", 0, " ", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='hanatawi'),
              Occasion('wadding'), Gender('female'), Person_type('relatives'), Season("summer"), piece_name("dress"),
              piece_type("Long_robe"), piece_color("beige")), salience=1)
    def clothes1029(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 0, "", "", 5, "black", "Kandra", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='dark'),
              Occasion('wadding'), Gender('female'), Person_type('relatives'), Season("summer"), piece_name("dress"),
              piece_type("MidiDress"), piece_color("gray")), salience=1)
    def clothes1030(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 0, " ", "", 5, "black", "Kandra", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='dark'),
              Occasion('wadding'), Gender('female'), Person_type('relatives'), Season("summer"), piece_name("dress"),
              piece_type("Long_robe"), piece_color("black")), salience=1)
    def clothes1031(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 0, "", "", 5, "vinous", "Kandra", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='dark'),
              Occasion('wadding'), Gender('female'), Person_type('relatives'), Season("summer"), piece_name("T_Shirt"),
              piece_type("T_Shirt"), piece_color("black")), salience=1)
    def clothes1032(self):
        self.myclothes = Myclothes(1, "cyan", "jeans", 0, "", "", 0, "", "", 0, "", "", 5, "white", "shose", 0, "",
                                   "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='dark'),
              Occasion('wadding'), Gender('female'), Person_type('relatives'), Season("summer"), piece_name("T_Shirt"),
              piece_type("T_Shirt"), piece_color("yellow")), salience=1)
    def clothes1033(self):
        self.myclothes = Myclothes(1, "darkblue", "jeans", 0, "", "", 0, "", "", 0, "", "", 5, "white", "shose", 0,
                                   "", "", 0, "", "", 0, " ", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='dark'),
              Occasion('wadding'), Gender('female'), Person_type('relatives'), Season("summer"), piece_name("T_Shirt"),
              piece_type("T_Shirt"), piece_color("pink")), salience=1)
    def clothes1034(self):
        self.myclothes = Myclothes(1, "cyan", "jeans", 0, "", "", 0, "", "", 0, "", "", 5, "white", "shose", 0, "",
                                   "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='dark'),
              Occasion('wadding'), Gender('female'), Person_type('relatives'), Season("summer"), piece_name("Trousers"),
              piece_type("jeans"), piece_color("cyan")), salience=1)
    def clothes1035(self):
        self.myclothes = Myclothes(0, "", "", 2, "black", "T_Shirt", 0, "", "", 0, "", "", 5, "white", "shose", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='dark'),
              Occasion('wadding'), Gender('female'), Person_type('relatives'), Season("summer"), piece_name("Trousers"),
              piece_type("Trousers"), piece_color("darkblue")), salience=1)
    def clothes1036(self):
        self.myclothes = Myclothes(0, "", "", 2, "yellow", "T_Shirt", 0, "", "", 0, "", "", 5, "white", "shose", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='dark'),
              Occasion('wadding'), Gender('female'), Person_type('relatives'), Season("summer"), piece_name("Trousers"),
              piece_type("Trousers"), piece_color("cyan")), salience=1)
    def clothes1037(self):
        self.myclothes = Myclothes(0, "", "", 2, "pink", "T_Shirt", 0, "", "", 0, "", "", 5, "white", "shose", 0, "",
                                   "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='dark'),
              Occasion('wadding'), Gender('female'), Person_type('relatives'), Season("summer"), piece_name("Trousers"),
              piece_type("Trousers"), piece_color("cyan")), salience=1)
    def clothes1038(self):
        self.myclothes = Myclothes(0, "", "", 2, "brown", "T_Shirt", 0, "", "", 0, "", "", 5, "white", "shose", 0, "",
                                   "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='hanatawi'),
              Occasion('wadding'), Gender('female'), Person_type('relatives'), Season("summer"), piece_name("Trousers"),
              piece_type("jeans"), piece_color("cyan")), salience=1)
    def clothes1039(self):
        self.myclothes = Myclothes(0, "", "", 2, "yellow", "T_Shirt", 0, "", "", 0, " ", "", 5, "white", "shose", 0,
                                   "", "", 0, "", "", 0, " ", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='dark'),
              Occasion('wadding'), Gender('female'), Person_type('relatives'), Season("summer"), piece_name("T_Shirt"),
              piece_type("T_Shirt"), piece_color("red")), salience=1)
    def clothes1040(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 4, "black", "MidSkirt", 5, "white", "shose", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, " ", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('female'), Person_type('relatives'), Season("summer"), piece_name("Skirt"),
              piece_type("MidSkirt"), piece_color("white")), salience=1)
    def clothes1041(self):
        self.myclothes = Myclothes(0, "", "", 2, "green", "T_Shirt", 0, "", "", 0, "", "", 5, "white", "shose", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, " ", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='hanatawi'),
              Occasion('wadding'), Gender('female'), Person_type('relatives'), Season("summer"), piece_name("dress"),
              piece_type("Midriff"), piece_color("red")), salience=1)
    def clothes1042(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 0, "", "", 5, "gold", "Kandra", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='hanatawi'),
              Occasion('wadding'), Gender('female'), Person_type('relatives'), Season("summer"), piece_name("dress"),
              piece_type("Midriff"), piece_color("pink")), salience=1)
    def clothes1043(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 0, " ", "", 5, "black", "Kandra", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='hanatawi'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer"), piece_name("dress"),
              piece_type("Long_robe"), piece_color("gold")), salience=1)
    def clothes1044(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 0, "", "", 5, "gold", "Kandra", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='hanatawi'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer"), piece_name("dress"),
              piece_type("Long_robe"), piece_color("silver")), salience=1)
    def clothes1045(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 0, "", "", 5, "black", "Kandra", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='hanatawi'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer"), piece_name("dress"),
              piece_type("MidiDress"), piece_color("pink")), salience=1)
    def clothes1046(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 0, "", "", 5, "white", "Sandal", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='hanatawi'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer"), piece_name("dress"),
              piece_type("MidiDress"), piece_color("pink")), salience=1)
    def clothes1047(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 0, "", "", 5, "black", "Kandra", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer"), piece_name("dress"),
              piece_type("MidiDress"), piece_color("darkblue")), salience=1)
    def clothes1048(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 0, "", "", 5, "pink", "Kandra", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "", 0, " ", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer"), piece_name("dress"),
              piece_type("MidiDress"), piece_color("red")), salience=1)
    def clothes1049(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 0, "", "", 5, "black", "Kandra", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "", 0, " ", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer"), piece_name("dress"),
              piece_type("Long_robe"), piece_color("pink")), salience=1)
    def clothes1050(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 0, "", "", 5, "silver", "Kandra", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer"), piece_name("dress"),
              piece_type("Long_robe"), piece_color("beige")), salience=1)
    def clothes1051(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 0, "", "", 5, "black", "Kandra", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer"), piece_name("dress"),
              piece_type("Long_robe"), piece_color("black")), salience=1)
    def clothes1052(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 0, "", "", 5, "silver", "Kandra", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer"), piece_name("T_Shirt"),
              piece_type("T_Shirt"), piece_color("pink")), salience=1)
    def clothes1053(self):
        self.myclothes = Myclothes(1, "cyan", "jeans", 0, "", "", 0, "", "", 0, "", "", 5, "white", "shose", 0, "",
                                   "", 0, "", "", 0, " ", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer"), piece_name("T_Shirt"),
              piece_type("T_Shirt"), piece_color("cyan")), salience=1)
    def clothes1054(self):
        self.myclothes = Myclothes(1, "darkblue", "jeans", 0, "", "", 0, "", "", 0, "", "", 5, "white", "shose", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer"), piece_name("T_Shirt"),
              piece_type("T_Shirt"), piece_color("blue")), salience=1)
    def clothes1055(self):
        self.myclothes = Myclothes(1, "cyan", "jeans", 0, "", "", 0, "", "", 0, "", "", 5, "white", "shose", 0, "",
                                   "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer"), piece_name("T_Shirt"),
              piece_type("T_Shirt"), piece_color("vinous")), salience=1)
    def clothes1056(self):
        self.myclothes = Myclothes(1, "cyan", "jeans", 0, "", "", 0, "", "", 0, "", "", 5, "white", "shose", 0, "",
                                   "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer"), piece_name("Trousers"),
              piece_type("Trousers"), piece_color("black")), salience=1)
    def clothes1057(self):
        self.myclothes = Myclothes(0, "", "", 2, "vinous", "T_Shirt", 0, "", "", 0, "", "", 5, "white", "shose", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer"), piece_name("Trousers"),
              piece_type("jeans"), piece_color("black")), salience=1)
    def clothes1058(self):
        self.myclothes = Myclothes(0, "", "", 2, "cyan", "T_Shirt", 0, "", "", 0, "", "", 5, "white", "shose", 0, "",
                                   "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer"), piece_name("Trousers"),
              piece_type("jeans"), piece_color("black")), salience=1)
    def clothes1059(self):
        self.myclothes = Myclothes(0, "", "", 2, "red", "T_Shirt", 0, "", "", 0, "", "", 5, "white", "shose", 0, "",
                                   "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer"), piece_name("Trousers"),
              piece_type("jeans"), piece_color("black")), salience=1)
    def clothes1060(self):
        self.myclothes = Myclothes(0, "", "", 2, "green", "T_Shirt", 0, "", "", 0, "", "", 5, "white", "shose", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer"), piece_name("Trousers"),
              piece_type("jeans"), piece_color("cyan")), salience=1)
    def clothes1061(self):
        self.myclothes = Myclothes(0, "", "", 2, "blue", "T_Shirt", 0, "", "", 0, "", "", 5, "white", "shose", 0, "",
                                   "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer"), piece_name("Trousers"),
              piece_type("jeans"), piece_color("darkblue")), salience=1)
    def clothes1062(self):
        self.myclothes = Myclothes(0, "", "", 2, "oil", "T_Shirt", 0, "", "", 0, "", "", 5, "white", "shose", 0, "",
                                   "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer"), piece_name("Trousers"),
              piece_type("jeans"), piece_color("darkblue")), salience=1)
    def clothes1063(self):
        self.myclothes = Myclothes(0, "", "", 2, "brown ", "T_Shirt", 0, "", "", 0, "", "", 5, "white", "shose", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer"), piece_name("Trousers"),
              piece_type("jeans"), piece_color("white")), salience=1)
    def clothes1064(self):
        self.myclothes = Myclothes(0, "", "", 2, "pink", "T_Shirt", 0, "", "", 0, "", "", 5, "white", "shose", 0, "",
                                   "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer"), piece_name("Trousers"),
              piece_type("jeans"), piece_color("white")), salience=1)
    def clothes1065(self):
        self.myclothes = Myclothes(0, "", "", 2, "yellow", "T_Shirt", 0, "", "", 0, "", "", 5, "white", "shose", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer"), piece_name("Trousers"),
              piece_type("jeans"), piece_color("white")), salience=1)
    def clothes1066(self):
        self.myclothes = Myclothes(0, "", "", 2, "black", "T_Shirt", 0, "", "", 0, "", "", 5, "white", "shose", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer"), piece_name("Trousers"),
              piece_type("jeans"), piece_color("black")), salience=1)
    def clothes1067(self):
        self.myclothes = Myclothes(0, "", "", 2, "white", "T_Shirt", 0, "", "", 0, "", "", 5, "white", "shose", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer"), piece_name("Trousers"),
              piece_type("jeans"), piece_color("pink")), salience=1)
    def clothes1068(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "black", "Kandra", 0, "",
                                   "", 0, "", "", 0, " ", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer"), piece_name("dress"),
              piece_type("MidiDress"), piece_color("brown")), salience=1)
    def clothes1069(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 0, "", "", 5, "silver", "Kandra", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer"), piece_name("Skirt"),
              piece_type("shortSkirt"), piece_color("black")), salience=1)
    def clothes1070(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "pink", "Shirt", 4, "", "", 5, "pink", "Kandra", 0, "",
                                   "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer"), piece_name("Skirt"),
              piece_type("MidSkirt"), piece_color("black")), salience=1)
    def clothes1071(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "silver", "Shirt", 4, "", "", 5, "black", "Kandra", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, " ", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer"), piece_name("Skirt"),
              piece_type("shortSkirt"), piece_color("black")), salience=1)
    def clothes1072(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 4, "", "", 5, "black", "Kandra", 0, "",
                                   "", 0, "", "", 0, "", "", 0, "", "", 0, " ", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer"), piece_name("Skirt"),
              piece_type("MidSkirt"), piece_color("white")), salience=1)
    def clothes1073(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "cyan", "Shirt", 0, "", "", 5, "black", "Kandra", 0, "",
                                   "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer"), piece_name("Skirt"),
              piece_type("MidSkirt"), piece_color("white")), salience=1)
    def clothes1074(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "pink", "Shirt", 0, "", "", 5, "pink", "Kandra", 0, "",
                                   "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer"), piece_name("Skirt"),
              piece_type("shortSkirt"), piece_color("white")), salience=1)
    def clothes1075(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "green", "Shirt", 0, "", "", 5, "white", "Kandra", 0, "",
                                   "", 0, "", "", 0, "", "", 0, "", "", 0, " ", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer"), piece_name("Skirt"),
              piece_type("shortSkirt"), piece_color("white")), salience=1)
    def clothes1076(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "pink", "Shirt", 0, "", "", 5, "white", "Kandra", 0, "",
                                   "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='hanatawi'),
              Occasion('wadding'), Gender('female'), Person_type('brother'), Season("summer"), piece_name("dress"),
              piece_type("Long_robe"), piece_color("gold")), salience=1)
    def clothes1077(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 0, "", "", 5, "black", "Kandra", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='hanatawi'),
              Occasion('wadding'), Gender('female'), Person_type('brother'), Season("summer"), piece_name("dress"),
              piece_type("Long_robe"), piece_color("vinous")), salience=1)
    def clothes1078(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 0, "", "", 5, "gold", "Kandra", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='hanatawi'),
              Occasion('wadding'), Gender('female'), Person_type('brother'), Season("summer"), piece_name("dress"),
              piece_type("Midriff"), piece_color("pink")), salience=1)
    def clothes1079(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 0, "", "", 5, "black", "Kandra", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='hanatawi'),
              Occasion('wadding'), Gender('female'), Person_type('brother'), Season("summer"), piece_name("dress"),
              piece_type("Long_robe"), piece_color("silver")), salience=1)
    def clothes1080(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 0, "", "", 5, "silver", "Kandra", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='hanatawi'),
              Occasion('wadding'), Gender('female'), Person_type('brother'), Season("summer"), piece_name("dress"),
              piece_type("Long_robe"), piece_color("black")), salience=1)
    def clothes1081(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 0, "", "", 5, "vinous", "Kandra", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='hanatawi'),
              Occasion('wadding'), Gender('female'), Person_type('brother'), Season("summer"), piece_name("dress"),
              piece_type("Midriff"), piece_color("white")), salience=1)
    def clothes1082(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 0, "", "", 5, "silver", "Kandra", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='hanatawi'),
              Occasion('wadding'), Gender('female'), Person_type('brother'), Season("summer"), piece_name("dress"),
              piece_type("Long_robe"), piece_color("yellow")), salience=1)
    def clothes1083(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 0, "", "", 5, "vinous", "Kandra", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='hanatawi'),
              Occasion('wadding'), Gender('female'), Person_type('brother'), Season("summer"), piece_name("dress"),
              piece_type("Long_robe"), piece_color("blue")), salience=1)
    def clothes1084(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 0, "", "", 5, "vinous", "Kandra", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='hanatawi'),
              Occasion('wadding'), Gender('female'), Person_type('brother'), Season("summer"), piece_name("Trousers"),
              piece_type("wide_pants"), piece_color("black")), salience=1)
    def clothes1085(self):
        self.myclothes = Myclothes(0, "", "", 2, "vinous", "T_Shirt", 0, "", "", 0, "", "", 5, "white", "shose", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='hanatawi'),
              Occasion('wadding'), Gender('female'), Person_type('brother'), Season("summer"), piece_name("Trousers"),
              piece_type("wide_pants"), piece_color("white")), salience=1)
    def clothes1086(self):
        self.myclothes = Myclothes(0, "", "", 2, "vinous", "T_Shirt", 0, "", "", 0, "", "", 5, "white", "shose ", 0,
                                   "", "", 0, "", "", 0, " ", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='hanatawi'),
              Occasion('wadding'), Gender('female'), Person_type('brother'), Season("summer"), piece_name("Trousers"),
              piece_type("wide_pants"), piece_color("black")), salience=1)
    def clothes1087(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "black", "Kandra", 0, "",
                                   "", 0, "", "", 0, " ", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='hanatawi'),
              Occasion('wadding'), Gender('female'), Person_type('brother'), Season("summer"), piece_name("Skirt"),
              piece_type("shortSkirt"), piece_color("cyan")), salience=1)
    def clothes1088(self):
        self.myclothes = Myclothes(0, "", "", 2, "white", "T_Shirt", 0, "", "", 0, "", "", 5, "white", "shose", 0, "",
                                   "", 0, "", "", 0, " ", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('female'), Person_type('brother'), Season("summer"), piece_name("dress"),
              piece_type("Long_robe"), piece_color("gold")), salience=1)
    def clothes1089(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 0, "", "", 5, "black", "Kandra", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "", 0, " ", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('female'), Person_type('brother'), Season("summer"), piece_name("dress"),
              piece_type("Long_robe"), piece_color("silver")), salience=1)
    def clothes1090(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 0, "", "", 5, "black", "Kandra", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('female'), Person_type('brother'), Season("summer"), piece_name("dress"),
              piece_type("Long_robe"), piece_color("red")), salience=1)
    def clothes1091(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 0, "", "", 5, "white", "Kandra", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "", 0, " ", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('female'), Person_type('brother'), Season("summer"), piece_name("dress"),
              piece_type("Long_robe"), piece_color("pink")), salience=1)
    def clothes1092(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 0, "", "", 5, "black", "Kandra", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "", 10, "vinous", "Mididress", 0, "", "", 0, "", "", 0,
                                   "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('female'), Person_type('brother'), Season("summer"), piece_name("dress"),
              piece_type("Long_robe"), piece_color("beige")), salience=1)
    def clothes1093(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 0, "", "", 5, "black", "Kandra", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "", 0, " ", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('female'), Person_type('brother'), Season("summer"), piece_name("dress"),
              piece_type("Midriff"), piece_color("yellow")), salience=1)
    def clothes1094(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 0, "", "", 5, "silver", "Kandra", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('female'), Person_type('brother'), Season("summer"), piece_name("dress"),
              piece_type("Midriff"), piece_color("pink")), salience=1)
    def clothes1095(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 0, "", "", 5, "silver", "Kandra", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "", 0, " ", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('female'), Person_type('brother'), Season("summer"), piece_name("Trousers"),
              piece_type("wide_pants"), piece_color("white")), salience=1)
    def clothes1096(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "pink", "Shirt", 0, "", "", 5, "pink", "shose", 0, "",
                                   "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('female'), Person_type('brother'), Season("summer"), piece_name("Trousers"),
              piece_type("wide_pants"), piece_color("black")), salience=1)
    def clothes1097(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "pink", "Shirt", 0, "", "", 5, "pink", "shose", 0, "",
                                   "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('female'), Person_type('brother'), Season("summer"), piece_name("Shirt"),
              piece_type("Shirt"), piece_color("cyan")), salience=1)
    def clothes1098(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 4, "gray ", "Skirt", 5, "gray", "Kandra", 6,
                                   "white", "Coat", 0, "", "", 0, "", "", 0, "", "", 0, " ", "", 0, "", "", 0, "", "",
                                   0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('female'), Person_type('brother'), Season("summer"), piece_name("Skirt"),
              piece_type("shortSkirt"), piece_color("pink")), salience=1)
    def clothes1099(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "cyan", "Shirt", 0, "", "", 5, "gray", "Kandra", 6,
                                   "white", "Coat", 0, "", "", 0, "", "", 0, "", "", 0, " ", "", 0, "", "", 0, "", "",
                                   0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='dark'),
              Occasion('wadding'), Gender('female'), Person_type('brother'), Season("summer"), piece_name("dress"),
              piece_type("Long_robe"), piece_color("gold")), salience=1)
    def clothes1100(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 0, "", "", 5, "black", "Kandra", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='dark'),
              Occasion('wadding'), Gender('female'), Person_type('brother'), Season("summer"), piece_name("dress"),
              piece_type("Long_robe"), piece_color("silver")), salience=1)
    def clothes1101(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 0, "", "", 5, "black", "Kandra", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='dark'),
              Occasion('wadding'), Gender('female'), Person_type('brother'), Season("summer"), piece_name("dress"),
              piece_type("Long_robe"), piece_color("pink")), salience=1)
    def clothes1102(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 0, "", "", 5, "silver", "Kandra ", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='dark'),
              Occasion('wadding'), Gender('female'), Person_type('brother'), Season("summer"), piece_name("dress"),
              piece_type("Long_robe"), piece_color("bule")), salience=1)
    def clothes1103(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 0, " ", "", 5, "gray", "Kandra", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='dark'),
              Occasion('wadding'), Gender('female'), Person_type('brother'), Season("summer"), piece_name("dress"),
              piece_type("Long_robe"), piece_color("vinous")), salience=1)
    def clothes1104(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 0, " ", "", 5, "silver", "Kandra", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='dark'),
              Occasion('wadding'), Gender('female'), Person_type('brother'), Season("summer"), piece_name("dress"),
              piece_type("Long_robe"), piece_color("gray")), salience=1)
    def clothes1105(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 0, " ", "", 5, "silver", "Kandra", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='dark'),
              Occasion('wadding'), Gender('female'), Person_type('brother'), Season("summer"), piece_name("dress"),
              piece_type("Long_robe"), piece_color("black")), salience=1)
    def clothes1106(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 0, "", "", 5, "silver", "Kandra", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='dark'),
              Occasion('wadding'), Gender('female'), Person_type('brother'), Season("summer"), piece_name("Trousers"),
              piece_type("jeans"), piece_color("pink")), salience=1)
    def clothes1107(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "pink", "Kandra", 0, "",
                                   "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='dark'),
              Occasion('wadding'), Gender('female'), Person_type('brother'), Season("summer"), piece_name("Trousers"),
              piece_type("wide_pants"), piece_color("green")), salience=1)
    def clothes1108(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "black", "Shirt", 0, "", "", 5, "pink", "Kandra", 0, "",
                                   "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='dark'),
              Occasion('wadding'), Gender('female'), Person_type('brother'), Season("summer"), piece_name("Shirt"),
              piece_type("Shirt"), piece_color("pink")), salience=1)
    def clothes1109(self):
        self.myclothes = Myclothes(1, "blue", "Trousers", 0, "", "", 0, "", "", 0, "", "", 5, "black", "Kandra", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='dark'),
              Occasion('wadding'), Gender('female'), Person_type('brother'), Season("summer"), piece_name("Shirt"),
              piece_type("Shirt"), piece_color("white")), salience=1)
    def clothes1110(self):
        self.myclothes = Myclothes(1, "blue", "Trousers", 0, "", "", 0, "", "", 0, "", "", 5, "white", "Kandra", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='dark'),
              Occasion('wadding'), Gender('female'), Person_type('brother'), Season("summer"), piece_name("Shirt"),
              piece_type("Shirt"), piece_color("white")), salience=1)
    def clothes1111(self):
        self.myclothes = Myclothes(1, "black", "Trousers", 0, "", "", 0, "", "", 0, "", "", 5, "white", "Kandra",
                                   0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "",
                                   "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='dark'),
              Occasion('wadding'), Gender('female'), Person_type('brother'), Season("summer"), piece_name("Trousers"),
              piece_type("wide_pants"), piece_color("black")), salience=1)
    def clothes1112(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "black", "Kandra", 0, "",
                                   "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='dark'),
              Occasion('wadding'), Gender('female'), Person_type('brother'), Season("summer"), piece_name("Trousers"),
              piece_type("wide_pants"), piece_color("black")), salience=1)
    def clothes1113(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "pink", "Shirt", 0, "", "", 5, "black", "Kandra", 0, "",
                                   "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='dark'),
              Occasion('wadding'), Gender('female'), Person_type('brother'), Season("summer"), piece_name("Trousers"),
              piece_type("wide_pants"), piece_color("gray")), salience=1)
    def clothes1114(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "vinous", "Shirt", 0, "", "", 5, "black", "Kandra", 0, "",
                                   "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='dark'),
              Occasion('wadding'), Gender('female'), Person_type('brother'), Season("summer"), piece_name("Trousers"),
              piece_type("wide_pants"), piece_color("gray")), salience=1)
    def clothes1115(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "brown", "Shirt", 0, "", "", 5, "black", "Kandra", 0, "",
                                   "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='dark'),
              Occasion('wadding'), Gender('female'), Person_type('brother'), Season("summer"), piece_name("Skirt"),
              piece_type("shortSkirt"), piece_color("black")), salience=1)
    def clothes1116(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "black", "Kandra", 0, "",
                                   "", 0, "", "", 0, "", "", 0, "", "", 0, " ", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='dark'),
              Occasion('wadding'), Gender('female'), Person_type('brother'), Season("summer"), piece_name("Skirt"),
              piece_type("MidSkirt"), piece_color("white")), salience=1)
    def clothes1117(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "pink", "Shirt", 0, "", "", 5, "black", "Kandra", 0, "",
                                   "", 0, "", "", 0, "", "", 0, "", "", 0, " ", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='dark'),
              Occasion('wadding'), Gender('female'), Person_type('brother'), Season("summer"), piece_name("Skirt"),
              piece_type("shortSkirt"), piece_color("darkblue")), salience=1)
    def clothes1118(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "brown", "Shirt", 0, "", "", 5, "black", "Kandra", 0, "",
                                   "", 0, "", "", 0, "", "", 0, "", "", 0, " ", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='dark'),
              Occasion('wadding'), Gender('female'), Person_type('brother'), Season("summer"), piece_name("Shirt"),
              piece_type("Shirt"), piece_color("white")), salience=1)
    def clothes1119(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 4, "black", "Skirt", 5, "black", "Kandra", 6,
                                   "black", "Coat", 0, "", "", 0, "", "", 0, "", "", 0, " ", "", 0, "", "", 0, "", "",
                                   0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='dark'),
              Occasion('wadding'), Gender('female'), Person_type('brother'), Season("summer"), piece_name("Shirt"),
              piece_type("Shirt"), piece_color("vinous")), salience=1)
    def clothes1120(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 4, "white", "Skirt", 5, "white", "Kandra", 0, "",
                                   "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='hanatawi'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer"), piece_name("dress"),
              piece_type("Long_robe"), piece_color("gold")), salience=1)
    def clothes1121(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 0, "", "", 5, "pink", "Kandra", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "", 0, " ", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='hanatawi'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer"), piece_name("dress"),
              piece_type("Long_robe"), piece_color("beige")), salience=1)
    def clothes1122(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 0, "", "", 5, "black", "Kandra", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='hanatawi'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer"), piece_name("dress"),
              piece_type("Long_robe"), piece_color("cyan")), salience=1)
    def clothes1123(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 0, "", "", 5, "white", "Sandal", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='hanatawi'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer"), piece_name("dress"),
              piece_type("Long_robe"), piece_color("blue")), salience=1)
    def clothes1124(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 0, "", "", 5, "white", "Sandal", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='hanatawi'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer"), piece_name("dress"),
              piece_type("Long_robe"), piece_color("white")), salience=1)
    def clothes1125(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 0, "", "", 5, "white", "Sandal", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='hanatawi'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer"), piece_name("dress"),
              piece_type("Long_robe"), piece_color("pink")), salience=1)
    def clothes1126(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 0, "", "", 5, "silver", "Kandra", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='hanatawi'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer"), piece_name("dress"),
              piece_type("Long_robe"), piece_color("vinous")), salience=1)
    def clothes1127(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 0, "", "", 5, "black", "Kandra", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='hanatawi'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer"), piece_name("dress"),
              piece_type("Long_robe"), piece_color("black")), salience=1)
    def clothes1128(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 0, "", "", 5, "black", "Kandra", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='hanatawi'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer"), piece_name("Trousers"),
              piece_type("wide_pants"), piece_color("pink")), salience=1)
    def clothes1129(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "black", "Shirt", 0, "", "", 5, "black", "Kandra", 0, "",
                                   "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='hanatawi'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer"), piece_name("Trousers"),
              piece_type("wide_pants"), piece_color("pink")), salience=1)
    def clothes1130(self):
        self.myclothes = Myclothes(0, "", "", 2, "white", "T_Shirt", 0, "", "", 0, "", "", 5, "white", "shose", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='hanatawi'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer"), piece_name("Trousers"),
              piece_type("wide_pants"), piece_color("black")), salience=1)
    def clothes1131(self):
        self.myclothes = Myclothes(0, "", "", 2, "vinous", "T_Shirt", 0, "", "", 0, "", "", 5, "white", "shose", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='hanatawi'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer"), piece_name("Trousers"),
              piece_type("wide_pants"), piece_color("white")), salience=1)
    def clothes1132(self):
        self.myclothes = Myclothes(0, "", "", 2, "vinous", "T_Shirt", 0, "", "", 0, "", "", 5, "white", "shose", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='hanatawi'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer"), piece_name("Trousers"),
              piece_type("wide_pants"), piece_color("brown")), salience=1)
    def clothes1139(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, " beige", "Shirt", 0, " ", "", 5, "gold", "Sandal ", 0, "",
                                   "", 0, "", "", 0, " ", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='hanatawi'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer"), piece_name("Trousers"),
              piece_type("wide_pants"), piece_color("brown")), salience=1)
    def clothes1133(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "black", "Sandal", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='hanatawi'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer"), piece_name("Trousers"),
              piece_type("wide_pants"), piece_color("pink")), salience=1)
    def clothes1134(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "black", "Sandal", 0, "",
                                   "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer"), piece_name("Skirt"),
              piece_type("shortSkirt"), piece_color("darkblue")), salience=1)
    def clothes1135(self):
        self.myclothes = Myclothes(0, "", "", 2, "yellow", "T_Shirt", 0, "", "", 0, "", "", 5, "white", "shose", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer"), piece_name("Skirt"),
              piece_type("shortSkirt"), piece_color("black")), salience=1)
    def clothes5472(self):
        self.myclothes = Myclothes(0, "", "", 2, "pink", "T_Shirt", 0, "", "", 0, "", "", 5, "white", "shose", 0, "",
                                   "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer"), piece_name("Skirt"),
              piece_type("shortSkirt"), piece_color("white")), salience=1)
    def clothes5482(self):
        self.myclothes = Myclothes(0, "", "", 2, "pink", "T_Shirt", 0, "", "", 0, "", "", 5, "white", "shose", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, " ", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer"), piece_name("Skirt"),
              piece_type("shortSkirt"), piece_color("black")), salience=1)
    def clothes5492(self):
        self.myclothes = Myclothes(0, "", "", 2, "gold", "T_Shirt", 0, "", "", 0, "", "", 5, "white", "shose", 0, "",
                                   "", 0, "", "", 0, "", "", 0, "", "", 0, " ", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)


    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('Hinking_with_friends'), Gender('female'), Person_type('person'), Season("summer"),
              piece_name("Shirt"), piece_type("Shirt"), piece_color("Shirt")), salience=1)
    def clothes64911(self):
        self.myclothes = Myclothes(1, "gray", "Trousers", 0, "", "", 0, "", "", 0, "", "", 5, "white", "shose", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)


    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('Hinking_with_friends'), Gender('female'), Person_type('person'), Season("summer"),
              piece_name("Shirt"), piece_type("Shirt"), piece_color("pink")), salience=1)
    def clothes6511(self):
        self.myclothes = Myclothes(1, "gray", "Trousers", 0, "", "", 0, "", "", 0, "", "", 5, "white", "shose", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='dark'),
              Occasion('Hinking_with_friends'), Gender('female'), Person_type('person'), Season("summer"),
              piece_name("Shirt"), piece_type("Shirt"), piece_color("vinous")), salience=1)
    def clothes6521(self):
        self.myclothes = Myclothes(1, "gray", "Trousers", 0, "", "", 0, "", "", 0, "", "", 5, "dark", "shose", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='white'),
              Occasion('Hinking_with_friends'), Gender('female'), Person_type('person'), Season("summer"),
              piece_name("T_Shirt"), piece_type("T_Shirt"), piece_color("red")), salience=1)
    def clothes6531(self):
        self.myclothes = Myclothes(1, "gray", "jeans", 0, "", "", 0, "", "", 0, "", "", 5, "white", "shose", 0, "",
                                   "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('Hinking_with_friends'), Gender('female'), Person_type('person'), Season("summer"),
              piece_name("T_Shirt"), piece_type("T_Shirt"), piece_color("pink")), salience=1)
    def clothes6541(self):
        self.myclothes = Myclothes(1, "gray", "jeans", 0, "", "", 0, "", "", 0, "", "", 5, "white", "shose", 0, "",
                                   "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='white'),
              Occasion('Hinking_with_friends'), Gender('female'), Person_type('person'), Season("summer"),
              piece_name("T_Shirt"), piece_type("T_Shirt"), piece_color("pink")), salience=1)
    def clothes6551(self):
        self.myclothes = Myclothes(1, "gray", "jeans", 0, "", "", 0, "", "", 0, "", "", 5, "white", "shose", 0, "",
                                   "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='dark'),
              Occasion('Hinking_with_friends'), Gender('female'), Person_type('person'), Season("summer"),
              piece_name("T_Shirt"), piece_type("T_Shirt"), piece_color("pink")), salience=1)
    def clothes6561(self):
        self.myclothes = Myclothes(1, "white", "jeans", 0, "", "", 0, "", "", 0, "", "", 5, "white", "shose", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='white'),
              Occasion('Hinking_with_friends'), Gender('female'), Person_type('person'), Season("summer"),
              piece_name("T_Shirt"), piece_type("T_Shirt"), piece_color("green")), salience=1)
    def clothes6571(self):
        self.myclothes = Myclothes(1, "white", "jeans", 0, "", "", 0, "", "", 0, "", "", 5, "white", "shose", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('Hinking_with_friends'), Gender('female'), Person_type('person'), Season("summer"),
              piece_name("T_Shirt"), piece_type("T_Shirt"), piece_color("yellow")), salience=1)
    def clothes6581(self):
        self.myclothes = Myclothes(1, "white", "jeans", 0, "", "", 0, "", "", 0, "", "", 5, "white", "shose", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='dark'),
              Occasion('Hinking_with_friends'), Gender('female'), Person_type('person'), Season("summer"),
              piece_name("T_Shirt"), piece_type("T_Shirt"), piece_color("pink")), salience=1)
    def clothes6591(self):
        self.myclothes = Myclothes(1, "black", "jeans", 0, "", "", 0, "", "", 0, "", "", 5, "white", "shose", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='dark'),
              Occasion('Hinking_with_friends'), Gender('female'), Person_type('person'), Season("summer"),
              piece_name("T_Shirt"), piece_type("T_Shirt"), piece_color("brown")), salience=1)
    def clothes6601(self):
        self.myclothes = Myclothes(1, "black", "jeans", 0, "", "", 0, "", "", 0, "", "", 5, "white", "shose", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='white'),
              Occasion('Hinking_with_friends'), Gender('female'), Person_type('person'), Season("summer"),
              piece_name("T_Shirt"), piece_type("T_Shirt"), piece_color("beige")), salience=1)
    def clothes6611(self):
        self.myclothes = Myclothes(1, "black", "jeans", 0, "", "", 0, "", "", 0, "", "", 5, "white", "shose", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('Hinking_with_friends'), Gender('female'), Person_type('person'), Season("summer"),
              piece_name("T_Shirt"), piece_type("T_Shirt"), piece_color("yellow")), salience=1)
    def clothes6621(self):
        self.myclothes = Myclothes(1, "black", "jeans", 0, "", "", 0, "", "", 0, "", "", 5, "white", "shose", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('Hinking_with_friends'), Gender('female'), Person_type('person'), Season("summer"),
              piece_name("T_Shirt"), piece_type("T_Shirt"), piece_color("yellow")), salience=1)
    def clothes6631(self):
        self.myclothes = Myclothes(1, "darkblue", "jeans", 0, "", "", 0, "", "", 0, "", "", 5, "white", "shose", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='white'),
              Occasion('Hinking_with_friends'), Gender('female'), Person_type('person'), Season("summer"),
              piece_name("Hoodie"), piece_type("T_Shirt"), piece_color("orange")), salience=1)
    def clothes6641(self):
        self.myclothes = Myclothes(1, "black", "Trousers", 0, "", "", 0, "", "", 0, "", "", 5, "white", "shose", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('Hinking_with_friends'), Gender('female'), Person_type('person'), Season("summer"),
              piece_name("T_Shirt"), piece_type("Hoodie"), piece_color("yellow")), salience=1)
    def clothes6651(self):
        self.myclothes = Myclothes(1, "white", "Trousers", 0, "", "", 0, "", "", 0, " ", "", 5, "white", "shose", 0,
                                   "", "", 0, "", "", 0, " ", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='dark'),
              Occasion('Hinking_with_friends'), Gender('female'), Person_type('person'), Season("summer"),
              piece_name("T_Shirt"), piece_type("Hoodie"), piece_color("vinous")), salience=1)
    def clothes6661(self):
        self.myclothes = Myclothes(1, "white", "Trousers", 0, "", "", 0, "", "", 0, "", "", 5, "white", "shose", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='white'),
              Occasion('Hinking_with_friends'), Gender('male'), Person_type('person'), Season("summer"),
              piece_name("T_Shirt"), piece_type("T_Shirt"), piece_color("cyan")), salience=1)
    def clothes6671(self):
        self.myclothes = Myclothes(1, "beige", "short", 0, "", "", 0, "", "", 5, "white", "shose", 0, "", "", 0, "",
                                   "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='dark'),
              Occasion('Hinking_with_friends'), Gender('male'), Person_type('person'), Season("summer"),
              piece_name("T_Shirt"), piece_type("T_Shirt"), piece_color("brown")), salience=1)
    def clothes6681(self):
        self.myclothes = Myclothes(1, "beige", "short", 0, "", "", 0, "", "", 5, "white", "shose", 0, "", "", 0, "",
                                   "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('Hinking_with_friends'), Gender('male'), Person_type('person'), Season("summer"),
              piece_name("T_Shirt"), piece_type("T_Shirt"), piece_color("white")), salience=1)
    def clothes6691(self):
        self.myclothes = Myclothes(1, "black", "short", 0, "", "", 0, "", "", 5, "white", "shose ", 0, "", "", 0, "",
                                   "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='white'),
              Occasion('Hinking_with_friends'), Gender('male'), Person_type('person'), Season("summer"),
              piece_name("T_Shirt"), piece_type("T_Shirt"), piece_color("yellow")), salience=1)
    def clothes6701(self):
        self.myclothes = Myclothes(1, "black", "short", 0, "", "", 0, "", "", 5, "white", "shose", 0, "", "", 0, "",
                                   "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='dark'),
              Occasion('Hinking_with_friends'), Gender('male'), Person_type('person'), Season("summer"),
              piece_name("T_Shirt"), piece_type("T_Shirt"), piece_color("white")), salience=1)
    def clothes6711(self):
        self.myclothes = Myclothes(1, "vinous", "short", 0, "", "", 0, "", "", 5, "white", "shose", 0, "", "", 0, "",
                                   "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('Hinking_with_friends'), Gender('male'), Person_type('person'), Season("summer"),
              piece_name("T_Shirt"), piece_type("T_Shirt"), piece_color("oil")), salience=1)
    def clothes6721(self):
        self.myclothes = Myclothes(1, "black", "short", 0, "", "", 0, "", "", 5, "white", "shose", 0, "", "", 0, "",
                                   "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('Hinking_with_friends'), Gender('male'), Person_type('person'), Season("summer"),
              piece_name("T_Shirt"), piece_type("T_Shirt"), piece_color("gray")), salience=1)
    def clothes6731(self):
        self.myclothes = Myclothes(1, "black", "short", 0, "", "", 0, "", "", 5, "white", "shose", 0, "", "", 0, "",
                                   "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('Hinking_with_friends'), Gender('male'), Person_type('person'), Season("summer"),
              piece_name("T_Shirt"), piece_type("T_Shirt"), piece_color("vinous")), salience=1)
    def clothes6741(self):
        self.myclothes = Myclothes(1, "gray", "short", 0, "", "", 0, "", "", 5, "white", "shose", 0, "", "", 0, "",
                                   "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='dark'),
              Occasion('Hinking_with_friends'), Gender('male'), Person_type('person'), Season("summer"),
              piece_name("T_Shirt"), piece_type("T_Shirt"), piece_color("black")), salience=1)
    def clothes6751(self):
        self.myclothes = Myclothes(1, "white", "short", 0, "", "", 0, "", "", 5, "white", "shose", 0, "", "", 0, "",
                                   "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('Hinking_with_friends'), Gender('male'), Person_type('person'), Season("summer"),
              piece_name("T_Shirt"), piece_type("T_Shirt"), piece_color("black")), salience=1)
    def clothes6761(self):
        self.myclothes = Myclothes(1, "white", "short", 0, "", "", 0, "", "", 5, "white", "shose", 0, "", "", 0, "",
                                   "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)


    @Rule(AND(age(value=P(lambda value: value >= 21) & P(lambda value: value <= 35)), SkinColor(color='hanatawi'),
              Occasion('gradution'), Gender('female'), Person_type('student'), Season("summer"), piece_name("Skirt"),
              piece_type("MidSkirt"), piece_color("black")), salience=1)
    def clothes42555(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "gray", "Kandra", 6,
                                   "cyan", "Coat", 7, "black", "Hat", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "",
                                   "", 13, "black", "graduation_gown")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 21) & P(lambda value: value <= 35)), SkinColor(color='dark'),
              Occasion('gradution'), Gender('female'), Person_type('student'), Season("summer"), piece_name("Skirt"),
              piece_type("MidSkirt"), piece_color("black")), salience=1)
    def clothes2844(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "black", "Kandra", 6,
                                   "black", "Coat", 7, "black", "Hat", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0,
                                   "", "", 13, "black", "graduation_gown")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 21) & P(lambda value: value <= 35)), SkinColor(color='hanatawi'),
              Occasion('gradution'), Gender('female'), Person_type('student'), Season("summer"), piece_name("Skirt"),
              piece_type("MidSkirt"), piece_color("black")), salience=1)
    def clothes2855(self):
        self.myclothes = Myclothes(0, "", " ", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "black", "Kandra", 6,
                                   "black", "Coat", 7, "black", "Hat", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0,
                                   "", "", 13, "black", " graduation_gown")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 21) & P(lambda value: value <= 35)), SkinColor(color='hanatawi'),
              Occasion('gradution'), Gender('female'), Person_type('student'), Season("summer"), piece_name("Skirt"),
              piece_type("MidSkirt"), piece_color("black")), salience=1)
    def clothes286(self):
        self.myclothes = Myclothes(0, "", " ", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "black", "Kandra", 6,
                                   "vinous", "Coat", 7, "black", "Hat", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0,
                                   "", "", 13, "black", "graduation_gown")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 21) & P(lambda value: value <= 35)), SkinColor(color='hanatawi'),
              Occasion('gradution'), Gender('female'), Person_type('student'), Season("summer"), piece_name("Skirt"),
              piece_type("MidSkirt"), piece_color("black")), salience=1)
    def clothes2877(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "gray", "Kandra", 6,
                                   "cyan", "Coat", 7, "black", "Hat", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "",
                                   "", 13, "black", "graduation_gown")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 21) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('gradution'), Gender('female'), Person_type('student'), Season("summer"), piece_name("Skirt"),
              piece_type("MidSkirt"), piece_color("black")), salience=1)
    def clothes2888(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "black", "Kandra", 6,
                                   "vinous", "Coat", 7, "black", "Hat", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0,
                                   "", "", 13, "black", "graduation_gown")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 21) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('gradution'), Gender('female'), Person_type('student'), Season("summer"), piece_name("Skirt"),
              piece_type("MidSkirt"), piece_color("white")), salience=1)
    def clothes2899(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "cyan", "Kandra", 6,
                                   "cyan", "Coat", 7, "black", "Hat", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "",
                                   "", 13, "black", "graduation_gown")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 21) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('gradution'), Gender('female'), Person_type('student'), Season("summer"), piece_name("Skirt"),
              piece_type("MidSkirt"), piece_color("white")), salience=1)
    def clothes2900(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "pink", "Shirt", 0, "", "", 5, "cyan", "Kandra", 6, "cyan",
                                   "Coat", 7, "black", "Hat", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 13,
                                   "black", "graduation_gown")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 21) & P(lambda value: value <= 35)), SkinColor(color='dark'),
              Occasion('gradution'), Gender('female'), Person_type('student'), Season("summer"), piece_name("Skirt"),
              piece_type("MidSkirt"), piece_color("black")), salience=1)
    def clothes2911(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "black", "Kandra", 6,
                                   "black", "Coat", 7, "black", "Hat", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0,
                                   "", "", 13, "black", "graduation_gown")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 21) & P(lambda value: value <= 35)), SkinColor(color='hanatawi'),
              Occasion('gradution'), Gender('female'), Person_type('student'), Season("summer"), piece_name("Skirt"),
              piece_type("MidSkirt"), piece_color("black")), salience=1)
    def clothes2922(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "black", "Kandra", 6,
                                   "black", "Coat", 7, "black", "Hat", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0,
                                   "", "", 13, "black", "graduation_gown")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 21) & P(lambda value: value <= 35)), SkinColor(color='hanatawi'),
              Occasion('gradution'), Gender('female'), Person_type('student'), Season("summer"), piece_name("Trousers"),
              piece_type("wide_pants"), piece_color("white")), salience=1)
    def clothes2932(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "white", "Kandra", 6,
                                   "pink", "Coat", 7, "black", "Hat", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "",
                                   "", 13, "black", "graduation_gown")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 21) & P(lambda value: value <= 35)), SkinColor(color='hanatawi'),
              Occasion('gradution'), Gender('female'), Person_type('student'), Season("summer"), piece_name("Trousers"),
              piece_type("wide_pants"), piece_color("black")), salience=1)
    def clothes2942(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "white", "Kandra", 6,
                                   "cyan", "Coat", 7, "black", "Hat", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "",
                                   "", 13, "black", "graduation_gown")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 21) & P(lambda value: value <= 35)), SkinColor(color='dark'),
              Occasion('gradution'), Gender('female'), Person_type('student'), Season("summer"), piece_name("Trousers"),
              piece_type("wide_pants"), piece_color("black")), salience=1)
    def clothes2952(self):
        self.myclothes = Myclothes(0, "", " ", 0, "", "", 3, "vinous", "Shirt", 0, "", "", 5, "black", "Kandra", 6,
                                   "black", "Coat", 7, "black", "Hat", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0,
                                   "", "", 13, "black", "graduation_gown")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 21) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('gradution'), Gender('female'), Person_type('student'), Season("summer"), piece_name("Trousers"),
              piece_type("wide_pants"), piece_color("white")), salience=1)
    def clothes2962(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "pink", "Kandra", 6,
                                   "pink", "Coat", 7, "black", "Hat", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "",
                                   "", 13, "black", "graduation_gown")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 21) & P(lambda value: value <= 35)), SkinColor(color='dark'),
              Occasion('gradution'), Gender('female'), Person_type('student'), Season("summer"), piece_name("Trousers"),
              piece_type("wide_pants"), piece_color("black")), salience=1)
    def clothes2972(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "white", "Kandra", 6,
                                   "pink", "Coat", 7, "black", "Hat", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "",
                                   "", 13, "black", "graduation_gown")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 21) & P(lambda value: value <= 35)), SkinColor(color='hanatawi'),
              Occasion('gradution'), Gender('female'), Person_type('student'), Season("summer"), piece_name("Shirt"),
              piece_type("Shirt"), piece_color("white")), salience=1)
    def clothes2982(self):
        self.myclothes = Myclothes(1, "white", "Trousers", 0, "", "", 3, "", "", 0, "", "", 5, "white", "Kandra", 6,
                                   "pink", "Coat", 7, "black", "Hat", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "",
                                   "", 13, "black", "graduation_gown")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 21) & P(lambda value: value <= 35)), SkinColor(color='hanatawi'),
              Occasion('gradution'), Gender('female'), Person_type('student'), Season("summer"), piece_name("Shirt"),
              piece_type("Shirt"), piece_color("white")), salience=1)
    def clothes2992(self):
        self.myclothes = Myclothes(1, "black", "Trousers", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "white",
                                   "Kandra", 6, "cyan", "Coat", 7, "black", "Hat", 0, "", "", 0, "", "", 0, "", "", 0,
                                   "", "", 0, "", "", 13, "black", "graduation_gown")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 21) & P(lambda value: value <= 35)), SkinColor(color='dark'),
              Occasion('gradution'), Gender('female'), Person_type('student'), Season("summer"), piece_name("Shirt"),
              piece_type("Shirt"), piece_color("white")), salience=1)
    def clothes3002(self):
        self.myclothes = Myclothes(1, "black", "Trousers", 0, "", "", 3, "vinous", "Shirt", 0, "", "", 5, "black",
                                   "Kandra", 6, "black", "Coat", 7, "black", "Hat", 0, "", "", 0, "", "", 0, "", "", 0,
                                   "", "", 0, "", "", 13, "black", "graduation_gown")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 21) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('gradution'), Gender('female'), Person_type('student'), Season("summer"), piece_name("Shirt"),
              piece_type("Shirt"), piece_color("white")), salience=1)
    def clothes3002(self):
        self.myclothes = Myclothes(1, "white", "Trousers", 0, "", "", 0, "", "", 0, "", "", 5, "pink", "Kandra", 6,
                                   "pink", "Coat", 7, "black", "Hat", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "",
                                   "", 13, "black", "graduation_gown")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 21) & P(lambda value: value <= 35)), SkinColor(color='dark'),
              Occasion('gradution'), Gender('female'), Person_type('student'), Season("summer"), piece_name("Shirt"),
              piece_type("Shirt"), piece_color("white")), salience=1)
    def clothes3012(self):
        self.myclothes = Myclothes(1, "black", "Trousers", 0, "", "", 0, "", "", 0, "", "", 5, "white", "Kandra", 6,
                                   "pink", "Coat", 7, "black", "Hat", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "",
                                   "", 13, "black", "graduation_gown")
        self.result.append(self.myclothes)

    #   ///////////

    @Rule(AND(age(value=P(lambda value: value >= 21) & P(lambda value: value <= 35)), SkinColor(color='hanatawi'),
              Occasion('gradution'), Gender('male'), Person_type('student'), Season("summer"), piece_name("Trousers"),
              piece_type("Trousers"), piece_color("black")), salience=2)
    def clothes30550(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "black", "Kandra", 0, "",
                                   "", 7, "black", "Hat", 8, "darkblue", "carafe", 0, "", "", 0, "", "", 0, "", "", 0,
                                   "", "", 13, "black", "graduation_gown")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 21) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('gradution'), Gender('male'), Person_type('student'), Season("summer"), piece_name("Trousers"),
              piece_type("Trousers"), piece_color("gray")), salience=2)
    def clothes30660(self):
        self.myclothes = Myclothes(0, "", " ", 0, "", "", 3, "white", "Shirt", 0, " ", "", 5, "black", "Kandra", 0, "",
                                   "", 7, "black", "Hat", 8, "black", "carafe", 0, "", "", 0, "", "", 0, "", "", 0, "",
                                   "", 13, "black", "graduation_gown")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 21) & P(lambda value: value <= 35)), SkinColor(color='dark'),
              Occasion('gradution'), Gender('male'), Person_type('student'), Season("summer"), piece_name("Trousers"),
              piece_type("Trousers"), piece_color("darkblue")), salience=2)
    def clothes30770(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, " ", "", 5, "brown", "Kandra", 0, "",
                                   "", 7, "black", "Hat", 8, "brown", "carafe", 0, "", "", 0, "", "", 0, "", "", 0, "",
                                   "", 13, "black", "graduation_gown")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 21) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('gradution'), Gender('male'), Person_type('student'), Season("summer"), piece_name("Shirt"),
              piece_type("Shirt"), piece_color("white")), salience=1)
    def clothes3021(self):
        self.myclothes = Myclothes(1, "gray", "Trousers", 0, "", "", 0, "", "", 0, " ", "", 5, "darkblue", "Kandra", 0,
                                   "", "", 7, "black", "Hat", 8, "darkblue", "carafe", 0, "", "", 0, "", "", 0, "", "",
                                   0, "", "", 13, "black", "graduation_gown")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 21) & P(lambda value: value <= 35)), SkinColor(color='hanatawi'),
              Occasion('gradution'), Gender('male'), Person_type('student'), Season("summer"), piece_name("Shirt"),
              piece_type("Shirt"), piece_color("white")), salience=1)
    def clothes3031(self):
        self.myclothes = Myclothes(1, "black", "Trousers", 0, "", "", 0, "", "", 0, " ", "", 5, "black", "Kandra", 0,
                                   "", "", 7, "black", "Hat", 8, "vinous", "carafe", 0, "", "", 0, "", "", 0, "", "", 0,
                                   "", "", 13, "black", "graduation_gown")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 21) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('gradution'), Gender('male'), Person_type('student'), Season("summer"), piece_name("Shirt"),
              piece_type("Shirt"), piece_color("cyan")), salience=1)
    def clothes3041(self):
        self.myclothes = Myclothes(1, "darkblue", "Trousers", 0, "", "", 0, "", "", 0, "", "", 5, "brown", "Kandra",
                                   0, "", "", 7, "black", "Hat", 8, "brown", "carafe", 0, "", "", 0, "", "", 0, "", "",
                                   0, "", "", 13, "black", "graduation_gown")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 21) & P(lambda value: value <= 35)), SkinColor(color='hanatawi'),
              Occasion('gradution'), Gender('male'), Person_type('student'), Season("summer"), piece_name("Trousers"),
              piece_type("Trousers"), piece_color("gray")), salience=1)
    def clothes3051(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "black", "Kandra", 0, "",
                                   "", 7, "black", "Hat", 8, "darkblue", "carafe", 0, "", "", 0, "", "", 0, "", "", 0,
                                   "", "", 13, "black", "graduation_gown")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 21) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('gradution'), Gender('male'), Person_type('student'), Season("summer"), piece_name("Trousers"),
              piece_type("Trousers"), piece_color("darkblue")), salience=1)
    def clothes3061(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "beige", "Shirt", 0, " ", "", 5, "darkblue", "Kandra", 0,
                                   "", "", 7, "black", "Hat", 8, "beige", "carafe", 0, "", "", 0, "", "", 0, "", "", 0,
                                   "", "", 13, "black", "graduation_gown")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 21) & P(lambda value: value <= 35)), SkinColor(color='dark'),
              Occasion('gradution'), Gender('male'), Person_type('student'), Season("summer"), piece_name("Trousers"),
              piece_type("Trousers"), piece_color("black")), salience=1)
    def clothes3071(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, " ", "", 5, "grown", "Kandra", 0, "",
                                   "", 7, "black", "Hat", 8, "black", "carafe", 0, "", "", 0, "", "", 0, "", "", 0, "",
                                   "", 13, "black", "graduation_gown")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 21) & P(lambda value: value <= 35)), SkinColor(color='dark'),
              Occasion('gradution'), Gender('male'), Person_type('student'), Season("summer"), piece_name("Shirt"),
              piece_type("Shirt"), piece_color("white")), salience=1)
    def clothes3081(self):
        self.myclothes = Myclothes(1, "vinous ", "Trousers ", 0, "", "", 0, "", "", 0, " ", "", 5, "black", "Kandra", 0,
                                   "", "", 7, "black", "Hat", 8, "vinous", "carafe", 0, "", "", 0, "", "", 0, "", "", 0,
                                   "", "", 13, "black", "graduation_gown")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='dark'),
              Occasion('wadding'), Gender('male'), Person_type('brother'), Season("summer"), piece_name("Shirt"),
              piece_type("Shirt"), piece_color("white")), salience=1)
    def clothes3091(self):
        self.myclothes = Myclothes(1, "black", "Trousers", 0, "", "", 0, "", "", 0, "", "", 5, "gray", "shose", 0, "",
                                   "", 0, "", "", 8, "gray", "carafe", 0, "", "", 0, "", "", 11, "black", "waistband",
                                   0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='dark'),
              Occasion('wadding'), Gender('male'), Person_type('brother'), Season("summer"), piece_name("Shirt"),
              piece_type("Shirt"), piece_color("white")), salience=1)
    def clothes3101(self):
        self.myclothes = Myclothes(1, "gray", "Trousers", 0, "", "", 0, "", "", 0, " ", "", 5, "brown", "shose", 0,
                                   "", "", 0, "", "", 8, "grown", "carafe", 0, "", "", 0, "", "", 11, "black",
                                   "waistband", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('male'), Person_type('brother'), Season("summer"), piece_name("Shirt"),
              piece_type("Shirt"), piece_color("white")), salience=1)
    def clothes3111(self):
        self.myclothes = Myclothes(1, "darkblue", "Trousers", 0, "", "", 0, "", "", 0, "", "", 5, "black", "shose", 0,
                                   "", "", 0, "", "", 8, "vinous", "carafe", 0, "", "", 0, "", "", 11, "black",
                                   "waistband", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='hanatawi'),
              Occasion('wadding'), Gender('male'), Person_type('brother'), Season("summer"), piece_name("Shirt"),
              piece_type("Shirt"), piece_color("white")), salience=1)
    def clothes3121(self):
        self.myclothes = Myclothes(1, "black", "Trousers", 0, "", "", 0, "", "", 0, "", "", 5, "black", "shose", 0,
                                   "", "", 0, "", "", 8, "black", "carafe", 0, "", "", 0, "", "", 11, "black",
                                   "waistband", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='hanatawi'),
              Occasion('wadding'), Gender('male'), Person_type('friend'), Season("summer"), piece_name("Shirt"),
              piece_type("Shirt"), piece_color("white")), salience=1)
    def clothes3131(self):
        self.myclothes = Myclothes(1, "white", "jeans", 0, "", "", 0, "", "", 0, "", "", 5, "brown", "shose", 6,
                                   "darkblue", "Coat", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 11, "brown",
                                   "waistband", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='hanatawi'),
              Occasion('wadding'), Gender('male'), Person_type('friend'), Season("summer"), piece_name("Shirt"),
              piece_type("Shirt"), piece_color("pink")), salience=1)
    def clothes3141(self):
        self.myclothes = Myclothes(1, "black", "Trousers", 0, "", "", 0, " ", "", 0, " ", "", 5, "black", "shose", 0,
                                   "", "", 0, "", "", 8, "black", "carafe", 0, "", "", 0, "", "", 11, "black",
                                   "waistband", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='dark'),
              Occasion('wadding'), Gender('male'), Person_type('friend'), Season("summer"), piece_name("Shirt"),
              piece_type("Shirt"), piece_color("white")), salience=1)
    def clothes3151(self):
        self.myclothes = Myclothes(1, "gray", "Trousers", 0, "", "", 0, "", "", 0, "", "", 5, "brown", "shose", 0, "",
                                   "", 0, "", "", 8, "darkblue", "carafe", 0, "", "", 0, "", "", 11, "brown",
                                   "waistband", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('male'), Person_type('friend'), Season("summer"), piece_name("Shirt"),
              piece_type("Shirt"), piece_color("cyan")), salience=1)
    def clothes3161(self):
        self.myclothes = Myclothes(1, "darkblue", "Trousers", 0, "", "", 0, "", "", 0, "", "", 5, "brown", "shose",
                                   0, "", "", 0, "", "", 8, "grown", "carafe", 0, "", "", 0, "", "", 11, "brown",
                                   "waistband", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('male'), Person_type('friend'), Season("summer"), piece_name("Shirt"),
              piece_type("Shirt"), piece_color("gray")), salience=1)
    def clothes3171(self):
        self.myclothes = Myclothes(1, "black", "Trousers", 0, "", "", 0, "", "", 0, "", "", 5, "black", "shose", 0,
                                   "", "", 0, "", "", 8, "black", "carafe", 0, "", "", 0, "", "", 11, "black",
                                   "waistband", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='dark'),
              Occasion('wadding'), Gender('male'), Person_type('relatives'), Season("summer"), piece_name("Shirt"),
              piece_type("Shirt"), piece_color("white")), salience=1)
    def clothes3181(self):
        self.myclothes = Myclothes(1, "gray", "Trousers", 0, "", "", 0, "", "", 0, " ", "", 5, "brown", "shose", 0, "",
                                   "", 0, "", "", 8, "black", "carafe", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0,
                                   "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='dark'),
              Occasion('wadding'), Gender('male'), Person_type('relatives'), Season("summer"), piece_name("Shirt"),
              piece_type("Shirt"), piece_color("gray")), salience=1)
    def clothes3191(self):
        self.myclothes = Myclothes(1, "darkblue", "jeans", 0, "", "", 0, "", "", 0, " ", "", 5, "brown", "shose", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 11, "black", "waistband", 0, "",
                                   "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='hanatawi'),
              Occasion('wadding'), Gender('male'), Person_type('relatives'), Season("summer"), piece_name("Shirt"),
              piece_type("Shirt"), piece_color("vinous")), salience=1)
    def clothes3201(self):
        self.myclothes = Myclothes(1, "black", "Trousers", 0, "", "", 0, "", "", 0, " ", "", 5, "black", "shose", 0,
                                   "", "", 0, "", "", 8, "black ", "carafe", 0, "", "", 0, "", "", 11, "black",
                                   "waistband", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    #     /////////////////////////////////////////////////////مناسبة زفاف
    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='dark'),
              Occasion('wadding'), Gender('male'), Person_type('brother'), Season("summer"), piece_name("Trousers"),
              piece_type("Trousers"), piece_color("black")), salience=1)
    def clothes3211(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "gray", "shose", 0, "",
                                   "", 0, "", "", 8, "gray", "carafe", 0, "", "", 0, "", "", 11, "black", "waistband",
                                   0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='dark'),
              Occasion('wadding'), Gender('male'), Person_type('brother'), Season("summer"), piece_name("Trousers"),
              piece_type("Trousers"), piece_color("gray")), salience=1)
    def clothes3221(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "brown", "shose", 0, "",
                                   "", 0, "", "", 8, "grown", "carafe", 0, "", "", 0, "", "", 11, "black", "waistband",
                                   0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('male'), Person_type('brother'), Season("summer"), piece_name("Trousers"),
              piece_type("Trousers"), piece_color("darkblue")), salience=1)
    def clothes3231(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, " ", "", 5, "black", "shose", 0, "",
                                   "", 0, "", "", 8, "vinous", "carafe", 0, "", "", 0, "", "", 11, "black", "waistband",
                                   0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='hanatawi'),
              Occasion('wadding'), Gender('male'), Person_type('brother'), Season("summer"), piece_name("Trousers"),
              piece_type("jeans"), piece_color("black")), salience=1)
    def clothes3241(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "black", "shose", 0, "",
                                   "", 0, "", "", 8, "black", "carafe", 0, "", "", 0, "", "", 11, "black", "waistband",
                                   0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='hanatawi'),
              Occasion('wadding'), Gender('male'), Person_type('friend'), Season("summer"), piece_name("Trousers"),
              piece_type("jeans"), piece_color("white")), salience=1)
    def clothes3251(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, " ", "", 5, "brown", "shose", 6,
                                   "darkblue", "Coat", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 11, "brown",
                                   "waistband", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='hanatawi'),
              Occasion('wadding'), Gender('male'), Person_type('friend'), Season("summer"), piece_name("Trousers"),
              piece_type("Trousers"), piece_color("white")), salience=1)
    def clothes3261(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "pink ", "Shirt", 0, "", "", 5, "black", "shose", 0, "",
                                   "", 0, "", "", 8, "black", "carafe", 0, "", "", 0, "", "", 11, "black", "waistband",
                                   0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='dark'),
              Occasion('wadding'), Gender('male'), Person_type('friend'), Season("summer"), piece_name("Trousers"),
              piece_type("Trousers"), piece_color("gray")), salience=1)
    def clothes3271(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "brown", "shose", 0, "",
                                   "", 0, "", "", 8, "darkblue", "carafe", 0, "", "", 0, "", "", 11, "brown",
                                   "waistband", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('male'), Person_type('friend'), Season("summer"), piece_name("Trousers"),
              piece_type("Trousers"), piece_color("darkblue")), salience=1)
    def clothes3281(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "cyan", "Shirt", 0, " ", "", 5, "brown", "shose", 0, "",
                                   "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 11, "brown", "waistband", 0, "", "",
                                   0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('male'), Person_type('friend'), Season("summer"), piece_name("Trousers"),
              piece_type("jeans"), piece_color("black")), salience=1)
    def clothes3291(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "gray ", "Shirt", 0, "", "", 5, "black", "shose", 0, "",
                                   "", 0, "", "", 8, "black", "carafe", 0, "", "", 0, "", "", 11, "black", "waistband",
                                   0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='dark'),
              Occasion('wadding'), Gender('male'), Person_type('relatives'), Season("summer"), piece_name("Trousers"),
              piece_type("jeans"), piece_color("gray")), salience=1)
    def clothes3301(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "brown", "shose", 0, "",
                                   "", 0, "", "", 8, "black", "carafe", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0,
                                   "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='dark'),
              Occasion('wadding'), Gender('male'), Person_type('relatives'), Season("summer"), piece_name("Trousers"),
              piece_type("jeans"), piece_color("darkblue")), salience=1)
    def clothes3311(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "gray", "Shirt", 0, "", "", 5, "brown", "shose", 0, "",
                                   "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 11, "black", "waistband", 0, "", "",
                                   0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='hanatawi'),
              Occasion('wadding'), Gender('male'), Person_type('relatives'), Season("summer"), piece_name("Trousers"),
              piece_type("Trousers"), piece_color("black")), salience=1)
    def clothes3321(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "vinous", "Shirt", 0, " ", "", 5, "black ", "shose", 0,
                                   "", "", 0, "", "", 8, "black ", "carafe", 0, "", "", 0, "", "", 11, "black",
                                   "waistband", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('work'), Gender('female'), Person_type('officer'), Season("winter"), piece_name("Skirt"),
              piece_type("shortSkirt"), piece_color("black")), salience=1)
    def clothes333(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "black", "Kandra", 6,
                                   "vinous", "Coat", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 11, "black",
                                   "waistband", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='dark'),
              Occasion('work'), Gender('female'), Person_type('officer'), Season("winter"), piece_name("Skirt"),
              piece_type("shortSkirt"), piece_color("gray")), salience=1)
    def clothes3341(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "black", "Kandra", 6,
                                   "gray", "Coat", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 11, "black", "waistband",
                                   0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='white'),
              Occasion('work'), Gender('female'), Person_type('officer'), Season("winter"), piece_name("Trousers"),
              piece_type("Trousers"), piece_color("black")), salience=1)
    def clothes3351(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "black", "Kandra", 6,
                                   "beige", "Coat", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 11, "black",
                                   "waistband", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='white'),
              Occasion('work'), Gender('male'), Person_type('engineer'), Season("summer"), piece_name("Shirt"),
              piece_type("Shirt"), piece_color("white")), salience=1)
    def clothes3361(self):
        self.myclothes = Myclothes(1, "darkblue", "jeans", 0, "", "", 0, "", "", 0, "", "", 5, "white", "shose", 0, "",
                                   "", 7, "yellow", "Hat", 0, "", "", 9, "orange", "Jacket", 0, "", "", 0, "", "", 0,
                                   "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('work'), Gender('male'), Person_type('engineer'), Season("summer"), piece_name("Shirt"),
              piece_type("Shirt"), piece_color("white")), salience=1)
    def clothes3371(self):
        self.myclothes = Myclothes(1, "darkblue", "jeans", 0, "", "", 0, "", "", 0, "", "", 5, "white", "shose", 0, "",
                                   "", 7, "yellow", "Hat", 0, "", "", 9, "orange", "Jacket", 0, "", "", 0, "", "", 0,
                                   "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='dark'),
              Occasion('work'), Gender('male'), Person_type('engineer'), Season("summer"), piece_name("Shirt"),
              piece_type("Shirt"), piece_color("white")), salience=1)
    def clothes3381(self):
        self.myclothes = Myclothes(1, "darkblue", "jeans", 0, "", "", 0, "", "", 0, "", "", 5, "white", "shose", 0, "",
                                   "", 7, "yellow", "Hat", 0, "", "", 9, "orange", "Jacket", 0, "", "", 0, "", "", 0,
                                   "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='white'),
              Occasion('work'), Gender('male'), Person_type('engineer'), Season("winter"), piece_name("Shirt"),
              piece_type("Shirt"), piece_color("white")), salience=1)
    def clothes3391(self):
        self.myclothes = Myclothes(1, "gray", "jeans", 0, "", "", 0, "", "", 0, "", "", 5, "white", "shose", 0,
                                   "black", "Coat", 7, "yellow", "Hat", 0, "", "", 9, "orange", "Jacket", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('work'), Gender('male'), Person_type('engineer'), Season("winter"), piece_name("Shirt"),
              piece_type("Shirt"), piece_color("white")), salience=1)
    def clothes3401(self):
        self.myclothes = Myclothes(1, "gray", "jeans", 0, "", "", 0, "", "", 0, "", "", 5, "white", "shose", 0,
                                   "black", "Coat", 7, "yellow", "Hat", 0, "", "", 9, "orange", "Jacket", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='dark'),
              Occasion('work'), Gender('male'), Person_type('engineer'), Season("winter"), piece_name("Shirt"),
              piece_type("Shirt"), piece_color("white")), salience=1)
    def clothes3411(self):
        self.myclothes = Myclothes(1, "gray", "jeans", 0, "", "", 0, "", "", 0, "", "", 5, "white", "shose", 6, "gray",
                                   "Coat", 7, "yellow", "Hat", 0, "", "", 9, "orange", "Jacket", 0, "", "", 0, "", "",
                                   0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='white'),
              Occasion('work'), Gender('male'), Person_type('engineer'), Season("winter"), piece_name("Shirt"),
              piece_type("Shirt"), piece_color("white")), salience=1)
    def clothes3421(self):
        self.myclothes = Myclothes(1, "darkblue", "jeans", 0, "", "", 0, "", "", 0, "", "", 5, "white", "shose", 6,
                                   "darkblue", "Coat", 7, "yellow", "Hat", 0, "", "", 9, "orange", "Jacket", 0, "", "",
                                   0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='white'),
              Occasion('work'), Gender('male'), Person_type('engineer'), Season("summer"), piece_name("Shirt"),
              piece_type("Shirt"), piece_color("white")), salience=1)
    def clothes34221(self):
        self.myclothes = Myclothes(1, "darkblue", "jeans", 0, "", "", 0, "", "", 0, "", "", 5, "white", "shose", 6,
                                   "darkblue", "Coat", 7, "yellow", "Hat", 0, "", "", 9, "orange", "Jacket", 0, "", "",
                                   0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('work'), Gender('male'), Person_type('engineer'), Season("winter"), piece_name("Shirt"),
              piece_type("Shirt"), piece_color("white")), salience=2)
    def clothes3431(self):
        self.myclothes = Myclothes(1, "darkblue", "jeans", 0, "", "", 0, "", "", 0, "", "", 5, "white", "shose", 6,
                                   "dark", "Coat", 7, "yellow", "Hat", 0, "", "", 9, "orange", "Jacket", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='dark'),
              Occasion('work'), Gender('male'), Person_type('engineer'), Season("winter"), piece_name("Shirt"),
              piece_type("Shirt"), piece_color("white")), salience=1)
    def clothes3441(self):
        self.myclothes = Myclothes(1, "darkblue", "jeans", 0, "", "", 0, "", "", 0, "", "", 5, "white", "shose", 6,
                                   "gray", "Coat", 7, "yellow", "Hat", 0, "", "", 9, "orange", "Jacket", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='white'),
              Occasion('work'), Gender('male'), Person_type('engineer'), Season("winter"), piece_name("Trousers"),
              piece_type("jeans"), piece_color("gray")), salience=1)
    def clothes3451(self):
        self.myclothes = Myclothes(0, "", " ", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "white", "shose", 6,
                                   "darkblue", "Coat", 7, "yellow", "Hat", 0, "", "", 9, "orange", "Jacket", 0, "", "",
                                   0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('work'), Gender('male'), Person_type('engineer'), Season("winter"), piece_name("Trousers"),
              piece_type("jeans"), piece_color("gray")), salience=1)
    def clothes3461(self):
        self.myclothes = Myclothes(0, "", " ", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "white", "shose", 6,
                                   "dark", "Coat", 7, "yellow", "Hat", 0, "", "", 9, "orange", "Jacket", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='dark'),
              Occasion('work'), Gender('male'), Person_type('engineer'), Season("winter"), piece_name("Trousers"),
              piece_type("jeans"), piece_color("gray")), salience=1)
    def clothes3471(self):
        self.myclothes = Myclothes(0, "", " ", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "white", "shose", 6,
                                   "gray", "Coat", 7, "yellow", "Hat", 0, "", "", 9, "orange", "Jacket", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='white'),
              Occasion('work'), Gender('male'), Person_type('engineer'), Season("winter"), piece_name("Trousers"),
              piece_type("jeans"), piece_color("darkblue")), salience=1)
    def clothes3481(self):
        self.myclothes = Myclothes(0, "", " ", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "white", "shose", 6,
                                   "darkblue", "Coat", 7, "yellow", "Hat", 0, "", "", 9, "orange", "Jacket", 0, "", "",
                                   0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('work'), Gender('male'), Person_type('engineer'), Season("winter"), piece_name("Trousers"),
              piece_type("jeans"), piece_color("darkblue")), salience=1)
    def clothes3491(self):
        self.myclothes = Myclothes(0, "", " ", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "white", "shose", 6,
                                   "dark", "Coat", 7, "yellow", "Hat", 0, "", "", 9, "orange", "Jacket", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='dark'),
              Occasion('work'), Gender('male'), Person_type('engineer'), Season("winter"), piece_name("Trousers"),
              piece_type("jeans"), piece_color("darkblue")), salience=1)
    def clothes3501(self):
        self.myclothes = Myclothes(0, "", " ", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "white", "shose", 6,
                                   "gray", "Coat", 7, "yellow", "Hat", 0, "", "", 9, "orange", "Jacket", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='white'),
              Occasion('work'), Gender('male'), Person_type('engineer'), Season("summer"), piece_name("Trousers"),
              piece_type("jeans"), piece_color("gray")), salience=1)
    def clothes3511(self):
        self.myclothes = Myclothes(0, "", " ", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "white", "shose", 0, "",
                                   "", 7, "yellow", "Hat", 0, "", "", 9, "orange", "Jacket", 0, "", "", 0, "", "", 0,
                                   "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('work'), Gender('male'), Person_type('engineer'), Season("summer"), piece_name("Trousers"),
              piece_type("jeans"), piece_color("gray")), salience=1)
    def clothes3521(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "white", "shose", 0, "",
                                   "", 7, "yellow", "Hat", 0, "", "", 9, "orange", "Jacket", 0, "", "", 0, "", "", 0,
                                   "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='white'),
              Occasion('work'), Gender('male'), Person_type('engineer'), Season("summer"), piece_name("Trousers"),
              piece_type("jeans"), piece_color("darkblue")), salience=1)
    def clothes3531(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "white", "shose", 0, "",
                                   "", 7, "yellow", "Hat", 0, "", "", 9, "orange", "Jacket", 0, "", "", 0, "", "", 0,
                                   "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('work'), Gender('male'), Person_type('engineer'), Season("summer"), piece_name("Trousers"),
              piece_type("jeans"), piece_color("darkblue")), salience=1)
    def clothes3541(self):
        self.myclothes = Myclothes(0, "", " ", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "white", "shose", 0, "",
                                   "", 7, "yellow", "Hat", 0, "", "", 9, "orange", "Jacket", 0, "", "", 0, "", "", 0,
                                   "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='dark'),
              Occasion('work'), Gender('male'), Person_type('engineer'), Season("summer"), piece_name("Trousers"),
              piece_type("jeans"), piece_color("darkblue")), salience=1)
    def clothes35551(self):
        self.myclothes = Myclothes(0, "", " ", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "white", "shose", 0, "",
                                   "", 7, "yellow", "Hat", 0, "", "", 9, "orange", "Jacket", 0, "", "", 0, "", "", 0,
                                   "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='white'),
              Occasion('work'), Gender('female'), Person_type('engineer'), Season("summer"), piece_name("Shirt"),
              piece_type("Shirt"), piece_color("white")), salience=1)
    def clothes3561(self):
        self.myclothes = Myclothes(1, "darkblue", "jeans", 0, "", "", 0, "", "", 0, "", "", 5, "white", "shose", 0, "",
                                   "", 7, "yellow", "Hat", 0, "", "", 9, "orange", "Jacket", 0, "", "", 0, "", "", 0,
                                   "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('work'), Gender('female'), Person_type('engineer'), Season("summer"), piece_name("Shirt"),
              piece_type("Shirt"), piece_color("white")), salience=1)
    def clothes3571(self):
        self.myclothes = Myclothes(1, "darkblue", "jeans", 0, "", "", 0, "", "", 0, "", "", 5, "white", "shose", 0, "",
                                   "", 7, "yellow", "Hat", 0, "", "", 9, "orange", "Jacket", 0, "", "", 0, "", "", 0,
                                   "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='dark'),
              Occasion('work'), Gender('female'), Person_type('engineer'), Season("summer"), piece_name("Shirt"),
              piece_type("Shirt"), piece_color("white")), salience=1)
    def clothes35811(self):
        self.myclothes = Myclothes(1, "darkblue", "jeans", 0, "", "", 0, "", "", 0, "", "", 5, "white", "shose", 0, "",
                                   "", 7, "yellow", "Hat", 0, "", "", 9, "orange", "Jacket", 0, "", "", 0, "", "", 0,
                                   "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='white'),
              Occasion('work'), Gender('female'), Person_type('engineer'), Season("winter"), piece_name("Shirt"),
              piece_type("Shirt"), piece_color("white")), salience=1)
    def clothes35911(self):
        self.myclothes = Myclothes(1, "gray", "jeans", 0, "", "", 0, "", "", 0, "", "", 5, "white", "shose", 0,
                                   "black", "Coat", 7, "yellow", "Hat", 0, "", "", 9, "orange", "Jacket", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('work'), Gender('female'), Person_type('engineer'), Season("winter"), piece_name("Shirt"),
              piece_type("Shirt"), piece_color("white")), salience=1)
    def clothes3601(self):
        self.myclothes = Myclothes(1, "gray", "jeans", 0, "", "", 0, "", "", 0, "", "", 5, "white", "shose", 0,
                                   "black", "Coat", 7, "yellow", "Hat", 0, "", "", 9, "orange", "Jacket", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='dark'),
              Occasion('work'), Gender('female'), Person_type('engineer'), Season("winter"), piece_name("Shirt"),
              piece_type("Shirt"), piece_color("white")), salience=1)
    def clothes36111(self):
        self.myclothes = Myclothes(1, "gray", "jeans", 0, "", "", 0, "", "", 0, "", "", 5, "white", "shose", 6, "gray",
                                   "Coat", 7, "yellow", "Hat", 0, "", "", 9, "orange", "Jacket", 0, "", "", 0, "", "",
                                   0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='white'),
              Occasion('work'), Gender('female'), Person_type('engineer'), Season("winter"), piece_name("Shirt"),
              piece_type("Shirt"), piece_color("white")), salience=1)
    def clothes36211(self):
        self.myclothes = Myclothes(1, "darkblue", "jeans", 0, "", "", 0, "", "", 0, "", "", 5, "white", "shose", 6,
                                   "darkblue", "Coat", 7, "yellow", "Hat", 0, "", "", 9, "orange", "Jacket", 0, "", "",
                                   0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('work'), Gender('female'), Person_type('engineer'), Season("winter"), piece_name("Shirt"),
              piece_type("Shirt"), piece_color("white")), salience=1)
    def clothes36311(self):
        self.myclothes = Myclothes(1, "darkblue", "jeans", 0, "", "", 0, "", "", 0, "", "", 5, "white", "shose", 6,
                                   "dark", "Coat", 7, "yellow", "Hat", 0, "", "", 9, "orange", "Jacket", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='dark'),
              Occasion('work'), Gender('female'), Person_type('engineer'), Season("winter"), piece_name("Shirt"),
              piece_type("Shirt"), piece_color("white")), salience=1)
    def clothes36411(self):
        self.myclothes = Myclothes(1, "darkblue", "jeans", 0, "", "", 0, "", "", 0, "", "", 5, "white", "shose", 6,
                                   "gray", "Coat", 7, "yellow", "Hat", 0, "", "", 9, "orange", "Jacket", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='white'),
              Occasion('work'), Gender('female'), Person_type('engineer'), Season("winter"), piece_name("Trousers"),
              piece_type("Trousers"), piece_color("gray")), salience=1)
    def clothes36511(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "white", "shose", 6,
                                   "darkblue", "Coat", 7, "yellow", "Hat", 0, "", "", 9, "orange", "Jacket", 0, "", "",
                                   0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('work'), Gender('female'), Person_type('engineer'), Season("winter"), piece_name("Trousers"),
              piece_type("Trousers"), piece_color("gray")), salience=1)
    def clothes36611(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "white", "shose", 6,
                                   "dark", "Coat", 7, "yellow", "Hat", 0, "", "", 9, "orange", "Jacket", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='dark'),
              Occasion('work'), Gender('female'), Person_type('engineer'), Season("winter"), piece_name("Trousers"),
              piece_type("Trousers"), piece_color("gray")), salience=1)
    def clothes36711(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "white", "shose", 6,
                                   "gray", "Coat", 7, "yellow", "Hat", 0, "", "", 9, "orange", "Jacket", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='white'),
              Occasion('work'), Gender('female'), Person_type('engineer'), Season("winter"), piece_name("Trousers"),
              piece_type("Trousers"), piece_color("darkblue")), salience=1)
    def clothes36811(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "white", "shose", 6,
                                   "darkblue", "Coat", 7, "yellow", "Hat", 0, "", "", 9, "orange", "Jacket", 0, "", "",
                                   0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('work'), Gender('female'), Person_type('engineer'), Season("winter"), piece_name("Trousers"),
              piece_type("Trousers"), piece_color("darkblue")), salience=1)
    def clothes36911(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "white", "shose", 6,
                                   "black", "Coat", 7, "yellow", "Hat", 0, "", "", 9, "orange", "Jacket", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='dark'),
              Occasion('work'), Gender('female'), Person_type('engineer'), Season("winter"), piece_name("Trousers"),
              piece_type("Trousers"), piece_color("darkblue")), salience=1)
    def clothes37011(self):
        self.myclothes = Myclothes(0, "", " ", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "white", "shose", 6,
                                   "gray", "Coat", 7, "yellow", "Hat", 0, "", "", 9, "orange", "Jacket", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='white'),
              Occasion('work'), Gender('female'), Person_type('engineer'), Season("summer"), piece_name("Trousers"),
              piece_type("Trousers"), piece_color("gray")), salience=1)
    def clothes37111(self):
        self.myclothes = Myclothes(0, "", " ", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "white", "shose", 0, "",
                                   "", 7, "yellow", "Hat", 0, "", "", 9, "orange", "Jacket", 0, "", "", 0, "", "", 0,
                                   "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('work'), Gender('female'), Person_type('engineer'), Season("summer"), piece_name("Trousers"),
              piece_type("Trousers"), piece_color("gray")), salience=1)
    def clothes3721(self):
        self.myclothes = Myclothes(0, "", " ", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "white", "shose", 0, "",
                                   "", 7, "yellow", "Hat", 0, "", "", 9, "orange", "Jacket", 0, "", "", 0, "", "", 0,
                                   "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='dark'),
              Occasion('work'), Gender('female'), Person_type('engineer'), Season("summer"), piece_name("Trousers"),
              piece_type("Trousers"), piece_color("gray")), salience=1)
    def clothes37311(self):
        self.myclothes = Myclothes(0, "", " ", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "white", "shose", 0, "",
                                   "", 7, "yellow", "Hat", 0, "", "", 9, "orange", "Jacket", 0, "", "", 0, "", "", 0,
                                   "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='white'),
              Occasion('work'), Gender('female'), Person_type('engineer'), Season("summer"), piece_name("Trousers"),
              piece_type("Trousers"), piece_color("darkblue")), salience=1)
    def clothes37411(self):
        self.myclothes = Myclothes(0, "", " ", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "white", "shose", 0, "",
                                   "", 7, "yellow", "Hat", 0, "", "", 9, "orange", "Jacket", 0, "", "", 0, "", "", 0,
                                   "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('work'), Gender('female'), Person_type('engineer'), Season("summer"), piece_name("Trousers"),
              piece_type("Trousers"), piece_color("darkblue")), salience=1)
    def clothes37511(self):
        self.myclothes = Myclothes(0, "", " ", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "white", "shose", 0, "",
                                   "", 7, "yellow", "Hat", 0, "", "", 9, "orange", "Jacket", 0, "", "", 0, "", "", 0,
                                   "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='dark'),
              Occasion('work'), Gender('female'), Person_type('engineer'), Season("summer"), piece_name("Trousers"),
              piece_type("Trousers"), piece_color("darkblue")), salience=1)
    def clothes37611(self):
        self.myclothes = Myclothes(0, "", " ", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "white", "shose", 0, "",
                                   "", 7, "yellow", "Hat", 0, "", "", 9, "orange", "Jacket", 0, "", "", 0, "", "", 0,
                                   "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('work'), Gender('male'), Person_type('officer'), Season("winter"), piece_name("Trousers"),
              piece_type("Trousers"), piece_color("black")), salience=1)
    def clothes37711(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "brown", "shose", 6,
                                   "black", "Coat", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 11, "brown",
                                   "waistband", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='dark'),
              Occasion('work'), Gender('male'), Person_type('officer'), Season("winter"), piece_name("Trousers"),
              piece_type("Trousers"), piece_color("gray")), salience=1)
    def clothes37811(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "brown", "shose", 6,
                                   "black", "Coat", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 11, "brown",
                                   "waistband", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='white'),
              Occasion('work'), Gender('female'), Person_type('officer'), Season("winter"), piece_name("Trousers"),
              piece_type("Trousers"), piece_color("darkblue")), salience=1)
    def clothes37911(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "beige", "Kandra", 6,
                                   "darkblue", "Coat", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 11, "beige",
                                   "waistband", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='dark'),
              Occasion('work'), Gender('female'), Person_type('business'), Season("winter"), piece_name("skirt"),
              piece_type("shortSkirt"), piece_color("gray")), salience=1)
    def clothes38011(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "black", "Kandra", 6,
                                   "gray", "Coat", 0, "", "", 8, "blue", "carafe", 9, "black", "Jacket", 0, "", "", 0,
                                   "", "", 0, " ", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='white'),
              Occasion('work'), Gender('male'), Person_type('business'), Season("winter"), piece_name("skirt"),
              piece_type("shortSkirt"), piece_color("darkblue")), salience=1)
    def clothes38111(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "brown", "Kandra", 6,
                                   "darkblue", "Coat", 0, "", "", 8, "brown", "darkblue", 9, "black", "Jacket", 0, "",
                                   "", 0, "", "", 0, " ", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('work'), Gender('female'), Person_type('business'), Season("winter"), piece_name("skirt"),
              piece_type("shortSkirt"), piece_color("gray")), salience=1)
    def clothes38211(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "black", "Kandra", 6,
                                   "black", "Coat", 0, "", "", 8, "black", "carafe", 9, "black", "Jacket", 0, "", "", 0,
                                   "", "", 0, " ", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='dark'),
              Occasion('work'), Gender('female'), Person_type('business'), Season("winter"), piece_name("Trousers"),
              piece_type("Trousers"), piece_color("gray")), salience=1)
    def clothes38311(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "black", "Kandra", 6,
                                   "gray", "Coat", 0, "", "", 8, "blue", "carafe", 9, "black", "Jacket", 0, "", "", 0,
                                   "", "", 0, " ", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='white'),
              Occasion('work'), Gender('male'), Person_type('business'), Season("winter"), piece_name("Trousers"),
              piece_type("Trousers"), piece_color("darkblue")), salience=1)
    def clothes38411(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "brown", "Kandra", 6,
                                   "darkblue", "Coat", 0, "", "", 8, "brown", "darkblue", 9, "black", "Jacket", 0, "",
                                   "", 0, "", "", 0, " ", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('work'), Gender('female'), Person_type('business'), Season("winter"), piece_name("Trousers"),
              piece_type("Trousers"), piece_color("gray")), salience=1)
    def clothes38511(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "black", "Kandra", 6,
                                   "black", "Coat", 0, "", "", 8, "black", "carafe", 9, "black", "Jacket", 0, "", "", 0,
                                   "", "", 0, " ", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='white'),
              Occasion('work'), Gender('male'), Person_type('business '), Season("winter"), piece_name("Trousers"),
              piece_type("Trousers"), piece_color("black")), salience=1)
    def clothes38611(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "black", "Kandra", 6,
                                   "gray", "Coat", 0, "", "", 8, "vinous", "carafe", 9, "black", "Jacket", 0, "", "", 0,
                                   "", "", 0, " ", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='dark'),
              Occasion('work'), Gender('female'), Person_type('business'), Season("summer"), piece_name("Trousers"),
              piece_type("Trousers"), piece_color("gray")), salience=1)
    def clothes38711(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "black", "Kandra", 6,
                                   "gray", "Coat", 0, "", "", 8, "blue", "carafe", 0, "", "", 0, "", "", 0, "", "", 0,
                                   " ", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='white'),
              Occasion('work'), Gender('male'), Person_type('business'), Season("summer"), piece_name("Trousers"),
              piece_type("Trousers"), piece_color("darkblue")), salience=1)
    def clothes38811(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "brown", "Kandra", 6,
                                   "darkblue", "Coat", 0, "", "", 8, "brown", "darkblue", 0, "", "", 0, "", "", 0, "",
                                   "", 0, " ", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('work'), Gender('female'), Person_type('business'), Season("summer"), piece_name("Trousers"),
              piece_type("Trousers"), piece_color("gray")), salience=1)
    def clothes38911(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "black", "Kandra", 6,
                                   "black", "Coat", 0, "", "", 8, "black", "carafe", 0, "", "", 0, "", "", 0, "", "", 0,
                                   " ", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='white'),
              Occasion('work'), Gender('male'), Person_type('business'), Season("summer"), piece_name("Trousers"),
              piece_type("Trousers"), piece_color("black")), salience=1)
    def clothes39011(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "black", "Kandra", 6,
                                   "gray", "Coat", 0, "", "", 8, "vinous", "carafe", 0, "", "", 0, "", "", 0, "", "", 0,
                                   " ", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('work'), Gender('female'), Person_type('business'), Season("summer"), piece_name("Shirt"),
              piece_type("Shirt"), piece_color("white")), salience=1)
    def clothes39910(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 4, "darkblue", "skirt", 5, "beige", "Kandra", 6,
                                   "beige", "Coat", 0, "", "", 8, "beige", "carafe", 0, "", "", 0, "", "", 0, "", "", 0,
                                   "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('work'), Gender('female'), Person_type('business'), Season("summer"), piece_name("Shirt"),
              piece_type("Shirt"), piece_color("white")), salience=1)
    def clothes3911(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 4, "black", "skirt", 5, "black", "Kandra", 6,
                                   "black", "Coat", 0, "", "", 8, "vinous", "carafe", 0, "", "", 0, "", "", 0, "", "",
                                   0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='dark'),
              Occasion('work'), Gender('female'), Person_type('business'), Season("summer"), piece_name("Shirt"),
              piece_type("Shirt"), piece_color("white")), salience=1)
    def clothes3921(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 4, "gray", "skirt", 5, "black", "Kandra", 6, "gray",
                                   "Coat", 0, "", "", 8, "black", "carafe", 0, "", "", 0, "", "", 0, "", "", 0, " ", "",
                                   0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='white'),
              Occasion('work'), Gender('female'), Person_type('business'), Season("winter"), piece_name("Shirt"),
              piece_type("Shirt"), piece_color("white")), salience=1)
    def clothes3931(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 4, "darkblue", "skirt", 5, "darkblue", "Kandra", 6,
                                   "darkblue", "Coat", 0, "", "", 8, "darkblue", "carafe", 9, "darkblue", "Jacket", 0,
                                   "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('work'), Gender('female'), Person_type('business'), Season("winter"), piece_name("Shirt"),
              piece_type("Shirt"), piece_color("white")), salience=1)
    def clothes3941(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 4, "black", "skirt", 5, "black", "Kandra", 6,
                                   "black", "Coat", 0, "", "", 8, "vinous", "carafe", 9, "black", "Jacket", 0, "", "",
                                   0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='dark'),
              Occasion('work'), Gender('female'), Person_type('business'), Season("winter"), piece_name("Shirt"),
              piece_type("Shirt"), piece_color("white")), salience=1)
    def clothes3951(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 4, "gray", "skirt", 5, "black", "Kandra", 6, "gray",
                                   "Coat", 0, "", "", 8, "black", "carafe", 9, "black", "Jacket", 0, "", "", 0, "", "",
                                   0, " ", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='white'),
              Occasion('work'), Gender('male'), Person_type('business'), Season("summer"), piece_name("Trousers"),
              piece_type("Trousers"), piece_color("darkblue")), salience=1)
    def clothes3961(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "brown", "Kandra", 6,
                                   "darkblue", "Coat", 0, "", "", 8, "darkblue", "carafe", 0, "", "", 0, "", "", 0, "",
                                   "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('work'), Gender('male'), Person_type('business'), Season("summer"), piece_name("Trousers"),
              piece_type("Trousers"), piece_color("black")), salience=1)
    def clothes3971(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "black", "Kandra", 6,
                                   "black", "Coat", 0, "", "", 8, "vinous", "carafe", 0, "", "", 0, "", "", 0, "", "",
                                   0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='dark'),
              Occasion('work'), Gender('male'), Person_type('business'), Season("summer"), piece_name("Trousers"),
              piece_type("Trousers"), piece_color("gray")), salience=1)
    def clothes3981(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "black", "Kandra", 6,
                                   "gray", "Coat", 0, "", "", 8, "black", "carafe", 0, "", "", 0, "", "", 0, "", "", 0,
                                   "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='white'),
              Occasion('work'), Gender('male'), Person_type('business'), Season("summer"), piece_name("Shirt"),
              piece_type("Shirt"), piece_color("white")), salience=1)
    def clothes3991(self):
        self.myclothes = Myclothes(1, "darkblue", "Trousers", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "brown",
                                   "Kandra", 6, "darkblue", "Coat", 0, "", "", 8, "darkblue", "carafe", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('work'), Gender('male'), Person_type('business'), Season("summer"), piece_name("Shirt"),
              piece_type("Shirt"), piece_color("white")), salience=1)
    def clothes3401(self):
        self.myclothes = Myclothes(1, "black", "Trousers", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "black",
                                   "Kandra", 6, "black", "Coat", 0, "", "", 8, "vinous", "carafe", 0, "", "", 0, "", "",
                                   0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='dark'),
              Occasion('work'), Gender('male'), Person_type('business'), Season("summer"), piece_name("Shirt"),
              piece_type("Shirt"), piece_color("white")), salience=1)
    def clothes3411(self):
        self.myclothes = Myclothes(1, "gray", "Trousers", 0, "", "", 0, "", "", 0, "", "", 5, "black", "Kandra", 6,
                                   "gray", "Coat", 0, "", "", 8, "black", "carafe", 0, "", "", 0, "", "", 0, "", "", 0,
                                   "", "", 0, "", "")
        self.result.append(self.myclothes)

    #         //////////

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='white'),
              Occasion('work'), Gender('female'), Person_type('business'), Season("summer"), piece_name("Shirt"),
              piece_type("Shirt"), piece_color("white")), salience=1)
    def clothes3421(self):
        self.myclothes = Myclothes(1, "darkblue", "Trousers", 0, "", "", 0, "", "", 0, "", "", 5, "darkblue", "Kandra",
                                   6, "darkblue", "Coat", 0, "", "", 8, "darkblue", "carafe", 0, "", "", 0, "", "", 0,
                                   "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('work'), Gender('female'), Person_type('business'), Season("summer"), piece_name("Shirt"),
              piece_type("Shirt"), piece_color("white")), salience=1)
    def clothes3431(self):
        self.myclothes = Myclothes(1, "black", "Trousers", 0, "", "", 0, "", "", 0, "", "", 5, "black", "Kandra", 6,
                                   "black", "Coat", 0, "", "", 8, "vinous", "carafe", 0, "", "", 0, "", "", 0, "", "",
                                   0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='dark'),
              Occasion('work'), Gender('female'), Person_type('business'), Season("summer"), piece_name("Shirt"),
              piece_type("Shirt"), piece_color("white")), salience=1)
    def clothes3441(self):
        self.myclothes = Myclothes(1, "gray", "Trousers", 0, "", "", 0, "", "", 0, "", "", 5, "black", "Kandra", 6,
                                   "gray", "Coat", 0, "", "", 8, "black", "carafe", 0, "", "", 0, "", "", 0, "", "", 0,
                                   " ", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='white'),
              Occasion('work'), Gender('female'), Person_type('business'), Season("summer"), piece_name("Trousers"),
              piece_type("Trousers"), piece_color("darkblue")), salience=1)
    def clothes3451(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 0, "", "", 5, "darkblue", "Kandra", 6, "darkblue",
                                   "Coat", 0, "", "", 8, "darkblue", "carafe", 0, "", "", 0, "", "", 0, "", "", 0, "",
                                   "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('work'), Gender('female'), Person_type('business'), Season("summer"), piece_name("Trousers"),
              piece_type("Trousers"), piece_color("black")), salience=1)
    def clothes3461(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 0, "", "", 5, "black", "Kandra", 6, "black", "Coat",
                                   0, "", "", 8, "vinous", "carafe", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "",
                                   "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='dark'),
              Occasion('work'), Gender('female'), Person_type('business'), Season("summer"), piece_name("Trousers"),
              piece_type("Trousers"), piece_color("gray")), salience=1)
    def clothes3471(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 0, "", "", 5, "black", "Kandra", 6, "gray", "Coat",
                                   0, "", "", 8, "black", "carafe", 0, "", "", 0, "", "", 0, "", "", 0, " ", "", 0, "",
                                   "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='white'),
              Occasion('work'), Gender('female'), Person_type('business'), Season("winter"), piece_name("Jacket"),
              piece_type("Jacket"), piece_color("darkblue")), salience=1)
    def clothes3481(self):
        self.myclothes = Myclothes(1, "darkblue", "Trousers", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "darkblue",
                                   "Kandra", 6, "darkblue", "Coat", 0, "", "", 8, "darkblue", "carafe", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('work'), Gender('female'), Person_type('business'), Season("winter"), piece_name("Jacket"),
              piece_type("Jacket"), piece_color("black")), salience=1)
    def clothes3491(self):
        self.myclothes = Myclothes(1, "black", "Trousers", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "black",
                                   "Kandra", 6, "black", "Coat", 0, "", "", 8, "vinous", "carafe", 0, "", "", 0, "", "",
                                   0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='dark'),
              Occasion('work'), Gender('female'), Person_type('business'), Season("winter"), piece_name("Jacket"),
              piece_type("Jacket"), piece_color("black")), salience=1)
    def clothes3501(self):
        self.myclothes = Myclothes(1, "gray", "Trousers", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "black",
                                   "Kandra", 6, "gray", "Coat", 0, "", "", 8, "black", "carafe", 0, "", "", 0, "", "",
                                   0, "", "", 0, " ", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='white'),
              Occasion('work'), Gender('female'), Person_type('business'), Season("winter"), piece_name("Trousers"),
              piece_type("Trousers"), piece_color("darkblue")), salience=1)
    def clothes3511(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "darkblue", "Kandra", 6,
                                   "darkblue", "Coat", 0, "", "", 8, "darkblue", "carafe", 9, "darkblue", "Jacket", 0,
                                   "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('work'), Gender('female'), Person_type('business'), Season("winter"), piece_name("Trousers"),
              piece_type("Trousers"), piece_color("black")), salience=1)
    def clothes3521(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "black", "Kandra", 6,
                                   "black", "Coat", 0, "", "", 8, "vinous", "carafe", 9, "black", "Jacket", 0, "", "",
                                   0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='dark'),
              Occasion('work'), Gender('female'), Person_type('business'), Season("winter"), piece_name("Trousers"),
              piece_type("Trousers"), piece_color("gray")), salience=1)
    def clothes35311(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "black", "Kandra", 6,
                                   "gray", "Coat", 0, "", "", 8, "black", "carafe", 9, "black", "Jacket", 0, "", "", 0,
                                   "", "", 0, " ", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='white'),
              Occasion('work'), Gender('male'), Person_type('officer'), Season("summer"), piece_name("Trousers"),
              piece_type("Trousers"), piece_color("darkblue")), salience=1)
    def clothes35411(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "brown", "shose", 0, "", "",
                                   0, "", "", 0, "", "", 0, "", "", 0, "", "", 11, "brown", "waistband", 0, "", "", 0,
                                   "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='white'),
              Occasion('work'), Gender('male'), Person_type('officer'), Season("summer"), piece_name("Shirt"),
              piece_type("Shirt"), piece_color("white")), salience=1)
    def clothes3515(self):
        self.myclothes = Myclothes(1, "darkblue", "Trousers", 0, "", "", 0, "", "", 0, "", "", 5, "brown", "shose", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 11, "brown", "waistband", 0, "",
                                   "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='dark'),
              Occasion('work'), Gender('male'), Person_type('officer'), Season("summer"), piece_name("Shirt"),
              piece_type("Shirt"), piece_color("white")), salience=1)
    def clothes35611(self):
        self.myclothes = Myclothes(1, "gray", "Trousers", 0, "", "", 0, "", "", 0, "", "", 5, "black", "shose", 0, "",
                                   "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 11, "black", "waistband", 0, "", "",
                                   0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('work'), Gender('male'), Person_type('officer'), Season("summer"), piece_name("Shirt"),
              piece_type("Shirt"), piece_color("white")), salience=1)
    def clothes35711(self):
        self.myclothes = Myclothes(1, "black", "Trousers", 0, "", "", 0, "", "", 0, "", "", 5, "black", "shose", 0, "",
                                   "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 11, "gold", "waistband", 0, "", "",
                                   0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('work'), Gender('male'), Person_type('officer'), Season("summer"), piece_name("Trousers"),
              piece_type("Trousers"), piece_color("black")), salience=1)
    def clothes358111(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "black", "shose", 0, "", "",
                                   0, "", "", 0, "", "", 0, "", "", 0, "", "", 11, "black", "waistband", 0, "", "", 0,
                                   "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='dark'),
              Occasion('work'), Gender('male'), Person_type('officer'), Season("summer"), piece_name("Trousers"),
              piece_type("Trousers"), piece_color("gray")), salience=1)
    def clothes35912(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "black", "shose", 0, "", "",
                                   0, "", "", 0, "", "", 0, "", "", 0, "", "", 11, "black", "waistband", 0, "", "", 0,
                                   "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='white'),
              Occasion('work'), Gender('male'), Person_type('officer'), Season("summer"), piece_name("Trousers"),
              piece_type("Trousers"), piece_color("black")), salience=1)
    def clothes360112(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "brown", "shose", 0, "", "",
                                   0, "", "", 0, "", "", 0, "", "", 0, "", "", 11, "brown", "waistband", 0, "", "", 0,
                                   "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('work'), Gender('male'), Person_type('officer'), Season("summer"), piece_name("Trousers"),
              piece_type("Trousers"), piece_color("gray")), salience=1)
    def clothes36112(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "brown", "shose", 0, "", "",
                                   0, "", "", 0, "", "", 0, "", "", 0, "", "", 11, "black", "waistband", 0, "", "", 0,
                                   "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='dark'),
              Occasion('work'), Gender('male'), Person_type('officer'), Season("summer"), piece_name("Trousers"),
              piece_type("Trousers"), piece_color("darkblue")), salience=1)
    def clothes36212(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "brown", "shose", 0, "", "",
                                   0, "", "", 0, "", "", 0, "", "", 0, "", "", 11, "brown", "waistband", 0, "", "", 0,
                                   "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='white'),
              Occasion('work'), Gender('male'), Person_type('officer'), Season("summer"), piece_name("Trousers"),
              piece_type("Trousers"), piece_color("gray")), salience=1)
    def clothes36312(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "brown", "shose", 0, "", "",
                                   0, "", "", 0, "", "", 0, "", "", 0, "", "", 11, "brown", "waistband", 0, "", "", 0,
                                   "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('work'), Gender('male'), Person_type('officer'), Season("summer"), piece_name("Trousers"),
              piece_type("Trousers"), piece_color("darkblue")), salience=1)
    def clothes36412(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "darkblue", "shose", 0, "", "",
                                   0, "", "", 0, "", "", 0, "", "", 0, "", "", 11, "darkblue", "waistband", 0, "", "", 0,
                                   "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='dark'),
              Occasion('work'), Gender('male'), Person_type('officer'), Season("summer"), piece_name("Trousers"),
              piece_type("Trousers"), piece_color("black")), salience=1)
    def clothes36512(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "white", "shose", 0, "", "",
                                   0, "", "", 0, "", "", 0, "", "", 0, "", "", 11, "vions", "waistband", 0, "", "", 0,
                                   "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='white'),
              Occasion('work'), Gender('female'), Person_type('officer'), Season("summer"), piece_name("Trousers"),
              piece_type("Trousers"), piece_color("darkblue")), salience=1)
    def clothes36612(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "beige ", "Kandra", 0, "",
                                   "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 11, "beige", "waistband", 0, "", "",
                                   0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='white'),
              Occasion('work'), Gender('female'), Person_type('officer'), Season("summer"), piece_name("Shirt"),
              piece_type("Shirt"), piece_color("white")), salience=1)
    def clothes36712(self):
        self.myclothes = Myclothes(1, "darkblue", "Trousers", 0, "", "", 0, "", "", 0, "", "", 5, "beige ", "Kandra", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 11, "beige", "waistband", 0, "",
                                   "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='dark'),
              Occasion('work'), Gender('female'), Person_type('officer'), Season("summer"), piece_name("Shirt"),
              piece_type("Shirt"), piece_color("white")), salience=1)
    def clothes36812(self):
        self.myclothes = Myclothes(1, "gray", "Trousers", 0, "", "", 0, "", "", 0, "", "", 5, "beige", "Kandra", 0, "",
                                   "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 11, "beige", "waistband", 0, "", "",
                                   0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('work'), Gender('female'), Person_type('officer'), Season("summer"), piece_name("Shirt"),
              piece_type("Shirt"), piece_color("white")), salience=1)
    def clothes36912(self):
        self.myclothes = Myclothes(1, "black", "Trousers", 0, "", "", 0, "", "", 0, "", "", 5, "beige", "Kandra", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 11, "beige", "waistband", 0, "",
                                   "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('work'), Gender('female'), Person_type('officer'), Season("summer"), piece_name("Trousers"),
              piece_type("Trousers"), piece_color("black")), salience=1)
    def clothes37012(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "vinous", "Kandra", 0, "",
                                   "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 11, "vinous", "waistband", 0, "", "",
                                   0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='dark'),
              Occasion('work'), Gender('female'), Person_type('officer'), Season("summer"), piece_name("Trousers"),
              piece_type("Trousers"), piece_color("gray")), salience=1)
    def clothes37112(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "black", "Kandra", 0, "",
                                   "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 11, "black", "waistband",
                                   0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='white'),
              Occasion('work'), Gender('female'), Person_type('officer'), Season("summer"), piece_name("Trousers"),
              piece_type("Trousers"), piece_color("black")), salience=1)
    def clothes37212(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "beige", "Kandra", 0, "",
                                   "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 11, "beige", "waistband", 0, "", "",
                                   0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('work'), Gender('female'), Person_type('officer'), Season("summer"), piece_name("Trousers"),
              piece_type("Trousers"), piece_color("gray")), salience=1)
    def clothes37312(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "vinous", "Kandra", 0, "",
                                   "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 11, "vinous", "waistband", 0, "", "",
                                   0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='dark'),
              Occasion('work'), Gender('female'), Person_type('officer'), Season("summer"), piece_name("Trousers"),
              piece_type("Trousers"), piece_color("black")), salience=1)
    def clothes37412(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "black", "Kandra", 0, "",
                                   "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 11, "black", "waistband",
                                   0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='white'),
              Occasion('work'), Gender('female'), Person_type('officer'), Season("summer"), piece_name("Trousers"),
              piece_type("Trousers"), piece_color("darkblue")), salience=1)
    def clothes37512(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "darkblue", "Kandra", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "",
                                   )
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('work'), Gender('female'), Person_type('officer'), Season("winter"), piece_name("Skirt"),
              piece_type("shortSkirt"), piece_color("black")), salience=1)
    def clothes37612(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "black", "Kandra", 0, "",
                                   "", 0, "", "", 0, "", "", 9, "black", "Jacket", 0, "", "", 0, "", "", 0, "", "", 0,
                                   "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('work'), Gender('female'), Person_type('officer'), Season("winter"), piece_name("Shirt"),
              piece_type("Shirt"), piece_color("white")), salience=1)
    def clothes3771(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 4, "black", "Skirt", 5, "black", "Kandra", 0, "",
                                   "", 0, "", "", 0, "", "", 9, "black", "Jacket", 0, "", "", 0, "", "", 0, "", "", 0,
                                   "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('work'), Gender('female'), Person_type('officer'), Season("winter"), piece_name("Shirt"),
              piece_type("Shirt"), piece_color("white")), salience=1)
    def clothes37812(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 4, "black", "Skirt", 5, "black", "Kandra", 0, "",
                                   "", 0, "", "", 0, "", "", 9, "black", "Jacket", 0, "", "", 0, "", "", 0, "", "", 0,
                                   "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('work'), Gender('female'), Person_type('officer'), Season("winter"), piece_name("Jacket"),
              piece_type("Jacket"), piece_color("black")), salience=1)
    def clothes37912(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 4, "black", "Skirt", 5, "black",
                                   "Kandra", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "",
                                   "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='dark'),
              Occasion('work'), Gender('female'), Person_type('officer'), Season("winter"), piece_name("Jacket"),
              piece_type("Jacket"), piece_color("black")), salience=1)
    def clothes38012(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 4, "black", "Skirt", 5, "black",
                                   "Kandra", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "",
                                   "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='white'),
              Occasion('work'), Gender('female'), Person_type('officer'), Season("winter"), piece_name("Jacket"),
              piece_type("Jacket"), piece_color("darkblue")), salience=1)
    def clothes38112(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 4, "gray", "Skirt", 5, "gray", "Kandra",
                                   0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "",
                                   "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='white'),
              Occasion('work'), Gender('female'), Person_type('officer'), Season("winter"), piece_name("Jacket"),
              piece_type("Jacket"), piece_color("gray")), salience=1)
    def clothes38212(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 4, "black", "Skirt", 5, "black",
                                   "Kandra", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "",
                                   "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='dark'),
              Occasion('work'), Gender('female'), Person_type('officer'), Season("summer"), piece_name("Skirt"),
              piece_type("shortSkirt"), piece_color("darkblue")), salience=1)
    def clothes38312(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "black", "Kandra", 0, "",
                                   "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='dark'),
              Occasion('work'), Gender('female'), Person_type('officer'), Season("winter"), piece_name("Skirt"),
              piece_type("shortSkirt"), piece_color("darkblue")), salience=1)
    def clothes38412(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "black", "Kandra", 0, "",
                                   "", 0, "", "", 0, "", "", 9, "black", "Jacket", 0, "", "", 0, "", "", 0, "", "", 0,
                                   "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('work'), Gender('female'), Person_type('officer'), Season("winter"), piece_name("Skirt"),
              piece_type("shortSkirt"), piece_color("black")), salience=1)
    def clothes38512(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "black", "Kandra", 0, "",
                                   "", 0, "", "", 0, "", "", 9, "black", "Jacket", 0, "", "", 0, "", "", 0, "", "", 0,
                                   "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='dark'),
              Occasion('work'), Gender('female'), Person_type('officer'), Season("summer"), piece_name("Skirt"),
              piece_type("shortSkirt"), piece_color("gray")), salience=1)
    def clothes38612(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "black", "Kandra", 0, "",
                                   "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='dark'),
              Occasion('work'), Gender('female'), Person_type('officer'), Season("winter"), piece_name("Skirt"),
              piece_type("shortSkirt"), piece_color("gray")), salience=1)
    def clothes38712(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "black", "Kandra", 0, "",
                                   "", 0, "", "", 0, "", "", 9, "black", "Jacket", 0, "", "", 0, "", "", 0, "", "", 0,
                                   "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('work'), Gender('female'), Person_type('officer'), Season("winter"), piece_name("Skirt"),
              piece_type("shortSkirt"), piece_color("darkblue")), salience=1)
    def clothes38812(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "black", "Kandra", 0, "",
                                   "", 0, "", "", 0, "", "", 9, "black", "Jacket", 0, "", "", 0, "", "", 0, "", "", 0,
                                   "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='dark'),
              Occasion('work'), Gender('female'), Person_type('officer'), Season("summer"), piece_name("Skirt"),
              piece_type("shortSkirt"), piece_color("black")), salience=1)
    def clothes38912(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "black", "Kandra", 0, "",
                                   "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='dark'),
              Occasion('work'), Gender('female'), Person_type('officer'), Season("winter"), piece_name("Skirt"),
              piece_type("shortSkirt"), piece_color("black")), salience=1)
    def clothes39012(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "black", "Kandra", 0, "",
                                   "", 0, "", "", 0, "", "", 9, "black", "Jacket", 0, "", "", 0, "", "", 0, "", "", 0,
                                   "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='hanatawi'),
              Occasion('wadding'), Gender('male'), Person_type('relatives'), Season("summer"), piece_name("T_Shirt"),
              piece_type("T_Shirt"), piece_color("brown")), salience=1)
    def clothes39112(self):
        self.myclothes = Myclothes(1, "black", "jeans", 0, "", "", 0, "", "", 0, " ", "", 5, "black", "shose", 0, "",
                                   "", 0, "", "", 8, "black", "carafe", 0, "", "", 0, "", "", 11, "black", "waistband",
                                   0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='dark'),
              Occasion('wadding'), Gender('male'), Person_type('relatives'), Season("summer"), piece_name("T_Shirt"),
              piece_type("T_Shirt"), piece_color("beige")), salience=1)
    def clothes392122(self):
        self.myclothes = Myclothes(1, " black", "Trousers", 0, "", "", 0, "", "", 0, " ", "", 5, "black", "shose", 0,
                                   "", "", 0, "", "", 8, "black", "carafe", 0, "", "", 0, "", "", 11, "black",
                                   "waistband", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('male'), Person_type('relatives'), Season("summer"), piece_name("Shirt"),
              piece_type("Shirt"), piece_color("cyan")), salience=1)
    def clothes3931(self):
        self.myclothes = Myclothes(1, " darkblue", "jeans ", 0, "", "", 0, "", "", 0, " ", "", 5, "black", "shose", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 11, "black", "waistband", 0, "",
                                   "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('male'), Person_type('relatives'), Season("summer"), piece_name("Shirt"),
              piece_type("Shirt"), piece_color("oil")), salience=1)
    def clothes39412(self):
        self.myclothes = Myclothes(1, "black", "Trousers", 0, "", "", 0, " ", "", 0, " ", "", 5, "black", "shose", 0,
                                   "", "", 0, "", "", 8, "black ", "carafe", 0, "", "", 0, "", "", 11, "black",
                                   "waistband", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('male'), Person_type('relatives'), Season("summer"), piece_name("T_Shirt"),
              piece_type("T_Shirt"), piece_color("beige")), salience=1)
    def clothes39512(self):
        self.myclothes = Myclothes(1, "darkblue", "Trousers", 0, "", "", 0, "", "", 0, " ", "", 5, "brown", "shose",
                                   0, "", "", 0, "", "", 8, "black", "carafe", 0, "", "", 0, "", "", 11, "brown",
                                   "waistband", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='hanatawi'),
              Occasion('wadding'), Gender('male'), Person_type('relatives'), Season("summer"), piece_name("Trousers"),
              piece_type("jeans"), piece_color("black")), salience=1)
    def clothes39612(self):
        self.myclothes = Myclothes(0, "", "", 2, "brown", "T_Shirt", 0, "", "", 0, " ", "", 5, "black", "shose", 0,
                                   "", "", 0, "", "", 8, "black", "carafe", 0, "", "", 0, "", "", 11, "black",
                                   "waistband", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='dark'),
              Occasion('wadding'), Gender('male'), Person_type('relatives'), Season("summer"), piece_name("Trousers"),
              piece_type("jeans"), piece_color("darkblue")), salience=1)
    def clothes39712(self):
        self.myclothes = Myclothes(0, "  ", " ", 2, "beige", "T_Shirt", 0, "", "", 0, " ", "", 5, "brown", "shose", 0,
                                   "", "", 0, "", "", 8, "beige ", "carafe", 0, "", "", 0, "", "", 11, "brown",
                                   "waistband", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('male'), Person_type('relatives'), Season("summer"), piece_name("Trousers"),
              piece_type("jeans"), piece_color("darkblue")), salience=1)
    def clothes39812(self):
        self.myclothes = Myclothes(0, "", " ", 0, "", "", 3, "cyan", "Shirt", 0, " ", "", 5, "black", "shose", 0, "",
                                   "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 11, "black", "waistband", 0, "", "",
                                   0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('male'), Person_type('relatives'), Season("summer"), piece_name("Trousers"),
              piece_type("jeans"), piece_color("black")), salience=1)
    def clothes39912(self):
        self.myclothes = Myclothes(0, " ", " ", 0, "", "", 3, "oil", "Shirt", 0, " ", "", 5, "black", "shose", 0, "",
                                   "", 0, "", "", 8, "black", "carafe", 0, "", "", 0, "", "", 11, "black", "waistband",
                                   0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('male'), Person_type('relatives'), Season("summer"), piece_name("Trousers"),
              piece_type("jeans"), piece_color("darkblue")), salience=1)
    def clothes40012(self):
        self.myclothes = Myclothes(1, " ", "", 2, "beige ", "T_Shirt", 0, "", "", 0, " ", "", 5, "brown", "shose", 0,
                                   "", "", 0, "", "", 8, "darkblue", "carafe", 0, "", "", 0, "", "", 11, "brown",
                                   "waistband", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('female'), Person_type('relatives'), Season("summer"), piece_name("dress"),
              piece_type("Midriff"), piece_color("black")), salience=1)
    def clothes40112(self):
        self.myclothes = Myclothes(0, " ", "", 0, "", "", 0, " ", "", 0, " ", "", 5, "black", "Kandra", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('female'), Person_type('relatives'), Season("summer"), piece_name("dress"),
              piece_type("Midriff"), piece_color("vinous")), salience=1)
    def clothes40212(self):
        self.myclothes = Myclothes(0, " ", "", 0, "", "", 0, " ", "", 0, " ", "", 5, "black", "Kandra", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "", 0, " ", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('female'), Person_type('relatives'), Season("summer"), piece_name("dress"),
              piece_type("MidiDress"), piece_color("pink")), salience=1)
    def clothes40312(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, " ", "", 0, " ", "", 5, "black", "Kandra", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('female'), Person_type('relatives'), Season("summer"), piece_name("T_Shirt"),
              piece_type("T_Shirt"), piece_color("pink")), salience=1)
    def clothes40412(self):
        self.myclothes = Myclothes(1, "cyan", "jeans", 0, "", "", 0, "", "", 0, "", "", 5, "white", "Kandra", 0, "",
                                   "", 0, "", "", 0, " ", "", 0, "", "", 0, "", "", 11, "black", "waistband", 0, "", "",
                                   0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('female'), Person_type('relatives'), Season("summer"), piece_name("T_Shirt"),
              piece_type("T_Shirt"), piece_color("yellow")), salience=1)
    def clothes40512(self):
        self.myclothes = Myclothes(1, "black", "jeans", 0, "", "", 0, "", "", 0, " ", "", 5, "black", "Kandra", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 11, "black", "waistband", 0, "",
                                   "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='dark'),
              Occasion('wadding'), Gender('female'), Person_type('relatives'), Season("summer"), piece_name("dress"),
              piece_type("jeans"), piece_color("blue")), salience=1)
    def clothes40612(self):
        self.myclothes = Myclothes(0, " ", "", 0, "", "", 0, " ", "", 0, " ", "", 5, "silver", "Kandra", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('female'), Person_type('relatives'), Season("summer"), piece_name("Trousers"),
              piece_type("Trousers"), piece_color("cyan")), salience=1)
    def clothes40712(self):
        self.myclothes = Myclothes(0, " ", "", 2, "pink", "T_Shirt", 0, "", "", 0, " ", "", 5, "white", "Kandra", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 11, "black", "waistband", 0, "",
                                   "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('female'), Person_type('relatives'), Season("summer"), piece_name("Trousers"),
              piece_type("Trousers"), piece_color("black")), salience=1)
    def clothes40812(self):
        self.myclothes = Myclothes(0, " ", "", 2, "yellow", "T_Shirt", 0, "", "", 0, " ", "", 5, "black", "Kandra", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 11, "black", "waistband", 0, "",
                                   "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='dark'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer"), piece_name("dress"),
              piece_type("Midriff"), piece_color("gray")), salience=1)
    def clothes40912(self):
        self.myclothes = Myclothes(0, " ", "", 0, "", "", 0, " ", "", 0, " ", "", 5, "black", "Kandra", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='hanatawi'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer"), piece_name("dress"),
              piece_type("MidiDress"), piece_color("pink")), salience=1)
    def clothes41012(self):
        self.myclothes = Myclothes(0, " ", "", 0, "", "", 0, " ", "", 0, " ", "", 5, "white", "Kandra", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", " ", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer"), piece_name("dress"),
              piece_type("MidiDress"), piece_color("cyan")), salience=1)
    def clothes41112(self):
        self.myclothes = Myclothes(0, " ", "", 0, "", "", 0, " ", "", 0, " ", "", 5, "silver", "Kandra", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer"), piece_name("dress"),
              piece_type("MidiDress"), piece_color("red")), salience=1)
    def clothes4121(self):
        self.myclothes = Myclothes(0, " ", "", 0, "", "", 0, " ", "", 0, " ", "", 5, "gold", "Kandra", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='dark'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer"), piece_name("dress"),
              piece_type("Midriff"), piece_color("gold")), salience=1)
    def clothes41312(self):
        self.myclothes = Myclothes(0, " ", "", 0, "", "", 0, " ", "", 0, " ", "", 5, "black", "Kandra ", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='hanatawi'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer"), piece_name("dress"),
              piece_type("Long_robe"), piece_color("silver")), salience=1)
    def clothes41412(self):
        self.myclothes = Myclothes(0, " ", "", 0, "", "", 0, " ", "", 0, " ", "", 5, "black", "Kandra", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='dark'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer"), piece_name("dress"),
              piece_type("MidiDress"), piece_color("black")), salience=1)
    def clothes4151(self):
        self.myclothes = Myclothes(0, " ", "", 0, "", "", 0, " ", "", 0, " ", "", 5, "vinous", "Kandra", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "", 0, " ", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer"), piece_name("dress"),
              piece_type("Long_robe"), piece_color("black")), salience=1)
    def clothes41612(self):
        self.myclothes = Myclothes(0, " ", "", 0, "", "", 0, " ", "", 0, " ", "", 5, "vinous", "Kandra", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "", 0, " ", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer"), piece_name("dress"),
              piece_type("Midriff"), piece_color("pink")), salience=1)
    def clothes41712(self):
        self.myclothes = Myclothes(0, " ", "", 0, "", "", 0, " ", "", 0, " ", "", 5, "black", "Kandra", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "", 0, " ", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer"), piece_name("dress"),
              piece_type("Long_robe"), piece_color("cyan")), salience=1)
    def clothes41812(self):
        self.myclothes = Myclothes(0, " ", "", 0, "", "", 0, " ", "", 0, " ", "", 5, "gold", "Kandra", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "", 0, " ", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer"), piece_name("dress"),
              piece_type("Midriff"), piece_color("blue")), salience=1)
    def clothes41912(self):
        self.myclothes = Myclothes(0, " ", "", 0, "", "", 0, " ", "", 0, " ", "", 5, "black", "Kandra", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "", 0, " ", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='hanatawi'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer"), piece_name("dress"),
              piece_type("Long_robe"), piece_color("pink")), salience=1)
    def clothes42012(self):
        self.myclothes = Myclothes(0, " ", "", 0, "", "", 0, " ", "", 0, " ", "", 5, "black", "Kandra", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "", 0, " ", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='hanatawi'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer"), piece_name("dress"),
              piece_type("MidiDress"), piece_color("black")), salience=1)
    def clothes42112(self):
        self.myclothes = Myclothes(0, " ", "", 0, "", "", 0, " ", "", 0, " ", "", 5, "black", "Kandra", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "", 0, " ", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='dark'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer"), piece_name("Shirt"),
              piece_type("Shirt"), piece_color("white")), salience=1)
    def clothes42212(self):
        self.myclothes = Myclothes(1, "black", "Trousers", 0, "", "", 0, "", "", 0, " ", "", 5, "black", "Kandra", 6,
                                   "vinous", "Coat", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 11, "black",
                                   "waistband", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='dark'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer"), piece_name("Trousers"),
              piece_type("Trousers"), piece_color("black")), salience=1)
    def clothes42312(self):
        self.myclothes = Myclothes(0, " ", "", 0, "", "", 3, "white", "Shirt", 0, " ", "", 5, "black", "Kandra", 6,
                                   "vinous", "Coat", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 11, "black",
                                   "waistband", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='dark'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer"), piece_name("T_Shirt"),
              piece_type("T_Shirt"), piece_color("yellow")), salience=1)
    def clothes42412(self):
        self.myclothes = Myclothes(1, "cyan", "Trousers", 0, "", "", 0, "", "", 0, " ", "", 5, "black", "Kandra", 0,
                                   "", "", 0, "", "", 0, " ", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='dark'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer"), piece_name("Trousers"),
              piece_type("jeans"), piece_color("cyan")), salience=1)
    def clothes42512(self):
        self.myclothes = Myclothes(0, " ", "", 2, "yellow", "T_Shirt", 0, "", "", 0, " ", "", 5, "black", "Kandra", 0,
                                   "", "", 0, "", "", 0, " ", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='dark'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer"), piece_name("T_Shirt"),
              piece_type("T_Shirt"), piece_color("pink")), salience=1)
    def clothes42612(self):
        self.myclothes = Myclothes(1, "black", "Trousers", 0, "", "", 0, "", "", 0, " ", "", 5, "black", "Kandra", 0,
                                   "", "", 0, "", "", 0, " ", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer"), piece_name("T_Shirt"),
              piece_type("T_Shirt"), piece_color("yellow")), salience=1)
    def clothes42712(self):
        self.myclothes = Myclothes(1, "cyan", "Trousers", 0, "", "", 0, "", "", 0, " ", "", 5, "black", "Kandra", 0,
                                   "", "", 0, "", "", 0, " ", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)


class CLOTHESThird(KnowledgeEngine):
    result = []
    myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0,
                          "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")

    @DefFacts()
    def _init_(self):
        self.result = []
        yield age(16)

    @Rule(AND(age(value=P(lambda value: value >= 21) & P(lambda value: value <= 35)), SkinColor(color='dark'),
              Occasion('gradution'), Gender('female'), Person_type('student'), Season("summer"), piece_name("Skirt"),
              piece_color("black")), salience=1)
    def clothes281(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "black", "Kandra", 6,
                                   "black", "Coat", 7, "black", "Hat", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0,
                                   "", "", 13, "black", " graduation_gown")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 21) & P(lambda value: value <= 35)), SkinColor(color='hanatawi'),
              Occasion('gradution'), Gender('female'), Person_type('student'), Season("summer"), piece_name("Skirt"),
              piece_color("black")), salience=1)
    def clothes282(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "black", "Kandra", 6,
                                   "black", "Coat", 7, "black", "Hat", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0,
                                   "", "", 13, "black", " graduation_gown")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 21) & P(lambda value: value <= 35)), SkinColor(color='hanatawi'),
              Occasion('gradution'), Gender('female'), Person_type('student'), Season("summer"), piece_name("Skirt"),
              piece_color("black")), salience=1)
    def clothes283(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "black", "Kandra", 6,
                                   "vinous", "Coat", 7, "black", "Hat", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0,
                                   "", "", 13, "black", " graduation_gown")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 21) & P(lambda value: value <= 35)), SkinColor(color='hanatawi'),
              Occasion('gradution'), Gender('female'), Person_type('student'), Season("summer"), piece_name("Skirt"),
              piece_color("black")), salience=1)
    def clothes4250(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "vinous", "Kandra", 6,
                                   "black", "Coat", 7, "black", "Hat", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0,
                                   "", "", 13, "black", " graduation_gown")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 21) & P(lambda value: value <= 35)), SkinColor(color='dark'),
              Occasion('gradution'), Gender('female'), Person_type('student'), Season("summer"), piece_name("Skirt"),
              piece_color("black")), salience=1)
    def clothes284(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "black", "Kandra", 6,
                                   "black", "Coat", 7, "black", "Hat", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0,
                                   "", "", 13, "black", " graduation_gown")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 21) & P(lambda value: value <= 35)), SkinColor(color='hanatawi'),
              Occasion('gradution'), Gender('female'), Person_type('student'), Season("summer"), piece_name("Skirt"),
              piece_color("black")), salience=1)
    def clothes285(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "black", "Kandra", 6,
                                   "black", "Coat", 7, "black", "Hat", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0,
                                   "", "", 13, "black", " graduation_gown")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 21) & P(lambda value: value <= 35)), SkinColor(color='hanatawi'),
              Occasion('gradution'), Gender('female'), Person_type('student'), Season("summer"), piece_name("Skirt"),
              piece_color("black")), salience=1)
    def clothes286(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "black", "Kandra", 6,
                                   "vinous", "Coat", 7, "black", "Hat", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0,
                                   "", "", 13, "black", " graduation_gown")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 21) & P(lambda value: value <= 35)), SkinColor(color='hanatawi'),
              Occasion('gradution'), Gender('female'), Person_type('student'), Season("summer"), piece_name("Skirt"),
              piece_color("black")), salience=1)
    def clothes287(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "gray", "Kandra", 6,
                                   "gray", "Coat", 7, "black", "Hat", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "",
                                   "", 13, "black", "graduation_gown")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 21) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('gradution'), Gender('female'), Person_type('student'), Season("summer"), piece_name("Skirt"),
              piece_color("black")), salience=1)
    def clothes288(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "black", "Kandra", 6,
                                   "vinous", "Coat", 7, "black", "Hat", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0,
                                   "", "", 13, "black", "graduation_gown")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 21) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('gradution'), Gender('female'), Person_type('student'), Season("summer"), piece_name("Skirt"),
              piece_color("white")), salience=1)
    def clothes289(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "cyan", "Kandra", 6,
                                   "cyan", "Coat", 7, "black", "Hat", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "",
                                   "", 13, "black", "graduation_gown")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 21) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('gradution'), Gender('female'), Person_type('student'), Season("summer"), piece_name("Skirt"),
              piece_color("white")), salience=1)
    def clothes290(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "pink", "Shirt", 0, "", "", 5, "cyan", "Kandra", 6, "cyan",
                                   "Coat", 7, "black", "Hat", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 13,
                                   "black", "graduation_gown")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 21) & P(lambda value: value <= 35)), SkinColor(color='dark'),
              Occasion('gradution'), Gender('female'), Person_type('student'), Season("summer"), piece_name("Skirt"),
              piece_color("black")), salience=1)
    def clothes291(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "black", "Kandra", 6,
                                   "black", "Coat", 7, "black", "Hat", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0,
                                   "", "", 13, "black", " graduation_gown")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 21) & P(lambda value: value <= 35)), SkinColor(color='hanatawi'),
              Occasion('gradution'), Gender('female'), Person_type('student'), Season("summer"), piece_name("Skirt"),
              piece_color("black")), salience=1)
    def clothes292(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "black", "Kandra", 6,
                                   "black", "Coat", 7, "black", "Hat", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0,
                                   "", "", 13, "black", "graduation_gown")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 21) & P(lambda value: value <= 35)), SkinColor(color='hanatawi'),
              Occasion('gradution'), Gender('female'), Person_type('student'), Season("summer"), piece_name("Trousers"),
              piece_color("white")), salience=1)
    def clothes293(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "white", "Kandra", 6,
                                   "pink", "Coat", 7, "black", "Hat", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "",
                                   "", 13, "black", "graduation_gown")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 21) & P(lambda value: value <= 35)), SkinColor(color='hanatawi'),
              Occasion('gradution'), Gender('female'), Person_type('student'), Season("summer"), piece_name("Trousers"),
              piece_color("black")), salience=1)
    def clothes294(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "white", "Kandra", 6,
                                   "cyan", "Coat", 7, "black", "Hat", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "",
                                   "", 13, "black", "graduation_gown")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 21) & P(lambda value: value <= 35)), SkinColor(color='dark'),
              Occasion('gradution'), Gender('female'), Person_type('student'), Season("summer"), piece_name("Trousers"),
              piece_color("black")), salience=1)
    def clothes295(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "vinous", "Shirt", 0, "", "", 5, "black", "Kandra", 6,
                                   "black", "Coat", 7, "black", "Hat", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0,
                                   "", "", 13, "black", "graduation_gown")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 21) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('gradution'), Gender('female'), Person_type('student'), Season("summer"), piece_name("Trousers"),
              piece_color("white")), salience=1)
    def clothes296(self):
        self.myclothes = Myclothes(0, "", " ", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "pink", "Kandra", 6,
                                   "pink", "Coat", 7, "black", "Hat", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "",
                                   "", 13, "black", "graduation_gown")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 21) & P(lambda value: value <= 35)), SkinColor(color='dark'),
              Occasion('gradution'), Gender('female'), Person_type('student'), Season("summer"), piece_name("Trousers"),
              piece_color("black")), salience=1)
    def clothes297(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "white", "Kandra", 6,
                                   "pink", "Coat", 7, "black", "Hat", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "",
                                   "", 13, "black", "graduation_gown")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 21) & P(lambda value: value <= 35)), SkinColor(color='hanatawi'),
              Occasion('gradution'), Gender('female'), Person_type('student'), Season("summer"), piece_name("Shirt"),
              piece_color("white")), salience=1)
    def clothes298(self):
        self.myclothes = Myclothes(1, "white", "Trousers", 0, "", "", 3, "", "", 0, "", "", 5, "white", "Kandra", 6,
                                   "pink", "Coat", 7, "black", "Hat", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "",
                                   "", 13, "black", "graduation_gown")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 21) & P(lambda value: value <= 35)), SkinColor(color='hanatawi'),
              Occasion('gradution'), Gender('female'), Person_type('student'), Season("summer"), piece_name("Shirt"),
              piece_color("white")), salience=1)
    def clothes299(self):
        self.myclothes = Myclothes(1, "black", "Trousers", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "white",
                                   "Kandra", 6, "cyan", "Coat", 7, "black", "Hat", 0, "", "", 0, "", "", 0, "", "", 0,
                                   "", "", 0, "", "", 13, "black", "graduation_gown")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 21) & P(lambda value: value <= 35)), SkinColor(color='dark'),
              Occasion('gradution'), Gender('female'), Person_type('student'), Season("summer"), piece_name("Shirt"),
              piece_color("white")), salience=1)
    def clothes300(self):
        self.myclothes = Myclothes(1, "black", "Trousers", 0, "", "", 3, "vinous", "Shirt", 0, "", "", 5, "black",
                                   "Kandra", 6, "black", "Coat", 7, "black", "Hat", 0, "", "", 0, "", "", 0, "", "", 0,
                                   "", "", 0, "", "", 13, "black", "graduation_gown")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 21) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('gradution'), Gender('female'), Person_type('student'), Season("summer"), piece_name("Shirt"),
              piece_color("white")), salience=1)
    def clothes803(self):
        self.myclothes = Myclothes(1, "white", "Trousers ", 0, "", "", 0, "", "", 0, "", "", 5, "pink", "Kandra", 6,
                                   "pink", "Coat", 7, "black", "Hat", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "",
                                   "", 13, "black", "graduation_gown")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 21) & P(lambda value: value <= 35)), SkinColor(color='dark'),
              Occasion('gradution'), Gender('female'), Person_type('student'), Season("summer"), piece_name("Shirt"),
              piece_color("white")), salience=1)
    def clothes301(self):
        self.myclothes = Myclothes(1, "black", "Trousers", 0, "", "", 0, "", "", 0, "", "", 5, "white", "Kandra", 6,
                                   "pink", "Coat", 7, "black", "Hat", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "",
                                   "", 13, "black", "graduation_gown")
        self.result.append(self.myclothes)

    #   ///////////

    @Rule(AND(age(value=P(lambda value: value >= 21) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('gradution'), Gender('male'), Person_type('student'), Season("summer"), piece_name("Shirt"),
              piece_color("white")), salience=1)
    def clothes302(self):
        self.myclothes = Myclothes(1, "gray", "Trousers", 0, "", "", 0, "", "", 0, "", "", 5, "darkblue", "Kandra",
                                   0, "", "", 7, "black", "Hat", 8, "darkblue", "carafe", 0, "", "", 0, "", "", 0, "",
                                   "", 0, "", "", 13, "black", "graduation_gown")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 21) & P(lambda value: value <= 35)), SkinColor(color='hanatawi'),
              Occasion('gradution'), Gender('male'), Person_type('student'), Season("summer"), piece_name("Shirt"),
              piece_color("white")), salience=1)
    def clothes303(self):
        self.myclothes = Myclothes(1, "black", "Trousers", 0, "", "", 0, "", "", 0, " ", "", 5, "black", "Kandra", 0,
                                   "", "", 7, "black", "Hat", 8, "vinous", "carafe", 0, "", "", 0, "", "", 0, "", "", 0,
                                   "", "", 13, "black", "graduation_gown")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 21) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('gradution'), Gender('male'), Person_type('student'), Season("summer"), piece_name("Shirt"),
              piece_color("cyan")), salience=2)
    def clothes304(self):
        self.myclothes = Myclothes(1, "darkblue", "Trousers", 0, "", "", 0, "", "", 0, " ", "", 5, "darkblue",
                                   "Kandra", 0, "", "", 7, "black", "Hat", 8, "darkblue", "carafe", 0, "", "", 0, "",
                                   "", 0, "", "", 0, "", "", 13, "black", "graduation_gown")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 21) & P(lambda value: value <= 35)), SkinColor(color='hanatawi'),
              Occasion('gradution'), Gender('male'), Person_type('student'), Season("summer"), piece_name("Trousers"),
              piece_color("gray")), salience=2)
    def clothes305(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "black", "Kandra", 0, "",
                                   "", 7, "black", "Hat", 8, "darkblue", "carafe", 0, "", "", 0, "", "", 0, "", "", 0,
                                   "", "", 13, "black", "graduation_gown")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 21) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('gradution'), Gender('male'), Person_type('student'), Season("summer"), piece_name("Trousers"),
              piece_color("darkblue")), salience=2)
    def clothes306(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "beige", "Shirt", 0, " ", "", 5, "darkblue", "Kandra", 0,
                                   "", "", 7, "black", "Hat", 8, "beige", "carafe", 0, "", "", 0, "", "", 0, "", "", 0,
                                   "", "", 13, "black", "graduation_gown")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 21) & P(lambda value: value <= 35)), SkinColor(color='dark'),
              Occasion('gradution'), Gender('male'), Person_type('student'), Season("summer"), piece_name("Shirt"),
              piece_color("black")), salience=2)
    def clothes307(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, " ", "", 5, "grown", "Kandra", 0, "",
                                   "", 7, "black", "Hat", 8, "black", "carafe", 0, "", "", 0, "", "", 0, "", "", 0, "",
                                   "", 13, "black", "graduation_gown")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 21) & P(lambda value: value <= 35)), SkinColor(color='dark'),
              Occasion('gradution'), Gender('male'), Person_type('student'), Season("summer"), piece_name("Shirt"),
              piece_color("white")), salience=2)
    def clothes308(self):
        self.myclothes = Myclothes(1, "vinous", "Trousers", 0, "", "", 0, "", "", 0, "", "", 5, "black", "Kandra", 0,
                                   "", "", 7, "black", "Hat", 8, "vinous", "carafe", 0, "", "", 0, "", "", 0, "", "", 0,
                                   "", "", 13, "black", "graduation_gown")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='dark'),
              Occasion('wadding'), Gender('male'), Person_type('brother'), Season("summer"), piece_name("Shirt"),
              piece_color("white")), salience=1)
    def clothes309(self):
        self.myclothes = Myclothes(1, "black", "Trousers ", 0, "", "", 0, "", "", 0, " ", "", 5, "gray", "shose", 0,
                                   "", "", 0, "", "", 8, "gray", "carafe", 0, "", "", 0, "", "", 11, "black",
                                   "waistband", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='dark'),
              Occasion('wadding'), Gender('male'), Person_type('brother'), Season("summer"), piece_name("Shirt"),
              piece_color("white")), salience=1)
    def clothes310(self):
        self.myclothes = Myclothes(1, "gray", "Trousers", 0, "", "", 0, "", "", 0, "", "", 5, "brown", "shose", 0,
                                   "", "", 0, "", "", 8, "grown", "carafe", 0, "", "", 0, "", "", 11, "black",
                                   "waistband", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('male'), Person_type('brother'), Season("summer"), piece_name("Shirt"),
              piece_color("white")), salience=1)
    def clothes311(self):
        self.myclothes = Myclothes(1, "darkblue", "Trousers", 0, "", "", 0, "", "", 0, " ", "", 5, "black", "shose", 0,
                                   "", "", 0, "", "", 8, "vinous", "carafe", 0, "", "", 0, "", "", 11, "black",
                                   "waistband", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16)

                        & P(lambda value: value <= 35)), SkinColor(color='hanatawi'),
              Occasion('wadding'), Gender('male'), Person_type('brother'), Season("summer"), piece_name("Shirt"),
              piece_color("white")), salience=1)
    def clothes312(self):
        self.myclothes = Myclothes(1, "black", "Trousers", 0, "", "", 0, "", "", 0, " ", "", 5, "black", "shose", 0,
                                   "", "", 0, "", "", 8, "black", "carafe", 0, "", "", 0, "", "", 11, "black",
                                   "waistband", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='hanatawi'),
              Occasion('wadding'), Gender('male'), Person_type('friend'), Season("summer"), piece_name("Shirt"),
              piece_color("white")), salience=1)
    def clothes313(self):
        self.myclothes = Myclothes(1, "white", "Trousers", 0, "", "", 0, "", "", 0, " ", "", 5, "brown", "shose", 6,
                                   "darkblue", "Coat", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 11, "brown",
                                   "waistband", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='hanatawi'),
              Occasion('wadding'), Gender('male'), Person_type('friend'), Season("summer"), piece_name("Shirt"),
              piece_color("pink")), salience=1)
    def clothes314(self):
        self.myclothes = Myclothes(1, "black", "Trousers", 0, "", "", 0, " ", "", 0, " ", "", 5, "black", "shose", 0,
                                   "", "", 0, "", "", 8, "black", "carafe", 0, "", "", 0, "", "", 11, "black",
                                   "waistband", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='dark'),
              Occasion('wadding'), Gender('male'), Person_type('friend'), Season("summer"), piece_name("Shirt"),
              piece_color("white")), salience=1)
    def clothes315(self):
        self.myclothes = Myclothes(1, "gray", "Trousers", 0, "", "", 0, "", "", 0, " ", "", 5, "brown", "shose", 0, "",
                                   "", 0, "", "", 8, "darkblue", "carafe", 0, "", "", 0, "", "", 11, "brown",
                                   "waistband", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('male'), Person_type('friend'), Season("summer"), piece_name("Shirt"),
              piece_color("cyan")), salience=1)
    def clothes316(self):
        self.myclothes = Myclothes(1, "darkblue", "Trousers", 0, "", "", 0, "", "", 0, "", "", 5, "brown", "shose",
                                   0, "", "", 0, "", "", 8, "grown", "carafe", 0, "", "", 0, "", "", 11, "brown",
                                   "waistband", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('male'), Person_type('friend'), Season("summer"), piece_name("Shirt"),
              piece_color("gray")), salience=1)
    def clothes317(self):
        self.myclothes = Myclothes(1, "black", "Trousers", 0, "", "", 0, "", "", 0, "", "", 5, "black", "shose", 0,
                                   "", "", 0, "", "", 8, "black", "carafe", 0, "", "", 0, "", "", 11, "black",
                                   "waistband", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='dark'),
              Occasion('wadding'), Gender('male'), Person_type('relatives'), Season("summer"), piece_name("Shirt"),
              piece_color("white")), salience=1)
    def clothes318(self):
        self.myclothes = Myclothes(1, "gray", "Trousers", 0, "", "", 0, "", "", 0, " ", "", 5, "brown", "shose", 0, "",
                                   "", 0, "", "", 8, "black", "carafe", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0,
                                   "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='dark'),
              Occasion('wadding'), Gender('male'), Person_type('relatives'), Season("summer"), piece_name("Shirt"),
              piece_color("gray")), salience=1)
    def clothes319(self):
        self.myclothes = Myclothes(1, "darkblue", "jeans", 0, "", "", 0, "", "", 0, "", "", 5, "brown", "shose", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 11, "black", "waistband", 0, "",
                                   "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='hanatawi'),
              Occasion('wadding'), Gender('male'), Person_type('relatives'), Season("summer"), piece_name("Shirt"),
              piece_color("vinous")), salience=1)
    def clothes320(self):
        self.myclothes = Myclothes(1, "black", "Trousers ", 0, "", "", 0, "", "", 0, " ", "", 5, "black", "shose", 0,
                                   "", "", 0, "", "", 8, "black", "carafe", 0, "", "", 0, "", "", 11, "black",
                                   "waistband", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    #     /////////////////////////////////////////////////////مناسبة زفاف
    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='dark'),
              Occasion('wadding'), Gender('male'), Person_type('brother'), Season("summer"), piece_name("Trousers"),
              piece_color("black")), salience=1)
    def clothes321(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, " ", "", 5, "gray", "shose", 0, "",
                                   "", 0, "", "", 8, "gray", "carafe", 0, "", "", 0, "", "", 11, "black", "waistband",
                                   0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='dark'),
              Occasion('wadding'), Gender('male'), Person_type('brother'), Season("summer"), piece_name("Trousers"),
              piece_color("gray")), salience=1)
    def clothes322(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "brown", "shose", 0, "",
                                   "", 0, "", "", 8, "grown", "carafe", 0, "", "", 0, "", "", 11, "black", "waistband",
                                   0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('male'), Person_type('brother'), Season("summer"), piece_name("Trousers"),
              piece_color("darkblue")), salience=1)
    def clothes323(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, " ", "", 5, "black", "shose", 0, "",
                                   "", 0, "", "", 8, "vinous", "carafe", 0, "", "", 0, "", "", 11, "black", "waistband",
                                   0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='hanatawi'),
              Occasion('wadding'), Gender('male'), Person_type('brother'), Season("summer"), piece_name("Trousers"),
              piece_color("black")), salience=1)
    def clothes324(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, " ", "", 5, "black", "shose", 0, "",
                                   "", 0, "", "", 8, "black", "carafe", 0, "", "", 0, "", "", 11, "black", "waistband",
                                   0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='hanatawi'),
              Occasion('wadding'), Gender('male'), Person_type('friend'), Season("summer"), piece_name("Trousers"),
              piece_color("white")), salience=1)
    def clothes325(self):
        self.myclothes = Myclothes(0, "", " ", 0, "", "", 3, "white", "Shirt", 0, " ", "", 5, "brown", "shose", 6,
                                   "darkblue", "Coat", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 11, "brown",
                                   "waistband", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='hanatawi'),
              Occasion('wadding'), Gender('male'), Person_type('friend'), Season("summer"), piece_name("Trousers"),
              piece_color("white")), salience=1)
    def clothes326(self):
        self.myclothes = Myclothes(0, "black", "Trousers", 0, "", "", 3, "pink", "Shirt", 0, " ", "", 5, "black",
                                   "shose", 0, "", "", 0, "", "", 8, "black", "carafe", 0, "", "", 0, "", "", 11,
                                   "black", "waistband", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='dark'),
              Occasion('wadding'), Gender('male'), Person_type('friend'), Season("summer"), piece_name("Trousers"),
              piece_color("gray")), salience=1)
    def clothes327(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, " ", "", 5, "brown", "shose", 0, "",
                                   "", 0, "", "", 8, "darkblue", "carafe", 0, "", "", 0, "", "", 11, "brown",
                                   "waistband", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('male'), Person_type('friend'), Season("summer"), piece_name("Trousers"),
              piece_color("darkblue")), salience=1)
    def clothes328(self):
        self.myclothes = Myclothes(0, " ", " ", 0, "", "", 3, "cyan", "Shirt", 0, " ", "", 5, "brown", "shose", 0, "",
                                   "", 0, "", "", 8, "grown", "carafe", 0, "", "", 0, "", "", 11, "brown", "waistband",
                                   0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('male'), Person_type('friend'), Season("summer"), piece_name("Trousers"),
              piece_color("black")), salience=1)
    def clothes329(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "gray", "Shirt", 0, " ", "", 5, "black", "shose", 0, "",
                                   "", 0, "", "", 8, "black", "carafe", 0, "", "", 0, "", "", 11, "black", "waistband",
                                   0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='dark'),
              Occasion('wadding'), Gender('male'), Person_type('relatives'), Season("summer"), piece_name("Trousers"),
              piece_color("gray")), salience=1)
    def clothes330(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, " ", "", 5, "brown", "shose", 0, "",
                                   "", 0, "", "", 8, "black", "carafe", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0,
                                   "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='dark'),
              Occasion('wadding'), Gender('male'), Person_type('relatives'), Season("summer"), piece_name("Trousers"),
              piece_color("darkblue")), salience=1)
    def clothes331(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "gray", "Shirt", 0, " ", "", 5, "brown", "shose", 0, "",
                                   "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 11, "black", "waistband", 0, "", "",
                                   0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='hanatawi'),
              Occasion('wadding'), Gender('male'), Person_type('relatives'), Season("summer"), piece_name("Trousers"),
              piece_color("black")), salience=1)
    def clothes332(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "vinous", "Shirt", 0, " ", "", 5, "black", "shose", 0,
                                   "", "", 0, "", "", 8, "black", "carafe", 0, "", "", 0, "", "", 11, "black",
                                   "waistband", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('work'), Gender('female'), Person_type('officer'), Season("winter"), piece_name("Skirt"),
              piece_color("black")), salience=1)
    def clothes333(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "black", "Kandra", 6,
                                   "vinous", "Coat", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 11, "black",
                                   "waistband", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='dark'),
              Occasion('work'), Gender('female'), Person_type('officer'), Season("winter"), piece_name("Skirt"),
              piece_color("gray")), salience=1)
    def clothes334(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "black", "Kandra", 6,
                                   "gray", "Coat", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 11, "black", "waistband",
                                   0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='white'),
              Occasion('work'), Gender('female'), Person_type('officer'), Season("winter"), piece_name("darkblue"),
              piece_color("black")), salience=1)
    def clothes335(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "black", "Kandra", 6,
                                   "beige", "Coat", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 11, "black",
                                   "waistband", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='white'),
              Occasion('work'), Gender('male'), Person_type('engineer'), Season("summer"), piece_name("Shirt"),
              piece_color("white")), salience=1)
    def clothes336(self):
        self.myclothes = Myclothes(1, "darkblue", "jeans", 0, "", "", 0, "", "", 0, "", "", 5, "white", "shose", 0, "",
                                   "", 7, "yellow", "Hat", 0, "", "", 9, "orange", "Jacket", 0, "", "", 0, "", "", 0,
                                   "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('work'), Gender('male'), Person_type('engineer'), Season("summer"), piece_name("Shirt"),
              piece_color("white")), salience=1)
    def clothes337(self):
        self.myclothes = Myclothes(1, "darkblue", "jeans", 0, "", "", 0, "", "", 0, "", "", 5, "white", "shose", 0, "",
                                   "", 7, "yellow", "Hat", 0, "", "", 9, "orange", "Jacket", 0, "", "", 0, "", "", 0,
                                   "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='dark'),
              Occasion('work'), Gender('male'), Person_type('engineer'), Season("summer"), piece_name("Shirt"),
              piece_color("white")), salience=1)
    def clothes338(self):
        self.myclothes = Myclothes(1, "darkblue", "jeans", 0, "", "", 0, "", "", 0, "", "", 5, "white", "shose", 0, "",
                                   "", 7, "yellow", "Hat", 0, "", "", 9, "orange", "Jacket", 0, "", "", 0, "", "", 0,
                                   "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='white'),
              Occasion('work'), Gender('male'), Person_type('engineer'), Season("winter"), piece_name("Shirt"),
              piece_color("white")), salience=1)
    def clothes339(self):
        self.myclothes = Myclothes(1, "gray", "jeans", 0, "", "", 0, "", "", 0, "", "", 5, "white", "shose", 0,
                                   "black", "Coat", 7, "yellow", "Hat", 0, "", "", 9, "orange", "Jacket", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('work'), Gender('male'), Person_type('engineer'), Season("winter"), piece_name("Shirt"),
              piece_color("white")), salience=1)
    def clothes340(self):
        self.myclothes = Myclothes(1, "gray", "jeans", 0, "", "", 0, "", "", 0, "", "", 5, "white", "shose", 0,
                                   "black", "Coat", 7, "yellow", "Hat", 0, "", "", 9, "orange", "Jacket", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='dark'),
              Occasion('work'), Gender('male'), Person_type('engineer'), Season("winter"), piece_name("Shirt"),
              piece_color("white")), salience=1)
    def clothes341(self):
        self.myclothes = Myclothes(1, "gray", "jeans", 0, "", "", 0, "", "", 0, "", "", 5, "white", "shose", 6, "gray",
                                   "Coat", 7, "yellow", "Hat", 0, "", "", 9, "orange", "Jacket", 0, "", "", 0, "", "",
                                   0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='white'),
              Occasion('work'), Gender('male'), Person_type('engineer'), Season("winter"), piece_name("Shirt"),
              piece_color("white")), salience=1)
    def clothes342(self):
        self.myclothes = Myclothes(1, "darkblue", "jeans", 0, "", "", 0, "", "", 0, "", "", 5, "white", "shose", 6,
                                   "darkblue", "Coat", 7, "yellow", "Hat", 0, "", "", 9, "orange", "Jacket", 0, "", "",
                                   0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='white'),
              Occasion('work'), Gender('male'), Person_type('engineer'), Season("summer"), piece_name("Shirt"),
              piece_color("white")), salience=1)
    def clothes3422(self):
        self.myclothes = Myclothes(1, "darkblue", "jeans", 0, "", "", 0, "", "", 0, "", "", 5, "white", "shose", 6,
                                   "darkblue", "Coat", 7, "yellow", "Hat", 0, "", "", 9, "orange", "Jacket", 0, "", "",
                                   0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('work'), Gender('male'), Person_type('engineer'), Season("winter"), piece_name("Shirt"),
              piece_color("white")), salience=2)
    def clothes343(self):
        self.myclothes = Myclothes(1, "darkblue", "jeans", 0, "", "", 0, "", "", 0, "", "", 5, "white", "shose", 6,
                                   "dark", "Coat", 7, "yellow", "Hat", 0, "", "", 9, "orange", "Jacket", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='dark'),
              Occasion('work'), Gender('male'), Person_type('engineer'), Season("winter"), piece_name("Shirt"),
              piece_color("white")), salience=1)
    def clothes344(self):
        self.myclothes = Myclothes(1, "darkblue", "jeans", 0, "", "", 0, "", "", 0, "", "", 5, "white", "shose", 6,
                                   "gray", "Coat", 7, "yellow", "Hat", 0, "", "", 9, "orange", "Jacket", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='white'),
              Occasion('work'), Gender('male'), Person_type('engineer'), Season("winter"), piece_name("Trousers"),
              piece_color("gray")), salience=1)
    def clothes345(self):
        self.myclothes = Myclothes(0, "", " ", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "white", "shose", 6,
                                   "darkblue", "Coat", 7, "yellow", "Hat", 0, "", "", 9, "orange", "Jacket", 0, "", "",
                                   0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('work'), Gender('male'), Person_type('engineer'), Season("winter"), piece_name("Trousers"),
              piece_color("gray")), salience=1)
    def clothes346(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "white", "shose", 6,
                                   "dark", "Coat", 7, "yellow", "Hat", 0, "", "", 9, "orange", "Jacket", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='dark'),
              Occasion('work'), Gender('male'), Person_type('engineer'), Season("winter"), piece_name("Trousers"),
              piece_color("gray")), salience=1)
    def clothes347(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "white", "shose", 6,
                                   "gray", "Coat", 7, "yellow", "Hat", 0, "", "", 9, "orange", "Jacket", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='white'),
              Occasion('work'), Gender('male'), Person_type('engineer'), Season("winter"), piece_name("Trousers"),
              piece_color("darkblue")), salience=1)
    def clothes348(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "white", "shose", 6,
                                   "darkblue", "Coat", 7, "yellow", "Hat", 0, "", "", 9, "orange", "Jacket", 0, "", "",
                                   0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('work'), Gender('male'), Person_type('engineer'), Season("winter"), piece_name("Trousers"),
              piece_color("darkblue")), salience=1)
    def clothes349(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "white", "shose", 6,
                                   "dark", "Coat", 7, "yellow", "Hat", 0, "", "", 9, "orange", "Jacket", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='dark'),
              Occasion('work'), Gender('male'), Person_type('engineer'), Season("winter"), piece_name("Trousers"),
              piece_color("darkblue")), salience=1)
    def clothes350(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "white", "shose", 6,
                                   "gray", "Coat", 7, "yellow", "Hat", 0, "", "", 9, "orange", "Jacket", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='white'),
              Occasion('work'), Gender('male'), Person_type('engineer'), Season("summer"), piece_name("Trousers"),
              piece_color("gray")), salience=1)
    def clothes351(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "white", "shose", 0, "",
                                   "", 7, "yellow", "Hat", 0, "", "", 9, "orange", "Jacket", 0, "", "", 0, "", "", 0,
                                   "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('work'), Gender('male'), Person_type('engineer'), Season("summer"), piece_name("Trousers"),
              piece_color("gray")), salience=1)
    def clothes352(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "white", "shose", 0, "",
                                   "", 7, "yellow", "Hat", 0, "", "", 9, "orange", "Jacket", 0, "", "", 0, "", "", 0,
                                   "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='dark'),
              Occasion('work'), Gender('male'), Person_type('engineer'), Season("summer"), piece_name("Trousers"),
              piece_color("gray")), salience=1)
    def clothes352(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "white", "shose", 0, "",
                                   "", 7, "yellow", "Hat", 0, "", "", 9, "orange", "Jacket", 0, "", "", 0, "", "", 0,
                                   "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='white'),
              Occasion('work'), Gender('male'), Person_type('engineer'), Season("summer"), piece_name("Trousers"),
              piece_color("darkblue")), salience=1)
    def clothes353(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "white", "shose", 0, "",
                                   "", 7, "yellow", "Hat", 0, "", "", 9, "orange", "Jacket", 0, "", "", 0, "", "", 0,
                                   "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('work'), Gender('male'), Person_type('engineer'), Season("summer"), piece_name("Trousers"),
              piece_color("darkblue")), salience=1)
    def clothes354(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "white", "shose", 0, "",
                                   "", 7, "yellow", "Hat", 0, "", "", 9, "orange", "Jacket", 0, "", "", 0, "", "", 0,
                                   "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='dark'),
              Occasion('work'), Gender('male'), Person_type('engineer'), Season("summer"), piece_name("Trousers"),
              piece_color("darkblue")), salience=1)
    def clothes3556(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "white", "shose", 0, "",
                                   "", 7, "yellow", "Hat", 0, "", "", 9, "orange", "Jacket", 0, "", "", 0, "", "", 0,
                                   "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='white'),
              Occasion('work'), Gender('female'), Person_type('engineer'), Season("summer"), piece_name("Shirt"),
              piece_color("white")), salience=1)
    def clothes356(self):
        self.myclothes = Myclothes(1, "darkblue", "jeans", 0, "", "", 0, "", "", 0, "", "", 5, "white", "shose", 0, "",
                                   "", 7, "yellow", "Hat", 0, "", "", 9, "orange", "Jacket", 0, "", "", 0, "", "", 0,
                                   "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('work'), Gender('female'), Person_type('engineer'), Season("summer"), piece_name("Shirt"),
              piece_color("white")), salience=1)
    def clothes357(self):
        self.myclothes = Myclothes(1, "darkblue", "jeans", 0, "", "", 0, "", "", 0, "", "", 5, "white", "shose", 0, "",
                                   "", 7, "yellow", "Hat", 0, "", "", 9, "orange", "Jacket", 0, "", "", 0, "", "", 0,
                                   "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='dark'),
              Occasion('work'), Gender('female'), Person_type('engineer'), Season("summer"), piece_name("Shirt"),
              piece_color("white")), salience=1)
    def clothes358(self):
        self.myclothes = Myclothes(1, "darkblue", "jeans", 0, "", "", 0, "", "", 0, "", "", 5, "white", "shose", 0, "",
                                   "", 7, "yellow", "Hat", 0, "", "", 9, "orange", "Jacket", 0, "", "", 0, "", "", 0,
                                   "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='white'),
              Occasion('work'), Gender('female'), Person_type('engineer'), Season("winter"), piece_name("Shirt"),
              piece_color("white")), salience=1)
    def clothes359(self):
        self.myclothes = Myclothes(1, "gray", "jeans", 0, "", "", 0, "", "", 0, "", "", 5, "white", "shose", 0,
                                   "black", "Coat", 7, "yellow", "Hat", 0, "", "", 9, "orange", "Jacket", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('work'), Gender('female'), Person_type('engineer'), Season("winter"), piece_name("Shirt"),
              piece_color("white")), salience=1)
    def clothes360(self):
        self.myclothes = Myclothes(1, "gray", "jeans", 0, "", "", 0, "", "", 0, "", "", 5, "white", "shose", 0,
                                   "black", "Coat", 7, "yellow", "Hat", 0, "", "", 9, "orange", "Jacket", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='dark'),
              Occasion('work'), Gender('female'), Person_type('engineer'), Season("winter"), piece_name("Shirt"),
              piece_color("white")), salience=1)
    def clothes361(self):
        self.myclothes = Myclothes(1, "gray", "jeans", 0, "", "", 0, "", "", 0, "", "", 5, "white", "shose", 6, "gray",
                                   "Coat", 7, "yellow", "Hat", 0, "", "", 9, "orange", "Jacket", 0, "", "", 0, "", "",
                                   0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='white'),
              Occasion('work'), Gender('female'), Person_type('engineer'), Season("winter"), piece_name("Shirt"),
              piece_color("white")), salience=1)
    def clothes362(self):
        self.myclothes = Myclothes(1, "darkblue", "jeans", 0, "", "", 0, "", "", 0, "", "", 5, "white", "shose", 6,
                                   "darkblue", "Coat", 7, "yellow", "Hat", 0, "", "", 9, "orange", "Jacket", 0, "", "",
                                   0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('work'), Gender('female'), Person_type('engineer'), Season("winter"), piece_name("Shirt"),
              piece_color("white")), salience=1)
    def clothes363(self):
        self.myclothes = Myclothes(1, "darkblue", "jeans", 0, "", "", 0, "", "", 0, "", "", 5, "white", "shose", 6,
                                   "dark", "Coat", 7, "yellow", "Hat", 0, "", "", 9, "orange", "Jacket", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='dark'),
              Occasion('work'), Gender('female'), Person_type('engineer'), Season("winter"), piece_name("Shirt"),
              piece_color("white")), salience=1)
    def clothes364(self):
        self.myclothes = Myclothes(1, "darkblue", "jeans", 0, "", "", 0, "", "", 0, "", "", 5, "white", "shose", 6,
                                   "gray", "Coat", 7, "yellow", "Hat", 0, "", "", 9, "orange", "Jacket", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='white'),
              Occasion('work'), Gender('female'), Person_type('engineer'), Season("winter"), piece_name("Trousers"),
              piece_color("gray")), salience=1)
    def clothes365(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "white", "shose", 6,
                                   "darkblue", "Coat", 7, "yellow", "Hat", 0, "", "", 9, "orange", "Jacket", 0, "", "",
                                   0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('work'), Gender('female'), Person_type('engineer'), Season("winter"), piece_name("Trousers"),
              piece_color("gray")), salience=1)
    def clothes366(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "white", "shose", 6,
                                   "dark", "Coat", 7, "yellow", "Hat", 0, "", "", 9, "orange", "Jacket", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='dark'),
              Occasion('work'), Gender('female'), Person_type('engineer'), Season("winter"), piece_name("Trousers"),
              piece_color("gray")), salience=1)
    def clothes367(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "white", "shose", 6,
                                   "gray", "Coat", 7, "yellow", "Hat", 0, "", "", 9, "orange", "Jacket", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='white'),
              Occasion('work'), Gender('female'), Person_type('engineer'), Season("winter"), piece_name("Trousers"),
              piece_color("darkblue")), salience=1)
    def clothes368(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "white", "shose", 6,
                                   "darkblue", "Coat", 7, "yellow", "Hat", 0, "", "", 9, "orange", "Jacket", 0, "", "",
                                   0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('work'), Gender('female'), Person_type('engineer'), Season("winter"), piece_name("Trousers"),
              piece_color("darkblue")), salience=1)
    def clothes369(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "white", "shose", 6,
                                   "dark", "Coat", 7, "yellow", "Hat", 0, "", "", 9, "orange", "Jacket", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='dark'),
              Occasion('work'), Gender('female'), Person_type('engineer'), Season("winter"), piece_name("Trousers"),
              piece_color("darkblue")), salience=1)
    def clothes370(self):
        self.myclothes = Myclothes(0, "", " ", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "white", "shose", 6,
                                   "gray", "Coat", 7, "yellow", "Hat", 0, "", "", 9, "orange", "Jacket", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='white'),
              Occasion('work'), Gender('female'), Person_type('engineer'), Season("summer"), piece_name("Trousers"),
              piece_color("gray")), salience=1)
    def clothes371(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "white", "shose", 0, "",
                                   "", 7, "yellow", "Hat", 0, "", "", 9, "orange", "Jacket", 0, "", "", 0, "", "", 0,
                                   "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('work'), Gender('female'), Person_type('engineer'), Season("summer"), piece_name("Trousers"),
              piece_color("gray")), salience=1)
    def clothes372(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "white", "shose", 0, "",
                                   "", 7, "yellow", "Hat", 0, "", "", 9, "orange", "Jacket", 0, "", "", 0, "", "", 0,
                                   "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='dark'),
              Occasion('work'), Gender('female'), Person_type('engineer'), Season("summer"), piece_name("Trousers"),
              piece_color("gray")), salience=1)
    def clothes373(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "white", "shose", 0, "",
                                   "", 7, "yellow", "Hat", 0, "", "", 9, "orange", "Jacket", 0, "", "", 0, "", "", 0,
                                   "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='white'),
              Occasion('work'), Gender('female'), Person_type('engineer'), Season("summer"), piece_name("Trousers"),
              piece_color("darkblue")), salience=1)
    def clothes374(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "white", "shose", 0, "",
                                   "", 7, "yellow", "Hat", 0, "", "", 9, "orange", "Jacket", 0, "", "", 0, "", "", 0,
                                   "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('work'), Gender('female'), Person_type('engineer'), Season("summer"), piece_name("Trousers"),
              piece_color("darkblue")), salience=1)
    def clothes375(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "white", "shose", 0, "",
                                   "", 7, "yellow", "Hat", 0, "", "", 9, "orange", "Jacket", 0, "", "", 0, "", "", 0,
                                   "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='dark'),
              Occasion('work'), Gender('female'), Person_type('engineer'), Season("summer"), piece_name("Trousers"),
              piece_color("darkblue")), salience=1)
    def clothes376(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "white", "shose", 0, "",
                                   "", 7, "yellow", "Hat", 0, "", "", 9, "orange", "Jacket", 0, "", "", 0, "", "", 0,
                                   "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('work'), Gender('male'), Person_type('officer'), Season("winter"), piece_name("Trousers"),
              piece_color("black")), salience=1)
    def clothes377(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "brown", "shose", 6,
                                   "black", "Coat", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 11, "brown",
                                   "waistband", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='dark'),
              Occasion('work'), Gender('male'), Person_type('officer'), Season("winter"), piece_name("Trousers"),
              piece_color("gray")), salience=1)
    def clothes378(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "brown", "shose", 6,
                                   "black", "Coat", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 11, "brown",
                                   "waistband", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='white'),
              Occasion('work'), Gender('female'), Person_type('officer'), Season("winter"), piece_name("Trousers"),
              piece_color("darkblue")), salience=1)
    def clothes379(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "beige", "Kandra", 6,
                                   "darkblue", "Coat", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 11, "beige",
                                   "waistband", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='dark'),
              Occasion('work'), Gender('female'), Person_type('business'), Season("winter"), piece_name("skirt"),
              piece_color("gray")), salience=1)
    def clothes380(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "black", "Kandra", 6,
                                   "gray", "Coat", 0, "", "", 8, "blue", "carafe", 9, "black", "Jacket", 0, "", "", 0,
                                   "", "", 0, " ", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='white'),
              Occasion('work'), Gender('male'), Person_type('business'), Season("winter"), piece_name("skirt"),
              piece_color("darkblue")), salience=1)
    def clothes381(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "brown", "Kandra", 6,
                                   "darkblue", "Coat", 0, "", "", 8, "brown", "darkblue", 9, "black", "Jacket", 0, "",
                                   "", 0, "", "", 0, " ", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('work'), Gender('female'), Person_type('business'), Season("winter"), piece_name("skirt"),
              piece_color("gray")), salience=1)
    def clothes382(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "black", "Kandra", 6,
                                   "dark", "Coat", 0, "", "", 8, "black", "carafe", 9, "black", "Jacket", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='dark'),
              Occasion('work'), Gender('female'), Person_type('business'), Season("winter"), piece_name("Trousers"),
              piece_color("gray")), salience=1)
    def clothes383(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "black", "Kandra", 6,
                                   "gray", "Coat", 0, "", "", 8, "blue", "carafe", 9, "black", "Jacket", 0, "", "", 0,
                                   "", "", 0, " ", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='white'),
              Occasion('work'), Gender('male'), Person_type('business'), Season("winter"), piece_name("Trousers"),
              piece_color("darkblue")), salience=1)
    def clothes384(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "brown", "Kandra", 6,
                                   "darkblue", "Coat", 0, "", "", 8, "brown", "darkblue", 9, "black", "Jacket", 0, "",
                                   "", 0, "", "", 0, " ", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('work'), Gender('female'), Person_type('business'), Season("winter"), piece_name("Trousers"),
              piece_color("gray")), salience=1)
    def clothes385(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "black", "Kandra", 6,
                                   "dark", "Coat", 0, "", "", 8, "black", "carafe", 9, "black", "Jacket", 0, "", "", 0,
                                   "", "", 0, " ", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='white'),
              Occasion('work'), Gender('male'), Person_type('business '), Season("winter"), piece_name("Trousers"),
              piece_color("black")), salience=1)
    def clothes386(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "black", "Kandra", 6,
                                   "gray", "Coat", 0, "", "", 8, "vinous", "carafe", 9, "black", "Jacket", 0, "", "", 0,
                                   "", "", 0, " ", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='dark'),
              Occasion('work'), Gender('female'), Person_type('business'), Season("summer"), piece_name("Trousers"),
              piece_color("gray")), salience=1)
    def clothes387(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "black", "Kandra", 6,
                                   "gray", "Coat", 0, "", "", 8, "blue", "carafe", 0, "", "", 0, "", "", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='white'),
              Occasion('work'), Gender('male'), Person_type('business'), Season("summer"), piece_name("Trousers"),
              piece_color("darkblue")), salience=1)
    def clothes388(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "brown", "Kandra", 6,
                                   "darkblue", "Coat", 0, "", "", 8, "brown", "darkblue", 0, "", "", 0, "", "", 0, "",
                                   "", 0, " ", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('work'), Gender('female'), Person_type('business'), Season("summer"), piece_name("Trousers"),
              piece_color("gray")), salience=1)
    def clothes389(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "black", "Kandra", 6,
                                   "dark", "Coat", 0, "", "", 8, "black", "carafe", 0, "", "", 0, "", "", 0, "", "", 0,
                                   " ", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='white'),
              Occasion('work'), Gender('male'), Person_type('business'), Season("summer"), piece_name("Trousers"),
              piece_color("black")), salience=1)
    def clothes390(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "black", "Kandra", 6,
                                   "gray", "Coat", 0, "", "", 8, "vinous", "carafe", 0, "", "", 0, "", "", 0, "", "", 0,
                                   " ", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('work'), Gender('female'), Person_type('business'), Season("summer"), piece_name("Shirt"),
              piece_color("white")), salience=1)
    def clothes3991(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 4, "darkblue", "skirt", 5, "beige", "Kandra", 6,
                                   "beige", "Coat", 0, "", "", 8, "beige", "carafe", 0, "", "", 0, "", "", 0, "", "", 0,
                                   "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('work'), Gender('female'), Person_type('business'), Season("summer"), piece_name("Shirt"),
              piece_color("white")), salience=1)
    def clothes391(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 4, "black", "skirt", 5, "black", "Kandra", 6,
                                   "black", "Coat", 0, "", "", 8, "vinous", "carafe", 0, "", "", 0, "", "", 0, "", "",
                                   0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='dark'),
              Occasion('work'), Gender('female'), Person_type('business'), Season("summer"), piece_name("Shirt"),
              piece_color("white")), salience=1)
    def clothes392(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 4, "gray", "skirt", 5, "black", "Kandra", 6, "gray",
                                   "Coat", 0, "", "", 8, "black", "carafe", 0, "", "", 0, "", "", 0, "", "", 0, " ", "",
                                   0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='white'),
              Occasion('work'), Gender('female'), Person_type('business'), Season("winter"), piece_name("Shirt"),
              piece_color("white")), salience=1)
    def clothes393(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 4, "darkblue", "skirt", 5, "darkblue", "Kandra", 6,
                                   "darkblue", "Coat", 0, "", "", 8, "darkblue", "carafe", 9, "darkblue", "Jacket", 0,
                                   "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('work'), Gender('female'), Person_type('business'), Season("winter"), piece_name("Shirt"),
              piece_color("white")), salience=1)
    def clothes394(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 4, "black", "skirt", 5, "black", "Kandra", 6,
                                   "black", "Coat", 0, "", "", 8, "vinous", "carafe", 9, "black", "Jacket", 0, "", "",
                                   0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='dark'),
              Occasion('work'), Gender('female'), Person_type('business'), Season("winter"), piece_name("Shirt"),
              piece_color("white")), salience=1)
    def clothes395(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 4, "gray", "skirt", 5, "black", "Kandra", 6, "gray",
                                   "Coat", 0, "", "", 8, "black", "carafe", 9, "black", "Jacket", 0, "", "", 0, "", "",
                                   0, " ", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='white'),
              Occasion('work'), Gender('male'), Person_type('business'), Season("summer"), piece_name("Trousers"),
              piece_color("darkblue")), salience=1)
    def clothes396(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "brown", "Kandra", 6,
                                   "darkblue", "Coat", 0, "", "", 8, "darkblue", "carafe", 0, "", "", 0, "", "", 0, "",
                                   "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('work'), Gender('male'), Person_type('business'), Season("summer"), piece_name("Trousers"),
              piece_color("black")), salience=1)
    def clothes397(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "black", "Kandra", 6,
                                   "black", "Coat", 0, "", "", 8, "vinous", "carafe", 0, "", "", 0, "", "", 0, "", "",
                                   0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='dark'),
              Occasion('work'), Gender('male'), Person_type('business'), Season("summer"), piece_name("Trousers"),
              piece_color("gray")), salience=1)
    def clothes398(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "black", "Kandra", 6,
                                   "gray", "Coat", 0, "", "", 8, "black", "carafe", 0, "", "", 0, "", "", 0, "", "", 0,
                                   "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='white'),
              Occasion('work'), Gender('male'), Person_type('business'), Season("summer"), piece_name("Shirt"),
              piece_color("white")), salience=1)
    def clothes399(self):
        self.myclothes = Myclothes(1, "darkblue", "Trousers", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "brown",
                                   "Kandra", 6, "darkblue", "Coat", 0, "", "", 8, "darkblue", "carafe", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('work'), Gender('male'), Person_type('business'), Season("summer"), piece_name("Shirt"),
              piece_color("white")), salience=1)
    def clothes340(self):
        self.myclothes = Myclothes(1, "black", "Trousers", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "black",
                                   "Kandra", 6, "black", "Coat", 0, "", "", 8, "vinous", "carafe", 0, "", "", 0, "", "",
                                   0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='dark'),
              Occasion('work'), Gender('male'), Person_type('business'), Season("summer"), piece_name("Shirt"),
              piece_color("white")), salience=1)
    def clothes341(self):
        self.myclothes = Myclothes(1, "gray", "Trousers", 0, "", "", 0, "", "", 0, "", "", 5, "black", "Kandra", 6,
                                   "gray", "Coat", 0, "", "", 8, "black", "carafe", 0, "", "", 0, "", "", 0, "", "", 0,
                                   "", "", 0, "", "")
        self.result.append(self.myclothes)

    #         //////////

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='white'),
              Occasion('work'), Gender('female'), Person_type('business'), Season("summer"), piece_name("Shirt"),
              piece_color("white")), salience=1)
    def clothes342(self):
        self.myclothes = Myclothes(1, "darkblue", "Trousers", 0, "", "", 0, "", "", 0, "", "", 5, "darkblue", "Kandra",
                                   6, "darkblue", "Coat", 0, "", "", 8, "darkblue", "carafe", 0, "", "", 0, "", "", 0,
                                   "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('work'), Gender('female'), Person_type('business'), Season("summer"), piece_name("Shirt"),
              piece_color("white")), salience=1)
    def clothes343(self):
        self.myclothes = Myclothes(1, "black", "Trousers", 0, "", "", 0, "", "", 0, "", "", 5, "black", "Kandra", 6,
                                   "black", "Coat", 0, "", "", 8, "vinous", "carafe", 0, "", "", 0, "", "", 0, "", "",
                                   0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='dark'),
              Occasion('work'), Gender('female'), Person_type('business'), Season("summer"), piece_name("Shirt"),
              piece_color("white")), salience=1)
    def clothes344(self):
        self.myclothes = Myclothes(1, "gray", "Trousers", 0, "", "", 0, "", "", 0, "", "", 5, "black", "Kandra", 6,
                                   "gray", "Coat", 0, "", "", 8, "black", "carafe", 0, "", "", 0, "", "", 0, "", "", 0,
                                   " ", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='white'),
              Occasion('work'), Gender('female'), Person_type('business'), Season("summer"), piece_name("Trousers"),
              piece_color("darkblue")), salience=1)
    def clothes345(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 0, "", "", 5, "darkblue", "Kandra", 6, "darkblue",
                                   "Coat", 0, "", "", 8, "darkblue", "carafe", 0, "", "", 0, "", "", 0, "", "", 0, "",
                                   "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('work'), Gender('female'), Person_type('business'), Season("summer"), piece_name("Trousers"),
              piece_color("black")), salience=1)
    def clothes346(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 0, "", "", 5, "black", "Kandra", 6, "black", "Coat",
                                   0, "", "", 8, "vinous", "carafe", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "",
                                   "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='dark'),
              Occasion('work'), Gender('female'), Person_type('business'), Season("summer"), piece_name("Trousers"),
              piece_color("gray")), salience=1)
    def clothes347(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 0, "", "", 5, "black", "Kandra", 6, "gray", "Coat",
                                   0, "", "", 8, "black", "carafe", 0, "", "", 0, "", "", 0, "", "", 0, " ", "", 0, "",
                                   "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='white'),
              Occasion('work'), Gender('female'), Person_type('business'), Season("winter"), piece_name("Jacket"),
              piece_color("darkblue")), salience=1)
    def clothes348(self):
        self.myclothes = Myclothes(1, "darkblue", "Trousers", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "darkblue",
                                   "Kandra", 6, "darkblue", "Coat", 0, "", "", 8, "darkblue", "carafe", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('work'), Gender('female'), Person_type('business'), Season("winter"), piece_name("Jacket"),
              piece_color("black")), salience=1)
    def clothes349(self):
        self.myclothes = Myclothes(1, "black", "Trousers", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "black",
                                   "Kandra", 6, "black", "Coat", 0, "", "", 8, "vinous", "carafe", 0, "", "", 0, "", "",
                                   0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='dark'),
              Occasion('work'), Gender('female'), Person_type('business'), Season("winter"), piece_name("Jacket"),
              piece_color("black")), salience=1)
    def clothes350(self):
        self.myclothes = Myclothes(1, "gray", "Trousers", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "black",
                                   "Kandra", 6, "gray", "Coat", 0, "", "", 8, "black", "carafe", 0, "", "", 0, "", "",
                                   0, "", "", 0, " ", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='white'),
              Occasion('work'), Gender('female'), Person_type('business'), Season("winter"), piece_name("Trousers"),
              piece_color("darkblue")), salience=1)
    def clothes351(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "darkblue", "Kandra", 6,
                                   "darkblue", "Coat", 0, "", "", 8, "darkblue", "carafe", 9, "darkblue", "Jacket", 0,
                                   "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('work'), Gender('female'), Person_type('business'), Season("winter"), piece_name("Trousers"),
              piece_color("black")), salience=1)
    def clothes352(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "black", "Kandra", 6,
                                   "black", "Coat", 0, "", "", 8, "vinous", "carafe", 9, "black", "Jacket", 0, "", "",
                                   0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='dark'),
              Occasion('work'), Gender('female'), Person_type('business'), Season("winter"), piece_name("Trousers"),
              piece_color("gray")), salience=1)
    def clothes353(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "black", "Kandra", 6,
                                   "gray", "Coat", 0, "", "", 8, "black", "carafe", 9, "black", "Jacket", 0, "", "", 0,
                                   "", "", 0, " ", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='white'),
              Occasion('work'), Gender('male'), Person_type('officer'), Season("summer"), piece_name("Trousers"),
              piece_color("darkblue")), salience=1)
    def clothes354(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "brown", "shose", 0, "", "",
                                   0, "", "", 0, "", "", 0, "", "", 0, "", "", 11, "brown", "waistband", 0, "", "", 0,
                                   "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='white'),
              Occasion('work'), Gender('male'), Person_type('officer'), Season("summer"), piece_name("Shirt"),
              piece_color("white")), salience=1)
    def clothes355(self):
        self.myclothes = Myclothes(1, "darkblue", "Trousers", 0, "", "", 0, "", "", 0, "", "", 5, "brown", "shose", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 11, "brown", "waistband", 0, "",
                                   "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='dark'),
              Occasion('work'), Gender('male'), Person_type('officer'), Season("summer"), piece_name("Shirt"),
              piece_color("white")), salience=1)
    def clothes356(self):
        self.myclothes = Myclothes(1, "gray", "Trousers", 0, "", "", 0, "", "", 0, "", "", 5, "brown", "shose", 0, "",
                                   "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 11, "brown", "waistband", 0, "", "",
                                   0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('work'), Gender('male'), Person_type('officer'), Season("summer"), piece_name("Shirt"),
              piece_color("white")), salience=1)
    def clothes357(self):
        self.myclothes = Myclothes(1, "black", "Trousers", 0, "", "", 0, "", "", 0, "", "", 5, "brown", "shose", 0, "",
                                   "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 11, "black", "waistband", 0, "", "",
                                   0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('work'), Gender('male'), Person_type('officer'), Season("summer"), piece_name("Trousers"),
              piece_color("black")), salience=1)
    def clothes358(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "brown", "shose", 0, "", "",
                                   0, "", "", 0, "", "", 0, "", "", 0, "", "", 11, "black", "waistband", 0, "", "", 0,
                                   "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='dark'),
              Occasion('work'), Gender('male'), Person_type('officer'), Season("summer"), piece_name("Trousers"),
              piece_color("gray")), salience=1)
    def clothes359(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "brown", "shose", 0, "", "",
                                   0, "", "", 0, "", "", 0, "", "", 0, "", "", 11, "brown", "waistband", 0, "", "", 0,
                                   "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='white'),
              Occasion('work'), Gender('male'), Person_type('officer'), Season("summer"), piece_name("Trousers"),
              piece_color("black")), salience=1)
    def clothes360(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "brown", "shose", 0, "", "",
                                   0, "", "", 0, "", "", 0, "", "", 0, "", "", 11, "brown", "waistband", 0, "", "", 0,
                                   "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('work'), Gender('male'), Person_type('officer'), Season("summer"), piece_name("Trousers"),
              piece_color("gray")), salience=1)
    def clothes361(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "brown", "shose", 0, "", "",
                                   0, "", "", 0, "", "", 0, "", "", 0, "", "", 11, "black", "waistband", 0, "", "", 0,
                                   "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='dark'),
              Occasion('work'), Gender('male'), Person_type('officer'), Season("summer"), piece_name("Trousers"),
              piece_color("darkblue")), salience=1)
    def clothes362(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "brown", "shose", 0, "", "",
                                   0, "", "", 0, "", "", 0, "", "", 0, "", "", 11, "brown", "waistband", 0, "", "", 0,
                                   "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='white'),
              Occasion('work'), Gender('male'), Person_type('officer'), Season("summer"), piece_name("Trousers"),
              piece_color("gray")), salience=1)
    def clothes363(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "brown", "shose", 0, "", "",
                                   0, "", "", 0, "", "", 0, "", "", 0, "", "", 11, "brown", "waistband", 0, "", "", 0,
                                   "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('work'), Gender('male'), Person_type('officer'), Season("summer"), piece_name("Trousers"),
              piece_color("darkblue")), salience=1)
    def clothes364(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "brown", "shose", 0, "", "",
                                   0, "", "", 0, "", "", 0, "", "", 0, "", "", 11, "black", "waistband", 0, "", "", 0,
                                   "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='dark'),
              Occasion('work'), Gender('male'), Person_type('officer'), Season("summer"), piece_name("Trousers"),
              piece_color("black")), salience=1)
    def clothes365(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "brown", "shose", 0, "", "",
                                   0, "", "", 0, "", "", 0, "", "", 0, "", "", 11, "brown", "waistband", 0, "", "", 0,
                                   "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='white'),
              Occasion('work'), Gender('female'), Person_type('officer'), Season("summer"), piece_name("Trousers"),
              piece_color("darkblue")), salience=1)
    def clothes366(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "beige ", "Kandra", 0, "",
                                   "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 11, "beige", "waistband", 0, "", "",
                                   0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='white'),
              Occasion('work'), Gender('female'), Person_type('officer'), Season("summer"), piece_name("Shirt"),
              piece_color("white")), salience=1)
    def clothes367(self):
        self.myclothes = Myclothes(1, "darkblue", "Trousers", 0, "", "", 0, "", "", 0, "", "", 5, "beige", "Kandra", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 11, "beige", "waistband", 0, "",
                                   "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='dark'),
              Occasion('work'), Gender('female'), Person_type('officer'), Season("summer"), piece_name("Shirt"),
              piece_color("white")), salience=1)
    def clothes368(self):
        self.myclothes = Myclothes(1, "gray", "Trousers", 0, "", "", 0, "", "", 0, "", "", 5, "beige ", "Kandra", 0, "",
                                   "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 11, "beige", "waistband", 0, "", "",
                                   0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('work'), Gender('female'), Person_type('officer'), Season("summer"), piece_name("Shirt"),
              piece_color("white")), salience=1)
    def clothes369(self):
        self.myclothes = Myclothes(1, "black", "Trousers", 0, "", "", 0, "", "", 0, "", "", 5, "beige ", "Kandra", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 11, "beige", "waistband", 0, "",
                                   "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('work'), Gender('female'), Person_type('officer'), Season("summer"), piece_name("Trousers"),
              piece_color("black")), salience=1)
    def clothes370(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "vinous", "Kandra", 0, "",
                                   "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 11, "vinous", "waistband", 0, "", "",
                                   0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='dark'),
              Occasion('work'), Gender('female'), Person_type('officer'), Season("summer"), piece_name("Trousers"),
              piece_color("gray")), salience=1)
    def clothes371(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "black", "Kandra", 0, "",
                                   "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 11, "black", "waistband",
                                   0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='white'),
              Occasion('work'), Gender('female'), Person_type('officer'), Season("summer"), piece_name("Trousers"),
              piece_color("black")), salience=1)
    def clothes372(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "beige ", "Kandra", 0, "",
                                   "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 11, "beige", "waistband", 0, "", "",
                                   0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('work'), Gender('female'), Person_type('officer'), Season("summer"), piece_name("Trousers"),
              piece_color("gray")), salience=1)
    def clothes373(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "vinous", "Kandra", 0, "",
                                   "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 11, "vinous", "waistband", 0, "", "",
                                   0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='dark'),
              Occasion('work'), Gender('female'), Person_type('officer'), Season("summer"), piece_name("Trousers"),
              piece_color("black")), salience=1)
    def clothes374(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "black", "Kandra", 0, "",
                                   "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 11, "black", "waistband",
                                   0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='white'),
              Occasion('work'), Gender('female'), Person_type('officer'), Season("summer"), piece_name("Trousers"),
              piece_color("darkblue")), salience=1)
    def clothes375(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "darkblue", "Kandra", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('work'), Gender('female'), Person_type('officer'), Season("winter"), piece_name("Skirt"),
              piece_color("black")), salience=1)
    def clothes376(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "black", "Kandra", 0, "",
                                   "", 0, "", "", 0, "", "", 9, "black", "Jacket", 0, "", "", 0, "", "", 0, "", "", 0,
                                   "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('work'), Gender('female'), Person_type('officer'), Season("winter"), piece_name("Shirt"),
              piece_color("white")), salience=1)
    def clothes377(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 4, "black", "Skirt", 5, "black", "Kandra", 0, "",
                                   "", 0, "", "", 0, "", "", 9, "black", "Jacket", 0, "", "", 0, "", "", 0, "", "", 0,
                                   "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('work'), Gender('female'), Person_type('officer'), Season("winter"), piece_name("Shirt"),
              piece_color("white")), salience=1)
    def clothes378(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 4, "black", "Skirt", 5, "black", "Kandra", 0, "",
                                   "", 0, "", "", 0, "", "", 9, "black", "Jacket", 0, "", "", 0, "", "", 0, "", "", 0,
                                   "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('work'), Gender('female'), Person_type('officer'), Season("winter"), piece_name("Jacket"),
              piece_color("black")), salience=1)
    def clothes379(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 4, "black", "Skirt", 5, "black",
                                   "Kandra", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "",
                                   "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='dark'),
              Occasion('work'), Gender('female'), Person_type('officer'), Season("winter"), piece_name("Jacket"),
              piece_color("black")), salience=1)
    def clothes380(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 4, "black", "Skirt", 5, "black",
                                   "Kandra", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "",
                                   "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='white'),
              Occasion('work'), Gender('female'), Person_type('officer'), Season("winter"), piece_name("Jacket"),
              piece_color("darkblue")), salience=1)
    def clothes381(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 4, "gray", "Skirt", 5, "gray", "Kandra",
                                   0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "",
                                   "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='white'),
              Occasion('work'), Gender('female'), Person_type('officer'), Season("winter"), piece_name("Jacket"),
              piece_color("gray")), salience=1)
    def clothes382(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 4, "black", "Skirt", 5, "black",
                                   "Kandra", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "",
                                   "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='dark'),
              Occasion('work'), Gender('female'), Person_type('officer'), Season("summer"), piece_name("Skirt"),
              piece_color("darkblue")), salience=1)
    def clothes383(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "black", "Kandra", 0, "",
                                   "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='dark'),
              Occasion('work'), Gender('female'), Person_type('officer'), Season("winter"), piece_name("Skirt"),
              piece_color("darkblue")), salience=1)
    def clothes384(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "black", "Kandra", 0, "",
                                   "", 0, "", "", 0, "", "", 9, "black", "Jacket", 0, "", "", 0, "", "", 0, "", "", 0,
                                   "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('work'), Gender('female'), Person_type('officer'), Season("winter"), piece_name("Skirt"),
              piece_color("black")), salience=1)
    def clothes385(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "black", "Kandra", 0, "",
                                   "", 0, "", "", 0, "", "", 9, "black", "Jacket", 0, "", "", 0, "", "", 0, "", "", 0,
                                   "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='dark'),
              Occasion('work'), Gender('female'), Person_type('officer'), Season("summer"), piece_name("Skirt"),
              piece_color("gray")), salience=1)
    def clothes386(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "black", "Kandra", 0, "",
                                   "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='dark'),
              Occasion('work'), Gender('female'), Person_type('officer'), Season("winter"), piece_name("Skirt"),
              piece_color("gray")), salience=1)
    def clothes387(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "black", "Kandra", 0, "",
                                   "", 0, "", "", 0, "", "", 9, "black", "Jacket", 0, "", "", 0, "", "", 0, "", "", 0,
                                   "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('work'), Gender('female'), Person_type('officer'), Season("winter"), piece_name("Skirt"),
              piece_color("darkblue")), salience=1)
    def clothes388(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "black", "Kandra", 0, "",
                                   "", 0, "", "", 0, "", "", 9, "black", "Jacket", 0, "", "", 0, "", "", 0, "", "", 0,
                                   "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='dark'),
              Occasion('work'), Gender('female'), Person_type('officer'), Season("summer"), piece_name("Skirt"),
              piece_color("black")), salience=1)
    def clothes389(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "black", "Kandra", 0, "",
                                   "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 20) & P(lambda value: value <= 60)), SkinColor(color='dark'),
              Occasion('work'), Gender('female'), Person_type('officer'), Season("winter"), piece_name("Skirt"),
              piece_color("black")), salience=1)
    def clothes390(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "black", "Kandra", 0, "",
                                   "", 0, "", "", 0, "", "", 9, "black", "Jacket", 0, "", "", 0, "", "", 0, "", "", 0,
                                   "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='hanatawi'),
              Occasion('wadding'), Gender('male'), Person_type('relatives'), Season("summer"), piece_name("T_Shirt"),
              piece_color("brown")), salience=1)
    def clothes391(self):
        self.myclothes = Myclothes(1, "black", "jeans", 0, "", "", 0, "", "", 0, "", "", 5, "black", "shose", 0, "",
                                   "", 0, "", "", 8, "black", "carafe", 0, "", "", 0, "", "", 11, "black", "waistband",
                                   0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='dark'),
              Occasion('wadding'), Gender('male'), Person_type('relatives'), Season("summer"), piece_name("T_Shirt"),
              piece_color("beige")), salience=1)
    def clothes392(self):
        self.myclothes = Myclothes(1, " brown", "Trousers", 0, "", "", 0, "", "", 0, " ", "", 5, "brown", "shose", 0,
                                   "", "", 0, "", "", 8, "brown", "carafe", 0, "", "", 0, "", "", 11, "brown",
                                   "waistband", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('male'), Person_type('relatives'), Season("summer"), piece_name("Shirt"),
              piece_color("cyan")), salience=1)
    def clothes393(self):
        self.myclothes = Myclothes(1, "darkblue", "jeans", 0, "", "", 0, "", "", 0, "", "", 5, "black", "shose", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 11, "black", "waistband", 0, "",
                                   "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('male'), Person_type('relatives'), Season("summer"), piece_name("Shirt"),
              piece_color("oil")), salience=1)
    def clothes394(self):
        self.myclothes = Myclothes(1, "black", "Trousers", 0, "", "", 0, "", "", 0, " ", "", 5, "black", "shose", 0,
                                   "", "", 0, "", "", 8, "black", "carafe", 0, "", "", 0, "", "", 11, "black",
                                   "waistband", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('male'), Person_type('relatives'), Season("summer"), piece_name("T_Shirt"),
              piece_color("beige")), salience=1)
    def clothes395(self):
        self.myclothes = Myclothes(1, "darkblue", "Trousers", 0, "", "", 0, "", "", 0, " ", "", 5, "brown", "shose",
                                   0, "", "", 0, "", "", 8, "black", "carafe", 0, "", "", 0, "", "", 11, "black",
                                   "waistband", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='hanatawi'),
              Occasion('wadding'), Gender('male'), Person_type('relatives'), Season("summer"), piece_name("Trousers"),
              piece_color("black")), salience=1)
    def clothes396(self):
        self.myclothes = Myclothes(0, "", "", 2, "brown", "T_Shirt", 0, "", "", 0, " ", "", 5, "black", "shose", 0,
                                   "", "", 0, "", "", 8, "black", "carafe", 0, "", "", 0, "", "", 11, "black",
                                   "waistband", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='dark'),
              Occasion('wadding'), Gender('male'), Person_type('relatives'), Season("summer"), piece_name("Trousers"),
              piece_color("brown")), salience=1)
    def clothes397(self):
        self.myclothes = Myclothes(0, "", "", 2, "beige", "T_Shirt", 0, "", "", 0, "", "", 5, "brown", "shose", 0,
                                   "", "", 0, "", "", 8, "brown", "carafe", 0, "", "", 0, "", "", 11, "brown",
                                   "waistband", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('male'), Person_type('relatives'), Season("summer"), piece_name("Trousers"),
              piece_color("darkblue")), salience=1)
    def clothes398(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "cyan", "Shirt", 0, "", "", 5, "black ", "shose", 0, "",
                                   "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 11, "black", "waistband", 0, "", "",
                                   0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('male'), Person_type('relatives'), Season("summer"), piece_name("Trousers"),
              piece_color("black")), salience=1)
    def clothes399(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "oil", "Shirt", 0, "", "", 5, "black", "shose", 0, "",
                                   "", 0, "", "", 8, "black", "carafe", 0, "", "", 0, "", "", 11, "black", "waistband",
                                   0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('male'), Person_type('relatives'), Season("summer"), piece_name("Trousers"),
              piece_color("darkblue")), salience=1)
    def clothes400(self):
        self.myclothes = Myclothes(1, "", "", 2, "beige", "T_Shirt", 0, "", "", 0, "", "", 5, "brown", "shose", 0,
                                   "", "", 0, "", "", 8, "black", "carafe", 0, "", "", 0, "", "", 11, "black",
                                   "waistband", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('female'), Person_type('relatives'), Season("summer"), piece_name("dress"),
              piece_color("black")), salience=1)
    def clothes401(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 0, "", "", 5, "black", "Kandra", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('female'), Person_type('relatives'), Season("summer"), piece_name("dress"),
              piece_color("vinous")), salience=1)
    def clothes402(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 0, "", "", 5, "black", "Kandra", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('female'), Person_type('relatives'), Season("summer"), piece_name("dress"),
              piece_color("pink")), salience=1)
    def clothes403(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 0, "", "", 5, "black", "Kandra", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('female'), Person_type('relatives'), Season("summer"), piece_name("T_Shirt"),
              piece_color("pink")), salience=1)
    def clothes404(self):
        self.myclothes = Myclothes(1, "cyan", "jeans", 0, "", "", 0, "", "", 0, "", "", 5, "white", "Kandra ", 0, "",
                                   "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 11, "black", "waistband", 0, "", "",
                                   0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('female'), Person_type('relatives'), Season("summer"), piece_name("T_Shirt"),
              piece_color("yellow")), salience=1)
    def clothes405(self):
        self.myclothes = Myclothes(1, "black", "jeans", 0, "", "", 0, "", "", 0, "", "", 5, "black", "Kandra", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 11, "black", "waistband", 0, "",
                                   "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='dark'),
              Occasion('wadding'), Gender('female'), Person_type('relatives'), Season("summer"), piece_name("dress"),
              piece_color("blue")), salience=1)
    def clothes406(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 0, "", "", 5, "silver", "Kandra", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('female'), Person_type('relatives'), Season("summer"), piece_name("Trousers"),
              piece_color("cyan")), salience=1)
    def clothes407(self):
        self.myclothes = Myclothes(0, "", "", 2, " pink", "T_Shirt", 0, "", "", 0, "", "", 5, "white", "Kandra", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 11, "black", "waistband", 0, "",
                                   "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('female'), Person_type('relatives'), Season("summer"), piece_name("Trousers"),
              piece_color("black")), salience=1)
    def clothes408(self):
        self.myclothes = Myclothes(0, "", "", 2, "yellow", "T_Shirt", 0, "", "", 0, "", "", 5, "black", "Kandra", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 11, "black", "waistband", 0, "",
                                   "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='dark'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer"), piece_name("dress"),
              piece_color("gray")), salience=1)
    def clothes409(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 0, "", "", 5, "black", "Kandra", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='hanatawi'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer"), piece_name("dress"),
              piece_color("pink")), salience=1)
    def clothes410(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 0, " ", "", 5, "white", "Kandra", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", " ", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer"), piece_name("dress"),
              piece_color("cyan")), salience=1)
    def clothes411(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 0, "", "", 5, "silver", "Kandra", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer"), piece_name("dress"),
              piece_color("red")), salience=1)
    def clothes412(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 0, "", "", 5, "gold", "Kandra", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='dark'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer"), piece_name("dress"),
              piece_color("gold")), salience=1)
    def clothes413(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 0, "", "", 5, "black", "Kandra", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='hanatawi'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer"), piece_name("dress"),
              piece_color("silver")), salience=1)
    def clothes414(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 0, "", "", 5, "black", "Kandra", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='dark'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer"), piece_name("dress"),
              piece_color("black")), salience=1)
    def clothes415(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 0, "", "", 5, "vinous", "Kandra", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer"), piece_name("dress"),
              piece_color("black")), salience=1)
    def clothes416(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 0, "", "", 5, "vinous", "Kandra", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "", 0, " ", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer"), piece_name("dress"),
              piece_color("pink")), salience=1)
    def clothes417(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 0, "", "", 5, "black", "Kandra", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer"), piece_name("dress"),
              piece_color("cyan")), salience=1)
    def clothes418(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 0, "", "", 5, "gold", "Kandra", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer"), piece_name("dress"),
              piece_color("blue")), salience=1)
    def clothes419(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 0, "", "", 5, "black", "Kandra", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='hanatawi'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer"), piece_name("dress"),
              piece_color("pink")), salience=1)
    def clothes420(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 0, "", "", 5, "black", "Kandra", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='hanatawi'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer"), piece_name("dress"),
              piece_color("black")), salience=1)
    def clothes421(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 0, "", "", 5, "black", "Kandra", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='dark'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer"), piece_name("Shirt"),
              piece_color("white")), salience=1)
    def clothes422(self):
        self.myclothes = Myclothes(1, "black", "Trousers", 0, "", "", 0, "", "", 0, "", "", 5, "black", "Kandra", 6,
                                   "vinous", "Coat", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 11, "black",
                                   "waistband", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='dark'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer"), piece_name("Trousers"),
              piece_color("black")), salience=1)
    def clothes423(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "black", "Kandra", 6,
                                   "vinous", "Coat", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 11, "black",
                                   "waistband", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='dark'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer"), piece_name("T_Shirt"),
              piece_color("yellow")), salience=1)
    def clothes424(self):
        self.myclothes = Myclothes(1, "cyan", "Trousers", 0, "", "", 0, "", "", 0, "", "", 5, "black", "Kandra", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='dark'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer"), piece_name("Trousers"),
              piece_color("cyan")), salience=1)
    def clothes425(self):
        self.myclothes = Myclothes(0, "", "", 2, "yellow", "T_Shirt", 0, "", "", 0, "", "", 5, "black", "Kandra", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='dark'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer"), piece_name("T_Shirt"),
              piece_color("pink")), salience=1)
    def clothes426(self):
        self.myclothes = Myclothes(1, "black", "Trousers", 0, "", "", 0, "", "", 0, "", "", 5, "black", "Kandra", 0,
                                   "", "", 0, "", "", 0, " ", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer"), piece_name("T_Shirt"),
              piece_color("yellow")), salience=1)
    def clothes427(self):
        self.myclothes = Myclothes(1, "cyan", "Trousers", 0, "", "", 0, "", "", 0, " ", "", 5, "black", "Kandra", 0,
                                   "", "", 0, "", "", 0, " ", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer"), piece_name("Trousers"),
              piece_color("cyan")), salience=1)
    def clothes428(self):
        self.myclothes = Myclothes(0, "", "", 2, "yellow", "T_Shirt", 0, "", "", 0, "", "", 5, "black", "Kandra", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer"), piece_name("T_Shirt"),
              piece_color("red")), salience=1)
    def clothes429(self):
        self.myclothes = Myclothes(1, "black", "Trousers", 0, "", "", 0, "", "", 0, "", "", 5, "black", "Kandra", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='dark'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer"), piece_name("Trousers"),
              piece_color("black")), salience=1)
    def clothes430(self):
        self.myclothes = Myclothes(0, "", "", 2, "pink", "T_Shirt", 0, "", "", 0, "", "", 5, "black", "Kandra", 0, "",
                                   "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='dark'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer"), piece_name("Shirt"),
              piece_color("red")), salience=1)
    def clothes431(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 4, "white", "shortSkirt", 5, "white", "Kandra",
                                   6, "black", "Coat", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "",
                                   "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='dark'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer"), piece_name("Skirt"),
              piece_color("white")), salience=1)
    def clothes432(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "pink", "Shirt", 0, "", "", 5, "white", "Kandra", 6,
                                   "black", "Coat", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "",
                                   0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer"), piece_name("Skirt"),
              piece_color("white")), salience=1)
    def clothes433(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "red", "Shirt", 0, " ", "", 5, "white", "Kandra", 6,
                                   "black", "Coat", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "",
                                   0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='hanatawi'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer"), piece_name("Skirt"),
              piece_color("white")), salience=1)
    def clothes434(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "pink", "Shirt", 0, "", "", 5, "white", "Kandra", 6,
                                   "black", "Coat", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "",
                                   0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='dark'),
              Occasion('wadding'), Gender('female'), Person_type('relatives'), Season("summer"), piece_name("dress"),
              piece_color("beige")), salience=1)
    def clothes435(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 0, "", "", 5, "black", "Kandra", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='hanatawi'),
              Occasion('wadding'), Gender('female'), Person_type('relatives'), Season("summer"), piece_name("dress"),
              piece_color("beige")), salience=1)
    def clothes436(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 0, "", "", 5, "black", "Kandra", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='dark'),
              Occasion('wadding'), Gender('female'), Person_type('relatives'), Season("summer"), piece_name("dress"),
              piece_color("gray")), salience=1)
    def clothes437(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 0, " ", "", 5, "black", "Kandra", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "", 0, " ", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='dark'),
              Occasion('wadding'), Gender('female'), Person_type('relatives'), Season("summer"), piece_name("dress"),
              piece_color("black")), salience=1)
    def clothes438(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 0, "", "", 5, "vinous", "Kandra", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='dark'),
              Occasion('wadding'), Gender('female'), Person_type('relatives'), Season("summer"), piece_name("T_Shirt"),
              piece_color("black")), salience=1)
    def clothes439(self):
        self.myclothes = Myclothes(1, "cyan", "jeans", 0, "", "", 0, "", "", 0, "", "", 5, "white", "shose", 0, "",
                                   "", 0, "", "", 0, " ", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='dark'),
              Occasion('wadding'), Gender('female'), Person_type('relatives'), Season("summer"), piece_name("T_Shirt"),
              piece_color(" yellow")), salience=1)
    def clothes440(self):
        self.myclothes = Myclothes(1, "darkblue", "jeans", 0, "", "", 0, "", "", 0, " ", "", 5, "white", "shose", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='dark'),
              Occasion('wadding'), Gender('female'), Person_type('relatives'), Season("summer"), piece_name("T_Shirt"),
              piece_color("pink")), salience=1)
    def clothes441(self):
        self.myclothes = Myclothes(1, "cyan", "jeans", 0, "", "", 0, "", "", 0, "", "", 5, "white", "shose", 0, "",
                                   "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='dark'),
              Occasion('wadding'), Gender('female'), Person_type('relatives'), Season("summer"), piece_name("Trousers"),
              piece_color("cyan")), salience=1)
    def clothes442(self):
        self.myclothes = Myclothes(0, "", "", 2, "black", "T_Shirt", 0, "", "", 0, "", "", 5, "white", "shose", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='dark'),
              Occasion('wadding'), Gender('female'), Person_type('relatives'), Season("summer"), piece_name("Trousers"),
              piece_color("darkblue")), salience=1)
    def clothes443(self):
        self.myclothes = Myclothes(0, "", "", 2, "yellow", "T_Shirt", 0, "", "", 0, "", "", 5, "white", "shose", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='dark'),
              Occasion('wadding'), Gender('female'), Person_type('relatives'), Season("summer"), piece_name("Trousers"),
              piece_color("cyan")), salience=1)
    def clothes444(self):
        self.myclothes = Myclothes(0, "", "", 2, "pink", "T_Shirt", 0, "", "", 0, "", "", 5, "white", "shose", 0, "",
                                   "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='dark'),
              Occasion('wadding'), Gender('female'), Person_type('relatives'), Season("summer"), piece_name("Trousers"),
              piece_color("cyan")), salience=1)
    def clothes445(self):
        self.myclothes = Myclothes(0, "", "", 2, "brown", "T_Shirt", 0, "", "", 0, "", "", 5, "white", "shose", 0, "",
                                   "", 0, "", "", 0, " ", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='hanatawi'),
              Occasion('wadding'), Gender('female'), Person_type('relatives'), Season("summer"), piece_name("Trousers"),
              piece_color("cyan")), salience=1)
    def clothes446(self):
        self.myclothes = Myclothes(0, "", "", 2, "yellow", "T_Shirt", 0, "", "", 0, "", "", 5, "white", "shose", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='dark'),
              Occasion('wadding'), Gender('female'), Person_type('relatives'), Season("summer"), piece_name("T_Shirt"),
              piece_color("red")), salience=1)
    def clothes447(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 4, "black", "MidSkirt", 5, "white ", "shose", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('female'), Person_type('relatives'), Season("summer"), piece_name("Skirt"),
              piece_color("white")), salience=1)
    def clothes448(self):
        self.myclothes = Myclothes(0, "", "", 2, "green", "T_Shirt", 0, "", "", 0, "", "", 5, "white", "shose", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='hanatawi'),
              Occasion('wadding'), Gender('female'), Person_type('relatives'), Season("summer"), piece_name("dress"),
              piece_color("red")), salience=1)
    def clothes449(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 0, "", "", 5, "gold", "Kandra", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='hanatawi'),
              Occasion('wadding'), Gender('female'), Person_type('relatives'), Season("summer"), piece_name("dress"),
              piece_color("pink")), salience=1)
    def clothes450(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 0, " ", "", 5, "black", "Kandra", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='hanatawi'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer"), piece_name("dress"),
              piece_color("gold")), salience=1)
    def clothes451(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 0, "", "", 5, "gold", "Kandra", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='hanatawi'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer"), piece_name("dress"),
              piece_color("silver")), salience=1)
    def clothes452(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, " ", "", 0, "", "", 5, "black", "Kandra", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='hanatawi'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer"), piece_name("dress"),
              piece_color("pink")), salience=1)
    def clothes453(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 0, "", "", 5, "white", "Sandal", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='hanatawi'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer"), piece_name("dress"),
              piece_color("pink")), salience=1)
    def clothes454(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 0, "", "", 5, "black", "Kandra", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer"), piece_name("dress"),
              piece_color("darkblue")), salience=1)
    def clothes455(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 0, "", "", 5, "pink", "Kandra", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer"), piece_name("dress"),
              piece_color("red")), salience=1)
    def clothes456(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 0, "", "", 5, "black", "Kandra", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer"), piece_name("dress"),
              piece_color("pink")), salience=1)
    def clothes457(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 0, "", "", 5, "silver", "Kandra", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer"), piece_name("dress"),
              piece_color("beige")), salience=1)
    def clothes458(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 0, "", "", 5, "black", "Kandra", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer"), piece_name("dress"),
              piece_color("black")), salience=1)
    def clothes459(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 0, "", "", 5, "silver", "Kandra", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer"), piece_name("T_Shirt"),
              piece_color("pink")), salience=1)
    def clothes460(self):
        self.myclothes = Myclothes(1, "cyan", "jeans", 0, "", "", 0, "", "", 0, "", "", 5, "white", "shose", 0, "",
                                   "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer"), piece_name("T_Shirt"),
              piece_color("cyan")), salience=1)
    def clothes461(self):
        self.myclothes = Myclothes(1, "darkblue", "jeans", 0, "", "", 0, "", "", 0, "", "", 5, "white", "shose", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer"), piece_name("T_Shirt"),
              piece_color("blue")), salience=1)
    def clothes462(self):
        self.myclothes = Myclothes(1, "cyan", "jeans", 0, "", "", 0, "", "", 0, "", "", 5, "white", "shose", 0, "",
                                   "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer"), piece_name("T_Shirt"),
              piece_color("vinous")), salience=1)
    def clothes463(self):
        self.myclothes = Myclothes(1, "cyan", "jeans", 0, "", "", 0, "", "", 0, "", "", 5, "white", "shose", 0, "",
                                   "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer"), piece_name("Trousers"),
              piece_color("black")), salience=1)
    def clothes464(self):
        self.myclothes = Myclothes(0, "", "", 2, "vinous", "T_Shirt", 0, "", "", 0, "", "", 5, "white", "shose", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer"), piece_name("Trousers"),
              piece_color("black")), salience=1)
    def clothes467(self):
        self.myclothes = Myclothes(0, "", "", 2, "cyan", "T_Shirt", 0, "", "", 0, "", "", 5, "white", "shose", 0, "",
                                   "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer"), piece_name("Trousers"),
              piece_color("black")), salience=1)
    def clothes468(self):
        self.myclothes = Myclothes(0, "", "", 2, "red", "T_Shirt", 0, "", "", 0, "", "", 5, "white", "shose", 0, "",
                                   "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer"), piece_name("Trousers"),
              piece_color("black")), salience=1)
    def clothes469(self):
        self.myclothes = Myclothes(0, "", "", 2, "green", "T_Shirt", 0, "", "", 0, "", "", 5, "white", "shose", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer"), piece_name("Trousers"),
              piece_color("cyan")), salience=1)
    def clothes470(self):
        self.myclothes = Myclothes(0, "", "", 2, "blue", "T_Shirt", 0, "", "", 0, " ", "", 5, "white", "shose", 0, "",
                                   "", 0, "", "", 0, " ", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer"), piece_name("Trousers"),
              piece_color("darkblue")), salience=1)
    def clothes471(self):
        self.myclothes = Myclothes(0, "", "", 2, "oil", "T_Shirt", 0, "", "", 0, "", "", 5, "white", "shose", 0, "",
                                   "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer"), piece_name("Trousers"),
              piece_color("darkblue")), salience=1)
    def clothes472(self):
        self.myclothes = Myclothes(0, "", "", 2, "brown", "T_Shirt", 0, "", "", 0, "", "", 5, "white", "shose", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer"), piece_name("Trousers"),
              piece_color("white")), salience=1)
    def clothes473(self):
        self.myclothes = Myclothes(0, "", "", 2, "pink", "T_Shirt", 0, "", "", 0, "", "", 5, "white", "shose", 0, "",
                                   "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer"), piece_name("Trousers"),
              piece_color("white")), salience=1)
    def clothes474(self):
        self.myclothes = Myclothes(0, "", "", 2, "yellow", "T_Shirt", 0, "", "", 0, "", "", 5, "white", "shose", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer"), piece_name("Trousers"),
              piece_color("white")), salience=1)
    def clothes475(self):
        self.myclothes = Myclothes(0, "", "", 2, "black", "T_Shirt", 0, "", "", 0, "", "", 5, "white", "shose", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer"), piece_name("Trousers"),
              piece_color("black")), salience=1)
    def clothes476(self):
        self.myclothes = Myclothes(0, "", "", 2, "white", "T_Shirt", 0, "", "", 0, "", "", 5, "white", "shose", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer"), piece_name("Trousers"),
              piece_color("pink")), salience=1)
    def clothes478(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "black", "Kandra", 0, "",
                                   "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer"), piece_name("dress"),
              piece_color("brown")), salience=1)
    def clothes805(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 0, "", "", 5, "silver", "Kandra", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer"), piece_name("Skirt"),
              piece_color("black")), salience=1)
    def clothes479(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "pink", "Shirt", 4, "", "", 5, "pink", "Kandra", 0, "",
                                   "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer"), piece_name("Skirt"),
              piece_color("black")), salience=1)
    def clothes480(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "silver", "Shirt", 4, "", "", 5, "black", "Kandra", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer"), piece_name("Skirt"),
              piece_color("black")), salience=1)
    def clothes481(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 4, "", "", 5, "black", "Kandra", 0, "",
                                   "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer"), piece_name("Skirt"),
              piece_color("white")), salience=1)
    def clothes482(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "cyan", "Shirt", 0, "", "", 5, "black", "Kandra", 0, "",
                                   "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer"), piece_name("Skirt"),
              piece_color("white")), salience=1)
    def clothes483(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "pink", "Shirt", 0, "", "", 5, "pink", "Kandra", 0, "",
                                   "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer"), piece_name("Skirt"),
              piece_color("white")), salience=1)
    def clothes484(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "green", "Shirt", 0, "", "", 5, "white", "Kandra", 0, "",
                                   "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer"), piece_name("Skirt"),
              piece_color("white")), salience=1)
    def clothes485(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "pink", "Shirt", 0, "", "", 5, "white", "Kandra", 0, "",
                                   "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='hanatawi'),
              Occasion('wadding'), Gender('female'), Person_type('brother'), Season("summer"), piece_name("dress"),
              piece_color("gold")), salience=1)
    def clothes486(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 0, "", "", 5, "black", "Kandra", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='hanatawi'),
              Occasion('wadding'), Gender('female'), Person_type('brother'), Season("summer"), piece_name("dress"),
              piece_color("vinous")), salience=1)
    def clothes487(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 0, "", "", 5, "gold", "Kandra", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "", 0, " ", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='hanatawi'),
              Occasion('wadding'), Gender('female'), Person_type('brother'), Season("summer"), piece_name("dress"),
              piece_color("pink")), salience=1)
    def clothes488(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 0, "", "", 5, "black", "Kandra", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='hanatawi'),
              Occasion('wadding'), Gender('female'), Person_type('brother'), Season("summer"), piece_name("dress"),
              piece_color("silver")), salience=1)
    def clothes489(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 0, "", "", 5, "silver", "Kandra", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='hanatawi'),
              Occasion('wadding'), Gender('female'), Person_type('brother'), Season("summer"), piece_name("dress"),
              piece_color("black")), salience=1)
    def clothes490(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 0, "", "", 5, "vinous", "Kandra", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='hanatawi'),
              Occasion('wadding'), Gender('female'), Person_type('brother'), Season("summer"), piece_name("dress"),
              piece_color("white")), salience=1)
    def clothes491(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 0, "", "", 5, "silver", "Kandra", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='hanatawi'),
              Occasion('wadding'), Gender('female'), Person_type('brother'), Season("summer"), piece_name("dress"),
              piece_color("yellow")), salience=1)
    def clothes492(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 0, "", "", 5, "vinous", "Kandra", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='hanatawi'),
              Occasion('wadding'), Gender('female'), Person_type('brother'), Season("summer"), piece_name("dress"),
              piece_color("blue")), salience=1)
    def clothes493(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 0, " ", "", 5, "vinous", "Kandra", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='hanatawi'),
              Occasion('wadding'), Gender('female'), Person_type('brother'), Season("summer"), piece_name("Trousers"),
              piece_color("black")), salience=1)
    def clothes494(self):
        self.myclothes = Myclothes(0, "", "", 2, "vinous", "T_Shirt", 0, "", "", 0, "", "", 5, "white", "shose", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='hanatawi'),
              Occasion('wadding'), Gender('female'), Person_type('brother'), Season("summer"), piece_name("Trousers"),
              piece_color("white")), salience=1)
    def clothes495(self):
        self.myclothes = Myclothes(0, "", "", 2, "vinous", "T_Shirt", 0, "", "", 0, "", "", 5, "white", "shose", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='hanatawi'),
              Occasion('wadding'), Gender('female'), Person_type('brother'), Season("summer"), piece_name("Trousers"),
              piece_color("black")), salience=1)
    def clothes496(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "black", "Kandra", 0, "",
                                   "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='hanatawi'),
              Occasion('wadding'), Gender('female'), Person_type('brother'), Season("summer"), piece_name("Skirt"),
              piece_color("cyan")), salience=1)
    def clothes497(self):
        self.myclothes = Myclothes(0, "", "", 2, "white", "T_Shirt", 0, "", "", 0, "", "", 5, "white", "shose", 0, "",
                                   "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('female'), Person_type('brother'), Season("summer"), piece_name("dress"),
              piece_color("gold")), salience=1)
    def clothes498(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 0, "", "", 5, "black", "Kandra", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('female'), Person_type('brother'), Season("summer"), piece_name("dress"),
              piece_color("silver")), salience=1)
    def clothes500(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 0, "", "", 5, "black", "Kandra", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('female'), Person_type('brother'), Season("summer"), piece_name("dress"),
              piece_color("red")), salience=1)
    def clothes501(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 0, "", "", 5, "white", "Kandra", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('female'), Person_type('brother'), Season("summer"), piece_name("dress"),
              piece_color("pink")), salience=1)
    def clothes502(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 0, "", "", 5, "black", "Kandra", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "", 10, "vinous", "Mididress", 0, "", "", 0, "", "", 0,
                                   "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('female'), Person_type('brother'), Season("summer"), piece_name("dress"),
              piece_color("beige")), salience=1)
    def clothes503(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 0, "", "", 5, "black", "Kandra", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('female'), Person_type('brother'), Season("summer"), piece_name("dress"),
              piece_color("yellow")), salience=1)
    def clothes504(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 0, "", "", 5, "silver", "Kandra", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('female'), Person_type('brother'), Season("summer"), piece_name("dress"),
              piece_color("pink")), salience=1)
    def clothes505(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 0, "", "", 5, "silver", "Kandra", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('female'), Person_type('brother'), Season("summer"), piece_name("Trousers"),
              piece_color("white")), salience=1)
    def clothes506(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "pink", "Shirt", 0, "", "", 5, "pink", "shose", 0, "",
                                   "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('female'), Person_type('brother'), Season("summer"), piece_name("Trousers"),
              piece_color("black")), salience=1)
    def clothes507(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "pink", "Shirt", 0, "", "", 5, "pink", "shose", 0, "",
                                   "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('female'), Person_type('brother'), Season("summer"), piece_name("Shirt"),
              piece_color("cyan")), salience=1)
    def clothes508(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 4, "gray", "Skirt", 5, "gray", "Kandra", 6,
                                   "white", "Coat", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "",
                                   0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('female'), Person_type('brother'), Season("summer"), piece_name("Skirt"),
              piece_color("pink")), salience=1)
    def clothes509(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "cyan", "Shirt", 0, "", "", 5, "gray", "Kandra", 6,
                                   "white", "Coat", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "",
                                   0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='dark'),
              Occasion('wadding'), Gender('female'), Person_type('brother'), Season("summer"), piece_name("dress"),
              piece_color("gold")), salience=1)
    def clothes510(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 0, "", "", 5, "black", "Kandra", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='dark'),
              Occasion('wadding'), Gender('female'), Person_type('brother'), Season("summer"), piece_name("dress"),
              piece_color("silver")), salience=1)
    def clothes511(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 0, "", "", 5, "black", "Kandra", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='dark'),
              Occasion('wadding'), Gender('female'), Person_type('brother'), Season("summer"), piece_name("dress"),
              piece_color("pink")), salience=1)
    def clothes512(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 0, "", "", 5, "silver", "Kandra", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='dark'),
              Occasion('wadding'), Gender('female'), Person_type('brother'), Season("summer"), piece_name("dress"),
              piece_color("bule")), salience=1)
    def clothes513(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 0, "", "", 5, "gray", "Kandra", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='dark'),
              Occasion('wadding'), Gender('female'), Person_type('brother'), Season("summer"), piece_name("dress"),
              piece_color("vinous")), salience=1)
    def clothes514(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 0, "", "", 5, "silver", "Kandra", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='dark'),
              Occasion('wadding'), Gender('female'), Person_type('brother'), Season("summer"), piece_name("dress"),
              piece_color("gray")), salience=1)
    def clothes515(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 0, "", "", 5, "silver", "Kandra", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='dark'),
              Occasion('wadding'), Gender('female'), Person_type('brother'), Season("summer"), piece_name("dress"),
              piece_color("black")), salience=1)
    def clothes516(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 0, "", "", 5, "silver", "Kandra", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='dark'),
              Occasion('wadding'), Gender('female'), Person_type('brother'), Season("summer"), piece_name("Trousers"),
              piece_color("pink")), salience=1)
    def clothes517(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "pink", "Kandra", 0, "",
                                   "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='dark'),
              Occasion('wadding'), Gender('female'), Person_type('brother'), Season("summer"), piece_name("Trousers"),
              piece_color("green")), salience=1)
    def clothes518(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "black", "Shirt", 0, "", "", 5, "pink", "Kandra", 0, "",
                                   "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='dark'),
              Occasion('wadding'), Gender('female'), Person_type('brother'), Season("summer"), piece_name("Shirt"),
              piece_color("pink")), salience=1)
    def clothes519(self):
        self.myclothes = Myclothes(1, "blue", "Trousers", 0, "", "", 0, "", "", 0, "", "", 5, "black", "Kandra", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='dark'),
              Occasion('wadding'), Gender('female'), Person_type('brother'), Season("summer"), piece_name("Shirt"),
              piece_color("white")), salience=1)
    def clothes520(self):
        self.myclothes = Myclothes(1, "blue", "Trousers", 0, "", "", 0, "", "", 0, "", "", 5, "white", "Kandra", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='dark'),
              Occasion('wadding'), Gender('female'), Person_type('brother'), Season("summer"), piece_name("Shirt"),
              piece_color("white")), salience=1)
    def clothes521(self):
        self.myclothes = Myclothes(1, "black", "Trousers", 0, "", "", 0, "", "", 0, "", "", 5, "white", "Kandra",
                                   0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "",
                                   "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='dark'),
              Occasion('wadding'), Gender('female'), Person_type('brother'), Season("summer"), piece_name("Trousers"),
              piece_color("black")), salience=1)
    def clothes522(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, " white", "Shirt", 0, "", "", 5, "black", "Kandra", 0, "",
                                   "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='dark'),
              Occasion('wadding'), Gender('female'), Person_type('brother'), Season("summer"), piece_name("Trousers"),
              piece_color("black")), salience=1)
    def clothes523(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "pink", "Shirt", 0, "", "", 5, "black", "Kandra", 0, "",
                                   "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='dark'),
              Occasion('wadding'), Gender('female'), Person_type('brother'), Season("summer"), piece_name("Trousers"),
              piece_color("gray")), salience=1)
    def clothes524(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "vinous", "Shirt", 0, "", "", 5, "black", "Kandra", 0, "",
                                   "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='dark'),
              Occasion('wadding'), Gender('female'), Person_type('brother'), Season("summer"), piece_name("Trousers"),
              piece_color("gray")), salience=1)
    def clothes525(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "brown", "Shirt", 0, "", "", 5, "black", "Kandra", 0, "",
                                   "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='dark'),
              Occasion('wadding'), Gender('female'), Person_type('brother'), Season("summer"), piece_name("Skirt"),
              piece_color("black")), salience=1)
    def clothes526(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "black", "Kandra", 0, "",
                                   "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='dark'),
              Occasion('wadding'), Gender('female'), Person_type('brother'), Season("summer"), piece_name("Skirt"),
              piece_color("white")), salience=1)
    def clothes527(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "pink", "Shirt", 0, "", "", 5, "black", "Kandra", 0, "",
                                   "", 0, "", "", 0, "", "", 0, "", "", 0, " ", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='dark'),
              Occasion('wadding'), Gender('female'), Person_type('brother'), Season("summer"), piece_name("Skirt"),
              piece_color("darkblue")), salience=1)
    def clothes528(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "brown", "Shirt", 0, "", "", 5, "black", "Kandra", 0, "",
                                   "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='dark'),
              Occasion('wadding'), Gender('female'), Person_type('brother'), Season("summer"), piece_name("Shirt"),
              piece_color("white")), salience=1)
    def clothes529(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 4, "black", "Skirt", 5, "black", "Kandra", 6,
                                   "black", "Coat", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "",
                                   0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='dark'),
              Occasion('wadding'), Gender('female'), Person_type('brother'), Season("summer"), piece_name("Shirt"),
              piece_color("vinous")), salience=1)
    def clothes530(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 4, "white", "Skirt", 5, "white", "Kandra", 0, "",
                                   "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='hanatawi'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer"), piece_name("dress"),
              piece_color("gold")), salience=1)
    def clothes531(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 0, "", "", 5, "pink", "Kandra", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='hanatawi'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer"), piece_name("dress"),
              piece_color("beige")), salience=1)
    def clothes532(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 0, "", "", 5, "black", "Kandra", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='hanatawi'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer"), piece_name("dress"),
              piece_color("cyan")), salience=1)
    def clothes533(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 0, "", "", 5, "white", "Sandal", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='hanatawi'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer"), piece_name("dress"),
              piece_color("blue")), salience=1)
    def clothes534(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 0, "", "", 5, "white", "Sandal", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='hanatawi'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer"), piece_name("dress"),
              piece_color("white")), salience=1)
    def clothes535(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 0, "", "", 5, "white", "Sandal", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='hanatawi'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer"), piece_name("dress"),
              piece_color("pink")), salience=1)
    def clothes536(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 0, "", "", 5, "silver", "Kandra", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='hanatawi'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer"), piece_name("dress"),
              piece_color("vinous")), salience=1)
    def clothes537(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 0, "", "", 5, "black", "Kandra", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='hanatawi'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer"), piece_name("dress"),
              piece_color(" black")), salience=1)
    def clothes538(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 0, "", "", 5, "black", "Kandra", 0, "", "", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='hanatawi'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer"), piece_name("Trousers"),
              piece_color("pink")), salience=1)
    def clothes539(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "black", "Shirt", 0, "", "", 5, "black", "Kandra", 0, "",
                                   "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='hanatawi'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer"), piece_name("Trousers"),
              piece_color("pink")), salience=1)
    def clothes540(self):
        self.myclothes = Myclothes(0, "", "", 2, " white", "T_Shirt", 0, "", "", 0, "", "", 5, "white", "shose", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='hanatawi'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer"), piece_name("Trousers"),
              piece_color("black")), salience=1)
    def clothes541(self):
        self.myclothes = Myclothes(0, "", "", 2, "vinous", "T_Shirt", 0, "", "", 0, "", "", 5, "white", "shose", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='hanatawi'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer"), piece_name("Trousers"),
              piece_color("white")), salience=1)
    def clothes542(self):
        self.myclothes = Myclothes(0, "", "", 2, "vinous", "T_Shirt", 0, "", "", 0, "", "", 5, "white", "shose", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='hanatawi'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer"), piece_name("Trousers"),
              piece_color("brown")), salience=1)
    def clothes543(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "beige", "Shirt", 0, "", "", 5, "gold", "Sandal ", 0, "",
                                   "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='hanatawi'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer"), piece_name("Trousers"),
              piece_color("brown")), salience=1)
    def clothes544(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, " white", "Shirt", 0, "", "", 5, "black", "Sandal ", 0,
                                   "", "", 0, "", "", 0, " ", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='hanatawi'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer"), piece_name("Trousers"),
              piece_color("pink")), salience=1)
    def clothes545(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, " white", "Shirt", 0, "", "", 5, "black", "Sandal", 0, "",
                                   "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer"), piece_name("Skirt"),
              piece_color("darkblue")), salience=1)
    def clothes546(self):
        self.myclothes = Myclothes(0, "", "", 2, "yellow", "T_Shirt", 0, "", "", 0, "", "", 5, "white", "shose", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer"), piece_name("Skirt"),
              piece_color("black")), salience=1)
    def clothes547(self):
        self.myclothes = Myclothes(0, "", "", 2, "pink", "T_Shirt", 0, "", "", 0, "", "", 5, "white", "shose", 0, "",
                                   "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer"), piece_name("Skirt"),
              piece_color("white")), salience=1)
    def clothes548(self):
        self.myclothes = Myclothes(0, "", "", 2, "pink", "T_Shirt", 0, "", "", 0, "", "", 5, "white", "shose", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer"), piece_name("Skirt"),
              piece_color("black")), salience=1)
    def clothes549(self):
        self.myclothes = Myclothes(0, "", "", 2, "gold", "T_Shirt", 0, "", "", 0, "", "", 5, "white", "shose", 0, "",
                                   "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer"), piece_name("Skirt"),
              piece_color("white")), salience=1)
    def clothes550(self):
        self.myclothes = Myclothes(0, "", "", 2, "green", "T_Shirt", 0, "", "", 0, "", "", 5, "white", "shose", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer"), piece_name("T_Shirt"),
              piece_color("pink")), salience=1)
    def clothes551(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 4, "white", "Skirt", 5, "white", "shose", 0, "",
                                   "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer"), piece_name("T_Shirt"),
              piece_color("black")), salience=1)
    def clothes552(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 4, "pink", "Skirt", 5, "white", "shose", 0, "",
                                   "", 0, "", "", 0, "", "", 0, "", "", 0, " ", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer"), piece_name("T_Shirt"),
              piece_color("pink")), salience=1)
    def clothes553(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 4, "white", "Skirt", 5, "white", "shose", 0, "",
                                   "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer"), piece_name("T_Shirt"),
              piece_color("white")), salience=1)
    def clothes554(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 4, "cyan", "Skirt", 5, "white", "shose", 0, "",
                                   "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer"), piece_name("Skirt"),
              piece_color("pink")), salience=1)
    def clothes555(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "black", "Kandra", 0, "",
                                   "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer"), piece_name("Skirt"),
              piece_color("black")), salience=1)
    def clothes556(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "pink", "Shirt", 0, "", "", 5, "black", "Kandra", 0, "",
                                   "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer"), piece_name("Skirt"),
              piece_color("gray")), salience=1)
    def clothes557(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "cyan", "Shirt", 0, "", "", 5, "silver", "Kandra", 0, "",
                                   "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer"), piece_name("Skirt"),
              piece_color("white")), salience=1)
    def clothes558(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "red", "Shirt", 0, "", "", 5, "white", "Kandra", 0, "",
                                   "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer"), piece_name("Shirt"),
              piece_color("vinous")), salience=1)
    def clothes559(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 4, "black", "Skirt", 5, "silver", "Kandra", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer"), piece_name("Shirt"),
              piece_color("pink")), salience=1)
    def clothes560(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 0, "", "", 4, "black", "Skirt", 5, "silver", "Kandra", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='hanatawi'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer"), piece_name("Skirt"),
              piece_color("vinous")), salience=1)
    def clothes561(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "beige", "Shirt", 0, "", "", 5, "black", "Kandra", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='hanatawi'),
              Occasion('wadding'), Gender('female'), Person_type('friend'), Season("summer"), piece_name("Skirt"),
              piece_color("vinous")), salience=1)
    def clothes562(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "white", "Shirt", 0, "", "", 5, "black", "Kandra", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('Sport'), Gender('female'), Person_type('person'), Season("summer"), piece_name("Hoodie"),
              piece_color("pink")), salience=1)
    def clothes563(self):
        self.myclothes = Myclothes(1, "pink", "pajama", 0, "", "", 0, "", "", 0, "", "", 5, "white", "shose", 0, "",
                                   "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('Sport'), Gender('female'), Person_type('person'), Season("summer"), piece_name("Hoodie"),
              piece_color("orange")), salience=1)
    def clothes564(self):
        self.myclothes = Myclothes(1, "orange", "pajama", 0, "", "", 0, "", "", 0, "", "", 5, "white", "shose", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('Sport'), Gender('female'), Person_type('person'), Season("summer"), piece_name("Hoodie"),
              piece_color("yellow")), salience=1)
    def clothes565(self):
        self.myclothes = Myclothes(1, "yellow", "pajama", 0, "", "", 0, "", "", 0, "", "", 5, "white", "shose", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='dark'),
              Occasion('Sport'), Gender('female'), Person_type('person'), Season("summer"), piece_name("Hoodie"),
              piece_color("blue")), salience=1)
    def clothes566(self):
        self.myclothes = Myclothes(1, "blue", "pajama", 0, "", "", 0, "", "", 0, "", "", 5, "white", "shose", 0, "",
                                   "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('Sport'), Gender('female'), Person_type('person'), Season("summer"), piece_name("Hoodie"),
              piece_color("red")), salience=1)
    def clothes567(self):
        self.myclothes = Myclothes(1, "red", "pajama", 0, "", "", 0, "", "", 5, "white", "shose", 0, "", "", 0, "",
                                   "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='dark'),
              Occasion('Sport'), Gender('female'), Person_type('person'), Season("summer"), piece_name("Hoodie"),
              piece_color("gray")), salience=1)
    def clothes568(self):
        self.myclothes = Myclothes(1, "gray", "pajama", 0, "", "", 0, "", "", 0, "", "", 5, "white", "shose", 0, "",
                                   "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('Sport'), Gender('female'), Person_type('person'), Season("summer"), piece_name("Hoodie"),
              piece_color("green")), salience=1)
    def clothes569(self):
        self.myclothes = Myclothes(1, "black", "pajama", 0, "", "", 0, "", "", 0, "", "", 5, "white", "shose", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='white'),
              Occasion('Sport'), Gender('female'), Person_type('person'), Season("summer"), piece_name("Hoodie"),
              piece_color("red")), salience=1)
    def clothes570(self):
        self.myclothes = Myclothes(1, "black", "pajama", 0, "", "", 0, "", "", 0, "", "", 5, "white", "shose", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='white'),
              Occasion('Sport'), Gender('female'), Person_type('person'), Season("summer"), piece_name("Hoodie"),
              piece_color("vinous")), salience=1)
    def clothes571(self):
        self.myclothes = Myclothes(1, "vinous", "pajama", 0, "", "", 0, "", "", 0, "", "", 5, "white", "shose", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='dark'),
              Occasion('Sport'), Gender('female'), Person_type('person'), Season("summer"), piece_name("Hoodie"),
              piece_color("vinous")), salience=1)
    def clothes572(self):
        self.myclothes = Myclothes(1, "black", "pajama", 0, "", "", 0, "", "", 0, "", "", 5, "white", "shose", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='white'),
              Occasion('Sport'), Gender('female'), Person_type('person'), Season("summer"), piece_name("Hoodie"),
              piece_color("white")), salience=1)
    def clothes573(self):
        self.myclothes = Myclothes(1, "white", "pajama", 0, "", "", 0, "", "", 0, "", "", 5, "white", "shose", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('Sport'), Gender('female'), Person_type('person'), Season("summer"), piece_name("Hoodie"),
              piece_color("yellow")), salience=1)
    def clothes574(self):
        self.myclothes = Myclothes(1, "gray", "pajama", 0, "", "", 0, "", "", 0, "", "", 5, "white", "shose", 0, "",
                                   "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('Sport'), Gender('female'), Person_type('person'), Season("summer"), piece_name("Trousers"),
              piece_color("pink")), salience=1)
    def clothes575(self):
        self.myclothes = Myclothes(0, "", "", 2, "pink", "Hoodie", 0, "", "", 0, "", "", 5, "white", "shose", 0, "",
                                   "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('Sport'), Gender('female'), Person_type('person'), Season("summer"), piece_name("Trousers"),
              piece_color("orange")), salience=1)
    def clothes576(self):
        self.myclothes = Myclothes(0, "", "", 2, "orange", "Hoodie", 0, "", "", 0, "", "", 5, "white", "shose", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('Sport'), Gender('female'), Person_type('person'), Season("summer"), piece_name("Trousers"),
              piece_color("yellow")), salience=1)
    def clothes577(self):
        self.myclothes = Myclothes(0, "", "", 2, "yellow", "Hoodie", 0, "", "", 0, "", "", 5, "white", "shose", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='dark'),
              Occasion('Sport'), Gender('female'), Person_type('person'), Season("summer"), piece_name("Trousers"),
              piece_color("blue")), salience=1)
    def clothes578(self):
        self.myclothes = Myclothes(0, "", "", 2, "blue", "Hoodie", 0, "", "", 0, "", "", 5, "white", "shose", 0, "",
                                   "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('Sport'), Gender('female'), Person_type('person'), Season("summer"), piece_name("Trousers"),
              piece_color("red")), salience=1)
    def clothes579(self):
        self.myclothes = Myclothes(0, "", "", 2, "red", "Hoodie", 0, "", "", 5, "white", "shose", 0, "", "", 0, "",
                                   "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='dark'),
              Occasion('Sport'), Gender('female'), Person_type('person'), Season("summer"), piece_name("Trousers"),
              piece_color("red")), salience=1)
    def clothes580(self):
        self.myclothes = Myclothes(0, "", "", 2, "gray", "Hoodie", 0, "", "", 0, "", "", 5, "white", "shose", 0, "",
                                   "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('Sport'), Gender('female'), Person_type('person'), Season("summer"), piece_name("Trousers"),
              piece_color("black")), salience=1)
    def clothes581(self):
        self.myclothes = Myclothes(0, "", "", 2, "green", "Hoodie", 0, "", "", 0, "", "", 5, "white", "shose", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='white'),
              Occasion('Sport'), Gender('female'), Person_type('person'), Season("summer"), piece_name("Trousers"),
              piece_color("black")), salience=1)
    def clothes582(self):
        self.myclothes = Myclothes(0, "", "", 2, "red", "Hoodie", 0, "", "", 0, "", "", 5, "white", "shose", 0, "",
                                   "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='white'),
              Occasion('Sport'), Gender('female'), Person_type('person'), Season("summer"), piece_name("Trousers"),
              piece_color("vinous")), salience=1)
    def clothes583(self):
        self.myclothes = Myclothes(0, "", "", 2, "vinous", "Hoodie", 0, "", "", 0, "", "", 5, "white", "shose", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='dark'),
              Occasion('Sport'), Gender('female'), Person_type('person'), Season("summer"), piece_name("Trousers"),
              piece_color("black")), salience=1)
    def clothes584(self):
        self.myclothes = Myclothes(0, "", "", 2, "vinous", "Hoodie", 0, "", "", 0, "", "", 5, "white", "shose", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='white'),
              Occasion('Sport'), Gender('female'), Person_type('person'), Season("summer"), piece_name("Trousers"),
              piece_color("white")), salience=1)
    def clothes585(self):
        self.myclothes = Myclothes(0, "", "", 2, "white", "Hoodie", 0, "", "", 0, "", "", 5, "white", "shose", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('Sport'), Gender('female'), Person_type('person'), Season("summer"), piece_name("Trousers"),
              piece_color("gray")), salience=1)
    def clothes586(self):
        self.myclothes = Myclothes(0, "", "", 2, "yellow", "Hoodie", 0, "", "", 0, "", "", 5, "white", "shose", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='dark'),
              Occasion('Sport'), Gender('female'), Person_type('person'), Season("summer"), piece_name("Trousers"),
              piece_color("yellow")), salience=1)
    def clothes587(self):
        self.myclothes = Myclothes(0, "", "", 2, "green", "Hoodie", 0, "", "", 0, "", "", 5, "white", "shose", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('Sport'), Gender('female'), Person_type('person'), Season("summer"), piece_name("Trousers"),
              piece_color("darkblue")), salience=1)
    def clothes588(self):
        self.myclothes = Myclothes(0, "", "", 2, "pink", "Hoodie", 0, "", "", 0, "", "", 5, "white", "shose", 0, "",
                                   "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('Sport'), Gender('female'), Person_type('person'), Season("summer"), piece_name("Trousers"),
              piece_color("white")), salience=1)
    def clothes589(self):
        self.myclothes = Myclothes(0, "", "", 2, "green", "Hoodie", 0, "", "", 0, "", "", 5, "white", "shose", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('Sport'), Gender('female'), Person_type('person'), Season("summer"), piece_name("Trousers"),
              piece_color("darkblue")), salience=1)
    def clothes590(self):
        self.myclothes = Myclothes(0, "", "", 2, "white", "Hoodie", 0, "", "", 0, "", "", 5, "white", "shose", 0, "",
                                   "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('Sport'), Gender('female'), Person_type('person'), Season("summer"), piece_name("Trousers"),
              piece_color("beige")), salience=1)
    def clothes591(self):
        self.myclothes = Myclothes(0, "", "", 2, "beige", "Hoodie", 0, "", "", 0, "", "", 5, "white", "shose", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('Sport'), Gender('female'), Person_type('person'), Season("summer"), piece_name("Trousers"),
              piece_color("gray")), salience=1)
    def clothes592(self):
        self.myclothes = Myclothes(0, "", "", 2, "cyan", "Hoodie", 0, "", "", 0, "", "", 5, "white", "shose", 0, "",
                                   "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('Sport'), Gender('male'), Person_type('person'), Season("summer"), piece_name("Trousers"),
              piece_color("cyan")), salience=1)
    def clothes593(self):
        self.myclothes = Myclothes(0, "", "", 2, "black", "Hoodie", 0, "", "", 0, "", "", 5, "white", "shose", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('Sport'), Gender('male'), Person_type('person'), Season("summer"), piece_name("Trousers"),
              piece_color("gray")), salience=1)
    def clothes594(self):
        self.myclothes = Myclothes(0, "", "", 2, "darlblue", "Hoodie", 0, "", "", 0, "", "", 5, "white", "shose", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('Sport'), Gender('male'), Person_type('person'), Season("summer"), piece_name("Trousers"),
              piece_color("blue")), salience=1)
    def clothes595(self):
        self.myclothes = Myclothes(0, "", "", 2, "blue", "Hoodie", 0, "", "", 0, "", "", 5, "white", "shose", 0, "",
                                   "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('Sport'), Gender('male'), Person_type('person'), Season("summer"), piece_name("Trousers"),
              piece_color("gray")), salience=1)
    def clothes596(self):
        self.myclothes = Myclothes(0, "", "", 2, "gray", "Hoodie", 0, "", "", 0, "", "", 5, "white", "shose", 0, "",
                                   "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('Sport'), Gender('male'), Person_type('person'), Season("summer"), piece_name("Trousers"),
              piece_color("vinous")), salience=1)
    def clothes597(self):
        self.myclothes = Myclothes(0, "", "", 2, "vinous", "Hoodie", 0, "", "", 0, "", "", 5, "white", "shose", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='dark'),
              Occasion('Sport'), Gender('female'), Person_type('person'), Season("summer"), piece_name("Hoodie"),
              piece_color("green")), salience=1)
    def clothes598(self):
        self.myclothes = Myclothes(1, "yellow", "pajama", 0, "", "", 0, "", "", 0, "", "", 5, "white", "shose", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('Sport'), Gender('female'), Person_type('person'), Season("summer"), piece_name("Hoodie"),
              piece_color("pink")), salience=1)
    def clothes599(self):
        self.myclothes = Myclothes(1, "darkblue", "pajama", 0, "", "", 0, "", "", 0, "", "", 5, "white", "shose", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('Sport'), Gender('female'), Person_type('person'), Season("summer"), piece_name("Hoodie"),
              piece_color("green")), salience=1)
    def clothes600(self):
        self.myclothes = Myclothes(1, "white", "pajama", 0, "", "", 0, "", "", 0, "", "", 5, "white", "shose", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('Sport'), Gender('female'), Person_type('person'), Season("summer"), piece_name("Hoodie"),
              piece_color("white")), salience=1)
    def clothes601(self):
        self.myclothes = Myclothes(1, "darkblue", "pajama", 0, "", "", 0, "", "", 0, "", "", 5, "white", "shose", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('Sport'), Gender('female'), Person_type('person'), Season("summer"), piece_name("Hoodie"),
              piece_color("beige")), salience=1)
    def clothes602(self):
        self.myclothes = Myclothes(1, "beige", "pajama", 0, "", "", 0, "", "", 0, "", "", 5, "white", "shose", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('Sport'), Gender('female'), Person_type('person'), Season("summer"), piece_name("Hoodie"),
              piece_color("cyan")), salience=1)
    def clothes603(self):
        self.myclothes = Myclothes(1, "cyan", "pajama", 0, "", "", 0, "", "", 0, "", "", 5, "white", "shose", 0, "",
                                   "", 0, "", "", 0, " ", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('Sport'), Gender('male'), Person_type('person'), Season("summer"), piece_name("Hoodie"),
              piece_color("black")), salience=1)
    def clothes604(self):
        self.myclothes = Myclothes(1, " black", "pajama", 0, "", "", 0, "", "", 0, "", "", 5, "white", "shose", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('Sport'), Gender('male'), Person_type('person'), Season("summer"), piece_name("Hoodie"),
              piece_color("darlblue")), salience=1)
    def clothes605(self):
        self.myclothes = Myclothes(1, "darlblue", "pajama", 0, "", "", 0, "", "", 0, "", "", 5, "white", "shose", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('Sport'), Gender('male'), Person_type('person'), Season("summer"), piece_name("Hoodie"),
              piece_color("blue")), salience=1)
    def clothes606(self):
        self.myclothes = Myclothes(1, "blue", "pajama", 0, "", "", 0, "", "", 0, "", "", 5, "white", "shose", 0, "",
                                   "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('Sport'), Gender('male'), Person_type('person'), Season("summer"), piece_name("Hoodie"),
              piece_color("gray")), salience=1)
    def clothes607(self):
        self.myclothes = Myclothes(1, "gray", "pajama", 0, "", "", 0, "", "", 0, "", "", 5, "white", "shose", 0, "",
                                   "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('Sport'), Gender('male'), Person_type('person'), Season("summer"), piece_name("Hoodie"),
              piece_color("vinous")), salience=1)
    def clothes608(self):
        self.myclothes = Myclothes(1, "vinous", "pajama", 0, "", "", 0, "", "", 0, "", "", 5, "white", "shose", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('Sport'), Gender('male'), Person_type('person'), Season("summer"), piece_name("Hoodie"),
              piece_color("white")), salience=1)
    def clothes609(self):
        self.myclothes = Myclothes(1, "black", "pajama", 0, "", "", 0, "", "", 0, "", "", 5, "white", "shose", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('Sport'), Gender('male'), Person_type('person'), Season("summer"), piece_name("Hoodie"),
              piece_color("yellow")), salience=1)
    def clothes610(self):
        self.myclothes = Myclothes(1, "yellow", "pajama", 0, "", "", 0, "", "", 0, "", "", 5, "white", "shose", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='white'),
              Occasion('Sport'), Gender('male'), Person_type('person'), Season("summer"), piece_name("Hoodie"),
              piece_color("Hoodie")), salience=1)
    def clothes611(self):
        self.myclothes = Myclothes(1, "black", "short", 0, "", "", 0, "", "", 0, "", "", 5, "white", "shose", 0, "",
                                   "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='dark'),
              Occasion('Sport'), Gender('male'), Person_type('person'), Season("summer"), piece_name("Hoodie"),
              piece_color("oil")), salience=1)
    def clothes612(self):
        self.myclothes = Myclothes(1, "oil", "short", 0, "", "", 0, "", "", 0, "", "", 5, "white", "shose", 0, "",
                                   "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='white'),
              Occasion('Sport'), Gender('male'), Person_type('person'), Season("summer"), piece_name("Hoodie"),
              piece_color("yellow")), salience=1)
    def clothes613(self):
        self.myclothes = Myclothes(1, "red", "short", 0, "", "", 0, "", "", 0, "", "", 5, "white", "shose", 0, "",
                                   "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='white'),
              Occasion('Sport'), Gender('male'), Person_type('person'), Season("summer"), piece_name("Hoodie"),
              piece_color("red")), salience=1)
    def clothes614(self):
        self.myclothes = Myclothes(1, "white", "short", 0, "", "", 0, "", "", 0, "", "", 5, "white", "shose", 0, "",
                                   "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='dark'),
              Occasion('Sport'), Gender('male'), Person_type('person'), Season("summer"), piece_name("Hoodie"),
              piece_color("yellow")), salience=1)
    def clothes615(self):
        self.myclothes = Myclothes(1, "green", "short", 0, "", "", 0, "", "", 0, "", "", 5, "white", "shose", 0, "",
                                   "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='dark'),
              Occasion('Sport'), Gender('male'), Person_type('person'), Season("summer"), piece_name("Hoodie"),
              piece_color("green")), salience=1)
    def clothes616(self):
        self.myclothes = Myclothes(1, "black", "short", 0, "", "", 0, "", "", 0, "", "", 5, "white", "shose", 0, "",
                                   "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('Sport'), Gender('male'), Person_type('person'), Season("summer"), piece_name("Hoodie"),
              piece_color("black")), salience=1)
    def clothes617(self):
        self.myclothes = Myclothes(1, "orange", "short", 0, "", "", 0, "", "", 0, "", "", 5, "white", "shose", 0, "",
                                   "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('Sport'), Gender('male'), Person_type('person'), Season("summer"), piece_name("Trousers"),
              piece_color("black")), salience=1)
    def clothes618(self):
        self.myclothes = Myclothes(0, "", "", 2, "white", "Hoodie", 0, "", "", 0, "", "", 5, "white", "shose", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='dark'),
              Occasion('Sport'), Gender('male'), Person_type('person'), Season("summer"), piece_name("Trousers"),
              piece_color("oil")), salience=1)
    def clothes619(self):
        self.myclothes = Myclothes(0, "", "", 2, "oil", "Hoodie", 0, "", "", 0, "", "", 5, "white", "shose", 0, "",
                                   "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='white'),
              Occasion('Sport'), Gender('male'), Person_type('person'), Season("summer"), piece_name("Trousers"),
              piece_color("red")), salience=1)
    def clothes620(self):
        self.myclothes = Myclothes(0, "", "", 2, "yellow", "Hoodie", 0, "", "", 0, "", "", 5, "white", "shose", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='white'),
              Occasion('Sport'), Gender('male'), Person_type('person'), Season("summer"), piece_name("Trousers"),
              piece_color("white")), salience=1)
    def clothes621(self):
        self.myclothes = Myclothes(0, "", "", 2, "red", "Hoodie", 0, "", "", 0, "", "", 5, "white", "shose", 0, "",
                                   "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='dark'),
              Occasion('Sport'), Gender('male'), Person_type('person'), Season("summer"), piece_name("Trousers"),
              piece_color("green")), salience=1)
    def clothes622(self):
        self.myclothes = Myclothes(0, "", "", 2, "yellow", "Hoodie", 0, "", "", 0, "", "", 5, "white", "shose", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('Sport'), Gender('male'), Person_type('person'), Season("summer"), piece_name("Trousers"),
              piece_color("orange")), salience=1)
    def clothes623(self):
        self.myclothes = Myclothes(0, "", "", 2, "black", "Hoodie", 0, "", "", 0, "", "", 5, "white", "shose", 0, "",
                                   "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='white'),
              Occasion('Sport'), Gender('female'), Person_type('person'), Season("summer"), piece_name("Trousers"),
              piece_color("white")), salience=1)
    def clothes624(self):
        self.myclothes = Myclothes(0, "", "", 2, "pink", "Hoodie", 0, "", "", 0, "", "", 5, "white", "shose", 0, "",
                                   "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='white'),
              Occasion('Hinking_with_friends'), Gender('female'), Person_type('person'), Season("summer"),
              piece_name("Trousers"), piece_color("black")), salience=1)
    def clothes625(self):
        self.myclothes = Myclothes(0, "", "", 2, "black", "Hoodie", 0, "", "", 0, "", "", 5, "white", "shose", 0, "",
                                   "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('Hinking_with_friends'), Gender('female'), Person_type('person'), Season("summer"),
              piece_name("Trousers"), piece_color("yellow")), salience=1)
    def clothes626(self):
        self.myclothes = Myclothes(0, "", "", 2, "yellow", "Hoodie", 0, "", "", 0, "", "", 5, "white", "shose", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='dark'),
              Occasion('Hinking_with_friends'), Gender('female'), Person_type('person'), Season("summer"),
              piece_name("Trousers"), piece_color("blue")), salience=1)
    def clothes627(self):
        self.myclothes = Myclothes(0, "", "", 2, "blue", "Hoodie", 0, "", "", 0, "", "", 5, "white", "shose", 0, "",
                                   "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('Hinking_with_friends'), Gender('female'), Person_type('person'), Season("summer"),
              piece_name("Trousers"), piece_color("gray")), salience=1)
    def clothes628(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "cyan", "Shirt", 0, "", "", 5, "white", "shose", 0, "",
                                   "", 0, "", "", 0, " ", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='white'),
              Occasion('Hinking_with_friends'), Gender('female'), Person_type('person'), Season("summer"),
              piece_name("Trousers"), piece_color("gray")), salience=1)
    def clothes629(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "brown", "Shirt", 0, "", "", 5, "white", "shose", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('Hinking_with_friends'), Gender('female'), Person_type('person'), Season("summer"),
              piece_name("Trousers"), piece_color("gray")), salience=1)
    def clothes630(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "pink", "Shirt", 0, "", "", 5, "white", "shose", 0, "",
                                   "", 0, "", "", 0, " ", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='dark'),
              Occasion('Hinking_with_friends'), Gender('female'), Person_type('person'), Season("summer"),
              piece_name("Trousers"), piece_color("gray")), salience=1)
    def clothes631(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "vinous", "Shirt", 0, "", "", 5, "dark", "shose", 0, "",
                                   "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='white'),
              Occasion('Hinking_with_friends'), Gender('female'), Person_type('person'), Season("summer"),
              piece_name("Trousers"), piece_color("gray")), salience=1)
    def clothes632(self):
        self.myclothes = Myclothes(0, "", "", 2, "red", "T_Shirt", 0, "", "", 0, "", "", 5, "white", "shose", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='dark'),
              Occasion('Hinking_with_friends'), Gender('female'), Person_type('person'), Season("summer"),
              piece_name("Trousers"), piece_color("gray")), salience=1)
    def clothes633(self):
        self.myclothes = Myclothes(0, "", "", 2, "pink", "T_Shirt", 0, "", "", 0, "", "", 5, "white", "shose", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='white'),
              Occasion('Hinking_with_friends'), Gender('female'), Person_type('person'), Season("summer"),
              piece_name("Trousers"), piece_color("gray")), salience=1)
    def clothes634(self):
        self.myclothes = Myclothes(0, "", "", 2, "pink", "T_Shirt", 0, "", "", 0, "", "", 5, "white", "shose", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('Hinking_with_friends'), Gender('female'), Person_type('person'), Season("summer"),
              piece_name("Trousers"), piece_color("white")), salience=1)
    def clothes635(self):
        self.myclothes = Myclothes(0, "", "", 2, "pink", "T_Shirt", 0, "", "", 0, "", "", 5, "white", "shose", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('Hinking_with_friends'), Gender('female'), Person_type('person'), Season("summer"),
              piece_name("Trousers"), piece_color("white")), salience=1)
    def clothes636(self):
        self.myclothes = Myclothes(0, "", "", 2, "yellow", "T_Shirt", 0, "", "", 0, "", "", 5, "white", "shose", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='white'),
              Occasion('Hinking_with_friends'), Gender('female'), Person_type('person'), Season("summer"),
              piece_name("Trousers"), piece_color("white")), salience=1)
    def clothes637(self):
        self.myclothes = Myclothes(0, "", "", 2, "green", "T_Shirt", 0, "", "", 0, "", "", 5, "white", "shose", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='white'),
              Occasion('Hinking_with_friends'), Gender('female'), Person_type('person'), Season("summer"),
              piece_name("Trousers"), piece_color("black")), salience=1)
    def clothes638(self):
        self.myclothes = Myclothes(0, "", "", 2, "orange", "T_Shirt", 0, "", "", 0, "", "", 5, "white", "shose", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='dark'),
              Occasion('Hinking_with_friends'), Gender('female'), Person_type('person'), Season("summer"),
              piece_name("Trousers"), piece_color("black")), salience=1)
    def clothes639(self):
        self.myclothes = Myclothes(0, "", "", 2, "brown", "T_Shirt", 0, "", "", 0, "", "", 5, "white", "shose", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('Hinking_with_friends'), Gender('female'), Person_type('person'), Season("summer"),
              piece_name("Trousers"), piece_color("black")), salience=1)
    def clothes640(self):
        self.myclothes = Myclothes(0, "", "", 2, "beige", "T_Shirt", 0, "", "", 0, "", "", 5, "white", "shose", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='white'),
              Occasion('Hinking_with_friends'), Gender('female'), Person_type('person'), Season("summer"),
              piece_name("Trousers"), piece_color("white")), salience=1)
    def clothes641(self):
        self.myclothes = Myclothes(0, "", "", 2, "cyan", "T_Shirt", 0, "", "", 0, "", "", 5, "white", "shose", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='dark'),
              Occasion('Hinking_with_friends'), Gender('female'), Person_type('person'), Season("summer"),
              piece_name("Trousers"), piece_color("white")), salience=1)
    def clothes642(self):
        self.myclothes = Myclothes(0, "", "", 2, "pink", "T_Shirt", 0, "", "", 0, "", "", 5, "white", "shose", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('Hinking_with_friends'), Gender('female'), Person_type('person'), Season("summer"),
              piece_name("Trousers"), piece_color("white")), salience=1)
    def clothes643(self):
        self.myclothes = Myclothes(0, "", "", 2, "pink", "T_Shirt", 0, "", "", 0, "", "", 5, "white", "shose", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    #     //////////////////////////////////////////////////
    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='white'),
              Occasion(''), Gender('female'), Person_type('person'), Season("summer"), piece_name("Hoodie"),
              piece_color("pink")), salience=1)
    def clothes644(self):
        self.myclothes = Myclothes(1, "white", "Trousers", 0, "", "", 0, "", "", 0, "", "", 5, "white", "shose", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='white'),
              Occasion('Hinking_with_friends'), Gender('female'), Person_type('person'), Season("summer"),
              piece_name("Hoodie"), piece_color("black")), salience=1)
    def clothes645(self):
        self.myclothes = Myclothes(1, "black", "pajama", 0, "", "", 0, "", "", 0, "", "", 5, "white", "shose", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='white'),
              Occasion('Hinking_with_friends'), Gender('female'), Person_type('person'), Season("summer"),
              piece_name("Hoodie"), piece_color("orange")), salience=1)
    def clothes646(self):
        self.myclothes = Myclothes(1, "black", "pajama", 0, "", "", 0, "", "", 0, "", "", 5, "white", "shose", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('Hinking_with_friends'), Gender('female'), Person_type('person'), Season("summer"),
              piece_name("Hoodie"), piece_color("yellow")), salience=1)
    def clothes647(self):
        self.myclothes = Myclothes(1, "yellow", "pajama", 0, "", "", 0, "", "", 0, "", "", 5, "white", "shose", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='dark'),
              Occasion('Hinking_with_friends'), Gender('female'), Person_type('person'), Season("summer"),
              piece_name("Hoodie"), piece_color("blue")), salience=1)
    def clothes648(self):
        self.myclothes = Myclothes(1, "blue", "pajama", 0, "", "", 0, "", "", 0, "", "", 5, "white", "shose", 0, "",
                                   "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('Hinking_with_friends'), Gender('female'), Person_type('person'), Season("summer"),
              piece_name("Shirt"), piece_color("Shirt")), salience=1)
    def clothes649(self):
        self.myclothes = Myclothes(1, "gray", "Trousers", 0, "", "", 0, "", "", 0, "", "", 5, "white", "shose", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='white'),
              Occasion('Hinking_with_friends'), Gender('female'), Person_type('person'), Season("summer"),
              piece_name("Shirt"), piece_color("black")), salience=1)
    def clothes650(self):
        self.myclothes = Myclothes(1, "gray", "Trousers", 0, "", "", 0, "", "", 0, "", "", 5, "white", "shose", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('Hinking_with_friends'), Gender('female'), Person_type('person'), Season("summer"),
              piece_name("Shirt"), piece_color("pink")), salience=1)
    def clothes651(self):
        self.myclothes = Myclothes(1, "gray", "Trousers", 0, "", "", 0, "", "", 0, "", "", 5, "white", "shose", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='dark'),
              Occasion('Hinking_with_friends'), Gender('female'), Person_type('person'), Season("summer"),
              piece_name("Shirt"), piece_color("vinous")), salience=1)
    def clothes652(self):
        self.myclothes = Myclothes(1, "gray", "Trousers", 0, "", "", 0, "", "", 0, "", "", 5, "dark", "shose", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='white'),
              Occasion('Hinking_with_friends'), Gender('female'), Person_type('person'), Season("summer"),
              piece_name("T_Shirt"), piece_color("red")), salience=1)
    def clothes653(self):
        self.myclothes = Myclothes(1, "gray", "jeans", 0, "", "", 0, "", "", 0, "", "", 5, "white", "shose", 0, "",
                                   "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('Hinking_with_friends'), Gender('female'), Person_type('person'), Season("summer"),
              piece_name("T_Shirt"), piece_color("pink")), salience=1)
    def clothes654(self):
        self.myclothes = Myclothes(1, "gray", "jeans", 0, "", "", 0, "", "", 0, "", "", 5, "white", "shose", 0, "",
                                   "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='white'),
              Occasion('Hinking_with_friends'), Gender('female'), Person_type('person'), Season("summer"),
              piece_name("T_Shirt"), piece_color("pink")), salience=1)
    def clothes655(self):
        self.myclothes = Myclothes(1, "gray", "jeans", 0, "", "", 0, "", "", 0, "", "", 5, "white", "shose", 0, "",
                                   "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='dark'),
              Occasion('Hinking_with_friends'), Gender('female'), Person_type('person'), Season("summer"),
              piece_name("T_Shirt"), piece_color("pink")), salience=1)
    def clothes656(self):
        self.myclothes = Myclothes(1, "white", "jeans", 0, "", "", 0, "", "", 0, "", "", 5, "white", "shose", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='white'),
              Occasion('Hinking_with_friends'), Gender('female'), Person_type('person'), Season("summer"),
              piece_name("T_Shirt"), piece_color("green")), salience=1)
    def clothes657(self):
        self.myclothes = Myclothes(1, "white", "jeans", 0, "", "", 0, "", "", 0, "", "", 5, "white", "shose", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('Hinking_with_friends'), Gender('female'), Person_type('person'), Season("summer"),
              piece_name("T_Shirt"), piece_color("yellow")), salience=1)
    def clothes658(self):
        self.myclothes = Myclothes(1, "white", "jeans", 0, "", "", 0, "", "", 0, "", "", 5, "white", "shose", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='dark'),
              Occasion('Hinking_with_friends'), Gender('female'), Person_type('person'), Season("summer"),
              piece_name("T_Shirt"), piece_color("pink")), salience=1)
    def clothes659(self):
        self.myclothes = Myclothes(1, "black", "jeans", 0, "", "", 0, "", "", 0, "", "", 5, "white", "shose", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='dark'),
              Occasion('Hinking_with_friends'), Gender('female'), Person_type('person'), Season("summer"),
              piece_name("T_Shirt"), piece_color("brown")), salience=1)
    def clothes660(self):
        self.myclothes = Myclothes(1, "black", "jeans", 0, "", "", 0, "", "", 0, "", "", 5, "white", "shose", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='white'),
              Occasion('Hinking_with_friends'), Gender('female'), Person_type('person'), Season("summer"),
              piece_name("T_Shirt"), piece_color("beige")), salience=1)
    def clothes661(self):
        self.myclothes = Myclothes(1, "black", "jeans", 0, "", "", 0, "", "", 0, "", "", 5, "white", "shose", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('Hinking_with_friends'), Gender('female'), Person_type('person'), Season("summer"),
              piece_name("T_Shirt"), piece_color("yellow")), salience=1)
    def clothes662(self):
        self.myclothes = Myclothes(1, "black", "jeans", 0, "", "", 0, "", "", 0, "", "", 5, "white", "shose", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('Hinking_with_friends'), Gender('female'), Person_type('person'), Season("summer"),
              piece_name("T_Shirt"), piece_color("yellow")), salience=1)
    def clothes663(self):
        self.myclothes = Myclothes(1, "darkblue", "jeans", 0, "", "", 0, "", "", 0, "", "", 5, "white", "shose", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='white'),
              Occasion('Hinking_with_friends'), Gender('female'), Person_type('person'), Season("summer"),
              piece_name("Hoodie"), piece_color("orange")), salience=1)
    def clothes664(self):
        self.myclothes = Myclothes(1, "black", "Trousers", 0, "", "", 0, "", "", 0, "", "", 5, "white", "shose", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('Hinking_with_friends'), Gender('female'), Person_type('person'), Season("summer"),
              piece_name("Hoodie"), piece_color("yellow")), salience=1)
    def clothes665(self):
        self.myclothes = Myclothes(1, "white", "Trousers", 0, "", "", 0, "", "", 0, "", "", 5, "white", "shose", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='dark'),
              Occasion('Hinking_with_friends'), Gender('female'), Person_type('person'), Season("summer"),
              piece_name("Hoodie"), piece_color("vinous")), salience=1)
    def clothes666(self):
        self.myclothes = Myclothes(1, "white", "Trousers", 0, "", "", 0, "", "", 0, "", "", 5, "white", "shose", 0,
                                   "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='white'),
              Occasion('Hinking_with_friends'), Gender('male'), Person_type('person'), Season("summer"),
              piece_name("T_Shirt"), piece_color("cyan")), salience=1)
    def clothes667(self):
        self.myclothes = Myclothes(1, "beige", "short", 0, "", "", 0, "", "", 5, "white", "shose", 0, "", "", 0, "",
                                   "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='dark'),
              Occasion('Hinking_with_friends'), Gender('male'), Person_type('person'), Season("summer"),
              piece_name("T_Shirt"), piece_color("brown")), salience=1)
    def clothes668(self):
        self.myclothes = Myclothes(1, "beige", "short", 0, "", "", 0, "", "", 5, "white", "shose", 0, "", "", 0, "",
                                   "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('Hinking_with_friends'), Gender('male'), Person_type('person'), Season("summer"),
              piece_name("T_Shirt"), piece_color("white")), salience=1)
    def clothes669(self):
        self.myclothes = Myclothes(1, "black", "short", 0, "", "", 0, "", "", 5, "white", "shose", 0, "", "", 0, "",
                                   "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)
        #         //////////////

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='white'),
              Occasion('Hinking_with_friends'), Gender('male'), Person_type('person'), Season("summer"),
              piece_name("T_Shirt"), piece_color("yellow")), salience=1)
    def clothes670(self):
        self.myclothes = Myclothes(1, "black", "short", 0, "", "", 0, "", "", 5, "white", "shose", 0, "", "", 0, "",
                                   "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='dark'),
              Occasion('Hinking_with_friends'), Gender('male'), Person_type('person'), Season("summer"),
              piece_name("T_Shirt"), piece_color("white")), salience=1)
    def clothes671(self):
        self.myclothes = Myclothes(1, "vinous", "short", 0, "", "", 0, "", "", 5, "white", "shose", 0, "", "", 0, "",
                                   "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('Hinking_with_friends'), Gender('male'), Person_type('person'), Season("summer"),
              piece_name("T_Shirt"), piece_color("oil")), salience=1)
    def clothes672(self):
        self.myclothes = Myclothes(1, "black", "short", 0, "", "", 0, "", "", 5, "white", "shose", 0, "", "", 0, "",
                                   "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('Hinking_with_friends'), Gender('male'), Person_type('person'), Season("summer"),
              piece_name("T_Shirt"), piece_color("gray")), salience=1)
    def clothes673(self):
        self.myclothes = Myclothes(1, "black", "short", 0, "", "", 0, "", "", 5, "white", "shose", 0, "", "", 0, "",
                                   "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('Hinking_with_friends'), Gender('male'), Person_type('person'), Season("summer"),
              piece_name("T_Shirt"), piece_color("vinous")), salience=1)
    def clothes674(self):
        self.myclothes = Myclothes(1, "gray", "short", 0, "", "", 0, "", "", 5, "white", "shose", 0, "", "", 0, "",
                                   "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='dark'),
              Occasion('Hinking_with_friends'), Gender('male'), Person_type('person'), Season("summer"),
              piece_name("T_Shirt"), piece_color("black")), salience=1)
    def clothes675(self):
        self.myclothes = Myclothes(1, "white", "short", 0, "", "", 0, "", "", 5, "white", "shose", 0, "", "", 0, "",
                                   "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('Hinking_with_friends'), Gender('male'), Person_type('person'), Season("summer"),
              piece_name("T_Shirt"), piece_color("black")), salience=1)
    def clothes676(self):
        self.myclothes = Myclothes(1, "white", "short", 0, "", "", 0, "", "", 5, "white", "shose", 0, "", "", 0, "",
                                   "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('Hinking_with_friends'), Gender('male'), Person_type('person'), Season("summer"),
              piece_name("T_Shirt"), piece_color("pink")), salience=1)
    def clothes677(self):
        self.myclothes = Myclothes(1, "white", "short", 0, "", "", 0, "", "", 5, "white", "shose", 0, "", "", 0, "",
                                   "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")
        self.result.append(self.myclothes)

    @Rule(AND(age(value=P(lambda value: value >= 10) & P(lambda value: value <= 60)), SkinColor(color='hanatawi'),
              Occasion('Hinking_with_friends'), Gender('male'), Person_type('person'), Season("summer"),
              piece_name("T_Shirt"), piece_color("vinous")), salience=1)
    def clothes678(self):
        self.myclothes = Myclothes(1, "white", "short", 0, "", "", 0, "", "", 5, "white", "shose", 0, "", "", 0, "",
                                   "", 0, " ", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "")


    @Rule(AND(age(value=P(lambda value: value >= 16) & P(lambda value: value <= 35)), SkinColor(color='white'),
              Occasion('wadding'), Gender('male'), Person_type('friend'), Season("summer"), piece_name("dress"),
              piece_color("vinous")), salience=1)
    def clothes859909(self):
        self.myclothes = Myclothes(0, "", "", 0, "", "", 3, "darkblue", "Trousers", 0, " ", "", 5, "white", "shose", 0, "",
                                   "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "", 0, "", "",
                                   0, "", "")
        self.result.append(self.myclothes)