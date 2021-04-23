def sozluk(liste1,liste2):
    sozluk={}
    for i in set(liste1):
        for j in range(len(liste1)):
            if i==liste1[j] and i not in sozluk:
                sozluk[i]=list(liste2[j])
            elif i==liste1[j] and i in sozluk:
                sozluk[i].append(liste2[j])
    yeni_sozluk=dict(zip(sorted(sozluk,reverse=False)[:10],sorted(list(map(lambda x:len(x),list(sozluk.values()))),reverse=True)[:10]))
    for i in yeni_sozluk:
        print(i,"--->",yeni_sozluk[i])


dosya=open("Makaleler.txt","r").read().split("\n")
sonuc=[dosya[i].split() for i in range(len(dosya)) if  i%14==0]
editor=list((map(lambda x:" ".join(x[i] for i in range(5,len(x),2)),sonuc)))
makale=list((map(lambda x:list(x[i] for i in range(3,len(x),4)),sonuc)))
print("   TOP 10 EDİTORLER   ")
sozluk(editor,makale)

makaleler=list((map(lambda x:" ".join(x[i] for i in range(3,len(x),4)),sonuc)))
editorler=list((map(lambda x:list(x[i] for i in range(5,len(x),2)),sonuc)))
print("   TOP 10 MAKALELER   ")
sozluk(makaleler,editorler)

makale_adi=list((map(lambda x:" ".join(x[i] for i in range(3,len(x),4)),sonuc)))
print("   TOP 10 REVİZELER   ")
sozluk(makale_adi,makale_adi)