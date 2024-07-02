import tkinter as tk
from tkinter import filedialog
import pandas as pd
from pandastable import Table, TableModel
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from PIL import ImageGrab, Image
from molmass import Formula
import matplotlib as mpl
from tkinter import ttk

class MassSpectrumAnalyzer:
    def __init__(self,root):
        
        #Initialisation de la fenêtre
        
        self.root = root
        root.title('Mass spectrum analyzer V 0.5')
        root.iconbitmap("Icon.ico")
        root.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}")
        root.config(bg="#EBECF0")
        
        #Création des deux frames : gauche = entrées, droite = résultats

        
        self.left_frame  =  tk.Frame(root,  width=200,  height=400,  bg='white')
        self.left_frame.pack(side='left',  padx=10,  pady=5)

        self.right_frame  =  tk.Frame(root,  width=650,  height=400,  bg='white')
        self.right_frame.pack(side='right',  fill='both',  padx=10,  pady=5,  expand=True)
        
        tk.Label(self.left_frame, text="Données d'analyse").pack(side='top',padx=5,pady=5)
        
        #Affichage des logos
        
        self.image_path = "logoUMET.png"  
        self.image = tk.PhotoImage(file=self.image_path)
        self.image_label = tk.Label(self.left_frame, image=self.image, bg='white')
        self.image_label.pack(side = 'left', pady=10, anchor ='ne')
        
        self.image_path1 = "logoUnivLille.png"
        self.image1 = tk.PhotoImage(file=self.image_path1)
        self.image_label1 = tk.Label(self.left_frame,image=self.image1, bg='white')
        self.image_label1.pack(side = 'right', pady=10, anchor ='nw')
        
        #Frame pour les bouts de chaînes
        
        BDC = tk.LabelFrame(self.left_frame, text="Bouts de chaînes", padx=5, pady=5)
        BDC.pack(side ='top',fill='y', pady=10)
        
        #Frame pour le bouts de chaînes 1
        
        BDC1 = tk.LabelFrame(BDC, text="Bout de chaînes 1", padx=5, pady=5)
        BDC1.pack(side ='top',fill='y', padx=10, pady=10)
        
        
        self.NomBDC1 = tk.StringVar()
        NomBDC1_label = tk.Label(BDC1, text="Nom")
        NomBDC1_entry = tk.Entry(BDC1, textvariable=self.NomBDC1, width=15)
        NomBDC1_label.pack(side ='left')
        NomBDC1_entry.pack(side ='left',padx=10)
        
        self.CarboneBDC1 = tk.IntVar()
        CarboneBDC1_label = tk.Label(BDC1, text="C")
        CarboneBDC1_entry = tk.Entry(BDC1, textvariable=self.CarboneBDC1, width=5)
        CarboneBDC1_label.pack(side ='left')
        CarboneBDC1_entry.pack(side ='left',padx=10)
        
        self.HydrogeneBDC1 = tk.IntVar()
        HydrogeneBDC1_label = tk.Label(BDC1, text="H")
        HydrogeneBDC1_entry = tk.Entry(BDC1, textvariable=self.HydrogeneBDC1, width=5)
        HydrogeneBDC1_label.pack(side ='left')
        HydrogeneBDC1_entry.pack(side ='left',padx=10)
        
        self.OxygeneBDC1 = tk.IntVar()
        OxygeneBDC1_label = tk.Label(BDC1, text="O")
        OxygeneBDC1_entry = tk.Entry(BDC1, textvariable=self.OxygeneBDC1, width=5)
        OxygeneBDC1_label.pack(side ='left')
        OxygeneBDC1_entry.pack(side ='left',padx=10)
        
        self.SoufreBDC1 = tk.IntVar()
        SoufreBDC1_label = tk.Label(BDC1, text="S")
        SoufreBDC1_entry = tk.Entry(BDC1, textvariable=self.SoufreBDC1, width=5)
        SoufreBDC1_label.pack(side ='left')
        SoufreBDC1_entry.pack(side ='left',padx=10)
        
        self.AzoteBDC1 = tk.IntVar()
        AzoteBDC1_label = tk.Label(BDC1, text="N")
        AzoteBDC1_entry = tk.Entry(BDC1, textvariable=self.AzoteBDC1, width=5)
        AzoteBDC1_label.pack(side ='left')
        AzoteBDC1_entry.pack(side ='left',padx=10)
        
        self.BromeBDC1 = tk.IntVar()
        BromeBDC1_label = tk.Label(BDC1, text="Br")
        BromeBDC1_entry = tk.Entry(BDC1, textvariable=self.BromeBDC1, width=5)
        BromeBDC1_label.pack(side ='left')
        BromeBDC1_entry.pack(side ='left',padx=10)
        
        #Frame pour le bouts de chaînes 2
        
        BDC2 = tk.LabelFrame(BDC, text="Bout de chaînes 2", padx=5, pady=5)
        BDC2.pack(side ='top',fill='y', padx=10, pady=10)
        
        self.NomBDC2 = tk.StringVar()
        NomBDC2_label = tk.Label(BDC2, text="Nom")
        NomBDC2_entry = tk.Entry(BDC2, textvariable=self.NomBDC2, width=15)
        NomBDC2_label.pack(side ='left')
        NomBDC2_entry.pack(side ='left',padx=10)
        
        self.CarboneBDC2 = tk.IntVar()
        CarboneBDC2_label = tk.Label(BDC2, text="C")
        CarboneBDC2_entry = tk.Entry(BDC2, textvariable=self.CarboneBDC2, width=5)
        CarboneBDC2_label.pack(side ='left')
        CarboneBDC2_entry.pack(side ='left',padx=10)
        
        self.HydrogeneBDC2 = tk.IntVar()
        HydrogeneBDC2_label = tk.Label(BDC2, text="H")
        HydrogeneBDC2_entry = tk.Entry(BDC2, textvariable=self.HydrogeneBDC2, width=5)
        HydrogeneBDC2_label.pack(side ='left')
        HydrogeneBDC2_entry.pack(side ='left',padx=10)
        
        self.OxygeneBDC2 = tk.IntVar()
        OxygeneBDC2_label = tk.Label(BDC2, text="O")
        OxygeneBDC2_entry = tk.Entry(BDC2, textvariable=self.OxygeneBDC2, width=5)
        OxygeneBDC2_label.pack(side ='left')
        OxygeneBDC2_entry.pack(side ='left',padx=10)
        
        self.SoufreBDC2 = tk.IntVar()
        SoufreBDC2_label = tk.Label(BDC2, text="S")
        SoufreBDC2_entry = tk.Entry(BDC2, textvariable=self.SoufreBDC2, width=5)
        SoufreBDC2_label.pack(side ='left')
        SoufreBDC2_entry.pack(side ='left',padx=10)
        
        self.AzoteBDC2 = tk.IntVar()
        AzoteBDC2_label = tk.Label(BDC2, text="N")
        AzoteBDC2_entry = tk.Entry(BDC2, textvariable=self.AzoteBDC2, width=5)
        AzoteBDC2_label.pack(side ='left')
        AzoteBDC2_entry.pack(side ='left',padx=10)
        
        self.BromeBDC2 = tk.IntVar()
        BromeBDC2_label = tk.Label(BDC2, text="Br")
        BromeBDC2_entry = tk.Entry(BDC2, textvariable=self.BromeBDC2, width=5)
        BromeBDC2_label.pack(side ='left')
        BromeBDC2_entry.pack(side ='left',padx=10)
        
        #Frame pour le bouts de chaînes 3
        
        BDC3 = tk.LabelFrame(BDC, text="Bout de chaînes 3", padx=5, pady=5)
        BDC3.pack(side ='top',fill='y', padx=10, pady=10)
        
        self.NomBDC3 = tk.StringVar()
        NomBDC3_label = tk.Label(BDC3, text="Nom")
        NomBDC3_entry = tk.Entry(BDC3, textvariable=self.NomBDC3, width=15)
        NomBDC3_label.pack(side ='left')
        NomBDC3_entry.pack(side ='left',padx=10)
        
        self.CarboneBDC3 = tk.IntVar()
        CarboneBDC3_label = tk.Label(BDC3, text="C")
        CarboneBDC3_entry = tk.Entry(BDC3, textvariable=self.CarboneBDC3, width=5)
        CarboneBDC3_label.pack(side ='left')
        CarboneBDC3_entry.pack(side ='left',padx=10)
        
        self.HydrogeneBDC3 = tk.IntVar()
        HydrogeneBDC3_label = tk.Label(BDC3, text="H")
        HydrogeneBDC3_entry = tk.Entry(BDC3, textvariable=self.HydrogeneBDC3, width=5)
        HydrogeneBDC3_label.pack(side ='left')
        HydrogeneBDC3_entry.pack(side ='left',padx=10)
        
        self.OxygeneBDC3 = tk.IntVar()
        OxygeneBDC3_label = tk.Label(BDC3, text="O")
        OxygeneBDC3_entry = tk.Entry(BDC3, textvariable=self.OxygeneBDC3, width=5)
        OxygeneBDC3_label.pack(side ='left')
        OxygeneBDC3_entry.pack(side ='left',padx=10)
        
        self.SoufreBDC3 = tk.IntVar()
        SoufreBDC3_label = tk.Label(BDC3, text="S")
        SoufreBDC3_entry = tk.Entry(BDC3, textvariable=self.SoufreBDC3, width=5)
        SoufreBDC3_label.pack(side ='left')
        SoufreBDC3_entry.pack(side ='left',padx=10)
        
        self.AzoteBDC3 = tk.IntVar()
        AzoteBDC3_label = tk.Label(BDC3, text="N")
        AzoteBDC3_entry = tk.Entry(BDC3, textvariable=self.AzoteBDC3, width=5)
        AzoteBDC3_label.pack(side ='left')
        AzoteBDC3_entry.pack(side ='left',padx=10)
        
        self.BromeBDC3 = tk.IntVar()
        BromeBDC3_label = tk.Label(BDC3, text="Br")
        BromeBDC3_entry = tk.Entry(BDC3, textvariable=self.BromeBDC3, width=5)
        BromeBDC3_label.pack(side ='left')
        BromeBDC3_entry.pack(side ='left',padx=10)
        
        #Frame pour l'unité répétitrice
        
        UR = tk.LabelFrame(self.left_frame, text="Unité répetitrice", padx=5, pady=5)
        UR.pack(side ='top',fill='y', padx=10, pady=10)
        
        self.CarboneUR = tk.IntVar()
        CarboneUR_label = tk.Label(UR, text="C")
        CarboneUR_entry = tk.Entry(UR, textvariable=self.CarboneUR, width=5)
        CarboneUR_label.pack(side ='left')
        CarboneUR_entry.pack(side ='left',padx=10)
        
        self.HydrogeneUR = tk.IntVar()
        HydrogeneUR_label = tk.Label(UR, text="H")
        HydrogeneUR_entry = tk.Entry(UR, textvariable=self.HydrogeneUR, width=5)
        HydrogeneUR_label.pack(side ='left')
        HydrogeneUR_entry.pack(side ='left',padx=10)
        
        self.OxygeneUR = tk.IntVar()
        OxygeneUR_label = tk.Label(UR, text="O")
        OxygeneUR_entry = tk.Entry(UR, textvariable=self.OxygeneUR, width=5)
        OxygeneUR_label.pack(side ='left')
        OxygeneUR_entry.pack(side ='left',padx=10)
        
        self.SoufreUR = tk.IntVar()
        SoufreUR_label = tk.Label(UR, text="S")
        SoufreUR_entry = tk.Entry(UR, textvariable=self.SoufreUR, width=5)
        SoufreUR_label.pack(side ='left')
        SoufreUR_entry.pack(side ='left',padx=10)
        
        self.AzoteUR = tk.IntVar()
        AzoteUR_label = tk.Label(UR, text="N")
        AzoteUR_entry = tk.Entry(UR, textvariable=self.AzoteUR, width=5)
        AzoteUR_label.pack(side ='left')
        AzoteUR_entry.pack(side ='left',padx=10)
        
        self.BromeUR = tk.IntVar()
        BromeUR_label = tk.Label(UR, text="Br")
        BromeUR_entry = tk.Entry(UR, textvariable=self.BromeUR, width=5)
        BromeUR_label.pack(side ='left')
        BromeUR_entry.pack(side ='left',padx=10)
        
        #Charge à chercher
        
        CM = tk.LabelFrame(self.left_frame, text="Charge", padx=5, pady=5)
        CM.pack(side ='top',fill='y', padx=10, pady=10)
        
        self.CheckCharge1 = tk.BooleanVar()
        self.CheckCharge2 = tk.BooleanVar()
        self.CheckCharge3 = tk.BooleanVar()
        self.CheckCharge4 = tk.BooleanVar()
        self.CheckCharge5 = tk.BooleanVar()
        self.CheckCharge6 = tk.BooleanVar()
        self.CheckCharge7 = tk.BooleanVar()
        self.CheckCharge8 = tk.BooleanVar()
        self.CheckCharge9 = tk.BooleanVar()
        self.CheckCharge10 = tk.BooleanVar()
        
        self.Charge1 = tk.Checkbutton(CM,variable = self.CheckCharge1, text="1", onvalue=True,offvalue=False)
        self.Charge2 = tk.Checkbutton(CM,variable = self.CheckCharge2, text="2", onvalue=True,offvalue=False)
        self.Charge3 = tk.Checkbutton(CM,variable = self.CheckCharge3, text="3", onvalue=True,offvalue=False)
        self.Charge4 = tk.Checkbutton(CM,variable = self.CheckCharge4, text="4", onvalue=True,offvalue=False)
        self.Charge5 = tk.Checkbutton(CM,variable = self.CheckCharge5, text="5", onvalue=True,offvalue=False)
        self.Charge6 = tk.Checkbutton(CM,variable = self.CheckCharge6, text="6", onvalue=True,offvalue=False)
        self.Charge7 = tk.Checkbutton(CM,variable = self.CheckCharge7, text="7", onvalue=True,offvalue=False)
        self.Charge8 = tk.Checkbutton(CM, variable = self.CheckCharge8,text="8", onvalue=True,offvalue=False)
        self.Charge9 = tk.Checkbutton(CM,variable = self.CheckCharge9, text="9", onvalue=True,offvalue=False)
        self.Charge10 = tk.Checkbutton(CM,variable = self.CheckCharge10, text="10", onvalue=True,offvalue=False)
        
        self.Charge1.pack(side='left',padx = 5)
        self.Charge2.pack(side='left',padx = 5)
        self.Charge3.pack(side='left',padx = 5)
        self.Charge4.pack(side='left',padx = 5)
        self.Charge5.pack(side='left',padx = 5)
        self.Charge6.pack(side='left',padx = 5)
        self.Charge7.pack(side='left',padx = 5)
        self.Charge8.pack(side='left',padx = 5)
        self.Charge9.pack(side='left',padx = 5)
        self.Charge10.pack(side='left',padx = 5)
        
        #Curseur pour la tolérance
        
        self.tolerance_var = tk.Scale(self.left_frame, from_=0, to=50, orient='horizontal',command=self.tolérance_paire,length=200)
        tolerance_label = tk.Label(self.left_frame, text="Tolérance (ppm) :")
        self.tolerance_var.set(10)
        tolerance_label.pack(side ='top',padx=10, pady=0)
        self.tolerance_var.pack(side ='top',padx=10, pady=5)
        
        #DP Max
        
        self.DPMax_var = tk.IntVar()
        DPMax_label = tk.Label(self.left_frame,text="DP maximum")
        DPMax_entry = tk.Entry(self.left_frame,textvariable=self.DPMax_var)
        DPMax_label.pack(side='top',padx=10,pady=10)
        DPMax_entry.pack(side='top',padx=10,pady=10)
        
        # Boutton d'accès aux options avancées
        
        self.advanced_options_button = tk.Button(self.left_frame, text="Options avancées", command=self.ouvrir_options_avancées)
        self.advanced_options_button.pack(side ='top',padx=10, pady=5)
        
        self.adduit_var = tk.StringVar()
        self.adduit_var = "Na"
        
        self.AbondanceIsoMinimum = tk.IntVar()
        self.AbondanceIsoMinimum = 90
        
        #Boutton pour charger le fichier CSV
        
        chargerCSV_button = tk.Button(self.left_frame, text='Charger le fichier CSV', command=self.charger_CSV)
        chargerCSV_button.pack(side='top',padx=10,pady=10)
        
        
        #Boutton pour lancer l'analyse du spectre
        
        lancer_analyser_button = tk.Button(self.left_frame, text="Lancer l'analyse", command=self.launch_analyse)
        lancer_analyser_button.pack(side ='top', padx=10,pady=10)
        
        self.fig, (self.ax1,self.ax3) = plt.subplots(2, 1)
        self.fig.patch.set_facecolor('white')
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.right_frame)
        self.widget = self.canvas.get_tk_widget()
        self.widget.pack(side ='top',expand = True, fill = 'both', padx=5, pady=5)
        
        #Boutton quitter
        
        self.quit_button = tk.Button(self.left_frame, text='Quitter', command=root.destroy)
        self.quit_button.pack(side='bottom', padx= 5, pady=5)
        
        #Tableau contenant les résultats
        
        self.DFR = tk.LabelFrame(self.left_frame, text="Tableau résulat", padx=5, pady=5)
        self.DFR.pack(side ='bottom',fill='both',expand=True, padx=10, pady=10)
        
    def ouvrir_options_avancées(self):
        
          """
          Cette fonction permet de gérer l'affichage de la fenêtre des paramètres avancés
          """
          
          advanced_window = tk.Toplevel(root)  # Create a new window
          advanced_window.title("Options avancées")
          advanced_window.geometry("520x360")
        
          label_adduit = tk.Label(advanced_window, text="Adduit formé")
          label_adduit.pack(side='top',padx=10, pady =10)
          
          AdduitPossible = ["Na","H","K","Li","NH4"]
          Adduit_var =  tk.StringVar(value=AdduitPossible[0])
          
          plot_menuCharge = tk.OptionMenu(advanced_window, Adduit_var,*AdduitPossible)
          plot_menuCharge.pack(side='top',padx=10, pady =10)
          
          label_isotope_treshold = tk.Label(advanced_window, text="Abondance relative minimum")
          label_isotope_treshold.pack(side='top',padx=10, pady =10)
          
          AbondanceIsoMin_var = tk.IntVar(value=90)
          AbondanceIsoMin_entry = tk.Entry(advanced_window, textvariable=AbondanceIsoMin_var)
          AbondanceIsoMin_entry.pack(side='top',padx=10, pady =10)
          
        
          def récupérer_infos_et_fermer():
            """
            Fonction permettant de récupérer les informations de la fenêtres des options avancées
            """
              
            self.adduit_var = Adduit_var.get()
            self.AbondanceIsoMinimum = AbondanceIsoMin_var.get()
            advanced_window.destroy()  
        
          # Close button
          close_button = tk.Button(advanced_window, text="Close", command=récupérer_infos_et_fermer)
          close_button.pack()
            
          advanced_window.mainloop()  

    def tolérance_paire(self, val):
        """
        Cette fonction assure que la valeur de la tolérance est un nombre pair
        """
        if int(val) % 2 != 0:
            self.tolerance_var.set(int(val) // 2 * 2)
        else:
            self.tolerance_var.set(val)
            
    def charger_CSV(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.dfOriginal = pd.read_csv(file_path,index_col=False, usecols=["Center X", "Height", "Z"])
            
    def MasseMono(self,C1,H1,O1,N1,S1,Br1,C2,H2,O2,N2,S2,Br2,LDC,Adduit):
        
        """
        Cette fonction permet d'obtenir la masse monoisotopique d'un polymère donné
        """
        
        Polymere = ""
        C = C1 + LDC*C2
        H = H1 + LDC*H2
        O = O1 + LDC*O2
        N = N1 + LDC*N2
        S = S1 + LDC*S2
        Br = Br1 + LDC*Br2
                
        if C !=0:
            Polymere+="C"
            Polymere+=str(C)
        if H !=0:
            Polymere+="H"
            Polymere+=str(H)
        if O !=0:
            Polymere+="O"
            Polymere+=str(O)
        if N !=0:
            Polymere+="N"
            Polymere+=str(N)
        if S !=0:
            Polymere+="S"
            Polymere+=str(S)
        if Br !=0:
            Polymere+="Br"
            Polymere+=str(Br)
            
        
        PolymereFormula = Formula(Polymere)
        
        return PolymereFormula.monoisotopic_mass
        
    def FaireTMO_I(self,C1,H1,O1,N1,S1,Br1,C2,H2,O2,N2,S2,Br2,charge,LDC, Adduit = "Na", AbondanceMin = 90):
        
        """
        Cette fonction permet d'obtenir les masses observables et leur distribution isotopique à partir de la formule brute des bouts de chaînes et de la
        formule brute de l'unité répetitrice
        
        INPUT
        
        C1 : nombre de carbone dans les bouts de chaînes
        H1 : nombre d'hydrogènes dans les bouts de chaînes
        O1 : nombre d'oxygène dans les bouts de chaînes
        N1 : nombre d'azote dans les bouts de chaînes
        S1 : nombre de soufre dans les bouts de chaînes
        
        C2 : nombre de carbone dans l'unité répetitrice
        H2 : nombre d'hydrogènes dans l'unité répetitrice
        O2 : nombre d'oxygène dans l'unité répetitrice
        N2 : nombre d'azote dans l'unité répetitrice
        S2 : nombre de soufre dans l'unité répetitrice
        
        charge : tableau contenant la valeur des masses à chercher
        LDC : longeur de chaîne maximale observable
        
        Adduit : type d'adduit formé
        AbondanceMin : Abondance relative minimum des isotopes générés 
        OUTPUT
        
        TableauMassesObservables : tableau contenant pour chaque polymère observable le pic mono isotopique
        TableauMassesObservablesEtIsotopes : tableau pour chaque polymère observable des isotopes et de leur abondance relative
        """
        
        TableauMassesObservables = []
        TableauMassesObservablesEtIsotopes = []

        for i in charge:
            TempTMO = []
            TempTMOI = []
            for s in range(1,LDC+1):  
                Polymere = ""
                C = C1 + s*C2
                H = H1 + s*H2
                O = O1 + s*O2
                N = N1 + s*N2
                S = S1 + s*S2
                Br = Br1 + s*Br2
                        
                if C !=0:
                    Polymere+="C"
                    Polymere+=str(C)
                if H !=0:
                    Polymere+="H"
                    Polymere+=str(H)
                if O !=0:
                    Polymere+="O"
                    Polymere+=str(O)
                if N !=0:
                    Polymere+="N"
                    Polymere+=str(N)
                if S !=0:
                    Polymere+="S"
                    Polymere+=str(S)
                if Br !=0:
                    Polymere+="Br"
                    Polymere+=str(Br)
                    
                Polymere += Adduit
                Polymere += str(i)
                
                PolymereFormula = Formula(Polymere)
                test = PolymereFormula.spectrum(min_intensity = 99.999999999).dataframe()
                TempTMO.append([test['Relative mass'].iloc[0]/i, i])
                Res = PolymereFormula.spectrum(min_intensity = AbondanceMin).dataframe()
                Res = Res.reset_index()
                Res = Res[['Relative mass', 'm/z','Intensity %']]
                Res['m/z'] = Res['Relative mass']/i
                TempTMOI.append([[Res['Relative mass'][t], Res['m/z'][t],Res['Intensity %'][t],i] for t in range(Res.shape[0])])  
            TableauMassesObservables.append(TempTMO)
            TableauMassesObservablesEtIsotopes.append(TempTMOI)
        return TableauMassesObservables,TableauMassesObservablesEtIsotopes

        
    def trouver_valeur_df(self, valeur, df, tolerance):
          """
          Fonction qui utilise la recherche dichotomique pour trouver la valeur la plus proche d'une valeur donnée dans un DataFrame avec une tolérance variable.
        
          INPUT:
            valeur: La valeur à comparer.
            df: Un DataFrame contenant les valeurs à comparer ('Center X' et 'Height').
            tolerance: La tolérance en ppm (pourcentage par million).
        
          OUPUT:
            Une liste contenant:
              - True si la valeur a été trouvée, False sinon.
              - La valeur de 'Center X' la plus proche.
              - La valeur de 'Height' correspondante.
              - L'index de la ligne correspondante dans le DataFrame.
              - La distance relative (différence / valeur * 10^6).
          """
        
          # Tri du DataFrame par 'Center X'
          df_trie = df.sort_values(by='Center X')
        
          # Valeurs initiales
          valeur_la_plus_proche = None
          distance_minimale = float("inf")
          debut = 0
          fin = df_trie.shape[0] - 1
        
          # Recherche dichotomique
          while debut <= fin:
            milieu = (debut + fin) // 2
            valeur_milieu = df_trie['Center X'].iloc[milieu]
        
            # Si la valeur du milieu est égale à la valeur recherchée, on retourne directement
            if valeur_milieu == valeur:
              return [True, valeur_milieu, df_trie['Height'].iloc[milieu], milieu, 0.0]
        
            # Si la valeur du milieu est plus petite que la valeur recherchée, on cherche à droite
            elif valeur_milieu < valeur:
              debut = milieu + 1
            
            # Sinon, on cherche à gauche
            else:
              fin = milieu - 1
              
          if debut == df_trie.shape[0]:
              valeur_la_plus_proche =df_trie['Center X'].iloc[debut-1]
              distance_minimale = abs(valeur_la_plus_proche - valeur)
              index_min = df[df['Center X'] == valeur_la_plus_proche].index[0]
          elif fin == -1:
              valeur_la_plus_proche = df_trie['Center X'].iloc[fin+1]
              distance_minimale = abs(valeur_la_plus_proche - valeur)
              index_min = df[df['Center X'] == valeur_la_plus_proche].index[0]
              
          # Si on n'a pas trouvé la valeur exacte, on calcule la distance minimale et la valeur la plus proche
          elif debut > fin:
            if fin >= 0 and fin < df_trie.shape[0] - 1 and abs(df_trie['Center X'].iloc[fin] - valeur) < abs(df_trie['Center X'].iloc[fin + 1] - valeur):
              valeur_la_plus_proche = df_trie['Center X'].iloc[fin]
              distance_minimale = abs(valeur_la_plus_proche - valeur)
              index_min = df[df['Center X'] == valeur_la_plus_proche].index[0]
            else:
              valeur_la_plus_proche = df_trie['Center X'].iloc[fin + 1]
              distance_minimale = abs(valeur_la_plus_proche - valeur)
              index_min = df[df['Center X'] == valeur_la_plus_proche].index[0]
        
          # Vérification de la tolérance et retour du résultat
          distance_relative = distance_minimale / valeur * 10**6
          if distance_relative <= tolerance:
            return [True, valeur_la_plus_proche, df['Height'].iloc[index_min], index_min, distance_relative]
          else:
            return [False]
    
    def trouver_isotopes(self,Isotopes,df,tolerance):
    
        
        """
        
        """
        
        IsotopesMasses = [Isotopes[k][1] for k in range(len(Isotopes))]
        IsotopesAbondancesRelatives = [Isotopes[k][2] for k in range(len(Isotopes))]
        
        Resultat = True
        IsotopesReels = []
        IndexToDrop = []
        
        for element in IsotopesMasses:
            if Resultat:
                temp = self.trouver_valeur_df(element,df, tolerance)
                if temp[0]:
                    IsotopesReels.append([temp[1],temp[2]])
                    IndexToDrop.append(temp[3])
                else :
                    Resultat *= False
                
        if Resultat:
            
            MaximumIndex = 0
            MaxAbondance = IsotopesReels[0][1]
            for i in range(1,len(IsotopesReels)):
                if IsotopesReels[i][1] > IsotopesReels[MaximumIndex][1]:
                    MaximumIndex = i
                    MaxAbondance = IsotopesReels[MaximumIndex][1]
            for i in range(len(IsotopesReels)):
                IsotopesReels[i].append(IsotopesReels[i][1]/MaxAbondance*100)
            
            for i in range(len(IsotopesReels)):
                IsotopesReels[i].append(IsotopesAbondancesRelatives[i])
                IsotopesReels[i].append(abs(IsotopesReels[i][-1]-IsotopesReels[i][-2]))
                IsotopesReels[i].append(abs(IsotopesMasses[i]-IsotopesReels[i][0]))
            
            # IsotopesReels est un tableau de tableau de la forme [[m/z, height, Abondance relative observée, Abondance relative théorique]]
            return [True, IsotopesReels, IndexToDrop]
        
        return [False]

    
    def launch_analyse(self):
        
        
        mpl.rcParams["font.size"] = 18
        
        self.df = self.dfOriginal.copy()
        z=[]
        
        if self.CheckCharge1.get():
           z.append(1)
        if self.CheckCharge2.get():
           z.append(2)
        if self.CheckCharge3.get():
           z.append(3)
        if self.CheckCharge4.get():
           z.append(4)
        if self.CheckCharge5.get():
           z.append(5)
        if self.CheckCharge6.get():
           z.append(6)
        if self.CheckCharge7.get():
           z.append(7)
        if self.CheckCharge8.get():
           z.append(8)
        if self.CheckCharge9.get():
           z.append(9)
        if self.CheckCharge10.get():
           z.append(10)
        
        BDC = [self.NomBDC1.get(),self.NomBDC2.get(),self.NomBDC3.get()]
        
        self.ax1.clear()
        self.ax3.clear()
        
        Resultat = pd.DataFrame({
        "Bout de chaînes" : ["Vide"],
        "m/z": [0.0],
        "Charge": [0.0],
        "Masse": [0],
        "Longueur de chaîne": [0],
        "Isotopes": [[0.0]],
        "Score":[0.0]
        })
        
        df = self.df
        tolerance = self.tolerance_var.get()
        DPMax = self.DPMax_var.get()
        
        # Récupération des informations sur la/les formule(s) chimique(s) des bouts de chaînes
        
        C1 = [self.CarboneBDC1.get(), self.CarboneBDC2.get(), self.CarboneBDC3.get()]
        H1 = [self.HydrogeneBDC1.get(),self.HydrogeneBDC2.get(),self.HydrogeneBDC3.get()]
        O1 = [self.OxygeneBDC1.get(),self.OxygeneBDC2.get(),self.OxygeneBDC3.get()]
        N1 = [self.AzoteBDC1.get(),self.AzoteBDC2.get(),self.AzoteBDC3.get()]
        S1 = [self.SoufreBDC1.get(),self.SoufreBDC2.get(),self.SoufreBDC3.get()]
        Br1 = [self.BromeBDC1.get(),self.BromeBDC2.get(),self.BromeBDC3.get()]
        
        # Récupération des informations sur la formule chimique de l'unité répétitrice
        
        C2 = self.CarboneUR.get()
        H2 = self.HydrogeneUR.get()
        O2 = self.OxygeneUR.get()
        N2 = self.AzoteUR.get()
        S2 = self.SoufreUR.get()
        Br2 = self.BromeUR.get()
        
        # Récupération des options avancées
        
        AbondanceIsoMiniumum = self.AbondanceIsoMinimum
        Adduit = self.adduit_var
        
        Nbre_BDC = 0
        
        if C1[0]+H1[0]+O1[0]+N1[0]+S1[0]+Br1[0]>0:
            Nbre_BDC +=1
            if C1[1]+H1[1]+O1[1]+N1[1]+S1[1]+Br1[1]>0:
                Nbre_BDC+=1
                if C1[2]+H1[2]+O1[2]+N1[2]+S1[2]+Br1[2]>0:
                    Nbre_BDC+=1
        
        for indexBDC in range(1,Nbre_BDC+1):
            
            
            # Récupération du Tableau des masses observables et de chacun de leur isotope
            
            temp = self.FaireTMO_I(C1[indexBDC-1],H1[indexBDC-1],O1[indexBDC-1],N1[indexBDC-1],S1[indexBDC-1],Br1[indexBDC-1],C2,H2,O2,N2,S2,Br2,z,DPMax,Adduit,AbondanceIsoMiniumum)
            TableauMassesObservables = temp[0]
            TableauMassesObservablesEtIsotopes = temp[1]
            
            # Pour chaque masses observables on vérifie si son pic monoisotopic est dans le tableau des masses observées
            
            for i in range(len(TableauMassesObservables)):
                for j in range(len(TableauMassesObservables[i])):
                    
                    score = 0
                    Cherche = self.trouver_valeur_df(TableauMassesObservables[i][j][0], df, tolerance)
                    
                    if Cherche[0]:
                        
                        score += 0.9**Cherche[4]*3/8
                        # Récupération des isotopes correspondants à la chaîne et à son état de charge trouvés
                        Isotopes = TableauMassesObservablesEtIsotopes[i][j]
                        
                        # Vérifier si on trouve les isotopes dans le tableau des masses observées 
                        
                        ResultatsTrouverIsotopes = self.trouver_isotopes(Isotopes, df, tolerance)
                        
                        #Si on trouve les isotopes on supprime les pics leur correspondant dans le tableau des massses 
                        #observées pour éviter des doubles attributions
                        
                        if ResultatsTrouverIsotopes[0]:
                            for element in ResultatsTrouverIsotopes[2]:
                                df.drop(index = element, inplace = True)
                            df.reset_index(inplace=True, drop = True)
                            nouvelle_entree = {"Bout de chaînes": BDC[indexBDC-1],
                                               "m/z": Cherche[1] ,
                                               "Charge": TableauMassesObservables[i][j][-1],
                                               "Masse": Cherche[1]*TableauMassesObservables[i][j][-1],
                                               "Longueur de chaîne": j+1,
                                               "Isotopes" : ResultatsTrouverIsotopes[1],
                                               "Score": score}
                            Resultat.loc[len(df.index)] = nouvelle_entree
                            
        Resultat.drop(0, inplace=True)
        Resultat.reset_index(drop=True,inplace=True)
        
        
        legend_mz = []
        legend_m = []
        legend = []
        color = [
        [
        "#800000",  # Maroon
        "#CB4335",  # Brick Red
        "#C0392B",  # Cherry Red
        "#CE2029",  # Fire Engine Red
        "#DC143C",  # Crimson
        "#FF7F50",  # Coral Red
        "#FFC0CB",  # Salmon Pink
        "#FFF0F5"   # Light Pink
        ],
        [
        "#2C3E50",  # Forest Green
        "#38A3A5",  # Hunter Green
        "#2ECC71",  # Emerald Green
        "#2D859E",  # Sea Green
        "#00FF00",  # Spring Green
        "#98FF98",  # Mint Green
        "#A7FF00",  # Lime Green
        "#F0FFF0"   # Pale Green
        ],
        [
        "#001F3F",  # Dark Navy
        "#00447E",  # Midnight Blue
        "#007BFF",  # Royal Blue
        "#1A73E8",  # Dodger Blue
        "#82CFFD",  # Sky Blue
        "#A0E7FF",  # Light Sky Blue
        "#C6E2FF",  # Light Blue 
        "#E3F2FD"   # Light Cornflower Blue 
        ] ]
        
        if Nbre_BDC>=1:
            
            ResultatBDC1 = Resultat[Resultat['Bout de chaînes'] == BDC[0]]
            
            charge1 = ResultatBDC1[ResultatBDC1['Charge']==1]
            charge2 = ResultatBDC1[ResultatBDC1['Charge']==2]
            charge3 = ResultatBDC1[ResultatBDC1['Charge']==3]
            charge4 = ResultatBDC1[ResultatBDC1['Charge']==4]
            charge5 = ResultatBDC1[ResultatBDC1['Charge']==5]
            charge6 = ResultatBDC1[ResultatBDC1['Charge']==6]
            charge7 = ResultatBDC1[ResultatBDC1['Charge']==7]
            charge8 = ResultatBDC1[ResultatBDC1['Charge']==8]
            charge9 = ResultatBDC1[ResultatBDC1['Charge']==9]
            charge10 = ResultatBDC1[ResultatBDC1['Charge']==10]
        
            affichage_charge1_x = []
            affichage_charge1_y = []
            affichage_charge2_x = []
            affichage_charge2_y = []
            affichage_charge3_x = []
            affichage_charge3_y = []
            affichage_charge4_x = []
            affichage_charge4_y = []
            affichage_charge5_x = []
            affichage_charge5_y = []
            affichage_charge6_x = []
            affichage_charge6_y = []
            affichage_charge7_x = []
            affichage_charge7_y = []
            affichage_charge8_x = []
            affichage_charge8_y = []
            affichage_charge9_x = []
            affichage_charge9_y = []
            affichage_charge10_x = []
            affichage_charge10_y = []
            
            if charge1.shape[0]>0:
                for i in range(charge1.shape[0]):
                    for j in range(len(charge1['Isotopes'].iloc[i])):   
                        affichage_charge1_x.append(charge1['Isotopes'].iloc[i][j][0])
                        affichage_charge1_y.append(charge1['Isotopes'].iloc[i][j][1])
                markerline, stemlines, baseline = self.ax1.stem(affichage_charge1_x, affichage_charge1_y, markerfmt='',basefmt='white',linefmt=color[0][2])
               
                legend_mz.append(BDC[0] + " z=1")
              
            if charge2.shape[0]>0:
                for i in range(charge2.shape[0]):
                    for j in range(len(charge2['Isotopes'].iloc[i])):
                        
                        affichage_charge2_x.append(charge2['Isotopes'].iloc[i][j][0])
                        affichage_charge2_y.append(charge2['Isotopes'].iloc[i][j][1])
                markerline, stemlines, baseline = self.ax1.stem(affichage_charge2_x, affichage_charge2_y, markerfmt='',basefmt='white',linefmt=color[1][2])
                legend_mz.append(BDC[0] + " z=2")
            if charge3.shape[0]>0:
                for i in range(charge3.shape[0]):
                    for j in range(len(charge3['Isotopes'].iloc[i])):
                        
                        affichage_charge3_x.append(charge3['Isotopes'].iloc[i][j][0])
                        affichage_charge3_y.append(charge3['Isotopes'].iloc[i][j][1])
                markerline, stemlines, baseline = self.ax1.stem(affichage_charge3_x, affichage_charge3_y, markerfmt='',basefmt='white',linefmt=color[2][2])
                legend_mz.append(BDC[0] + " z=3")
            if charge4.shape[0]>0:
                for i in range(charge4.shape[0]):
                    for j in range(len(charge4['Isotopes'].iloc[i])):
                        
                        affichage_charge4_x.append(charge4['Isotopes'].iloc[i][j][0])
                        affichage_charge4_y.append(charge4['Isotopes'].iloc[i][j][1])
                markerline, stemlines, baseline = self.ax1.stem(affichage_charge4_x, affichage_charge4_y, markerfmt='',basefmt='white',linefmt=color[0][-2])
                legend_mz.append(BDC[0] + " z=4")
            if charge5.shape[0]>0:
                for i in range(charge5.shape[0]):
                    for j in range(len(charge5['Isotopes'].iloc[i])):
                        
                        affichage_charge5_x.append(charge5['Isotopes'].iloc[i][j][0])
                        affichage_charge5_y.append(charge5['Isotopes'].iloc[i][j][1])
                markerline, stemlines, baseline = self.ax1.stem(affichage_charge5_x, affichage_charge5_y, markerfmt='',basefmt='white',linefmt=color[1][-2])
                legend_mz.append(BDC[0] + " z=5")
            if charge6.shape[0]>0:
                for i in range(charge6.shape[0]):
                    for j in range(len(charge6['Isotopes'].iloc[i])):
                        
                        affichage_charge6_x.append(charge6['Isotopes'].iloc[i][j][0])
                        affichage_charge6_y.append(charge6['Isotopes'].iloc[i][j][1])
                markerline, stemlines, baseline = self.ax1.stem(affichage_charge6_x, affichage_charge6_y, markerfmt='',basefmt='white',linefmt=color[2][-2])
                legend_mz.append(BDC[0] + " z=6")
            if charge7.shape[0]>0:
                for i in range(charge7.shape[0]):
                    for j in range(len(charge7['Isotopes'].iloc[i])):
                        
                        affichage_charge7_x.append(charge7['Isotopes'].iloc[i][j][0])
                        affichage_charge7_y.append(charge7['Isotopes'].iloc[i][j][1])
                markerline, stemlines, baseline = self.ax1.stem(affichage_charge7_x, affichage_charge7_y, markerfmt='',basefmt='white',linefmt=color[0][4])
                legend_mz.append(BDC[0] + " z=7")
            if charge8.shape[0]>0:
                for i in range(charge8.shape[0]):
                    for j in range(len(charge8['Isotopes'].iloc[i])):
                        
                        affichage_charge8_x.append(charge8['Isotopes'].iloc[i][j][0])
                        affichage_charge8_y.append(charge8['Isotopes'].iloc[i][j][1])
                markerline, stemlines, baseline = self.ax1.stem(affichage_charge8_x, affichage_charge8_y, markerfmt='',basefmt='white',linefmt=color[1][4])
                legend_mz.append(BDC[0] + " z=8")
            if charge9.shape[0]>0:
                for i in range(charge9.shape[0]):
                    for j in range(len(charge9['Isotopes'].iloc[i])):
                        
                        affichage_charge9_x.append(charge9['Isotopes'].iloc[i][j][0])
                        affichage_charge9_y.append(charge9['Isotopes'].iloc[i][j][1])
                markerline, stemlines, baseline = self.ax1.stem(affichage_charge9_x, affichage_charge9_y, markerfmt='',basefmt='white',linefmt=color[2][4])
                legend_mz.append(BDC[0] + " z=9")
            if charge10.shape[0]>0:
                for i in range(charge10.shape[0]):
                    for j in range(len(charge10['Isotopes'].iloc[i])):
                        
                        affichage_charge10_x.append(charge10['Isotopes'].iloc[i][j][0])
                        affichage_charge10_y.append(charge10['Isotopes'].iloc[i][j][1])
                markerline, stemlines, baseline = self.ax1.stem(affichage_charge10_x, affichage_charge10_y, markerfmt='',basefmt='white',linefmt=color[0][8])
                legend_mz.append(BDC[0] + " z=10")
            self.ax1.set_xlabel("m/z", fontsize = 18)
            
        if Nbre_BDC>=2:
            
            ResultatBDC2 = Resultat[Resultat['Bout de chaînes'] == BDC[1]]
            
            charge1 = ResultatBDC2[ResultatBDC2['Charge']==1]
            charge2 = ResultatBDC2[ResultatBDC2['Charge']==2]
            charge3 = ResultatBDC2[ResultatBDC2['Charge']==3]
            charge4 = ResultatBDC2[ResultatBDC2['Charge']==4]
            charge5 = ResultatBDC2[ResultatBDC2['Charge']==5]
            charge6 = ResultatBDC2[ResultatBDC2['Charge']==6]
            charge7 = ResultatBDC2[ResultatBDC2['Charge']==7]
            charge8 = ResultatBDC2[ResultatBDC2['Charge']==8]
            charge9 = ResultatBDC2[ResultatBDC2['Charge']==9]
            charge10 = ResultatBDC2[ResultatBDC2['Charge']==10]
        
            affichage_charge1_x2 = []
            affichage_charge1_y2 = []
            affichage_charge2_x2 = []
            affichage_charge2_y2 = []
            affichage_charge3_x2 = []
            affichage_charge3_y2 = []
            affichage_charge4_x2 = []
            affichage_charge4_y2 = []
            affichage_charge5_x2 = []
            affichage_charge5_y2 = []
            affichage_charge6_x2 = []
            affichage_charge6_y2 = []
            affichage_charge7_x2 = []
            affichage_charge7_y2 = []
            affichage_charge8_x2 = []
            affichage_charge8_y2 = []
            affichage_charge9_x2 = []
            affichage_charge9_y2 = []
            affichage_charge10_x2 = []
            affichage_charge10_y2 = []
            
            if charge1.shape[0]>0:
                for i in range(charge1.shape[0]):
                    for j in range(len(charge1['Isotopes'].iloc[i])):   
                        affichage_charge1_x2.append(charge1['Isotopes'].iloc[i][j][0])
                        affichage_charge1_y2.append(charge1['Isotopes'].iloc[i][j][1])
                markerline, stemlines, baseline = self.ax1.stem(affichage_charge1_x2, affichage_charge1_y2, markerfmt='',basefmt='white',linefmt=color[1][0])
                legend_mz.append(BDC[1] + " z=1")
              
            if charge2.shape[0]>0:
                for i in range(charge2.shape[0]):
                    for j in range(len(charge2['Isotopes'].iloc[i])):
                        
                        affichage_charge2_x2.append(charge2['Isotopes'].iloc[i][j][0])
                        affichage_charge2_y2.append(charge2['Isotopes'].iloc[i][j][1])
                markerline, stemlines, baseline = self.ax1.stem(affichage_charge2_x2, affichage_charge2_y2, markerfmt='',basefmt='white',linefmt=color[1][1])
                legend_mz.append(BDC[1] + " z=2")
            if charge3.shape[0]>0:
                for i in range(charge3.shape[0]):
                    for j in range(len(charge3['Isotopes'].iloc[i])):
                        
                        affichage_charge3_x2.append(charge3['Isotopes'].iloc[i][j][0])
                        affichage_charge3_y2.append(charge3['Isotopes'].iloc[i][j][1])
                markerline, stemlines, baseline = self.ax1.stem(affichage_charge3_x2, affichage_charge3_y2, markerfmt='',basefmt='white',linefmt=color[1][2])
                legend_mz.append(BDC[1] + " z=3")
            if charge4.shape[0]>0:
                for i in range(charge4.shape[0]):
                    for j in range(len(charge4['Isotopes'].iloc[i])):
                        
                        affichage_charge4_x2.append(charge4['Isotopes'].iloc[i][j][0])
                        affichage_charge4_y2.append(charge4['Isotopes'].iloc[i][j][1])
                markerline, stemlines, baseline = self.ax1.stem(affichage_charge4_x2, affichage_charge4_y2, markerfmt='',basefmt='white',linefmt=color[1][3])
                legend_mz.append(BDC[1] + " z=4")
            if charge5.shape[0]>0:
                for i in range(charge5.shape[0]):
                    for j in range(len(charge5['Isotopes'].iloc[i])):
                        
                        affichage_charge5_x2.append(charge5['Isotopes'].iloc[i][j][0])
                        affichage_charge5_y2.append(charge5['Isotopes'].iloc[i][j][1])
                markerline, stemlines, baseline = self.ax1.stem(affichage_charge5_x2, affichage_charge5_y2, markerfmt='',basefmt='white',linefmt=color[1][4])
                legend_mz.append(BDC[1] + " z=5")
            if charge6.shape[0]>0:
                for i in range(charge6.shape[0]):
                    for j in range(len(charge6['Isotopes'].iloc[i])):
                        
                        affichage_charge6_x2.append(charge6['Isotopes'].iloc[i][j][0])
                        affichage_charge6_y2.append(charge6['Isotopes'].iloc[i][j][1])
                markerline, stemlines, baseline = self.ax1.stem(affichage_charge6_x2, affichage_charge6_y2, markerfmt='',basefmt='white',linefmt=color[1][5])
                legend_mz.append(BDC[1] + " z=6")
            if charge7.shape[0]>0:
                for i in range(charge7.shape[0]):
                    for j in range(len(charge7['Isotopes'].iloc[i])):
                        
                        affichage_charge7_x2.append(charge7['Isotopes'].iloc[i][j][0])
                        affichage_charge7_y2.append(charge7['Isotopes'].iloc[i][j][1])
                markerline, stemlines, baseline = self.ax1.stem(affichage_charge7_x2, affichage_charge7_y2, markerfmt='',basefmt='white',linefmt=color[1][6])
                legend_mz.append(BDC[1] + " z=7")
            if charge8.shape[0]>0:
                for i in range(charge8.shape[0]):
                    for j in range(len(charge8['Isotopes'].iloc[i])):
                        
                        affichage_charge8_x2.append(charge8['Isotopes'].iloc[i][j][0])
                        affichage_charge8_y2.append(charge8['Isotopes'].iloc[i][j][1])
                markerline, stemlines, baseline = self.ax1.stem(affichage_charge8_x2, affichage_charge8_y2, markerfmt='',basefmt='white',linefmt=color[1][7])
                legend_mz.append(BDC[1] + " z=8")
            if charge9.shape[0]>0:
                for i in range(charge9.shape[0]):
                    for j in range(len(charge9['Isotopes'].iloc[i])):
                        
                        affichage_charge9_x2.append(charge9['Isotopes'].iloc[i][j][0])
                        affichage_charge9_y2.append(charge9['Isotopes'].iloc[i][j][1])
                markerline, stemlines, baseline = self.ax1.stem(affichage_charge9_x2, affichage_charge9_y2, markerfmt='',basefmt='white',linefmt=color[1][8])
                legend_mz.append(BDC[1] + " z=9")
            if charge10.shape[0]>0:
                for i in range(charge10.shape[0]):
                    for j in range(len(charge10['Isotopes'].iloc[i])):
                        
                        affichage_charge10_x2.append(charge10['Isotopes'].iloc[i][j][0])
                        affichage_charge10_y2.append(charge10['Isotopes'].iloc[i][j][1])
                markerline, stemlines, baseline = self.ax1.stem(affichage_charge10_x2, affichage_charge10_y2, markerfmt='',basefmt='white',linefmt=color[1][9])
                legend_mz.append(BDC[1] + " z=10")
            self.ax1.set_xlabel("m/z", fontsize = 18) 
           
        self.ax1.legend(legend_mz, ncols=round(2,0),fontsize=18,loc='upper right')
        self.ax1.set_ylabel("Counts (-)")
        plt.legend(legend_mz, ncols=round(2,0),fontsize=18,loc='upper right')
        plt.ylabel("Counts (-)", fontsize = 18)
        plt.xlabel("m/z", fontsize = 18)
        Resultats_Mn_Mw_D_text =""
        
        for k in range(Nbre_BDC):
            DataFrame_Cumulatif = Resultat
            DataFrame_Cumulatif = DataFrame_Cumulatif[DataFrame_Cumulatif['Bout de chaînes']==BDC[k]]
            Abondance_Cumulative = []
            for i in range(DataFrame_Cumulatif.shape[0]):
                AbondanceTemp = 0
                for j in range(1): #len(DataFrame_Cumulatif['Isotopes'].iloc[i])
                    AbondanceTemp += DataFrame_Cumulatif['Isotopes'].iloc[i][j][1]
                Abondance_Cumulative.append(AbondanceTemp)
            
            DataFrame_Cumulatif['Abondance totale isotope'] = Abondance_Cumulative
            Grouped_DataFrame_Cumulatif = DataFrame_Cumulatif.groupby("Longueur de chaîne")['Abondance totale isotope'].sum()
            Grouped_DataFrame_Cumulatif = Grouped_DataFrame_Cumulatif.reset_index()
            test_y = Grouped_DataFrame_Cumulatif['Abondance totale isotope']
            test_x = [self.MasseMono(C1[k], H1[k], O1[k], N1[k], S1[k], Br1[k], C2, H2, O2, N2, S2, Br2, Grouped_DataFrame_Cumulatif["Longueur de chaîne"].iloc[i],Adduit) for i in range(Grouped_DataFrame_Cumulatif.shape[0])]
            markerline, stemlines, baseline = self.ax3.stem(test_x, test_y, markerfmt='',basefmt='white', linefmt=color[k][5])      
            legend.append(BDC[k])
            
            MnNum = 0
            MnDenom = 0
            
            for i in range(len(test_x)):
                MnNum+=test_x[i]*test_y[i]
                MnDenom += test_y[i]
                
            MwNum = 0
            MwDenom = MnNum
            
            for i in range(len(test_x)):
                MwNum+=test_y[i]*test_x[i]**2
            BDC_text = str(BDC[k])+" : "    
            Mn = "Mn = " + str(MnNum/MnDenom) + " "
            Mw = "Mw = " + str(MwNum/MwDenom)+ " "
            D = "D = " + str((MwNum/MwDenom)/(MnNum/MnDenom))+ "\n"
            text_temp = BDC_text + Mn + Mw + D
            Resultats_Mn_Mw_D_text += text_temp
            
        self.ax3.legend(legend, fontsize = 18, loc='upper right')
        self.ax3.set_xlabel("Masse (Da)", fontsize = 18)
        self.ax3.set_ylabel("Counts (-)", fontsize = 18) 
        self.canvas.draw()
        self.fig.suptitle(Resultats_Mn_Mw_D_text, fontsize=18)
        
        pt = Table(self.DFR,dataframe=Resultat,showtoolbar=True, showstatusbar=True)
        pt.show()
        
if __name__ == '__main__':
    root = tk.Tk()
    app = MassSpectrumAnalyzer(root)
    root.mainloop()
