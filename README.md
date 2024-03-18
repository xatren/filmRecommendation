# Film Recommendation System

## Introduction

This Film Recommendation System is designed to suggest movies to users based on their viewing history and preferences. It utilizes a dataset of user ratings for various movies to identify movies similar to a given film. The system employs Pandas for data manipulation, leveraging a correlation matrix to find movies that share similar rating patterns.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Dependencies](#dependencies)
- [Data](#data)
- [Configuration](#configuration)
- [Examples](#examples)
- [Troubleshooting](#troubleshooting)
- [Contributors](#contributors)


## Installation

Ensure you have Python 3.6 or later installed. It's advisable to use a virtual environment:

```bash
pip install numpy pandas
```

## Usage

Run the script with Python to generate movie recommendations based on the dataset:

```bash
python filmrecommendation.py
```

## Features

- Reading and merging datasets of movies and user ratings.
- Creating a pivot table to index user IDs against movie titles and their ratings.
- Calculating correlation coefficients between movies to find similarities.
- Filtering recommendations based on a minimum number of ratings to improve reliability.

## Dependencies

- numpy
- pandas

## Data

The system uses two key datasets:
- User ratings (`users.data`): Contains user IDs, item IDs, ratings, and timestamps.
- Movie titles (`movie_id_titles.csv`): Contains item IDs and the titles of movies.

These files should be located in the `./datas` directory relative to the script.

## Configuration

No additional configuration is required to run the script as provided. Ensure the datasets are correctly placed in the `./datas` folder.

## Examples

The script calculates recommendations similar to "Terminator, The (1984)" by default. To change the reference movie, modify the `film_user_ratings` line in the script:

```python
film_user_ratings = moviemat['Your Movie Title Here']
```

## Troubleshooting

If the script fails to run:
- Check Python version (3.6+ required).
- Ensure all dependencies are installed.
- Verify the data files are correctly located and formatted.

## Contributors

Emircan Yüksel


# Film Öneri Sistemi

## Giriş

Bu Film Öneri Sistemi, kullanıcıların izleme geçmişi ve tercihlerine dayanarak kullanıcılara film önerileri sunmak üzere tasarlanmıştır. Çeşitli filmlere yapılan kullanıcı değerlendirmelerinin bulunduğu bir veri setini kullanarak, belirli bir filme benzer filmleri belirlemek için tasarlanmıştır. Sistem, veri manipülasyonu için Pandas kullanır ve benzer derecelendirme modellerine sahip filmleri bulmak için bir korelasyon matrisinden yararlanır.

## İçindekiler

- [Kurulum](#kurulum)
- [Kullanım](#kullanım)
- [Özellikler](#özellikler)
- [Bağımlılıklar](#bağımlılıklar)
- [Veri](#veri)
- [Konfigürasyon](#konfigürasyon)
- [Örnekler](#örnekler)
- [Sorun Giderme](#sorun-giderme)
- [Katkıda Bulunanlar](#katkıda-bulunanlar)


## Kurulum

Python 3.6 veya daha yeni bir sürümünün yüklü olduğundan emin olun. Sanal bir ortam kullanılması tavsiye edilir:

```bash
pip install numpy pandas
```

## Kullanım

Veri setine dayanarak film önerileri üretmek için scripti Python ile çalıştırın:

```bash
python filmrecommendation.py
```

## Özellikler

- Filmlere ve kullanıcı derecelendirmelerine dair veri setlerinin okunması ve birleştirilmesi.
- Kullanıcı ID'lerinin film başlıklarına ve derecelendirmelerine karşı indekslendiği bir pivot tablo oluşturma.
- Filmler arası benzerlikleri bulmak için korelasyon katsayıları hesaplama.
- Güvenilirliği artırmak için minimum derecelendirme sayısına göre önerileri filtreleme.

## Bağımlılıklar

- numpy
- pandas

## Veri

Sistem iki ana veri seti kullanır:
- Kullanıcı derecelendirmeleri (`users.data`): Kullanıcı ID'leri, öğe ID'leri, derecelendirmeler ve zaman damgaları içerir.
- Film başlıkları (`movie_id_titles.csv`): Öğe ID'leri ve filmlerin başlıklarını içerir.

Bu dosyalar, scripte göre `./datas` dizininde yer almalıdır.

## Konfigürasyon

Script, sağlandığı şekilde çalıştırmak için ek bir konfigürasyona ihtiyaç duymaz. Veri setlerinin `./datas` klasöründe doğru şekilde yerleştirildiğinden emin olun.

## Örnekler

Script varsayılan olarak "Terminator, The (1984)" filmine benzer öneriler hesaplar. Referans filmi değiştirmek için scriptteki `film_user_ratings` satırını değiştirin:

```python
film_user_ratings = moviemat['Film Başlığınız Buraya']
```

## Sorun Giderme

Script çalıştırılamazsa:
- Python sürümünü kontrol edin (3.6 veya daha yeni gerekli).
- Tüm bağımlılıkların yüklendiğinden emin olun.
- Veri dosyalarının doğru konumlandırıldığından ve uygun şekilde biçimlendirildiğinden emin olun.

## Katkıda Bulunanlar

Emircan Yüksel

