from datetime import datetime, timedelta
import sqlite3
print("\n*** Rezervasyon Sistemine Hoşgeldiniz ***\n")


#Connect to db
conn = sqlite3.connect('randevuSistemi.db')
#Create a cursor
c = conn.cursor()
#Firstly we need to create our table with execute command
#command = "CREATE TABLE appointments (TC text, date text, klinik text, doctor text)"
#c.execute(command)


#Fetch all the data from db selected
def fetchAllFromDB(db_name):
    print("******** Fetching All Data From {} Table ********".format(db_name))
    c.execute("SELECT * FROM appointments")
    conn.commit()
    print(c.fetchall())




#Class for Klinikler
class Klinik:
    def __init__(self, name):
        self.name = name
        self.docs = []
    #Add doctor by name
    def addDoctor(self, doctor_name):
        self.docs.append(doctor_name)
    #Add doctors with array of doctor names
    def addDoctorAsArray(self, doctors):
        for doc in doctors:
            self.docs.append(doc)
    #Get klinik name
    def getName(self):
        return self.name
    #Print doctors who works for klinik
    def printDoctors(self):
        for doc in self.docs:
            print(doc)
    #Get doctors array who works for klinik
    def getDoctors(self):
        return self.docs

#Cocuk Dahiliyesi
cocukDahiliye = Klinik("Çocuk Dahiliyesi")
cocukDahiliye.addDoctor("Cihan Sakman")
doktor_array = ["Barış Manço", "Sibel Can"]
cocukDahiliye.addDoctorAsArray(doktor_array)

#Dahiliye(İç Hastalıkları)
dahiliye = Klinik("Dahiliye(İç Hastalıkları)")
doktor_array = ["Müslüm Gürses","Yıldız Tilbe", "Azer Bülbül"]
dahiliye.addDoctorAsArray(doktor_array)

#Fizyoloji
fizyoloji = Klinik("Fizyoloji")
doktor_array = ["Can Bonomo","Hadise","Sezen Aksu"]
fizyoloji.addDoctorAsArray(doktor_array)

#Göğüs Hastalıkları
gogus_hastaliklari = Klinik("Göğüs Hastalıkları")
doktor_array = ["Hakkı Bulut","İzzet Altınmeşe","Selda Bağcan"]
gogus_hastaliklari.addDoctorAsArray(doktor_array)

#Gün seçimi yalnızca önümüzdeki 7 gün için geçerli olacaktır.
date = []
for N in range(7):
    date_N_days_after = datetime.now() + timedelta(days=N)
    date_N_days_after = date_N_days_after.strftime("%d/%m/%Y")
    date.append(date_N_days_after)

#Alınan tüm randevu özetleri
summary = {}
#Klinikler
klinikler = [cocukDahiliye, dahiliye, fizyoloji, gogus_hastaliklari]

exit = 0
tc = "0"
tekrar = "1"

#Throw Exception
def throwException():
    raise Exception("Error!")

#Gün sonu raporunu yazdıran ve randevuları database'e ekleyen fonksiyon
def printSummary(summary):
    print("Summary", summary)
    print("\n*** RANDEVU İŞLEM ÖZETİ ***")
    print("\n{} farklı TC No için Almış olduğunuz randevu bulunmaktadır.\n".format(len(summary)))
    for each_appointment in summary.keys():
        if(len(summary[each_appointment]) > 1):
            for i in range(len(summary[each_appointment])):
                print(

                    "{} TC nolu hasta için, {} tarihinde, {} kliniğinden, Dr. {}'dan".format(
                        each_appointment, summary[each_appointment][i][2], summary[each_appointment][i][0], summary[each_appointment][i][1]))

                #INSERT THE APPOINTMENT INFORMATIONS INTO DATABASE
                command = "INSERT INTO appointments VALUES ('{}', '{}', '{}', '{}')".format(
                        each_appointment, summary[each_appointment][i][2], summary[each_appointment][i][0], summary[each_appointment][i][1])
                c.execute(command)
        else:
            print(
                "{} TC nolu hasta için, {} tarihinde, {} kliniğinden, Dr. {}'dan".format(
                    each_appointment, summary[each_appointment][0][2], summary[each_appointment][0][0],
                    summary[each_appointment][0][1]))
            # INSERT THE APPOINTMENT INFORMATIONS INTO DATABASE
            command = "INSERT INTO appointments VALUES ('{}', '{}', '{}', '{}')".format(
                    each_appointment, summary[each_appointment][0][2], summary[each_appointment][0][0],
                    summary[each_appointment][0][1])
            c.execute(command)

