from django.db import models

# Create your models here.
'''
    seq INT AUTO_INCREMENT PRIMARY KEY,  -- 자동 증가 기본 키
    time DATETIME NOT NULL,  -- YYYY-MM-DD HH:MI:SS 형식의 시간 데이터
    user_id VARCHAR(255) NOT NULL,  -- 사용자 ID (문자열)
    servicemenu VARCHAR(255) NOT NULL,  -- 서비스 메뉴 (문자열)
    stars VARCHAR(255) NOT NULL,  -- 별점 (문자열)
    access_type VARCHAR(255) NOT NULL,  -- 접근 유형 (문자열)
    reserve VARCHAR(255) NOT NULL  -- 예약 (문자열)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
'''

class log_data(models.Model):
    seq = models.AutoField(primary_key=True)
    time = models.CharField(max_length=255)
    user_id = models.CharField(max_length=255)
    servicemenu = models.CharField(max_length=255)
    stars = models.CharField(max_length=255)
    access_type = models.CharField(max_length=255)
    reserve = models.CharField(max_length=255)

    def __str__(self):
        return self.user_id