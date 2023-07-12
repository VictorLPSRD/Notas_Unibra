import customtkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

#tela principal

janela = tk.CTk()# criando a tela principal !
janela. title('azuos')# titulo 
janela.geometry("1280x720+350+50 ")# tamanho dela !
janela.maxsize(width=900,height=550)
janela.minsize(width=500,height=250)

# imsgem da tela inicial 

imagem = Image.open("imagem2.png")
imagem = imagem.resize((450, 350), Image.ANTIALIAS)
imagem = ImageTk.PhotoImage(imagem)

imagem_label = tk.CTkLabel(janela, image=imagem,text='')
imagem_label.place(x=220,y=-30)

def tela_login():

    janela.withdraw()
    janela2 = tk.CTk()
    janela2.geometry("1280x720+350+50 ")
    janela2.maxsize(width=900,height=550)
    janela2.minsize(width=500,height=250)

    def login():
       
       aluno_certo=aluno.get()
       matricula_certa=matricula.get()
       if (aluno_certo == "unibra" and matricula_certa == 'unibra'):
           tela_media()

       else:
         messagebox.showerror('ERRO :','Uuario ou Matrícula estão errados !')

    texto=tk.CTkLabel(janela2,text='DIGITE SEU \n NOME E SUA \nMATRÍCULA !\n----------------',text_color="white",font=('impact',60))
    texto.place(x=225,y=30)

    seta=tk.CTkLabel(janela2,text='↳',text_color="white",font=('impact',130))
    seta.place(x=350,y=310)
 
    frame= tk.CTkFrame(janela2,height=270,width=300,border_color="white",border_width=2,corner_radius=25)
    frame.place(x=570,y=260)

    login_label=tk.CTkLabel(janela2,text='LOGIN :',text_color="white",font=('impact',30))
    login_label.place(x=605,y=280)

    aluno=tk.CTkEntry(janela2, fg_color='white', placeholder_text=' Aluno...', font=('System', 15),
                                     width=250, border_width=4, corner_radius=25,
                                     height=45, text_color='black')
    aluno.place(x=600,y=325)

    matricula=tk.CTkEntry(janela2, fg_color='white', placeholder_text=' Matricula...',
                                     font=('System', 15),
                                     width=250, border_width=4, corner_radius=25,
                                     height=45, text_color='black',)
    
    matricula.place(x=600,y=375)

    def tela_media():
        
        janela_md = tk.CTk()
        janela2.withdraw()
        janela_md.geometry("1280x720+350+50 ")
        janela_md.maxsize(width=900,height=550)
        janela_md.minsize(width=500,height=250)

        texto=tk.CTkLabel(janela_md,text="# informe as notas\nnos campos\n correspondentes !",text_color="white",font=('impact',27))
        texto.place(x=20,y=180)

        linha=tk.CTkLabel(janela_md,text="-------------------------",text_color="white",font=('impact',27))
        linha.place(x=25,y=290)

        texto2=tk.CTkLabel(janela_md,text="# Grupo Unibra !",text_color="white",font=('arial',27))
        texto2.place(x=550,y=450)

        frame= tk.CTkFrame(janela_md,height=380,width=450,border_color="white",border_width=2,corner_radius=25)
        frame.place(x=240,y=50)

        n1_labol= tk.CTkLabel(janela_md,text='[ NOTA 1 ]',text_color='white',font=('IMPACT',20))
        n1_labol.place(x=420,y=90)
         
        n1=tk.CTkEntry(janela_md, fg_color='white', font=('System', 15),
                                     width=250, border_width=4, corner_radius=25,
                                     height=45, text_color='black')
        n1.place(x=350,y=120)

        n2_labol= tk.CTkLabel(janela_md,text='[ NOTA 2 ]',text_color='white',font=('IMPACT',20))
        n2_labol.place(x=420,y=180)

        n2=tk.CTkEntry(janela_md, fg_color='white', font=('System', 15),
                                     width=250, border_width=4, corner_radius=25,
                                     height=45, text_color='black')
        n2.place(x=350,y=210)

        n3_labol= tk.CTkLabel(janela_md,text='[ NOTA 3 ]',text_color='white',font=('IMPACT',20))
        n3_labol.place(x=420,y=270)
         

        n3=tk.CTkEntry(janela_md, fg_color='white', font=('System', 15),
                                     width=250, border_width=4, corner_radius=25,
                                     height=45, text_color='black')
        n3.place(x=350,y=300)



        def voltar1():
            janela_md.withdraw()
            tela_login()

        def result():  
          
            try:
                nota1=n1.get()
                nota2=n2.get()
                nota3=n3.get()
                soma_nota= (float(nota1)+float(nota2)+float(nota3))
                divisao_nota=(float(soma_nota/3))
                final_nota=(float(10-divisao_nota))

                janela_md.withdraw()

            except ValueError:
                 messagebox.showerror('SYSTEMA','Prencha os campos corretamente !')
                 
            janela_result = tk.CTk()
            janela_result.geometry("1280x720+350+50 ")
            janela_result.maxsize(width=900,height=550)
            janela_result.minsize(width=500,height=250)

            def voltar2():
                janela_result.withdraw()
                tela_media()
            
            frame= tk.CTkFrame(janela_result,height=450,width=300,border_color="white",border_width=2,corner_radius=25)
            frame.place(x=55,y=80)
            
            texto_result=tk.CTkLabel(janela_result,text='BOAS FÉRIAS ! \n OU NÃO...',text_color="white",font=('impact',45))
            texto_result.place(x=490,y=190)

            media_label=tk.CTkLabel(janela_result,text="Sua média foi :",text_color="white",font=('IMPACT',40))
            media_label.place(x=95,y=130)

            bnt_voltar_notas=tk.CTkButton(janela_result,text="<voltar",width=50,height=40,border_width=4, corner_radius=25,command=voltar2)
            bnt_voltar_notas.place(x=20,y=20)

            if divisao_nota <=7:
                recu=tk.CTkLabel(janela_result,text=(f'{divisao_nota:.2f}'),text_color="red",font=('IMPACT',40))
                recu.place(x=160,y=250)

                reprovado=tk.CTkLabel(janela_result,text=' Reprovado  !',text_color="white",font=('IMPACT',40))
                reprovado.place(x=100,y=380)

                final=tk.CTkLabel(janela_result,text=(f' Você tem que tira\n{final_nota:.2f} na final ! '),text_color="white",font=('arial',20))
                final.place(x=115,y=450)

                emoji=tk.CTkLabel(janela_result,text='🤕',text_color="white",font=('',70))
                emoji.place(x=370,y=190)
                
                emoji1=tk.CTkLabel(janela_result,text='😵',text_color="white",font=('',70))
                emoji1.place(x=570,y=80)

                emoji2=tk.CTkLabel(janela_result,text='🥺',text_color="white",font=('',70))
                emoji2.place(x=480,y=350)

                emoji3=tk.CTkLabel(janela_result,text='💔',text_color="white",font=('',70))
                emoji3.place(x=660,y=350)
                
                emoji4=tk.CTkLabel(janela_result,text='😥',text_color="white",font=('',70))
                emoji4.place(x=740,y=190)
                
            else:
                apro=tk.CTkLabel(janela_result,text=(f'{divisao_nota:.2f}'),text_color="#11F128",font=('IMPACT',40))
                apro.place(x=160,y=250)
                parabens=tk.CTkLabel(janela_result,text=' Parabéns  !',text_color="white",font=('IMPACT',40))
                parabens.place(x=100,y=380)

                emoji=tk.CTkLabel(janela_result,text='😍',text_color="white",font=('',70))
                emoji.place(x=370,y=190)
                
                emoji1=tk.CTkLabel(janela_result,text='🥳',text_color="white",font=('',70))
                emoji1.place(x=530,y=80)

                emoji2=tk.CTkLabel(janela_result,text='🫰',text_color="white",font=('',70))
                emoji2.place(x=555,y=350)

                emoji3=tk.CTkLabel(janela_result,text='♡',text_color="white",font=('',80))
                emoji3.place(x=680,y=80)

                emoji4=tk.CTkLabel(janela_result,text='😺',text_color="white",font=('',70))
                emoji4.place(x=740,y=190)


            janela_result.mainloop()

        bnt_voltar = tk.CTkButton(janela_md,text="<voltar",width=50,height=40,border_width=4, corner_radius=25,command=voltar1)
        bnt_voltar.place(x=20,y=20)
        bnt_md = tk.CTkButton(janela_md,text="CONTINUAR",width=100,height=40,border_width=4, corner_radius=25,font=('system',25),command=result)
        bnt_md.place(x=465,y=360)
        
        
        

        janela_md.mainloop()

    bnt_janela2 = tk.CTkButton(janela2,text="CONTINUAR",width=250,height=70,border_width=4, corner_radius=25,font=('system',25),command=login)
    bnt_janela2.place(x=600,y=435)

    janela2.mainloop()



frame_janela= tk.CTkFrame(janela,height=165,width=300,border_color="white",border_width=2,corner_radius=25).place(x=300, y=240)
texto_janla=tk.CTkLabel(janela,text='Média do aluno',font=('IMPACT',30)).place(x=355,y=260)
btk_janela= tk.CTkButton(janela,text="INICIAR",font=('system',25),width=250,height=70,border_width=4, corner_radius=25,command=tela_login).place(x=325, y=310)


janela.mainloop()