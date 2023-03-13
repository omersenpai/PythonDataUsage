# -*- coding: utf-8 -*-
"""Diabet Datasets Ödevi

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1BGFlCjbYAlJScUjJXzvpU3I-AQ8Kmg6d
"""

# EDA
import numpy as np #lineer Cebir
import pandas as pd # veri işleme, CSV dosyası G/Ç (ör. pd.read_csv)

# Veri Görselleştirme
import matplotlib.pyplot as plt

import seaborn as sns


# Uyarıları Yoksay
import warnings
warnings.filterwarnings('ignore')

df = pd.read_csv('/content/diabetes.csv') #csv dosyası yükleme
df.shape #Veri setinin yapısı, kaç adet veri olduğu

# Gebelikler: Hamilelik Oranı
# Glukoz: Oral glukoz tolerans testinde 2 saatlik plazma glukoz konsantrasyonu
# Kan Basıncı: Diyastolik kan basıncı (mm Hg)
# Cilt Kalınlığı: Triceps cilt kıvrım kalınlığı (mm)
# İnsülin: 2 saatlik serum insülini (mu U/ml)
# BMI: Vücut kitle indeksi (kg cinsinden ağırlık/(m cinsinden boy)^2)
# DiabetesPedigreeFunction: Diyabet soyağacı işlevi
# Yaş: Yaş (yıl)
# Sonuç: Sınıf değişkeni (0 veya 1)  

df.info() #yapısal form hakkında bilgi

df.isnull().sum()  #eksik veri olup olmadığı kontrol edilir varsa 1 yoksa 0 döndürür.

print(df.duplicated()) #Tekrar eden her satır için boole değer döndürür.
df.drop_duplicates(inplace = True)#Tekrar eden kopyaları kaldırmak için kullanılır

df.rename(columns={'Pregnancies': 'Gebelik','Glucose': 'Glukoz','BloodPressure': 'KanBasıncı','SkinThickness': 'DeriKalınlığı','BMI': 'VKE','DiabetsPedigreeFunction': 'DiyabetSoyağacı','Age': 'Yaş','Outcome': 'Sonuç'}) 
#İsim değişikliği yaptık.

hamile_olanlar=df[df["Pregnancies"]>5]
print("Hamile olanların sayısı :\t " + str(len(hamile_olanlar)))
hamile_diyabetli=df[((df["Pregnancies"]>5) & df["Outcome"]==1)]  
print("Hamile ve Diyabeti Olanlar:\t"+ str(len(hamile_diyabetli)))
print("Hamilelerde Diyabet oranı:\t" + str(round(len(hamile_diyabetli)/len(df),2)) + " %")

# O sebeple tüm eksik verileri bulundukları sütunların medyan değeri ile dolduracağız
for i in list(df.columns):
    df[i] = df[i].fillna(df[i].median())
    # eksik veriler gitmiş mi diye kontrol edelim
for i in list(df.columns):
    print(f"{i} --> {df[i].isnull().sum()}")

#Below 18.5 -> Zayıf
#18.5 – 24.9 -> Normal 
#25.0 – 29.9 -> Kilolu
#30.0 and Above -> Obez

listBMI=["Zayıf","Normal","Kilolu","Obez"] #Vücut kitle endeksini derecelendirebileceğimiz bir list oluşturuyoruz.
newbmı=pd.Series(listBMI)

df["NBMI"]=newbmı

                                                                  
df.loc[df["BMI"]<18.5,"NBMI"]=newbmı[0]
df.loc[(df["BMI"]>18.5) & (df["BMI"]<=24.9) ,"NBMI"]=newbmı[1]
df.loc[(df["BMI"]>=25) & (df["BMI"]<=29.9) ,"NBMI"]=newbmı[2]
df.loc[df["BMI"]>=30 ,"NBMI"]=newbmı[3]
df.tail(10)

plt.figure(figsize = [20, 5] , dpi = 100) 
plt.scatter (df["BMI"] , df["Age"] , color = "blue")
plt.title ("Yaş ve Vücut Kitle Endeksi Arasındaki ilişki " , weight = 'bold', fontsize = 30)
plt.xticks (range (0 , 80 , 10) , fontsize = 10 )#xAralık belirle
plt.yticks (range (20 , 90 , 10) , fontsize = 10)#yAralık belirle
plt.xlabel ('Vücut Kitle Endeksi', fontsize = 30 )
plt.ylabel ('Yaş' , fontsize = 30)
plt.grid () #grid ekler
plt.show ()

