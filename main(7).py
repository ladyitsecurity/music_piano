ells1))
PlayMelody2.grid(row=0, column=1, padx=0, pady=0)

PlayMelody3 = Button(ABC2, height=2, width=16, justify=CENTER, text="а нам все равно", bg="pink",
                     fg="black", font=('arial', 18, 'bold'), command=lambda: play_melody(we_do_not_care))
PlayMelody3.grid(row=0, column=2, padx=0, pady=0)

# =========================================================================================

# верхний ряд (черные)
# до#, ре# (ре бемоль, ми бемоль)
btnCs = Button(ABC3, height=6, width=6, text="С#", bg="black", fg="white", font=('arial', 18, 'bold'),
               command=lambda: value_notes('C#'))
btnCs.grid(row=0, column=0, padx=5, pady=5)
btnDs = Button(ABC3, height=6, width=6, text="D#", bg="black", fg="white", font=('arial', 18, 'bold'),
               command=lambda: value_notes("D#"))
btnDs.grid(row=0, column=2, padx=5, pady=5)

btnSpace1 = Button(ABC3, state=DISABLED, height=6, width=15, bg='powder blue', relief=FLAT)
btnSpace1.grid(row=0, column=3, padx=0, pady=0)

# фа#, соль#, ля# (соль бемоль, ля бемоль, си бемоль)
btnFs = Button(ABC3, height=6, width=6, text="F#", bg="black", fg="white", font=('arial', 18, 'bold'),
               command=lambda: value_notes("F#"))
btnFs.grid(row=0, column=4, padx=5, pady=5)
btnGs = Button(ABC3, height=6, width=6, text="G#", bg="black", fg="white", font=('arial', 18, 'bold'),
               command=lambda: value_notes("G#"))
btnGs.grid(row=0, column=6, padx=5, pady=5)
btnBs = Button(ABC3, height=6, width=6, text="B#", bg="black", fg="white", font=('arial', 18, 'bold'),
               command=lambda: value_notes("B#"))
btnBs.grid(row=0, column=8, padx=5, pady=5)

btnSpace2 = Button(ABC3, state=DISABLED, height=6, width=15, bg='powder blue', relief=FLAT)
btnSpace2.grid(row=0, column=9, padx=0, pady=0)

# до#, ре# (ре бемоль, ми бемоль)
btnCs1 = Button(ABC3, height=6, width=6, text="С#1", bg="black", fg="white", font=('arial', 18, 'bold'),
                command=lambda: value_notes("C#1"))
btnCs1.grid(row=0, column=10, padx=5, pady=5)
btnDs1 = Button(ABC3, height=6, width=6, text="D#1", bg="black", fg="white", font=('arial', 18, 'bold'),
                command=lambda: value_notes("D#1"))
btnDs1.grid(row=0, column=12, padx=5, pady=5)

btnSpace3 = Button(ABC3, state=DISABLED, height=6, width=15, bg='powder blue', relief=FLAT)
btnSpace3.grid(row=0, column=13, padx=0, pady=0)

# =========================================================================================
# нижний ряд (белые)

btnC = Button(ABC4, height=6, width=6, text="C", bg="white", fg="black", font=('arial', 18, 'bold'),
              command=lambda: value_notes("C"))
btnC.grid(row=0, column=0, padx=5, pady=5)
btnD = Button(ABC4, height=6, width=6, text="D", bg="white", fg="black", font=('arial', 18, 'bold'),
              command=lambda: value_notes("D"))
btnD.grid(row=0, column=1, padx=5, pady=5)
btnE = Button(ABC4, height=6, width=6, text="E", bg="white", fg="black", font=('arial', 18, 'bold'),
              command=lambda: value_notes("E"))
btnE.grid(row=0, column=2, padx=5, pady=5)
btnF = Button(ABC4, height=6, width=6, text="F", bg="white", fg="black", font=('arial', 18, 'bold'),
              command=lambda: value_notes("F"))
btnF.grid(row=0, column=3, padx=5, pady=5)

btnG = Button(ABC4, height=6, width=6, text="G", bg="white", fg="black", font=('arial', 18, 'bold'),
              command=lambda: value_notes("G"))
btnG.grid(row=0, column=4, padx=5, pady=5)
btnA = Button(ABC4, height=6, width=6, text="A", bg="white", fg="black", font=('arial', 18, 'bold'),
              command=lambda: value_notes("A"))
btnA.grid(row=0, column=5, padx=5, pady=5)
btnB = Button(ABC4, height=6, width=6, text="B", bg="white", fg="black", font=('arial', 18, 'bold'),
              command=lambda: value_notes("B"))
btnB.grid(row=0, column=6, padx=5, pady=5)
btnC1 = Button(ABC4, height=6, width=6, text="C1", bg="white", fg="black", font=('arial', 18, 'bold'),
               command=lambda: value_notes("C1"))
btnC1.grid(row=0, column=7, padx=5, pady=5)

btnD1 = Button(ABC4, height=6, width=6, text="D1", bg="white", fg="black", font=('arial', 18, 'bold'),
               command=lambda: value_notes("D1"))
btnD1.grid(row=0, column=8, padx=5, pady=5)
btnE1 = Button(ABC4, height=6, width=6, text="E1", bg="white", fg="black", font=('arial', 18, 'bold'),
               command=lambda: value_notes("E1"))
btnE1.grid(row=0, column=9, padx=5, pady=5)
btnF1 = Button(ABC4, height=6, width=6, text="F1", bg="white", fg="black", font=('arial', 18, 'bold'),
               command=lambda: value_notes("F1"))
btnF1.grid(row=0, column=10, padx=5, pady=5)

root.mainloop()

# =========================================================================================
# =========================================================================================
# =========================================================================================
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           