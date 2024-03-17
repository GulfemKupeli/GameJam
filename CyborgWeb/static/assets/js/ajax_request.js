// Örnek AJAX isteği
$(document).ready(function() {
    $('#comment-form').submit(function(event) {
        event.preventDefault(); // Sayfa yenilenmesini engelle
        $.ajax({
            type: 'POST',
            url: '/comment/',
            data: $(this).serialize(),
            success: function(response) {
                if (response.success) {
                    alert('Yorum başarıyla kaydedildi');
                    // Yorum gönderildikten sonra gerekli işlemleri yapabilirsiniz, örneğin yorumu ekrana ekleyebilirsiniz.
                } else {
                    alert('Yorum kaydedilemedi');
                }
            },
            error: function() {
                alert('Bir hata oluştu');
            }
        });
    });
});
