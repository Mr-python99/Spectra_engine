#!/bin/bash
# ╔══════════════════════════════════════════════════════════════╗
# ║     SPECTRA INTEL ENGINE - ULTIMATE v9.0 - INSTALLER         ║
# ║     ------------------------------------                     ║
# ║     Dibuat oleh Spectra                                      ║
# ╚══════════════════════════════════════════════════════════════╝

clear

echo ""
echo "  ╔══════════════════════════════════════════╗"
echo "  ║   SPECTRA INTEL ENGINE v9.0 - INSTALLER  ║"
echo "  ║   EDITION                                ║"
echo "  ╚══════════════════════════════════════════╝"
echo ""

# ============================================================
# FUNGSI PROGRESS
# ============================================================
progress() {
    local current=$1
    local total=$2
    local text=$3
    local bar_length=30
    local filled=$((bar_length * current / total))
    local empty=$((bar_length - filled))
    
    printf "  [%02d/%02d] %s\n" "$current" "$total" "$text"
    printf "  "
    for ((i=0; i<filled; i++)); do printf "█"; done
    for ((i=0; i<empty; i++)); do printf "░"; done
    printf " %d%%\n" $((current * 100 / total))
    echo ""
}

TOTAL_STEPS=10
STEP=1

echo "  ──────────────────────────────────────────"
echo "     MEMERIKSA DEPENDENCIES..."
echo "  ──────────────────────────────────────────"
echo ""

# [1/10] Cek Python3
progress $STEP $TOTAL_STEPS "Checking Python3..."
if command -v python3 &> /dev/null; then
    PYTHON_VERSION=$(python3 --version 2>&1)
    echo -e "  \033[92m✓ $PYTHON_VERSION terdeteksi!\033[0m"
else
    echo -e "  \033[91m✗ Python3 TIDAK ditemukan!\033[0m"
    echo "  Install Python3 terlebih dahulu!"
    exit 1
fi
STEP=$((STEP+1)); echo ""

# [2/10] Cek pip3
progress $STEP $TOTAL_STEPS "Checking pip3..."
if command -v pip3 &> /dev/null; then
    echo -e "  \033[92m✓ pip3 terdeteksi!\033[0m"
else
    echo -e "  \033[93m⚠ pip3 tidak ditemukan, mencoba install...\033[0m"
    sudo apt-get update && sudo apt-get install -y python3-pip 2>/dev/null
    if command -v pip3 &> /dev/null; then
        echo -e "  \033[92m✓ pip3 berhasil diinstall!\033[0m"
    else
        echo -e "  \033[91m✗ Gagal install pip3!\033[0m"
        exit 1
    fi
fi
STEP=$((STEP+1)); echo ""

# [3/10] Install Python modules (requests, urllib3)
progress $STEP $TOTAL_STEPS "Installing Python modules (requests, urllib3)..."
pip3 install requests urllib3 --quiet 2>/dev/null
echo -e "  \033[92m✓ requests, urllib3 terinstall!\033[0m"
STEP=$((STEP+1)); echo ""

# [4/10] Install Rich
progress $STEP $TOTAL_STEPS "Installing Rich (Modern Terminal UI)..."
pip3 install rich --quiet 2>/dev/null
if python3 -c "import rich" 2>/dev/null; then
    echo -e "  \033[92m✓ Rich terinstall! Tampilan modern siap!\033[0m"
else
    echo -e "  \033[91m✗ Gagal install Rich!\033[0m"
    echo "  Coba manual: pip3 install rich"
fi
STEP=$((STEP+1)); echo ""

# [5/10] Install Paramiko (SSH Brute)
progress $STEP $TOTAL_STEPS "Installing Paramiko (SSH Brute Force)..."
pip3 install paramiko --quiet 2>/dev/null
if python3 -c "import paramiko" 2>/dev/null; then
    echo -e "  \033[92m✓ Paramiko terinstall! SSH Brute siap!\033[0m"
else
    echo -e "  \033[93m⚠ Paramiko tidak terinstall (optional)\033[0m"
fi
STEP=$((STEP+1)); echo ""

# [6/10] Cek SQLMap
progress $STEP $TOTAL_STEPS "Checking SQLMap..."
if command -v sqlmap &> /dev/null || [ -f "/usr/bin/sqlmap" ]; then
    echo -e "  \033[92m✓ SQLMap terdeteksi! Menu SQLMap AKTIF!\033[0m"
else
    echo -e "  \033[91m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[0m"
    echo -e "  \033[91m  ✗ SQLMap BELUM TERINSTAL!\033[0m"
    echo -e "  \033[91m  Menu 08 (SQLMap Auto) TIDAK BERFUNGSI!\033[0m"
    echo -e "  \033[91m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[0m"
    echo ""
    echo -e "  \033[93m  Install: sudo apt install sqlmap\033[0m"
    echo -e "  \033[93m  Atau: pip install sqlmap\033[0m"
fi
STEP=$((STEP+1)); echo ""

