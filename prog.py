from math import *
import math
def mat():
    print("Labdien, lietotājs! Šī programmatūra ir nepieciešama, lai aprēķīnāt ievilkta vai apvilkta riņķa līnijas parametrus regulāraja trījstūra un četrstūra(vai ja vajag, tad arī var vienkārši rēķīnāt regulāra trījstūra vai četrstūra parametrus). Zemāk ir uzrakstīt, ko vajag darīt, tikai izvēlēt kāda ir riņķa līnija(apvilkta vai ievilkta),kāda ir figūra(regulārs trījstūris vai četrstūris) un kāds no paramatriem jums ir dots un tad ierakstīt to un tad programmatūra dos Jums vērtības katram no parametriem(riņķa līnijas radiuss, diametrs, laukums, figūras malas garumu, perimetru, laukumu un ja ir dots trījstūrism, tad augstumu)")
    S=int(input("Jums ir ievilkta vai apvilkta riņķa līnija? Ja ievilkta rakstīt - 1, ja apvilkta, tad 2"))
    S1=int(input("Jums ir dots regulārs trijstūris vai kvadrāts? Ja regulārs trījstūris rakstīt - 1, ja kvadrāts, tad 2"))
    kortri=sqrt(3)
    if(S==1 and S1==1):
        S2=int(input("Kas Jums ir dots?Ja riņķa līnijas radiuss, tad rakstīt 1 . Ja Riņķa līnijas diametrs, tad rakstīt 2 . Ja Riņķa līnijas laukums, tad rakstīt 3 . Ja regulāra trījstura māla,tad rakstīt 4 . Ja regulāra trījstūra perimetrs, tad rakstīt 5 . Ja regulāra trījstūra laukums, tad rakstīt 6 . Ja regulāra trījstūra augstums, tad rakstīt 7"))
        if(S2==1):
            Stirr=int(input("Ierakstīt ievilkta regulāra trījstūrā riņķa līnijas radiusu:"))
            dtirr= 2*Stirr
            lrtirr= math.pi*pow(Stirr,2)
            atirr= 2*Stirr*kortri
            aatirr=atirr/2
            ptirr= 3*atirr
            lttirr= (pow(atirr, 2)* kortri)/4
            hhtirr= (pow(atirr,2)-pow(aatirr,2))
            htirr=sqrt(hhtirr)
            print( "Riņķa līnijas diametrs ir", dtirr ,"\nRiņķa līnijas laukums ir:", lrtirr , "\nRegulāra trījstūra mala ir:", atirr , "\nRegulāra trījstūra perimetrs ir:", ptirr , "\nRegulāra trījstūra laukums ir:",  lttirr , "\nRegulāra trījstūra augstums ir:", htirr, sep= ' ')
        if(S2==2):
            Stird=int(input("Ierakstīt ievilkta regulāra trījstūrā riņķa līnijas diametru:"))
            rtird= Stird/2
            lrtird= math.pi*pow(rtird,2)
            atird= 2*rtird*kortri
            aatird=atird/2
            ptird= 3*atird
            lttird= (pow(atird, 2)* kortri)/4
            hhtird= (pow(atird,2)-pow(aatird,2))
            htird=sqrt(hhtird)
            print( "Riņķa līnijas radiuss ir:", rtird ,"\nRiņķa līnijas laukums ir:", lrtird , "\nRegulāra trījstūra mala ir:", atird , "\nRegulāra trījstūra perimetrs ir:", ptird , "\nRegulāra trījstūra laukums ir:",  lttird , "\nRegulāra trījstūra augstums ir:", htird, sep= ' ')
        if(S2==3):
            Stirl=int(input("Ierakstīt ievilkta regulāra trījstūrā riņķa līnijas laukumu:"))
            rtirl=sqrt(Stirl/math.pi)
            dtirl=rtirl*2
            atirl=2*rtirl*kortri
            aatirl=atirl/2
            ptirl=3*atirl
            ltirl= (pow(atirl, 2)*kortri)/4
            hhtirl= (pow(atirl,2)-pow(aatirl,2))
            htirl= sqrt(hhtirl)
            print( "Riņķa līnijas radiuss ir:", rtirl ,"\nRiņķa līnijas diametrs ir:", dtirl , "\nRegulāra trījstūra mala ir:", atirl , "\nRegulāra trījstūra perimetrs ir:", ptirl , "\nRegulāra trījstūra laukums ir:",  ltirl , "\nRegulāra trījstūra augstums ir:", htirl, sep= ' ')
        if(S2==4):
            Stitm=int(input("Ierakstīt apvilkta ap riņķu līniju regulāra trījstūra malu:"))
            rtitm=Stitm/(2*kortri)
            dtitm=rtitm*2
            lrtitm=math.pi*pow(rtitm,2)
            ptitm=3*Stitm
            lttitm= (pow(Stitm, 2)*kortri)/4
            hhtitm= (pow(Stitm,2)-pow(Stitm/2,2))
            htitm= sqrt(hhtitm)
            print( "Riņķa līnijas radiuss ir:", rtitm ,"\nRiņķa līnijas diametrs ir:", dtitm , "\nRiņķa līnijas laukums ir:", lrtitm , "\nRegulāra trījstūra perimetrs ir:", ptitm , "\nRegulāra trījstūra laukums ir:",  lttitm , "\nRegulāra trījstūra augstums ir:", htitm, sep= ' ')
        if(S2==5):
            Stitp=int(input("Ierakstīt apvilkta ap riņķu līniju regulāra trījstūra perimetru:"))
            atitp=Stitp/3
            rtitp=atitp/(2*kortri)
            dtitp=rtitp*2
            lrtitp=math.pi*pow(rtitp,2)
            lttitp= (pow(atitp, 2)*kortri)/4
            hhtitp= (pow(atitp,2)-pow(atitp/2,2))
            htitp= sqrt(hhtitp)
            print( "Riņķa līnijas radiuss ir:", rtitp ,"\nRiņķa līnijas diametrs ir:", dtitp , "\nRiņķa līnijas laukums ir:", lrtitp , "\nRegulāra trījstūra mala ir:", atitp , "\nRegulāra trījstūra laukums ir:",  lttitp , "\nRegulāra trījstūra augstums ir:", htitp, sep= ' ')
        if(S2==6):
            Stitl=int(input("Ierakstīt apvilkta ap riņķu līniju regulāra trījstūra laukumu:"))
            atitl=2*sqrt(Stitl*kortri)
            rtitl=atitl/(2*kortri)
            dtitl=rtitl*2
            lrtitl=math.pi*pow(rtitl,2)
            ptitl=3*atitl
            hhtitl= (pow(atitl,2)-pow(atitl/2,2))
            htitl= sqrt(hhtitl)
            print( "Riņķa līnijas radiuss ir:", rtitl ,"\nRiņķa līnijas diametrs ir:", dtitl , "\nRiņķa līnijas laukums ir:", lrtitl ,"\nRegulāra trījstūra mala ir:", atitl, "\nRegulāra trījstūra perimetrs ir:", ptitl , "\nRegulāra trījstūra augstums ir:", htitl, sep= ' ')
        if(S2==7):
            Stita=int(input("Ierakstīt apvilkta ap riņķu līniju regulāra trījstūra augstumu:"))
            atita=(kortri*Stita)/2
            rtita=atita/(2*kortri)
            dtita=rtita*2
            lrtita=math.pi*pow(rtita,2)
            ptita=3*atita
            lttita=(pow(atita, 2)*kortri)/4
            print( "Riņķa līnijas radiuss ir:", rtita ,"\nRiņķa līnijas diametrs ir:", dtita , "\nRiņķa līnijas laukums ir:", lrtita ,"\nRegulāra trījstūra mala ir:", atita, "\nRegulāra trījstūra perimetrs ir:", ptita , "\nRegulāra trījstūra laukums ir:", lttita, sep= ' ')            

    if(S==1 and S1==2):
        S2=int(input("Kas Jums ir dots?Ja riņķa līnijas radiuss, tad rakstīt 1 . Ja Riņķa līnijas diametrs, tad rakstīt 2 . Ja Riņķa līnijas laukums, tad rakstīt 3 . Ja kvadrāta māla,tad rakstīt 4 . Ja kvadrāta perimetrs, tad rakstīt 5 . Ja kvadrāta laukums, tad rakstīt 6"))
        if(S2==1):
            Skirr=int(input("Ierakstīt ievilkta kvadrātā riņķa līnijas radiusu:"))
            dkirr=Skirr*2
            lrkirr=math.pi*pow(Skirr,2)
            mkirr=dkirr
            pkirr=mkirr*4
            lkkirr=mkirr*mkirr
            print("Riņķa līnijas diametrs ir:", dkirr , "\nRiņķa līnijas laukums ir:", lrkirr ,"\nRegulāra četrstūra mala ir:", mkirr, "\nRegulāra četrstūra perimetrs ir:", pkirr , "\nRegulāra četrstūra laukums ir:", lkkirr, sep= ' ')
        if(S2==2):
            Skird=int(input("Ierakstīt ievilkta kvadrātā riņķa līnijas diametru:"))
            rkird=Skird/2
            lrkird=math.pi*pow(rkird,2)
            mkird=Skird
            pkird=mkird*4
            lkkird=mkird*mkird
            print("Riņķa līnijas radiuss ir:", rkird , "\nRiņķa līnijas laukums ir:", lrkird ,"\nRegulāra četrstūra mala ir:", mkird, "\nRegulāra četrstūra perimetrs ir:", pkird , "\nRegulāra četrstūra laukums ir:", lkkird, sep= ' ')
        if(S2==3):
            Skirl=int(input("Ierakstīt ievilkta kvadrātā riņķa līnijas laukumu:"))
            rkirl=sqrt(Skirl/math.pi)
            dkirl=rkirl*2
            mkirl=dkirl
            pkirl=mkirl*4
            lkkirl=mkirl*mkirl
            print("Riņķa līnijas radiuss ir:", rkirl , "\nRiņķa līnijas diametrs ir:", dkirl , "\nRegulāra četrstūra mala ir:", mkirl, "\nRegulāra četrstūra perimetrs ir:", pkirl , "\nRegulāra četrstūra laukums ir:", lkkirl, sep= ' ')
        if(S2==4):
            Skikm=int(input("Ierakstīt apvilkta ap riņķu līniju kvadrāta malu:"))
            rkikm=Skikm/2
            dkikm=Skikm
            lrkikm=math.pi*pow(rkikm,2)
            pkikm=Skikm*4
            lkkikm=Skikm*Skikm
            print("Riņķa līnijas radiuss ir:", rkikm , "\nRiņķa līnijas diametrs ir:", dkikm , "\nRiņķa ļinijas laukums ir:", lrkikm, "\nRegulāra četrstūra perimetrs ir:", pkikm , "\nRegulāra četrstūra laukums ir:", lkkikm, sep= ' ')
        if(S2==5):
            Skikp=int(input("Ierakstīt apvilkta ap riņķu līniju kvadrāta perimetru:"))
            rkikp=Skikp/8
            dkikp=2*rkikp
            lrkikp=math.pi*pow(rkikp,2)
            mkikp=rkikp
            lkkikp=rkikp*rkikp
            print("Riņķa līnijas radiuss ir:", rkikp , "\nRiņķa līnijas diametrs ir:", dkikp , "\nRiņķa ļinijas laukums ir:", lrkikp, "\nRegulāra četrstūra mala ir:", mkikp , "\nRegulāra četrstūra laukums ir:", lkkikp, sep= ' ')
        if(S2==6):
            Skikl=int(input("Ierakstīt apvilkta ap riņķu līniju kvadrāta laukumu:"))
            rkikl=(sqrt(Skikl))/2
            dkikl=2*rkikl
            lrkikl=math.pi*pow(rkikl,2)
            mkikl=rkikl
            pkikl=mkikl*4
            print("Riņķa līnijas radiuss ir:", rkikl , "\nRiņķa līnijas diametrs ir:", dkikl , "\nRiņķa ļinijas laukums ir:", lrkikl,"\nRegulāra četrstūra mala ir:", mkikl, "\nRegulāra četrstūra perimetrs ir:", pkikl , sep= ' ')

    if(S==2 and S1==1):
        S2=int(input("Kas Jums ir dots?Ja riņķa līnijas radiuss, tad rakstīt 1 . Ja Riņķa līnijas diametrs, tad rakstīt 2 . Ja Riņķa līnijas laukums, tad rakstīt 3 . Ja regulāra trījstura māla,tad rakstīt 4 . Ja regulāra trījstūra perimetrs, tad rakstīt 5 . Ja regulāra trījstūra laukums, tad rakstīt 6 . Ja regulāra trījstūra augstums, tad rakstīt 7"))
        if(S2==1):
            Starr=int(input("Ierakstīt apvilkto ap regulāro trījstūru riņķa līnijas radiusu:"))
            dtarr=2*Starr
            lrtarr=math.pi*pow(Starr,2)
            mtarr=(3*Starr)/kortri
            ptarr=mtarr*3
            lttarr=(pow(mtarr, 2)*kortri)/4
            hhtarr= (pow(mtarr,2)-pow(mtarr/2,2))
            htarr= sqrt(hhtarr)
            print("Riņķa līnijas diametrs ir:", dtarr , "\nRiņķa līnijas laukums ir:", lrtarr ,"\nRegulāra trījstūra mala ir:", mtarr, "\nRegulāra trījstūra perimetrs ir:", ptarr , "\nRegulāra trījstūra laukums ir:", lttarr,"\nRegulāra trījstūra augstums ir:", htarr, sep= ' ')
        if(S2==2):
            Stard=int(input("Ierakstīt apvilkto ap regulāro trījstūru riņķa līnijas diametru:"))
            rtard=Stard/2
            lrtard=math.pi*pow(rtard,2)
            mtard=(3*rtard)/kortri
            ptard=mtard*3
            lttard=(pow(mtard, 2)*kortri)/4
            hhtard= (pow(mtard,2)-pow(mtard/2,2))
            htard= sqrt(hhtard)
            print("Riņķa līnijas radiuss ir:", rtard , "\nRiņķa līnijas laukums ir:", lrtard ,"\nRegulāra trījstūra mala ir:", mtard, "\nRegulāra trījstūra perimetrs ir:", ptard , "\nRegulāra trījstūra laukums ir:", lttard,"\nRegulāra trījstūra augstums ir:", htard, sep= ' ')
        if(S2==3):
            Starl=int(input("Ierakstīt apvilkto ap regulāro trījstūru riņķa līnijas laukumu:"))
            rtarl=sqrt(Starl/math.pi)
            dtarl=2*rtarl
            mtarl=(3*rtarl)/kortri
            ptarl=3*mtarl
            lttarl=(pow(mtarl, 2)*kortri)/4
            hhtarl= (pow(mtarl,2)-pow(mtarl/2,2))
            htarl= sqrt(hhtarl)
            print("Riņķa līnijas radiuss", rtarl, "\nRiņķa līnijas diametrs ir:", dtarl  ,"\nRegulāra trījstūra mala ir:", mtarl, "\nRegulāra trījstūra perimetrs ir:", ptarl , "\nRegulāra trījstūra laukums ir:", lttarl,"\nRegulāra trījstūra augstums ir:", htarl, sep= ' ')
        if(S2==4):
            Statm=int(input("Ierakstīt apvilkta ap riņķu līniju regulāra trījstūra malu:"))
            rtatm=(Statm*kortri)/3
            dtatm=rtatm*2
            lrtatm=math.pi*pow(rtatm,2)
            ptatm=3*Statm
            lttatm= (pow(Statm, 2)*kortri)/4
            hhtatm= (pow(Statm,2)-pow(Statm/2,2))
            htatm= sqrt(hhtatm)
            print( "Riņķa līnijas radiuss ir:", rtatm ,"\nRiņķa līnijas diametrs ir:", dtatm , "\nRiņķa līnijas laukums ir:", lrtatm , "\nRegulāra trījstūra perimetrs ir:", ptatm , "\nRegulāra trījstūra laukums ir:",  lttatm , "\nRegulāra trījstūra augstums ir:", htatm, sep= ' ')
        if(S2==5):
            Statp=int(input("Ierakstīt apvilkta ap riņķu līniju regulāra trījstūra perimetru:"))
            mtatp=Statp/3
            rtatp=(mtatp*kortri)/3
            dtatp=rtatp*2
            lrtatp=math.pi*pow(rtatp,2)
            lttatp= (pow(mtatp, 2)*kortri)/4
            hhtatp= (pow(mtatp,2)-pow(mtatp/2,2))
            htatp= sqrt(hhtatp)
            print( "Riņķa līnijas radiuss ir:", rtatp ,"\nRiņķa līnijas diametrs ir:", dtatp , "\nRiņķa līnijas laukums ir:", lrtatp , "\nRegulāra trījstūra mala ir:", mtatp , "\nRegulāra trījstūra laukums ir:",  lttatp , "\nRegulāra trījstūra augstums ir:", htatp, sep= ' ')
        if(S2==6):
            Statl=int(input("Ierakstīt apvilkta ap riņķu līniju regulāra trījstūra laukumu:"))
            mtatl=sqrt(Statl)
            rtatl=(mtatl*kortri)/3
            dtatl=rtatl*2
            lrtatl=math.pi*pow(rtatl,2)
            ptatl=3*mtatl
            hhtatl= (pow(mtatl,2)-pow(mtatl/2,2))
            htatl= sqrt(hhtatl)
            print( "Riņķa līnijas radiuss ir:", rtatl ,"\nRiņķa līnijas diametrs ir:", dtatl , "\nRiņķa līnijas laukums ir:", lrtatl ,"\nRegulāra trījstūra mala ir:", mtatl, "\nRegulāra trījstūra perimetrs ir:", ptatl , "\nRegulāra trījstūra augstums ir:", htatl, sep= ' ')
        if(S2==7):
            Stata=int(input("Ierakstīt apvilkta ap riņķu līniju regulāra trījstūra augstumu:"))
            mtata=(kortri*Stata)/2
            rtata=(mtata*kortri)/3
            dtata=rtata*2
            lrtata=math.pi*pow(rtata,2)
            ptata=3*mtata
            print( "Riņķa līnijas radiuss ir:", rtata ,"\nRiņķa līnijas diametrs ir:", dtata , "\nRiņķa līnijas laukums ir:", lrtata ,"\nRegulāra trījstūra mala ir:", mtata, "\nRegulāra trījstūra perimetrs ir:", ptata ,"\nRegulāra trījstūra laukums ir:",  lttata , sep= ' ')

    if(S==2 and S1==2):
        S2=int(input("Kas Jums ir dots?Ja riņķa līnijas radiuss, tad rakstīt 1 . Ja Riņķa līnijas diametrs, tad rakstīt 2 . Ja Riņķa līnijas laukums, tad rakstīt 3 . Ja kvadrāta māla,tad rakstīt 4 . Ja kvadrāta perimetrs, tad rakstīt 5 . Ja kvadrāta laukums, tad rakstīt 6"))
        if(S2==1):
            Skarr=int(input("Ierakstīt apvilktu ap kvadrātu riņķa līnijas radiusu:"))
            dkarr=Skarr*2
            lrkarr=math.pi*pow(Skarr,2)
            mkarr=dkarr/sqrt(2)
            pkarr=mkarr*4
            lkkarr=mkarr*mkarr
            print("Riņķa līnijas diametrs ir:", dkarr , "\nRiņķa līnijas laukums ir:", lrkarr ,"\nRegulāra četrstūra mala ir:", mkarr, "\nRegulāra četrstūra perimetrs ir:", pkarr ,"\nRegulāra četrstūra laukums ir:",  lkkarr , sep= ' ')
        if(S2==2):
            Skard=int(input("Ierakstīt apvilkta ap kvadrātu riņķa līnijas diametru:"))
            rkard=Skard/2
            lrkard=math.pi*pow(rkard,2)
            mkard=Skard/sqrt(2)
            pkard=mkard*4
            lkkard=mkard*mkard
            print("Riņķa līnijas radiuss ir:", rkard , "\nRiņķa līnijas laukums ir:", lrkard ,"\nRegulāra četrstūra mala ir:", mkard, "\nRegulāra četrstūra perimetrs ir:", pkard ,"\nRegulāra četrstūra laukums ir:",  lkkard , sep= ' ')

        if(S2==3):
            Skarl=int(input("Ierakstīt apvilkta ap kvadrātu riņķa līnijas laukumu:"))
            rkarl=sqrt(Skarl/math.pi)
            dkarl=rkarl*2
            mkarl=dkarl/sqrt(2)
            pkarl=mkarl*4
            lkkarl=mkarl*mkarl
            print("Riņķa līnijas radiuss ir:", rkarl , "\nRiņķa līnijas diametrs ir:", dkarl ,"\nRegulāra četrstūra mala ir:", mkarl, "\nRegulāra četrstūra perimetrs ir:", pkarl ,"\nRegulāra četrstūra laukums ir:",  lkkarl , sep= ' ')

        if(S2==4):
            Skakm=int(input("Ierakstīt ievilkta riņķu līnijā kvadrāta malu:"))
            dkakm=Skakm*sqrt(2)
            rkakm=dkakm/2
            lrkakm=math.pi*pow(rkakm,2)
            pkakm=Skakm*4
            lkkakm=Skakm*Skakm
            print("Riņķa līnijas radiuss ir:", rkakm ,"\nRiņķa līnijas diametrs", dkakm, "\nRiņķa līnijas laukums ir:", lrkakm, "\nRegulāra četrstūra perimetrs ir:", pkakm ,"\nRegulāra četrstūra laukums ir:",  lkkakm , sep= ' ')

        if(S2==5):
            Skakp=int(input("Ierakstīt ievilkta riņķu līnijā kvadrāta perimetru:"))
            mkakp=Skakp/4
            dkakp=mkakp*sqrt(2)
            rkakp=dkakp/2
            lrkakp=math.pi*pow(rkakp,2)
            lkkakp=mkakp*mkakp
            print("Riņķa līnijas radiuss ir:", rkakp ,"\nRiņķa līnijas diametrs", dkakp, "\nRiņķa līnijas laukums ir:", lrkakp ,"\nRegulāra četrstūra mala ir:", mkakp,"\nRegulāra četrstūra laukums ir:",  lkkakm , sep= ' ')

        if(S2==6):
            Skakl=int(input("Ierakstīt apvilkta ap riņķu līniju kvadrāta laukumu:"))
            mkakl=sqrt(Skakl)
            dkakl=mkakl*sqrt(2)
            rkakl=dkakl/2
            lrkakl=math.pi*pow(rkakl,2)
            pkakl=Skakl*4
            print("Riņķa līnijas radiuss ir:", rkakl ,"\nRiņķa līnijas diametrs", dkakl, "\nRiņķa līnijas laukums ir:", lrkakl ,"\nRegulāra četrstūra mala ir:", mkakl, "\nRegulāra četrstūra perimetrs ir:", pkakl, sep= ' ')
        if(S2<1 and S2>7):
            print("Kļūda! Jums vajag uzrakstīt vienu no cipariem, kuri ir doti. Mēģināt vēlreiz ")
            
    if(S<1 or S>2 and S1<1 or S1>2):
        print("Kļūda! Jums vajag uzrakstīt vienu no cipariem, kuri ir doti. Mēģināt vēlreiz ")
mat()
