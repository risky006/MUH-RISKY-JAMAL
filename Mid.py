import hashlib

def buat_hash_md5(nama, email, nomor_hp):
    data = f"{nama}|{email}|{nomor_hp}"
    hash_md5 = hashlib.md5(data.encode()).hexdigest()
    return hash_md5

print("=" * 50)
print("   SISTEM CEK PERUBAHAN DATA PROFIL USER (MD5)")
print("=" * 50)

# Input data awal
print("\n[LANGKAH 1] Input Data Profil Awal")
nama_awal    = input("Nama     : ")
email_awal   = input("Email    : ")
hp_awal      = input("Nomor HP : ")

# Buat dan simpan hash awal
hash_awal = buat_hash_md5(nama_awal, email_awal, hp_awal)
print(f"\n[INFO] Hash MD5 awal disimpan:")
print(f"       {hash_awal}")

# Input data baru
print("\n[LANGKAH 2] Input Data Profil Baru")
nama_baru    = input("Nama     : ")
email_baru   = input("Email    : ")
hp_baru      = input("Nomor HP : ")

# Buat hash baru
hash_baru = buat_hash_md5(nama_baru, email_baru, hp_baru)

# Tampilkan perbandingan
print("\n" + "=" * 50)
print("   HASIL PERBANDINGAN HASH MD5")
print("=" * 50)
print(f"Hash Lama : {hash_awal}")
print(f"Hash Baru : {hash_baru}")
print("-" * 50)

# Tampilkan status perubahan
if hash_awal == hash_baru:
    print("STATUS    : DATA TIDAK BERUBAH")
else:
    print("STATUS    : DATA TELAH DIMODIFIKASI!")
print("=" * 50)