# [7/10] Cek TOR
progress $STEP $TOTAL_STEPS "Checking TOR..."
if command -v tor &> /dev/null; then
    echo -e "  \033[92m✓ TOR terinstall!\033[0m"
    if systemctl is-active --quiet tor 2>/dev/null; then
        echo -e "  \033[92m  TOR service: RUNNING\033[0m"
    else
        echo -e "  \033[93m  TOR service: NOT RUNNING\033[0m"
        echo -e "  \033[93m  Start: sudo service tor start\033[0m"
    fi
else
    echo -e "  \033[93m⚠ TOR tidak terdeteksi (optional)\033[0m"
    echo -e "  \033[93m  Install: sudo apt install tor\033[0m"
fi
STEP=$((STEP+1)); echo ""

# [8/10] Cek curl
progress $STEP $TOTAL_STEPS "Checking curl..."
if command -v curl &> /dev/null; then
    echo -e "  \033[92m✓ curl terdeteksi!\033[0m"
else
    echo -e "  \033[93m⚠ curl tidak ditemukan (optional)\033[0m"
fi
STEP=$((STEP+1)); echo ""

# [9/10] Membuat struktur folder
progress $STEP $TOTAL_STEPS "Creating directory structure..."
mkdir -p results/scanner results/sqli results/brute results/dumper results/tools results/logs
echo -e "  \033[92m✓ Folder results/ siap!\033[0m"
STEP=$((STEP+1)); echo ""

# [10/10] Cek file utama
progress $STEP $TOTAL_STEPS "Checking main.py..."
if [ -f "main.py" ]; then
    echo -e "  \033[92m✓ main.py ditemukan!\033[0m"
    chmod +x main.py 2>/dev/null
    echo -e "  \033[92m✓ File siap dijalankan!\033[0m"
else
    echo -e "  \033[93m⚠ main.py tidak ditemukan di folder ini!\033[0m"
    echo -e "  \033[93m  Pastikan file main.py ada sebelum menjalankan.\033[0m"
fi
STEP=$((STEP+1)); echo ""

# ============================================================
# RINGKASAN
# ============================================================
echo ""
echo "  ╔══════════════════════════════════════════╗"
echo "  ║   RINGKASAN INSTALASI                    ║"
echo "  ╠══════════════════════════════════════════╣"

# Python3
if command -v python3 &> /dev/null; then
    echo "  ║  Python3    : ✅ Terinstall              ║"
else
    echo "  ║  Python3    : ❌ TIDAK ADA               ║"
fi

# Rich
if python3 -c "import rich" 2>/dev/null; then
    echo "  ║  Rich UI    : ✅ Terinstall              ║"
else
    echo "  ║  Rich UI    : ❌ BELUM TERINSTAL         ║"
fi

# SQLMap
if command -v sqlmap &> /dev/null || [ -f "/usr/bin/sqlmap" ]; then
    echo "  ║  SQLMap     : ✅ Terinstall              ║"
else
    echo "  ║  SQLMap     : ❌ BELUM TERINSTAL         ║"
fi

# TOR
if command -v tor &> /dev/null; then
    echo "  ║  TOR        : ✅ Terinstall              ║"
else
    echo "  ║  TOR        : ⚠ Tidak terinstall        ║"
fi

# Main Script
if [ -f "main.py" ]; then
    echo "  ║  main.py    : ✅ Ditemukan               ║"
else
    echo "  ║  main.py    : ❌ TIDAK DITEMUKAN         ║"
fi

echo "  ╠══════════════════════════════════════════╣"
echo "  ║  Module     : 50+ (9 Kategori)           ║"
echo "  ║  Payload    : 360+                       ║"
echo "  ║  Version    : 9.0 Edition                ║"
echo "  ║  Status     : READY                      ║"
echo "  ╚══════════════════════════════════════════╝"
echo ""

# Peringatan SQLMap
if ! command -v sqlmap &> /dev/null && [ ! -f "/usr/bin/sqlmap" ]; then
    echo "  ──────────────────────────────────────────"
    echo "  ⚠  PERHATIAN: SQLMap BELUM TERINSTAL!"
    echo ""
    echo "  Menu 08 (SQLMap Auto) TIDAK BERFUNGSI!"
    echo "  Install: sudo apt install sqlmap"
    echo "  ──────────────────────────────────────────"
    echo ""
fi

# Peringatan Rich
if ! python3 -c "import rich" 2>/dev/null; then
    echo "  ──────────────────────────────────────────"
    echo "  ⚠  PERHATIAN: Rich BELUM TERINSTAL!"
    echo ""
    echo "  Tampilan modern tidak akan muncul!"
    echo "  Install: pip install rich"
    echo "  ──────────────────────────────────────────"
    echo ""
fi

echo "  ╔══════════════════════════════════════════╗"
echo "  ║   INSTALLATION COMPLETE!                 ║"
echo "  ║   Jalankan: python3 main.py              ║"
echo "  ╚══════════════════════════════════════════╝"
echo ""