while(tekrar == "1"):
    #Hasta 11 haneli T.C kimlik numarasını girer.
    while(len(tc) != 11):
        #Her randevu bir array olarak tutulur
        appointment = [[]]
        try:
            tc = int(input("Lütfen 11 haneli kimlik numaranızı giriniz:"))
            tc = str(tc)
            if(len(tc) != 11):
                throwException()
        except:
            print("TC kimlik numaranızı doğru girdiğinizden emin olun!")
            continue

        #Muayene Olmak isteyen hastadan klinik seçimi yapılması istenir.
        klinik = "a"
        while(klinik not in ["0","1","2","3","4"]):
            try:
                print("\nLütfen muayene olmak istediğiniz kliniği tuşlayınız")
                klinik =int(input("""0. Vazgeç ve Çıkış yap
1. Çocuk Dahiliyesi
2. Dahiliye(İç Hastalıkları)
3. Fizyoloji
4. Göğüs Hastalıkları
"""))
                klinik = str(klinik)
               ###### DOKTOR SEÇİMİNİ WHİLE İLE YAP(KLİNİK SEÇİMİ GİBİ OLSUN) ######
                #klinikler = list(klinikler_ve_doktorlar.keys()) # Girilen klinik terchine göre doktorlar sıralanacaktır.
                #appointment[0].append(klinikler[int(klinik)-1]) #klinik randevu arrayine eklenir
                appointment[0].append(klinikler[int(klinik)-1].getName()) #klinik randevu arrayine eklenir

                if(klinik == "1" or klinik == "2" or klinik == "3" or klinik == "4"):
                    doktor = ...
                    while(doktor not in ["0","1","2","3"]):
                        try:
                            print("Lütfen muayene olmak istediğiniz doktoru tıklayınız.(0, 1, 2...)")
                            print("0 Vazgeç ve Çıkış yap")

                            #for i in klinikler_ve_doktorlar[klinikler[int(klinik) - 1]]:
                                #print(i)

                            index = 1
                            doktorlar = klinikler[int(klinik) - 1].getDoctors()
                            for i in doktorlar:
                                print(index, i)
                                index+=1
                            doktor = int(input(""))
                            doktor = str(doktor)
                            if(doktor == "0"):
                                exit = 1
                                break
                            elif(doktor == "1" or doktor == "2" or doktor == "3"):
                                #doktor_selected = (klinikler_ve_doktorlar[klinikler[int(klinik)-1]][int(doktor) - 1])[3:]  # Sadece doktor isimlerini seçiyoruz.
                                doctors_in_selected_klinik = klinikler[int(klinik)-1].getDoctors()
                                doktor_selected = doctors_in_selected_klinik[int(doktor) - 1]
                                appointment[0].append(doktor_selected) #doktor randevu arrayine eklenir
                        except:
                            print("3rd EXcept condition")
                            print("Lütfen geçerli bir seçim yapınız....")
                            continue
                elif(klinik == "0" ):
                    exit = 1
                    break
            except:
                print("2nd EXcept condition")
                print("Lütfen uygun bir klinik seçimi yapınız")
                continue

            if(exit == 1):
                break
            #Muayene Olunmak istenen tarih girilir.
            selected_date = "a"
            while (selected_date not in ["0", "1", "2", "3", "4","5","6","7"]):
                try:
                    print("Dr. {}'dan aldığınız muayene için lütfen geçerli bir tarih seçiniz".format(doktor_selected))
                    num = 1
                    print("0. Vazgeç ve Çıkış yap")
                    for i in date:
                        print(num," ",i)
                        num+=1
                    selected_date = int(input(""))
                    selected_date = str(selected_date)
                    if(selected_date == "0" or exit == 1):
                        exit=1
                    elif(selected_date in ["1", "2", "3", "4","5","6","7"]):
                        date_selected = date[int(selected_date)-1]
                        appointment[0].append(date_selected) #tarih randevu arrayine eklenir
                        #Alınan randevu RANDEVU ÖZETLERİ(summary) arrayine eklenir.
                        if tc in summary.keys():
                            oldList = summary[tc]
                            oldList.append(appointment[0])
                            print("New List:", oldList)
                            summary[tc] = (oldList)

                        else:
                            summary[tc]=appointment
                except:
                    print("4rd Except condition")
                    continue
    if(exit == 1):
        print("Sistemden çıkış yapıldı....")
        break
    elif(exit == 0):
        print("{} tarihinde, Dr. {}'dan aldığınız muayene randevusuna katılımınızı bekliyoruz.\nSağlıklı Günler Dileriz."
              .format(date_selected, doktor_selected))
        tekrar = input("Yeni bir randevu almak isterseniz 1'i Çıkış yapmak için 1 dışında herhang bir tuş tıklayınız:")
        if(tekrar == "1"):
            tc, klinik, doktor, selected_date = "a", ..., ..., ...
            continue

#print summary
printSummary(summary)
fetchAllFromDB('appointments')
conn.close()