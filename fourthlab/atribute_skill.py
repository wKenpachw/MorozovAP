import random
class Atribute_skill(object):
    _name           = str()
    _val            = int()
    _atr_val        = int()
    _mastered       = bool()
    _mastered_val   = int()

    """ имя навыка, молификатор атрибута, освоен ли, бонус мастерства"""
    def  __init__(self, name: str, atr_mod_value: int, mastered: bool, mastered_val:int ):
        self._name = name
        self._mastered = mastered
        self._mastered_val = mastered_val
        self.set_mastered_val()
        self._atr_val = atr_mod_value
        self._val = self.get_val()
       

    def set_mastered_val(self):
        if self._mastered:
            self._mastered_val = self._mastered_val
        else:
            self._mastered_val = 0

    def update_val(self, val):
        self._atr_val = val

    def get_val(self):
        return (self._atr_val + self._mastered_val)

    def get_name(self):
        return self._name

    def get_mastered(self):
        return self._mastered

    def check_skill(self):
        return int(random.randint(1, 20)) + int(self._val)

if __name__ == "__main__":
    skill = Atribute_skill("atl", 4, True, 2)
    skill.update_val(1)
    print("значение атрибута = " + str(skill._atr_val))
    print("добавить бонус мастерства? ответ:" + str(skill._mastered))
    print("бонус мастерства = " + str(skill._mastered_val))
    print("значение навыка = " + str(skill.get_val()))
    print("спасбросок = " + str(skill.check_skill()))    
