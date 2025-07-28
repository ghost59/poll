import flet as ft
from controls.controls import Voter_Diplayer



def main(page: ft.Page):
    
    #count = 0 
  #  yes_nay = ft.Text("Waiting")
   # text = ft.Text("0")
    #text2 = ft.Text("0")
 #   def logic(e):
  #      text.value = str(int(text.value) + 1)
   #     page.update()
   # def logic2(e):
    #    text2.value = str(int(text2.value) + 1)
     #   page.update()
   # def textlog(e):
    #    yes_nay.value = text_yet.value
     #   page.update()
    #text_yet = ft.TextField(hint_text="Ues",on_change=textlog)
   # voting1 = ft.Row(controls=[text,ft.ElevatedButton(text="Yes" , on_click=logic)])
   # voting2 = ft.Row(controls=[text2,ft.ElevatedButton(text="No", on_click=logic2)])
    #display = ft.Card(content=ft.Column(controls=[voting1,voting2]))
    page.add(Voter_Diplayer())

ft.app(main)
