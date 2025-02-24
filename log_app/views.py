from django.http import JsonResponse
from django.shortcuts import render
from .models import PacketLog
from .log_generator import generate_log
# Create your views here.

def index(request):
    # 기존 로그를 가져와서 템플릿에 전달
    logs = PacketLog.objects.all().order_by('-timestamp')[:10]
    return render(request, 'index.html', {'logs': logs})

def generate_log_ajax(request):
    # 랜덤 로그 생성
    log_data = generate_log()

    # 데이터베이스에 저장
    log = PacketLog.objects.create(
        timestamp=log_data["timestamp"],
        src_ip=log_data["src_ip"],
        dst_ip=log_data["dst_ip"],
        protocol=log_data["protocol"],
        bytes_in=log_data["bytes_in"],
        bytes_out=log_data["bytes_out"],
        packets_in=log_data["packets_in"],
        packets_out=log_data["packets_out"],
        host=log_data["host"]
    )

    # 새로 생성된 로그 반환
    return JsonResponse({
        'timestamp': log.timestamp,
        'src_ip': log.src_ip,
        'dst_ip': log.dst_ip,
        'protocol': log.protocol,
        'bytes_in': log.bytes_in,
        'bytes_out': log.bytes_out,
        'packets_in': log.packets_in,
        'packets_out': log.packets_out,
        'host': log.host,
    })

def logapp_index(request):
    return render(request,"log_index.html")
