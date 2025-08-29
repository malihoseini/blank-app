import streamlit as st
import numpy as np
import pandas as pd
import joblib
address_arr = ['Abazar', 'Abbasabad','Absard','Abuzar','Afsarieh','Ahang','Air force','Ajudaniye','Alborz Complex',
                                                    'Aliabad South','Amir Bahador','Amirabad','Amirieh','Andisheh','Aqdasieh','Araj','Argentina','Atabak',
                                                    'Azadshahr','Azarbaijan','Azari','Baghestan','Bahar','Baqershahr','Beryanak','Boloorsazi','Central Janatabad',
                                                    'Chahardangeh','Chardangeh','Chardivari','Chidz','Damavand','Darabad','Darakeh','Darband','Daryan No',
                                                    'Dehkade Olampic','Dezashib','Dolatabad','Dorous','East Ferdows Boulevard','East Pars','Ekbatan','Ekhtiarieh',
                                                    'Elahieh','Elm-o-Sanat','Enghelab','Eram','Eskandari','Fallah','Farmanieh','Fatemi','Feiz Garden','Firoozkooh',
                                                    'Firoozkooh Kuhsar','Garden of Saba','Gheitarieh','Ghiyamdasht','Ghoba','Gholhak','Gisha','Golestan','Haft Tir',
                                                    'Hakimiyeh','Hashemi','Hassan Abad','Hekmat','Heravi','Heshmatieh','Hor Square','Islamshahr','Islamshahr Elahieh',
                                                    'Javadiyeh','Jeyhoon','Jordan','Kahrizak','Kamranieh','Karimkhan','Karoon','Kazemabad','Keshavarz Boulevard',
                                                    'Khademabad Garden','Khavaran','Komeil','Koohsar','Kook','Lavizan','Mahallati','Mahmoudieh','Majidieh','Malard',
                                                    'Marzdaran','Mehrabad','Mehrabad River River','Mehran','Mirdamad','Mirza Shirazi','Moniriyeh','Narmak','Nasim Shahr',
                                                    'Nawab','Naziabad','Nezamabad','Niavaran','North Program Organization','Northern Chitgar','Northern Janatabad',
                                                    'Northern Suhrawardi','Northren Jamalzadeh','Ostad Moein','Ozgol','Pakdasht','Pakdasht KhatunAbad','Parand',
                                                    'Parastar','Pardis','Pasdaran','Persian Gulf Martyrs Lake','Pirouzi','Pishva','Punak','Qalandari','Qarchak',
                                                    'Qasr-od-Dasht','Qazvin Imamzadeh Hassan','Railway','Ray','Ray - Montazeri','Ray - Pilgosh','Razi','Republic',
                                                    'Robat Karim','Rudhen','Saadat Abad','SabaShahr','Sabalan','Sadeghieh','Safadasht','Salehabad','Salsabil','Sattarkhan',
                                                    'Seyed Khandan','Shadabad','Shahedshahr','Shahr-e-Ziba','ShahrAra','Shahrake Apadana','Shahrake Azadi','Shahrake Gharb',
                                                    'Shahrake Madaen','Shahrake Qods','Shahrake Quds','Shahrake Shahid Bagheri','Shahrakeh Naft','Shahran',
                                                    'Shahryar','Shams Abad','Shoosh','Si Metri Ji','Sohanak','Southern Chitgar','Southern Janatabad',
                                                    'Southern Program Organization','Southern Suhrawardi','Tajrish','Tarasht','Taslihat','Tehran Now','Tehransar',
                                                    'Telecommunication','Tenant','Thirteen November','Vahidieh','Vahidiyeh','Valiasr','Vanak','Varamin - Beheshti',
                                                    'Velenjak','Villa','Water Organization','Waterfall','West Ferdows Boulevard','West Pars','Yaftabad','Yakhchiabad',
                                                    'Yousef Abad','Zafar','Zaferanieh','Zargandeh','Zibadasht']
model = joblib.load('housePrice.joblib')
Area = st.number_input('Input Area', 0, 1000)
Rooms = st.slider('Choose Number of Rooms', 0, 4)
Parking = st.select_slider('Do you have Parking?', [False, True])
Warehouse = st.select_slider('Do you have Warehouse?', [False, True])
Elevator = st.select_slider('Do you have Elevator?', [False, True])
Address = st.select_slider('Select your Address?', address_arr)
columns = ['Area','Rooms','Parking','Warehouse', 'Elevator']
values = [Area, Rooms, Parking, Warehouse, Elevator]
for i in address_arr :
    columns.append('Address_'+i)
    if i==Address:
        values.append(1)
    else :
        values.append(0)
def predict():
    row = np.array(values)
    X = pd.DataFrame([row], columns=columns)
    prediction = model.predict(X)
    st.write(prediction)
trigger = st.button('predict', on_click=predict)
