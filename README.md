     BIG DATA ASSIGNMENT

     NAMES:NSABIMANA SIMON BRICE
     ID: 27451

<img width="1919" height="1005" alt="Screenshot 2025-07-26 161951" src="https://github.com/user-attachments/assets/b7ccdb2b-1d04-4d5b-8be5-f731e2895106" />
Here i was importing library to use (pandas) and also initilisation of main DataFrame used in your Python code to store and process the cleaned Uber ride data and display 1st few data to know the format
<img width="1795" height="807" alt="Screenshot 2025-07-26 162002" src="https://github.com/user-attachments/assets/dca4f861-86e9-4213-80ee-c2ee907e909c" />
this uber_df.info() displays the All columns are filled — no missing (null) values.

Data types:

datetime64[ns] for timestamps

float64 for coordinates, fares, and distances

int64 for numerical time features

object for text like day names and time categories
<img width="1557" height="670" alt="Screenshot 2025-07-26 162017" src="https://github.com/user-attachments/assets/a0fe52d5-4ef4-44bb-85b4-d5360c6a1281" />
drops null values raw
<img width="1585" height="873" alt="Screenshot 2025-07-26 162045" src="https://github.com/user-attachments/assets/60b6bcde-4210-409a-ba12-7d4d09eefa95" />
<img width="1910" height="975" alt="Screenshot 2025-07-26 162101" src="https://github.com/user-attachments/assets/b7714eb5-e2d6-47e3-82ec-701f067b7164" />
changed name column names, droped raw with 0 values, reset index
<img width="1771" height="881" alt="Screenshot 2025-07-26 162128" src="https://github.com/user-attachments/assets/00586b77-c92c-440b-ba14-406204d16735" />
display with new names

<img width="1885" height="970" alt="Screenshot 2025-07-26 164654" src="https://github.com/user-attachments/assets/afb90a1a-7b00-47f7-8235-d96be29cb01b" />
So, this contains very important data for analysis i.e ▪ Mean, median, standard deviation
 
▪ Quartiles and data ranges
▪ Outlier identification
<img width="1540" height="623" alt="Screenshot 2025-07-26 165520" src="https://github.com/user-attachments/assets/80fc0fce-4b16-4687-b59e-4677f3df50f5" />
and then the mode provided
<img width="1550" height="786" alt="Screenshot 2025-07-26 172355" src="https://github.com/user-attachments/assets/7402b236-c6b0-4088-bd0a-e224b16d44e1" />
since fare amount can't be negative we also clean
<img width="1825" height="746" alt="Screenshot 2025-07-26 190214" src="https://github.com/user-attachments/assets/eb52ff01-e57b-4ef4-8e28-eb2ee5fe8d3d" />
install geopy for distance and so on and also set real latitudes and longitudes
<img width="1513" height="797" alt="Screenshot 2025-07-26 190233" src="https://github.com/user-attachments/assets/7bf77c14-0257-4b2d-8ca0-c05fe5ebdaee" />
new column of distance
<img width="1910" height="624" alt="Screenshot 2025-07-26 190515" src="https://github.com/user-attachments/assets/a2c9bc19-02c8-4a63-b944-43401337c746" />
new columns (hour,day,month...)
<img width="1919" height="1017" alt="Screenshot 2025-07-26 162809" src="https://github.com/user-attachments/assets/cdfe8f72-7747-461f-a4bf-e4101cff12db" />
then saving it to the new data frame (cleaned data set)
  after that i extracted the new cleaned data set and loaded it in power bi for analysis
<img width="578" height="260" alt="Screenshot 2025-07-27 095112" src="https://github.com/user-attachments/assets/0339ce5b-b2cc-422b-b4db-e1797c3392bb" />
this shows the fare patterns across different time intervals
<img width="1854" height="932" alt="Screenshot 2025-07-27 102703" src="https://github.com/user-attachments/assets/09e92af2-52c5-4c96-ab23-54a1da09e92d" />
and this shows the hourly, daily, and monthly ride patterns
<img width="1919" height="1003" alt="Screenshot 2025-07-27 102654" src="https://github.com/user-attachments/assets/a02682bf-0303-4fff-bcc9-156a70cbffdd" />
and then this shows the Seasonal trends and variations
<img width="1887" height="969" alt="Screenshot 2025-07-27 102712" src="https://github.com/user-attachments/assets/b69d4fd6-8e62-4a41-8d6b-307da4ffaf75" />
this analyses the relationship between Fare amount and distance traveled
but !!!!!!!!! here since we were given longitudes and latitudes there were some difficulties since the distance might have came wrong because the geopy was just doing a straight line from place A to B which in real life might be wrong because some charges were wrong forexample a person might go to a go in a circle all go pickup something and the ride is finished were he/she started the journey but here they calculate and find that he/she moved like 3 metres and paid more than a person who went 1 km therefore it's not accurate
<img width="1920" height="1080" alt="Screenshot (17)" src="https://github.com/user-attachments/assets/de6bd33b-1c83-47f9-b92a-fc921d54b096" />
you can still see it here
<img width="1920" height="1080" alt="Screenshot (16)" src="https://github.com/user-attachments/assets/f9de913d-d328-4561-b913-031c1b780917" />
these are DAX formulas used to create a new column (Timesofday)
