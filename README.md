    git clone https://github.com/isikerenalp/django_blog.git
    cd django_blog/
    source env/bin/activate
    cd blog/
    python manage.py runserver 127.0.0.1:3000


# Özellikler
---
Üye giriş çıkışı ve kayıt olma (mail ile doğrulama)

Blog Yazısı C(create)R(read)U(update)D(delete)

Kategoriye ait blog yazılarının listelenmesi

Yorum ekle / sil

Sayfalama

Parola Değiştirme

Parola sıfırlama

# Eklenecek Özellikler
---

Kullanıcı Profili

Gönderi beğenme , kullanıcı takip etme , mesajlaşma

    Not: Sayfada henüz herhangi bir tasarım yoktur :/
    
    Not-2 : Mail işlemlerinin çalışması için django_blog/blog/blog/settings.py ' de 131. satırdan sonrasını güncellemeniz gerekmektedir
