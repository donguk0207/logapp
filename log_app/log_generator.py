import random
import time
from .models import PacketLog

# 랜덤한 IP 주소 생성
def generate_random_ip():
    return f"{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}"

# 패킷 크기 (bytes_in, bytes_out)
def generate_random_bytes():
    return random.randint(100, 1500)  # 패킷 크기 100~1500 bytes

# 패킷 수 (packets_in, packets_out)
def generate_random_packets():
    return random.randint(1, 10)  # 패킷 수 1~10

# 프로토콜 (TCP, UDP)
def generate_random_protocol():
    return random.choice(["TCP", "UDP"])

# 호스트 이름 생성
def generate_random_host():
    return f"host{random.randint(1, 100)}"

# 로그 생성 함수
def generate_log():
    src_ip = generate_random_ip()
    dst_ip = generate_random_ip()
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    bytes_in = generate_random_bytes()
    bytes_out = generate_random_bytes()
    packets_in = generate_random_packets()
    packets_out = generate_random_packets()
    protocol = generate_random_protocol()
    host = generate_random_host()

    log = {
        "timestamp": timestamp,
        "src_ip": src_ip,
        "dst_ip": dst_ip,
        "protocol": protocol,
        "bytes_in": bytes_in,
        "bytes_out": bytes_out,
        "packets_in": packets_in,
        "packets_out": packets_out,
        "host": host
    }

    return log
