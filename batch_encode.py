import os
import subprocess

# Daftar 5 file WAV sumber
files = ["audio1.wav", "audio2.wav", "audio3.wav", "audio4.wav", "audio5.wav"]
target_bitrate = "128k"

print("=== MEMULAI BATCH ENCODING AUDIO TO MP3 128K ===")

for file in files:
    if os.path.exists(file):
        output_file = f"encoded_{os.path.splitext(file)[0]}.mp3"
        # Memanggil file ffmpeg.exe di folder yang sama
        cmd = [
            ".\\ffmpeg.exe", "-y", "-i", file, 
            "-c:a", "libmp3lame", 
            "-b:a", target_bitrate, 
            output_file
        ]
        
        print(f"[PROSES] Encoding {file} -> {output_file}...")
        result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        
        if result.returncode == 0:
            print(f"[SUKSES] {output_file} berhasil dibuat.")
        else:
            print(f"[GAGAL] Gagal memproses {file}.")
    else:
        print(f"[WARNING] File {file} tidak ditemukan!")

print("=== BATCH ENCODING SELESAI ===")