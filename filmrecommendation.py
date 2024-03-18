import numpy as np
import pandas as pd

column_names = ['user_id' , 'item_id' , 'rating', 'timestamp']  # dataset için kolon isimleri oluşturuluyor
df = pd.read_csv('./datas/users.data', sep='\t', names=column_names) # Veri dosyası okunuyor, tab ile ayrılmış bir dosya olduğu belirtiliyor.

movie_titles = pd.read_csv("./datas/movie_id_titles.csv") # Film başlıklarını içeren bir CSV dosyası okunuyor.

df = pd.merge(df, movie_titles, on=['item_id'], how='left') # Veri çerçeveleri birleştiriliyor, 'item_id' sütununa göre birleştirme yapılıyor.


# 'user_id' sütununa göre indekslenmiş, 'title' ve 'rating' sütunlarını içeren bir pivot tablosu oluşturuluyor.
moviemat = df.pivot_table(index='user_id',columns='title',values='rating') 


# 'Bir Filmin' kullanıcı derecelendirmeleri alınıyor.

film_user_ratings = moviemat ['Terminator, The (1984)']

#corrwith() metodunu kullanarak Star wars filmi ile korelasyonları hesaplanıyor:
similar_to_film = moviemat.corrwith(film_user_ratings)


# Korelasyon değerleri bir DataFrame'e dönüştürülüyor ve NaN değerleri temizleniyor.
corr_films = pd.DataFrame(similar_to_film, columns=['Correlation'])
corr_films.dropna(inplace=True)

# 'timestamp' sütunu veri setinden kaldırılıyor.
df = df.drop(['timestamp'], axis = 1)

# Her bir film için ortalama derecelendirme hesaplanıyor.
ratings = pd.DataFrame(df.groupby('title')['rating'].mean())

# Derecelendirme sayısını içeren bir sütun ekleniyor.
ratings['rating_oy_sayisi'] = pd.DataFrame(df.groupby('title')['rating'].count())
corr_films = corr_films.join(ratings['rating_oy_sayisi'])

# Korelasyon tablosu, 100'den fazla oy alan filmlerle sınırlandırılıyor.
filtered_corr_films = corr_films[corr_films['rating_oy_sayisi'] > 100]
# Korelasyon tablosu, korelasyona göre sıralanıyor ve yazdırılıyor.
sorted_corr_starwars = filtered_corr_films.sort_values('Correlation', ascending=False).head()

print(sorted_corr_starwars.head())

"""
Results;
                                    Correlation  rating_oy_sayisi
title
Godfather, The (1972)                  1.000000               413
Godfather: Part II, The (1974)         0.683862               209
GoodFellas (1990)                      0.421477               226
People vs. Larry Flynt, The (1996)     0.393439               215
Bonnie and Clyde (1967)                0.386226               122

"""
