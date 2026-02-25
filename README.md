<div class="navbar">
  <div class="logo">CRAZYTEAM</div>
  <div class="badges">
    <img src="https://img.shields.io/badge/Bahasa-Indonesia-black?style=for-the-badge"/>
    <img src="https://img.shields.io/badge/Masuk-E50914?style=for-the-badge"/>
  </div>
</div>

<style>
/* ===== GLOBAL ===== */
body {
  background-color:#000;
  color:white;
  margin:0;
  padding:0;
  font-family: Arial, Helvetica, sans-serif;
}

/* ===== NAVBAR ===== */
.navbar {
  display:flex;
  justify-content:space-between;
  align-items:center;
  padding:20px 40px;
}

.logo {
  color:#E50914;
  font-weight:900;
  font-size:28px;
  letter-spacing:3px;
}

.badges img {
  margin-left:10px;
}

/* ===== HERO ===== */
.hero {
  position:relative;
  text-align:center;
}

.hero img {
  width:100%;
  height:auto;
  filter:brightness(35%);
}

.hero-text {
  position:absolute;
  top:50%;
  left:50%;
  transform:translate(-50%, -50%);
  width:90%;
  max-width:900px;
}

.hero-text h1 {
  font-size:60px;
  font-weight:900;
  margin-bottom:10px;
}

.hero-text h2 {
  font-size:26px;
  font-weight:400;
  margin-bottom:20px;
}

.hero-text p {
  font-size:18px;
  margin-bottom:25px;
}

/* ===== INPUT + BUTTON ===== */
.email-box {
  padding:15px;
  width:280px;
  border-radius:4px;
  border:none;
  margin-right:10px;
}

.netflix-btn {
  background-color:#E50914;
  color:white;
  padding:15px 35px;
  font-size:18px;
  font-weight:bold;
  text-decoration:none;
  border-radius:4px;
  transition:0.3s;
}

.netflix-btn:hover {
  background:#ff1f1f;
  transform:scale(1.05);
}

/* ===== SECTION DIVIDER ===== */
.divider {
  border:1px solid #222;
  margin:60px 0;
}

/* ===== TRENDING / FLOWCHART ===== */
.trending {
  text-align:center;
}

.trending img {
  width:250px;
  margin:10px;
  border-radius:6px;
  transition:0.3s;
}

.trending img:hover {
  transform:scale(1.08);
  box-shadow:0 0 20px rgba(229,9,20,0.7);
}
</style>

<div class="hero">
<img src="https://images.unsplash.com/photo-1605902711622-cfb43c4437b5?q=80&w=2070&auto=format&fit=crop"/>
<div class="hero-text">
<h1>Program Kas Kelas</h1>
<h2>Aplikasi Keuangan Tanpa Batas.</h2>
<p>
Kelola pemasukan dan pengeluaran kas kelas dengan sistem yang lebih profesional dan terstruktur.
</p>
<input class="email-box" placeholder="Masukkan Nama"/>
<a href="https://github.com/Dhilaja/Tugas-Proyek-Crayzteam.git" class="netflix-btn">Mulai ></a>
</div>
</div>

<hr class="divider">

<div class="trending">
<h2 style="font-weight:700; margin-bottom:20px;">🔥 Proyek Flowchart</h2>
<img src="docs/Flowchart Program Kas Kelas.png" width="300"/>
</div>

<hr class="divider">

# 🎬 Tentang Project

Program Kas Kelas adalah aplikasi berbasis **Python CLI** yang dikembangkan untuk membantu pencatatan pemasukan dan pengeluaran kas kelas secara sistematis dan efisien.

### 🎥 Fitur Utama (Episode List)
- **Episode 1** — Tambah Siswa  
- **Episode 2** — Catat Pembayaran & Denda  
- **Episode 3** — Catat Pengeluaran  
- **Episode 4** — Lihat Siswa Belum Bayar 
- **Episode 5** — Laporan Total Kas dan Saldo Akhir

---

# ⚙️ Cara Menjalankan

```bash
git clone [https://github.com/Dhilaja/Tugas-Proyek-Crayzteam.git](https://github.com/Dhilaja/Tugas-Proyek-Crayzteam.git)
cd Tugas-Proyek-Crayzteam
python main.py
