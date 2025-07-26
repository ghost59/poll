import flet as ft 

class Voter_Diplayer(ft.Column):
    def __init__(self, vote, ):
        self.vote = vote
        self.button = ft.ElevatedButton(on_click=self.logic_vote())
        self.button2 = ft.ElevatedButton(on_click=self.logic_vote())
        testbut = ft.ElevatedButton()
        
    def displays(self):
        self.controls = []
        def Bage_show(self,icon, size):
            return ft.Container(ft.Icon(),width=size, height=size,)
            
        normal_radius = 100 
        self.diplay_task = ft.Column( controls=[])
        self.result_display = ft.PieChart( sections=[ft.PieChartSection(
            self.vote, title=ft.Text(f"{self.vote}"),
            color=ft.Colors.RED, 
            radius=normal_radius,
             badge=Bage_show(icon=ft.Icons.WHERE_TO_VOTE, size=60)), 
             ft.PieChartSection()], visible=False
             )
        return self.controls

    def logic_vote(self):
        self.vote += 1

        
        