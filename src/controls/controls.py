import flet as ft 

class Voter_Diplayer(ft.Column):
    def __init__(self):
        super().__init__()
        '''
        This class is the display for the page votes to be added. What happpens is that vote is 
        appended to the column and you are able to vote between two ideas. The ideas can be edited with the
        poll input, which will change the text. So lets say tacos vs coffe. YOu can change the text using input1 and 2 for the 
        votes when you add them. So before pressing add. type in something. 
        
        '''
        self.text = ft.Text("vote")
        self.poll_input = ft.TextField( hint_text="Poll", on_change=self.textlog)
        self._input = ft.TextField( hint_text="Poll",width=50)
        self._input2 = ft.TextField( hint_text="Poll",width=50)
        self.display = ft.Column( controls=[self.text, self.poll_input,self._input,self._input2,ft.ElevatedButton(text="add" ,on_click=self.add)])

        self.controls = [self.display]

    def textlog(self,e):
        self.text.value = self.poll_input.value
        e.page.update()
    def add(self,e):
        adds = vote(text=self._input.value,text2=self._input2.value)
        self.display.controls.append(adds)
        adds.name.value = self.poll_input.value
        e.page.update()

        
class vote(ft.Column):
    def __init__(self,text,text2):
        super().__init__()
        '''
        adds a column that contains where people will be voting, 
        has two buttons that adds up the votes what the person votes for.
        Not perfect but it works.  
        '''
        self.number = ft.Text("0")
        self.number2 = ft.Text("0")
        self.text = ft.Text(text)
        self.text2 = ft.Text(text2)
        self.width = 200
        self.height = 100
        self.counts = 0
        self.but = ft.ElevatedButton(text="vote1",on_click=self.count)
        self.but2 = ft.ElevatedButton(text="vote2",on_click=self.count2)
        self.voter1 = ft.Row(controls=[self.number,self.text, self.but])
        self.voter2 = ft.Row(controls=[self.number2,self.text2 ,self.but2])
        self.diplay = ft.Row(controls=[ft.Container(content=ft.Column(controls=[self.voter1,self.voter2]),
                                                    height=100, 
                                                    width=200,bgcolor=ft.colors.DEEP_ORANGE_500,border_radius=ft.border_radius.all(5.6))],)
        self.controls = [self.diplay]

    def count(self,e):
        self.number.value = str(int(self.number.value) + 1)
        e.page.update()
    def count2(self,e):
        self.number2.value = str(int(self.number2.value) + 1)
        e.page.update()
    