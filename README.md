# gRPC-Redis
gRPC istemci ve gRPC sunucu kullanarak Redis veritabanına kayıt işlemi.

# Gerekli Kurulumlar
> [Docker for Windows](https://docs.docker.com/docker-for-windows/install/) indir ve kur.

# Çalıştırmak İçin
Proje klasörüne git ve
```
docker-compose build
docker-compose up
```
# Son Adım
Server kurulumu client kurulumundan uzun sürdüğü için server container'ının da ayağa kalkması uzun sürüyor. 
Bu nedenle client ilk başta bağlantı hatası veriyor. Düzeltmek amacıyla docker-compose içerisindeki client altına 
```
restart: on-failure
```
satırını ekledim. Böylece server tarafı hazır olana dek client yeniden başlatılacak ve her şey düzgün çalıştığında sonuçlar gözükecek.

```
gRPC server 4040 portunu dinliyor...
```