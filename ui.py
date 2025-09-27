from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.spinner import SpinnerOption
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.core.window import Window
from kivy.uix.scrollview import ScrollView

#เอาฟอร์นลงเเสดงspiner เลย
class CSO(SpinnerOption):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.font_name = "font/THSarabunNew.ttf"
        self.font_size = 30
#ใส่ทศนิยมอัตโนมัติ
class ScreenManagerCustom(ScreenManager):
    def textinput4(self,textinput):
        if len(textinput.text) > 5:
            textinput.text = textinput.text[:5] 
        elif len(textinput.text) > 2 and "." not in textinput.text:
            textinput.text = textinput.text[:2]+  "." + textinput.text[3:]
        else: 
            pass



    #เลือกfacultyเเล้วเเบ่งไปตามbranchhhhhhhhhhhhhhhhhhhhhh
    def facultychoose(self):
        faculty = self.ids.choosefaculty.text
        nasp = self.ids.chooseNS.text
        if faculty == "วิทยาการคอม" :
            self.current = "branchcomputerscience" 
        if faculty == "วิศวกรรมศาสตร์":
            self.current = "nolmalspac"
            if nasp == "ปกติ":
                self.current = "branchcomputeregineerA"

            if nasp == "พิเศษ":
                self.current = "branchcomputeregineerB"

            

        else:
            pass
    #เช็ค values เเล้วถึงกด next ได้ เเละลบตัวกรอกคะเเนนที่ไม่ต้องการ คับบบบบ
    def checkbranch(self):
        branchcomputersc = self.ids.choosebranch.text 
        branchcomputereg = self.ids.choosebranch1.text or self.ids.choosebranch2.text
        #วิทยาการคอม
        if branchcomputersc == "วิทยาการคอม" or branchcomputersc == "ปัญญาประดิษฐ์" or branchcomputersc == "ภูมิสารสนเทศศาสตร์" or branchcomputersc == "ความมั่นคงปลอดภัยทางไซเบอร์" or branchcomputersc == "เทคโนโลยีสารสนเทศ" :
            self.current = "score"
            for closetext in [self.ids.scoreche,self.ids.labelche,
                               self.ids.scorebio,self.ids.labelbio,
                               self.ids.scoretpat3,self.ids.labeltpat3]:
                closetext.opacity = 0
                closetext.disabled = True
                closetext.size_hint_y = None
                closetext.height = 0

        #วิศวกรรม
        if branchcomputereg == "วิศวกรรมเกษตร" or branchcomputereg == "วิศวกรรมคอมพิวเตอร์" or branchcomputereg == "วิศวกรรมโทรคมนาคม" or branchcomputereg == "วิศวกรรมไฟฟ้า" or branchcomputereg == "วิศวกรรมโยธา" or branchcomputereg == "วิศวกรรมโลจิสติกส์" or branchcomputereg == "วิศวกรรมสื่อดิจิทัล"or branchcomputereg == "วิศวกรรมอุตสาหการ" :
            self.current = "score"
            for closetext in [self.ids.scorethai,self.ids.labelthai,
                               self.ids.scoretech,self.ids.labeltech,
                               self.ids.scoreche,self.ids.labelche,
                               self.ids.scorebio,self.ids.labelbio
                               ]:
                closetext.opacity = 0
                closetext.disabled = True
                closetext.size_hint_y = None
                closetext.height = 0

        if branchcomputereg == "วิศวกรรมเคมี" :

            self.current = "score"
            for closetext in [self.ids.scoretech,self.ids.labeltech,
                               self.ids.scorebio,self.ids.labelbio
                               ]:
                closetext.opacity = 0
                closetext.disabled = True
                closetext.size_hint_y = None
                closetext.height = 0
        if branchcomputereg == "วิศวกรรมกระบวนการทางเคมี" or branchcomputereg == "วิศวกรรมเครื่องกล" or branchcomputereg == "วิศวกรรมสิ่งเเวดล้อม" :
            self.current = "score"
            for closetext in [ self.ids.scorethai,self.ids.labelthai,
                                self.ids.scoretech,self.ids.labeltech,
                               self.ids.scorebio,self.ids.labelbio
                               ]:
                closetext.opacity = 0
                closetext.disabled = True
                closetext.size_hint_y = None
                closetext.height = 0
        if branchcomputereg == "วิศวกรรมปัญญาประดิษฐ์" or branchcomputereg == "วิศวกรรมระบบอิเล็กทรอนิกส์" :
            
            self.current = "score"
            for closetext in [self.ids.scoreche,self.ids.labelche,
                                self.ids.scoretech,self.ids.labeltech,
                                self.ids.scorebio,self.ids.labelbio
                                ]:
                closetext.opacity = 0
                closetext.disabled = True
                closetext.size_hint_y = None
                closetext.height = 0
        else:
            pass

    
        #คำนวณคะเเนนมหาลัยยยยย        
    def branchchoose(self):
        branchcomputersc = self.ids.choosebranch.text 
        branchcomputereg = self.ids.choosebranch1.text or self.ids.choosebranch2.text
        self.math = self.ids.scoremath.text
        self.thai = self.ids.scorethai.text
        self.eng = self.ids.scoreeng.text
        self.tech = self.ids.scoretech.text
        self.phy = self.ids.scorephy.text
        self.che = self.ids.scoreche.text
        self.bio = self.ids.scorebio.text
        self.tpat3 = self.ids.scoretpat3.text

        #คณะวิทยาการคอม
        if branchcomputersc == "วิทยาการคอม" or branchcomputersc == "ปัญญาประดิษฐ์":
            self.mathb = float(self.math) * 25/100
            self.thaib = float(self.thai) * 5/100
            self.engb = float(self.eng) * 15/100
            self.techb = float(self.tech) * 40/100
            self.phyb = float(self.phy) * 15/100
            self.sum = sum([self.mathb,self.thaib,self.engb,self.techb,self.phyb])

            self.ids.showscoremath.text = f"คือ: {self.mathb:.2f} คะเเนน"
            self.ids.showscorethai.text = f"คือ: {self.thaib:.2f} คะเเนน"
            self.ids.showscoreeng.text = f"คือ: {self.engb:.2f} คะเเนน"
            self.ids.showscoretech.text = f"คือ: {self.techb:.2f} คะเเนน"
            self.ids.showscorephy.text = f"คือ: {self.phyb:.2f} คะเเนน"
            self.ids.showscoresum.text = f"รวมทั้งหมดคือ {self.sum:.2f}คะเเนน"
        if branchcomputersc == "ภูมิสารสนเทศศาสตร์" or branchcomputersc == "ความมั่นคงปลอดภัยทางไซเบอร์":
            self.mathb = float(self.math) * 20/100
            self.thaib = float(self.thai) * 10/100
            self.engb = float(self.eng) * 10/100
            self.techb = float(self.tech) * 45/100
            self.phyb = float(self.phy) * 15/100
            self.sum = sum([self.mathb,self.thaib,self.engb,self.techb,self.phyb])

            self.ids.showscoremath.text = f"คือ: {self.mathb:.2f} คะเเนน"
            self.ids.showscorethai.text = f"คือ: {self.thaib:.2f} คะเเนน"
            self.ids.showscoreeng.text = f"คือ: {self.engb:.2f} คะเเนน"
            self.ids.showscoretech.text = f"คือ: {self.techb:.2f} คะเเนน"
            self.ids.showscorephy.text = f"คือ: {self.phyb:.2f} คะเเนน"
            self.ids.showscoresum.text = f"รวมทั้งหมดคือ {self.sum:.2f}คะเเนน"
        if branchcomputersc == "เทคโนโลยีสารสนเทศ" :
            self.mathb = float(self.math) * 20/100
            self.thaib = float(self.thai) * 10/100
            self.engb = float(self.eng) * 10/100
            self.techb = float(self.tech) * 40/100
            self.phyb = float(self.phy) * 20/100
            self.sum = sum([self.mathb,self.thaib,self.engb,self.techb,self.phyb])

            self.ids.showscoremath.text = f"คือ: {self.mathb:.2f} คะเเนน"
            self.ids.showscorethai.text = f"คือ: {self.thaib:.2f} คะเเนน"
            self.ids.showscoreeng.text = f"คือ: {self.engb:.2f} คะเเนน"
            self.ids.showscoretech.text = f"คือ: {self.techb:.2f} คะเเนน"
            self.ids.showscorephy.text = f"คือ: {self.phyb:.2f} คะเเนน"
            self.ids.showscoresum.text = f"รวมทั้งหมดคือ {self.sum:.2f}คะเเนน"


        #วิศวะคอม 
        if branchcomputereg == "วิศวกรรมเกษตร" or branchcomputereg == "วิศวกรรมไฟฟ้า" :
            self.mathb = float(self.math) * 30/100
            self.engb = float(self.eng) * 20/100
            self.phyb = float(self.phy) * 30/100
            self.tpat3b = float(self.tpat3) * 20/100
            self.sum = sum([self.mathb,self.tpat3b,self.engb,self.phyb])

            self.ids.showscoremath.text = f"คือ: {self.mathb:.2f} คะเเนน"
            self.ids.showscoreeng.text = f"คือ: {self.engb:.2f} คะเเนน"
            self.ids.showscoretpat3.text = f"คือ: {self.tpat3b:.2f} คะเเนน"
            self.ids.showscorephy.text = f"คือ: {self.phyb:.2f} คะเเนน"
            self.ids.showscoresum.text = f"รวมทั้งหมดคือ {self.sum:.2f}คะเเนน"

        if branchcomputereg == "วิศวกรรมคอม" or branchcomputereg == "วิศวกรรมโลจิสติกส์" :
            self.mathb = float(self.math) * 30/100
            self.engb = float(self.eng) * 30/100
            self.phyb = float(self.phy) * 20/100
            self.tpat3b = float(self.tpat3) * 20/100
            self.sum = sum([self.mathb,self.tpat3b,self.engb,self.phyb])

            self.ids.showscoremath.text = f"คือ: {self.mathb:.2f} คะเเนน"
            self.ids.showscoreeng.text = f"คือ: {self.engb:.2f} คะเเนน"
            self.ids.showscoretpat3.text = f"คือ: {self.tpat3b:.2f} คะเเนน"
            self.ids.showscorephy.text = f"คือ: {self.phyb:.2f} คะเเนน"
            self.ids.showscoresum.text = f"รวมทั้งหมดคือ {self.sum:.2f}คะเเนน"

        if branchcomputereg == "วิศวกรรมกระบวนการทางเคมี":
            self.thaib = float(self.thai) * 5/100
            self.mathb = float(self.math) * 30/100
            self.engb = float(self.eng) * 10/100
            self.phyb = float(self.phy) * 30/100
            self.cheb = float(self.che) * 15/100
            self.tpat3b = float(self.tpat3) * 10/100
            self.sum = sum([self.mathb,self.thaib,self.tpat3b,self.engb,self.phyb,self.cheb])

            self.ids.showscoremath.text = f"คือ: {self.mathb:.2f} คะเเนน"
            self.ids.showscorethai.text = f"คือ: {self.thaib:.2f} คะเเนน"
            self.ids.showscoreeng.text = f"คือ: {self.engb:.2f} คะเเนน"
            self.ids.showscoretpat3.text = f"คือ: {self.tpat3b:.2f} คะเเนน"
            self.ids.showscorephy.text = f"คือ: {self.phyb:.2f} คะเเนน"
            self.ids.showscoreche.text = f"คือ: {self.cheb:.2f} คะเเนน"
            self.ids.showscoresum.text = f"รวมทั้งหมดคือ {self.sum:.2f}คะเเนน"

        if branchcomputereg == "วิศวกรรมกระบวนการทางเคมี" :
            self.mathb = float(self.math) * 30/100
            self.engb = float(self.eng) * 20/100
            self.phyb = float(self.phy) * 30/100
            self.cheb = float(self.che) * 10/100
            self.tpat3b = float(self.tpat3) * 10/100
            self.sum = sum([self.mathb,self.tpat3b,self.engb,self.phyb,self.cheb])

            self.ids.showscoremath.text = f"คือ: {self.mathb:.2f} คะเเนน"
            self.ids.showscoreeng.text = f"คือ: {self.engb:.2f} คะเเนน"
            self.ids.showscoretpat3.text = f"คือ: {self.tpat3b:.2f} คะเเนน"
            self.ids.showscorephy.text = f"คือ: {self.phyb:.2f} คะเเนน"
            self.ids.showscoreche.text = f"คือ: {self.cheb:.2f} คะเเนน"
            self.ids.showscoresum.text = f"รวมทั้งหมดคือ {self.sum:.2f}คะเเนน"

        if branchcomputereg == "วิศวกรรมเครื่องกล" :
            self.mathb = float(self.math) * 25/100
            self.engb = float(self.eng) * 10/100
            self.phyb = float(self.phy) * 25/100
            self.cheb = float(self.che) * 10/100
            self.tpat3b = float(self.tpat3) * 30/100
            self.sum = sum([self.mathb,self.tpat3b,self.engb,self.phyb,self.cheb])

            self.ids.showscoremath.text = f"คือ: {self.mathb:.2f} คะเเนน"
            self.ids.showscoreeng.text = f"คือ: {self.engb:.2f} คะเเนน"
            self.ids.showscoretpat3.text = f"คือ: {self.tpat3b:.2f} คะเเนน"
            self.ids.showscorephy.text = f"คือ: {self.phyb:.2f} คะเเนน"
            self.ids.showscoreche.text = f"คือ: {self.cheb:.2f} คะเเนน"
            self.ids.showscoresum.text = f"รวมทั้งหมดคือ {self.sum:.2f}คะเเนน"

        if branchcomputereg == "วิศวกรรมโทรคมนาคม" :
            self.mathb = float(self.math) * 30/100
            self.engb = float(self.eng) * 30/100
            self.phyb = float(self.phy) * 30/100
            self.tpat3b = float(self.tpat3) * 10/100
            self.sum = sum([self.mathb,self.tpat3b,self.engb,self.phyb])

            self.ids.showscoremath.text = f"คือ: {self.mathb:.2f} คะเเนน"
            self.ids.showscoreeng.text = f"คือ: {self.engb:.2f} คะเเนน"
            self.ids.showscoretpat3.text = f"คือ: {self.tpat3b:.2f} คะเเนน"
            self.ids.showscorephy.text = f"คือ: {self.phyb:.2f} คะเเนน"
            self.ids.showscoresum.text = f"รวมทั้งหมดคือ {self.sum:.2f}คะเเนน"

        if branchcomputereg == "วิศวกรรมโยธา" :
            self.mathb = float(self.math) * 35/100
            self.engb = float(self.eng) * 10/100
            self.phyb = float(self.phy) * 35/100
            self.tpat3b = float(self.tpat3) * 20/100
            self.sum = sum([self.mathb,self.tpat3b,self.engb,self.phyb])

            self.ids.showscoremath.text = f"คือ: {self.mathb:.2f} คะเเนน"
            self.ids.showscoreeng.text = f"คือ: {self.engb:.2f} คะเเนน"
            self.ids.showscoretpat3.text = f"คือ: {self.tpat3b:.2f} คะเเนน"
            self.ids.showscorephy.text = f"คือ: {self.phyb:.2f} คะเเนน"
            self.ids.showscoresum.text = f"รวมทั้งหมดคือ {self.sum:.2f}คะเเนน"

        if branchcomputereg == "วิศวกรรมปัญญาประดิษฐ์" or branchcomputereg == "วิศวกรรมระบบอิเล็กทรอนิกส์":
            self.thaib = float(self.thai) * 10/100
            self.mathb = float(self.math) * 30/100
            self.engb = float(self.eng) * 10/100
            self.phyb = float(self.phy) * 30/100
            self.tpat3b = float(self.tpat3) * 20/100
            self.sum = sum([self.mathb,self.thaib,self.tpat3b,self.engb,self.phyb])

            self.ids.showscoremath.text = f"คือ: {self.mathb:.2f} คะเเนน"
            self.ids.showscorethai.text = f"คือ: {self.thaib:.2f} คะเเนน"
            self.ids.showscoreeng.text = f"คือ: {self.engb:.2f} คะเเนน"
            self.ids.showscoretpat3.text = f"คือ: {self.tpat3b:.2f} คะเเนน"
            self.ids.showscorephy.text = f"คือ: {self.phyb:.2f} คะเเนน"
            self.ids.showscoresum.text = f"รวมทั้งหมดคือ {self.sum:.2f}คะเเนน"

        if branchcomputereg == "วิศวกรรมสิ่งเเวดล้อม" :
            self.mathb = float(self.math) * 25/100
            self.engb = float(self.eng) * 15/100
            self.phyb = float(self.phy) * 25/100
            self.cheb = float(self.che) * 15/100
            self.tpat3b = float(self.tpat3) * 20/100
            self.sum = sum([self.mathb,self.tpat3b,self.engb,self.phyb,self.cheb])

            self.ids.showscoremath.text = f"คือ: {self.mathb:.2f} คะเเนน"
            self.ids.showscoreeng.text = f"คือ: {self.engb:.2f} คะเเนน"
            self.ids.showscoretpat3.text = f"คือ: {self.tpat3b:.2f} คะเเนน"
            self.ids.showscorephy.text = f"คือ: {self.phyb:.2f} คะเเนน"
            self.ids.showscoreche.text = f"คือ: {self.cheb:.2f} คะเเนน"
            self.ids.showscoresum.text = f"รวมทั้งหมดคือ {self.sum:.2f}คะเเนน"

        if branchcomputereg == "วิศวกรรมสื่อดิจิทัล" :
            self.mathb = float(self.math) * 30/100
            self.engb = float(self.eng) * 30/100
            self.phyb = float(self.phy) * 30/100
            self.tpat3b = float(self.tpat3) * 10/100
            self.sum = sum([self.mathb,self.tpat3b,self.engb,self.phyb])

            self.ids.showscoremath.text = f"คือ: {self.mathb:.2f} คะเเนน"
            self.ids.showscoreeng.text = f"คือ: {self.engb:.2f} คะเเนน"
            self.ids.showscoretpat3.text = f"คือ: {self.tpat3b:.2f} คะเเนน"
            self.ids.showscorephy.text = f"คือ: {self.phyb:.2f} คะเเนน"
            self.ids.showscoresum.text = f"รวมทั้งหมดคือ {self.sum:.2f}คะเเนน"

        if branchcomputereg == "วิศวกรรมอุตสาหการ" :
            self.mathb = float(self.math) * 30/100
            self.engb = float(self.eng) * 25/100
            self.phyb = float(self.phy) * 25/100
            self.tpat3b = float(self.tpat3) * 20/100
            self.sum = sum([self.mathb,self.tpat3b,self.engb,self.phyb])

            self.ids.showscoremath.text = f"คือ: {self.mathb:.2f} คะเเนน"
            self.ids.showscoreeng.text = f"คือ: {self.engb:.2f} คะเเนน"
            self.ids.showscoretpat3.text = f"คือ: {self.tpat3b:.2f} คะเเนน"
            self.ids.showscorephy.text = f"คือ: {self.phyb:.2f} คะเเนน"
            self.ids.showscoresum.text = f"รวมทั้งหมดคือ {self.sum:.2f}คะเเนน"
        else:
            pass
    
        
    #def getscore(self):
    pass    
class textin(TextInput):
     pass
Window.size = (360,640)
class scroll(ScrollView):
    pass
class UI(App):
    def build(self):
        screenmg = ScreenManagerCustom()
        return screenmg
UI().run()