#We will see 0 as the False and 1 as the True cases in the data, i.e:

#0: Diyabeti Olmayanlar

#1: Diyabeti Olanlar

var_diyabet = df[df["Outcome"]==1]
yok_diyabet = df[~(df["Outcome"]==1)]
print("Diyabeti Olanlar:\t"+ str(len(var_diyabet)))
print("Diyabeti Olmayanlar:\t"+ str(len(yok_diyabet)))

x=np.array(['Diyabeti Olanlar','Diyabeti Olmayanlar'])
y=np.array([len(var_diyabet),len(yok_diyabet)])

plt.bar(x,y)
plt.show()

print("diyabet oranı:\t" + str(round(len(var_diyabet)/len(df),2)) + " %")#len(df)=768
print("diyabet olmayanların oranı:\t" + str(round(len(yok_diyabet)/len(df),2)) + " %")

plt.figure(figsize=(12,6))
zayif_olanlar=df[df["NBMI"]=="Zayıf"]
print("Zayıf olanların sayısı :\t " + str(len(zayif_olanlar)))
normal_olanlar=df[df["NBMI"]=="Normal"]
print("Normal olanların sayısı :\t " + str(len(normal_olanlar)))
kilolu_olanlar=df[df["NBMI"]=="Kilolu"]
print("Kilolu olanların sayısı :\t " + str(len(kilolu_olanlar)))
obez_olanlar=df[df["NBMI"]=="Obez"]
print("obez olanların sayısı : \t " + str(len(obez_olanlar)))

print("zayıf oranı:\t" + str(round(len(zayif_olanlar)/len(df),2)) + " %")
print("normal oranı:\t" + str(round(len(normal_olanlar)/len(df),2)) + " %")
print("kilolu oranı:\t" + str(round(len(kilolu_olanlar)/len(df),2)) + " %")
print("obez oranı:\t" + str(round(len(obez_olanlar)/len(df),2)) + " %")

labels = ('Zayıf','Normal','Kilolu','Obez')
sizes = [0.02, 0.13, 0.23,0.61]
colors = ['pink','lightblue','yellow','black']
plt.pie(sizes,labels=labels,colors=colors,autopct='%1.1f%%')
plt.title('Vücut Kitle Endeksi Dağılımı')
plt.show()

df.head(3)#İlk 3 değerin sütun değerlerini görmemizi sağlar.
plt.figure(figsize=(12,6))
xpoints=np.array([35,29,0])
ypoints=np.array([72,66,64])
plt.plot(xpoints,ypoints,
         marker='o',
         markersize='10',
         markeredgecolor='r',
         markerfacecolor='y',
         linewidth='5.5',
         color='#FFCBDB',
         ls='dashed'
         )


plt.xlabel("Deri Kalınlığı")
plt.ylabel("Kan Basıncı")
plt.show()

#Glucose sütununun her iki sınıf özelinde histogramının alınması
plt.figure(figsize=(12,6))
col = 'Glucose'
plt.hist(df[df['Outcome']==0][col], 10, alpha=0.5,color='#9acd32', label='diyabeti olmayanlar')
plt.hist(df[df['Outcome']==1][col], 10, alpha=0.5,color='#ee104e', label='diyabeti olanlar')
plt.legend(loc='upper right')#Grafiğe konum verdik.
plt.xlabel('Glikoz')
plt.ylabel('Sıklık')
plt.title('Glukozun Histogramı')
plt.show()

df.head(4)#İlk 4 değerin sütun değerlerini görmemizi sağlar.
plt.figure(figsize=(12,6))
xpoints=np.array([148,85,183,89])
ypoints=np.array([50,31,32,21])
plt.plot(xpoints,ypoints,
         marker='o',
         markersize='15',
         markeredgecolor='r',
         markerfacecolor='y',
         linewidth='5.5',
         color='y',
         ls='solid'
         )


plt.xlabel("Glukoz")
plt.ylabel("Yaş")
plt.show()

sns.distplot(df["BloodPressure"], color = "b");# bize verilerin dağılımlarını histogram (sütun grafiği) ile sunar.